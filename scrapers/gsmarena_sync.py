"""
GSMArena Auto-Ingestion & Synchronization Engine (Skenario B).
Mendukung ekstraksi spesifikasi hardware lengkap, pemecahan varian RAM/ROM,
serta penandaan platform sumber data 'GSMArena' ke dalam Master Katalog.
"""

import os
import sys
import re
import time
import requests
from typing import Dict, List, Any, Optional, Tuple
from bs4 import BeautifulSoup
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from models.database import get_db, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant

BASE_URL = "https://www.gsmarena.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.gsmarena.com/"
}

# Pemetaan brand ke slug URL GSMArena
GSMARENA_BRAND_SLUGS = {
    "Apple": "apple-phones-48.php",
    "Samsung": "samsung-phones-9.php",
    "Xiaomi": "xiaomi-phones-80.php",
    "Oppo": "oppo-phones-82.php",
    "Vivo": "vivo-phones-98.php",
    "Realme": "realme-phones-118.php",
    "Infinix": "infinix-phones-119.php",
    "Google": "google-phones-107.php",
    "Google Pixel": "google-phones-107.php",
    "Asus": "asus-phones-46.php",
    "Sony": "sony-phones-7.php",
    "Tecno": "tecno-phones-120.php",
    "OnePlus": "oneplus-phones-95.php",
    "Nothing": "nothing-phones-128.php",
    "Honor": "honor-phones-121.php",
    "Motorola": "motorola-phones-4.php",
    "Nokia": "nokia-phones-1.php",
    "Huawei": "huawei-phones-58.php",
    "ZTE": "zte-phones-62.php",
    "Meizu": "meizu-phones-74.php",
    "Sharp": "sharp-phones-23.php",
    "Lenovo": "lenovo-phones-73.php",
    "BlackBerry": "blackberry-phones-36.php"
}

NON_SMARTPHONE_KEYWORDS = ["watch", "band", "tab", "pad", "vr", "glass", "airtag", "buds", "pencil", "tv", "vision"]

def is_smartphone(dev_name: str) -> bool:
    """Memastikan perangkat yang di-ingest adalah smartphone, bukan tablet atau smartwatch."""
    dev_lower = dev_name.lower()
    return not any(re.search(rf"\b{kw}\b", dev_lower) for kw in NON_SMARTPHONE_KEYWORDS)

def clean_text(val: Optional[str]) -> Optional[str]:
    if not val:
        return None
    cleaned = re.sub(r"\s+", " ", val).strip()
    return cleaned if cleaned else None

def parse_price_to_idr(price_str: Optional[str]) -> float:
    """Konversi string harga GSMArena (EUR/USD/INR) ke estimasi rupiah peluncuran resmi."""
    if not price_str:
        return 7999000.0 # Default nilai wajar smartphone jika tidak ada data

    p_low = price_str.lower()
    
    # 1. Deteksi mata uang EUR (misal: "About 1200 EUR", "1,200 EUR")
    match_eur = re.search(r"(\d+[\d,.]*)\s*(?:eur|€)", p_low)
    if match_eur:
        val = float(match_eur.group(1).replace(",", ""))
        return round((val * 17000.0 * 1.15) / 100000.0) * 100000.0 - 1000.0

    # 2. Deteksi mata uang USD (misal: "$ 999.00", "999 USD")
    match_usd = re.search(r"(?:\$|usd)\s*(\d+[\d,.]*)", p_low) or re.search(r"(\d+[\d,.]*)\s*usd", p_low)
    if match_usd:
        val = float(match_usd.group(1).replace(",", ""))
        return round((val * 16000.0 * 1.15) / 100000.0) * 100000.0 - 1000.0

    # 3. Deteksi mata uang INR (misal: "₹ 74,999", "74999 inr")
    match_inr = re.search(r"(?:₹|inr)\s*(\d+[\d,.]*)", p_low) or re.search(r"(\d+[\d,.]*)\s*inr", p_low)
    if match_inr:
        val = float(match_inr.group(1).replace(",", ""))
        return round((val * 190.0 * 1.20) / 100000.0) * 100000.0 - 1000.0

    return 7999000.0

def parse_gsmarena_device_page(url: str, session: requests.Session) -> Optional[Dict[str, Any]]:
    """Mengekstrak spesifikasi detail dari halaman perangkat GSMArena."""
    try:
        resp = session.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200 or "Turnstile" in resp.text:
            return None
        
        soup = BeautifulSoup(resp.text, "html.parser")
        
        # 1. Identitas Nama & Foto
        title_el = soup.find("h1", class_="specs-phone-name-title")
        raw_name = title_el.get_text(strip=True) if title_el else "Unknown Phone"
        
        img_el = soup.find("div", class_="specs-photo-main")
        image_url = img_el.find("img").get("src") if (img_el and img_el.find("img")) else None

        # 2. Atribut data-spec (periksa atribut langsung dan tag turunan seperti <a>)
        ds = {}
        for nfo in soup.find_all("td", class_="nfo"):
            spec_key = nfo.get("data-spec")
            if not spec_key:
                child_spec = nfo.find(attrs={"data-spec": True})
                if child_spec:
                    spec_key = child_spec.get("data-spec")
            if spec_key:
                ds[spec_key] = clean_text(nfo.get_text(separator=" ", strip=True))

        # 3. Ekstraksi spesifik dari baris table non data-spec
        charging_text = None
        card_slot = None
        factory_model_code = ds.get("models")
        for tr in soup.find_all("tr"):
            ttl = tr.find("td", class_="ttl")
            if ttl:
                ttl_txt = ttl.get_text(strip=True)
                nfo = tr.find("td", class_="nfo")
                if nfo:
                    nfo_txt = clean_text(nfo.get_text(separator=" ", strip=True))
                    if "Charging" in ttl_txt:
                        charging_text = nfo_txt
                    elif "Card slot" in ttl_txt:
                        card_slot = nfo_txt
                    elif "Technology" in ttl_txt:
                        if not ds.get("nettech"):
                            ds["nettech"] = nfo_txt
                    elif re.search(r"\bmodels?\b", ttl_txt, re.IGNORECASE):
                        if not factory_model_code or len(nfo_txt or "") > len(factory_model_code or ""):
                            factory_model_code = nfo_txt

        # Sanitasi kode model pabrikan
        if factory_model_code:
            factory_model_code = re.sub(r"^models?:\s*", "", factory_model_code, flags=re.IGNORECASE).strip()
            factory_model_code = re.sub(r"\s*,\s*", ", ", factory_model_code)
            # Kembalikan format Apple Machine ID 'iPhoneXX, Y' -> 'iPhoneXX,Y' (e.g. iPhone18,5)
            factory_model_code = re.sub(r"(iPhone\d+),\s+(\d+)", r"\1,\2", factory_model_code)
            factory_model_code = re.sub(r"(iPad\d+),\s+(\d+)", r"\1,\2", factory_model_code)

        # 4. Parsing nilai numerik dan metadata
        # Tahun Rilis
        year_str = ds.get("year") or ""
        match_yr = re.search(r"\b(20\d\d)\b", year_str)
        release_year = int(match_yr.group(1)) if match_yr else 2024

        # Layar
        size_str = ds.get("displaysize") or ""
        match_sz = re.search(r"(\d+\.?\d*)\s*inch", size_str, re.IGNORECASE)
        screen_size_inch = float(match_sz.group(1)) if match_sz else 6.5

        dtype = ds.get("displaytype") or ""
        match_hz = re.search(r"(\d{2,3})\s*Hz", dtype, re.IGNORECASE)
        refresh_rate_hz = int(match_hz.group(1)) if match_hz else 60

        match_nits = re.search(r"(\d{3,5})\s*nits", dtype, re.IGNORECASE)
        peak_brightness_nits = int(match_nits.group(1)) if match_nits else None

        # Performa / SoC
        tbench = ds.get("tbench") or ""
        match_antutu = re.search(r"AnTuTu:\s*(\d+)", tbench)
        antutu_score = int(match_antutu.group(1)) if match_antutu else None

        # Baterai & Charging
        bat_str = ds.get("batdescription1") or ""
        match_bat = re.search(r"(\d{3,5})\s*mAh", bat_str)
        battery_mah = int(match_bat.group(1)) if match_bat else 5000

        fast_watt = 20
        has_wireless = False
        wireless_watt = 0
        if charging_text:
            match_w = re.search(r"(\d{2,3})W\s+wired", charging_text, re.IGNORECASE) or re.search(r"(\d{2,3})W", charging_text, re.IGNORECASE)
            if match_w:
                fast_watt = int(match_w.group(1))
            if "wireless" in charging_text.lower():
                has_wireless = True
                match_wl = re.search(r"(\d{1,2})W\s+wireless", charging_text, re.IGNORECASE)
                wireless_watt = int(match_wl.group(1)) if match_wl else 15

        # Kamera
        cam1 = ds.get("cam1modules") or "Single"
        cam_count = "Single"
        if "+" in cam1:
            parts = cam1.split("+")
            cam_count = "Quad" if len(parts) >= 4 else "Triple" if len(parts) == 3 else "Dual"
        elif "dual" in cam1.lower():
            cam_count = "Dual"
        elif "triple" in cam1.lower():
            cam_count = "Triple"
        elif "quad" in cam1.lower():
            cam_count = "Quad"

        has_ois = "ois" in cam1.lower()
        zoom_lvl = None
        match_zoom = re.search(r"(\d+x)\s*(?:optical|periscope)", cam1, re.IGNORECASE)
        if match_zoom:
            zoom_lvl = match_zoom.group(1)

        # Kamera Depan (Sanitasi placeholder rumor)
        selfie_raw = ds.get("cam2modules") or ""
        if "XX MP" in selfie_raw:
            selfie_raw = re.sub(r"XX\s*MP.*?(?:under display camera|camera)?", "12 MP (Rumored Under-display)", selfie_raw, flags=re.IGNORECASE).strip()
            if selfie_raw.startswith(","):
                selfie_raw = selfie_raw.lstrip(", ").strip()

        # Bobot
        wt_str = ds.get("weight") or ""
        match_wt = re.search(r"(\d{2,3})\s*g", wt_str)
        weight_grams = int(match_wt.group(1)) if match_wt else 200

        # IP Rating
        body_other = ds.get("bodyother") or ds.get("build") or ""
        match_ip = re.search(r"\b(IP\d{2})\b", body_other)
        ip_rating = match_ip.group(1) if match_ip else ("IP68" if "water" in body_other.lower() else "None")

        # NFC & Jaringan
        has_nfc = True if "yes" in str(ds.get("nfc")).lower() else False
        nettech = ds.get("nettech") or ""
        chipset_str = (ds.get("chipset") or "").lower()
        is_5g = (
            "5G" in nettech.upper() or
            "5G" in raw_name.upper() or
            any(kw in chipset_str for kw in [
                "dimensity", "tensor", "snapdragon 8", "snapdragon 7",
                "snapdragon 6 gen", "snapdragon 4 gen", "exynos 1", "exynos 2",
                "a14 bionic", "a15 bionic", "a16 bionic", "a17", "a18"
            ])
        )
        network_gen = "5G" if is_5g else "4G LTE"

        # 5. Parsing Varian RAM & Storage dari 'internalmemory'
        raw_internal = ds.get("internalmemory") or ""
        variants = []
        
        # Format pola 1: "128GB 8GB RAM, 256GB 8GB RAM, 512GB 12GB RAM"
        combos = re.findall(r"(\d+)(GB|TB)\s+(\d+)GB\s+RAM", raw_internal, re.IGNORECASE)
        if combos:
            for rom_num, unit, ram_num in combos:
                rom_gb = int(rom_num) * (1024 if unit.upper() == "TB" else 1)
                ram_gb = int(ram_num)
                variants.append((rom_gb, ram_gb))
        else:
            # Format pola 2: "128GB, 256GB, 512GB" (misal iPhone lama / format tanpa RAM eksplisit)
            rom_only = re.findall(r"(\d+)(GB|TB)", raw_internal, re.IGNORECASE)
            # Coba cari RAM di spotlight atau info lain
            ram_match = re.search(r"(\d+)GB\s+RAM", raw_internal, re.IGNORECASE)
            def_ram = int(ram_match.group(1)) if ram_match else 8
            for rom_num, unit in rom_only:
                rom_gb = int(rom_num) * (1024 if unit.upper() == "TB" else 1)
                if rom_gb not in [v[0] for v in variants]:
                    variants.append((rom_gb, def_ram))

        if not variants:
            # Fallback default 1 varian jika tidak terurai
            variants = [(256, 8)]

        # Harga Estimasi MSRP IDR
        price_raw = ds.get("price")
        base_msrp = parse_price_to_idr(price_raw)

        return {
            "raw_name": raw_name,
            "image_url": image_url,
            "release_year": release_year,
            "chipset": ds.get("chipset"),
            "cpu_architecture": ds.get("cpu"),
            "gpu": ds.get("gpu"),
            "antutu_benchmark_score": antutu_score,
            "display_type": ds.get("displaytype"),
            "screen_size_inch": screen_size_inch,
            "refresh_rate_hz": refresh_rate_hz,
            "resolution": ds.get("displayresolution"),
            "peak_brightness_nits": peak_brightness_nits,
            "screen_protection": ds.get("displayprotection"),
            "main_camera_mp": ds.get("cam1modules"),
            "camera_setup": cam_count,
            "has_ois": has_ois,
            "optical_zoom_level": zoom_lvl,
            "selfie_camera_mp": selfie_raw if selfie_raw else ds.get("cam2modules"),
            "video_recording_max": ds.get("cam1video"),
            "battery_capacity_mah": battery_mah,
            "fast_charging_watt": fast_watt,
            "has_wireless_charging": has_wireless,
            "wireless_charging_watt": wireless_watt,
            "network_gen": network_gen,
            "has_nfc": has_nfc,
            "ip_rating": ip_rating,
            "weight_grams": weight_grams,
            "os_at_launch": ds.get("os"),
            "colors": ds.get("colors"),
            "factory_model_code": factory_model_code or ds.get("models"),
            "base_msrp": base_msrp,
            "variants": variants
        }

    except Exception as e:
        print(f"[ERROR] Gagal parsing GSMArena {url}: {e}")
        return None

def ingest_gsmarena_brand_devices(
    brand_name: str,
    max_devices: int = 5,
    delay_sec: float = 1.0
) -> Dict[str, Any]:
    """
    Menjalankan Skenario B Auto-Ingestion dari GSMArena:
    Mendata smartphone baru dari brand tertentu dan menyimpannya ke database
    dengan penanda source_platform = 'GSMArena'.
    """
    slug = GSMARENA_BRAND_SLUGS.get(brand_name)
    if not slug:
        return {"status": "error", "message": f"Brand '{brand_name}' belum didukung dalam mapping GSMArena."}

    init_db()
    session = requests.Session()
    session.headers.update(HEADERS)

    brand_url = f"{BASE_URL}/{slug}"
    print(f"[*] Mengakses katalog GSMArena brand: {brand_name} -> {brand_url}")

    try:
        r_brand = session.get(brand_url, timeout=15)
        if r_brand.status_code != 200 or "Turnstile" in r_brand.text:
            return {"status": "error", "message": "Gagal mengakses halaman brand (HTTP error atau captcha)."}

        soup = BeautifulSoup(r_brand.text, "html.parser")
        makers_div = soup.find("div", class_="makers")
        if not makers_div:
            return {"status": "error", "message": "Elemen daftar ponsel tidak ditemukan pada halaman brand."}

        device_links = []
        for li in makers_div.find_all("li"):
            a = li.find("a")
            span = li.find("span")
            if a and a.get("href"):
                dev_name = span.get_text(strip=True) if span else "Unknown"
                device_links.append((dev_name, f"{BASE_URL}/{a.get('href')}"))

        # Filter hanya perangkat smartphone (mengabaikan tablet, jam tangan, & aksesori)
        smartphone_links = [dl for dl in device_links if is_smartphone(dl[0])]
        print(f"[*] Ditemukan {len(device_links)} perangkat ({len(smartphone_links)} smartphone) di katalog GSMArena untuk {brand_name}.")

        new_models_added = 0
        new_variants_added = 0
        models_enriched = 0
        processed_devices = []

        with get_db() as db:
            # 1. Pastikan MasterBrand ada (resolusi alias seperti Google Pixel -> Google)
            target_b_name = "Google" if brand_name in ["Google", "Google Pixel"] else brand_name
            brand_obj = db.query(MasterBrand).filter(
                (MasterBrand.name.ilike(target_b_name)) | (MasterBrand.name.ilike(brand_name))
            ).first()
            if not brand_obj:
                brand_obj = MasterBrand(
                    name=target_b_name,
                    country_origin="International",
                    tier_category="Mainstream"
                )
                db.add(brand_obj)
                db.flush()

            for dev_title, dev_url in smartphone_links[:max_devices]:
                time.sleep(delay_sec)
                
                # Bersihkan nama: jika nama mengandung brand (e.g. "Apple iPhone 16 Pro"), bersihkan duplikasi
                clean_m_name = dev_title
                for prefix in [brand_name, target_b_name, "Google Pixel", "Google"]:
                    if clean_m_name.lower().startswith(prefix.lower()):
                        clean_m_name = clean_m_name[len(prefix):].strip()
                        break

                # Cek apakah model sudah ada di DB
                existing_model = db.query(MasterModel).filter(
                    MasterModel.brand_id == brand_obj.id,
                    (MasterModel.name.ilike(clean_m_name)) | (MasterModel.name.ilike(dev_title))
                ).first()

                parsed = parse_gsmarena_device_page(dev_url, session)
                if not parsed:
                    continue

                if not existing_model:
                    # Skenario B: Tambahkan Model Baru ke MasterModel
                    new_model = MasterModel(
                        brand_id=brand_obj.id,
                        name=clean_m_name,
                        series="GSMArena Ingested",
                        release_year=parsed["release_year"],
                        chipset=parsed["chipset"],
                        cpu_architecture=parsed["cpu_architecture"],
                        gpu=parsed["gpu"],
                        antutu_benchmark_score=parsed["antutu_benchmark_score"],
                        display_type=parsed["display_type"],
                        screen_size_inch=parsed["screen_size_inch"],
                        refresh_rate_hz=parsed["refresh_rate_hz"],
                        resolution=parsed["resolution"],
                        peak_brightness_nits=parsed["peak_brightness_nits"],
                        screen_protection=parsed["screen_protection"],
                        main_camera_mp=parsed["main_camera_mp"],
                        camera_setup=parsed["camera_setup"],
                        has_ois=parsed["has_ois"],
                        optical_zoom_level=parsed["optical_zoom_level"],
                        selfie_camera_mp=parsed["selfie_camera_mp"],
                        video_recording_max=parsed["video_recording_max"],
                        battery_capacity_mah=parsed["battery_capacity_mah"],
                        fast_charging_watt=parsed["fast_charging_watt"],
                        has_wireless_charging=parsed["has_wireless_charging"],
                        wireless_charging_watt=parsed["wireless_charging_watt"],
                        network_gen=parsed["network_gen"],
                        has_nfc=parsed["has_nfc"],
                        ip_rating=parsed["ip_rating"],
                        weight_grams=parsed["weight_grams"],
                        os_at_launch=parsed["os_at_launch"],
                        image_url=parsed["image_url"],
                        source_platform="GSMArena",
                        factory_model_code=parsed.get("factory_model_code"),
                        generation=f"Gen {parsed['release_year'] - 2009}" if parsed.get("release_year") else "Gen 1",
                        commercial_generation=f"Gen {re.search(r'\b(\d+)\b', clean_m_name).group(1)}" if re.search(r'\b(\d+)\b', clean_m_name) else "Gen 1",
                        lineage_generation=f"Ingested dari katalog GSMArena ({clean_m_name})"
                    )
                    db.add(new_model)
                    db.flush()
                    new_models_added += 1

                    # Tambahkan Varian-varian RAM/Storage
                    for idx, (rom_gb, ram_gb) in enumerate(parsed["variants"]):
                        var_name = f"{new_model.name} {ram_gb}GB/{rom_gb}GB" if rom_gb < 1024 else f"{new_model.name} {ram_gb}GB/1TB"
                        msrp_tier = parsed["base_msrp"] + (idx * 1500000.0) # Skala bertahap per kapasitas

                        new_variant = MasterVariant(
                            model_id=new_model.id,
                            variant_name=var_name,
                            ram_gb=ram_gb,
                            storage_gb=rom_gb,
                            color_options=parsed["colors"],
                            official_msrp_new=msrp_tier,
                            aliases=f"{clean_m_name.lower()} {rom_gb}, {clean_m_name.lower()} {ram_gb}/{rom_gb}",
                            image_url=parsed["image_url"],
                            source_platform="GSMArena"  # <-- Kolom platform baru
                        )
                        db.add(new_variant)
                        new_variants_added += 1

                    processed_devices.append({
                        "name": new_model.name,
                        "status": "ADDED_NEW",
                        "variants_count": len(parsed["variants"])
                    })
                else:
                    # Model sudah ada: Lakukan enrichment atribut yang masih kosong atau belum sinkron
                    updated = False
                    scraped_code = parsed.get("factory_model_code")
                    if scraped_code and existing_model.factory_model_code != scraped_code:
                        existing_model.factory_model_code = scraped_code
                        updated = True
                    if existing_model.network_gen == "4G LTE" and parsed.get("network_gen") == "5G":
                        existing_model.network_gen = "5G"
                        updated = True
                    if existing_model.selfie_camera_mp and "XX MP" in existing_model.selfie_camera_mp:
                        existing_model.selfie_camera_mp = parsed.get("selfie_camera_mp")
                        updated = True
                    if (not existing_model.chipset or existing_model.chipset == "-") and parsed.get("chipset"):
                        existing_model.chipset = parsed["chipset"]
                        updated = True
                    if (not existing_model.display_type or existing_model.display_type == "-") and parsed.get("display_type"):
                        existing_model.display_type = parsed["display_type"]
                        updated = True
                    if (not existing_model.resolution or existing_model.resolution == "-") and parsed.get("resolution"):
                        existing_model.resolution = parsed["resolution"]
                        updated = True
                    if (not existing_model.main_camera_mp or existing_model.main_camera_mp == "-") and parsed.get("main_camera_mp"):
                        existing_model.main_camera_mp = parsed["main_camera_mp"]
                        updated = True
                    if (not existing_model.antutu_benchmark_score) and parsed.get("antutu_benchmark_score"):
                        existing_model.antutu_benchmark_score = parsed["antutu_benchmark_score"]
                        updated = True
                    if not existing_model.peak_brightness_nits and parsed.get("peak_brightness_nits"):
                        existing_model.peak_brightness_nits = parsed["peak_brightness_nits"]
                        updated = True
                    if not existing_model.image_url and parsed.get("image_url"):
                        existing_model.image_url = parsed["image_url"]
                        updated = True
                    if existing_model.battery_capacity_mah == 5000 and parsed.get("battery_capacity_mah") and parsed["battery_capacity_mah"] != 5000:
                        existing_model.battery_capacity_mah = parsed["battery_capacity_mah"]
                        updated = True
                    if existing_model.fast_charging_watt == 20 and parsed.get("fast_charging_watt") and parsed["fast_charging_watt"] != 20:
                        existing_model.fast_charging_watt = parsed["fast_charging_watt"]
                        updated = True
                    
                    if updated:
                        models_enriched += 1

                    processed_devices.append({
                        "name": existing_model.name,
                        "status": "ENRICHED" if updated else "UP_TO_DATE",
                        "variants_count": 0
                    })

            db.commit()

        return {
            "status": "success",
            "brand": brand_name,
            "new_models_added": new_models_added,
            "new_variants_added": new_variants_added,
            "models_enriched": models_enriched,
            "processed_devices": processed_devices
        }

    except Exception as e:
        print(f"[ERROR] Exception saat auto-ingestion GSMArena: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    target_brand = sys.argv[1] if len(sys.argv) > 1 else "Apple"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    res = ingest_gsmarena_brand_devices(target_brand, max_devices=count)
    print(res)
