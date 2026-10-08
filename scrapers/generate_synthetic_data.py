"""
Generator Snapshot Data Listing Pasar Smartphone Sekunder Indonesia.
Menghasilkan ribuan listing realistis multi-brand, multi-kondisi, dan multi-kota
yang dialirkan langsung melalui pipeline NLP, Scam Filter, dan Entity Matcher.
"""
import random
from datetime import datetime, timedelta
from models.database import SessionLocal, init_db
from models.catalog import MasterVariant, MasterModel, MasterBrand, ScrapedListing
from pipeline.normalizer import SmartphoneListingNormalizer
from pipeline.scam_detector import SmartphoneScamDetector
from pipeline.entity_matcher import SmartphoneEntityMatcher
from analytics.depreciation_engine import SmartphoneDepreciationEngine

CITIES = [
    ("Jakarta Selatan", "DKI Jakarta"),
    ("Jakarta Barat", "DKI Jakarta"),
    ("Jakarta Pusat", "DKI Jakarta"),
    ("Tangerang", "Banten"),
    ("Bekasi", "Jawa Barat"),
    ("Bandung", "Jawa Barat"),
    ("Surabaya", "Jawa Timur"),
    ("Semarang", "Jawa Tengah"),
    ("Yogyakarta", "DI Yogyakarta"),
    ("Malang", "Jawa Timur"),
    ("Medan", "Sumatera Utara"),
    ("Makassar", "Sulawesi Selatan"),
    ("Denpasar", "Bali")
]

PLATFORMS = ["olx", "facebook_marketplace", "tokopedia", "shopee"]

TITLES_TEMPLATES = [
    "{brand} {model} {storage}gb {color} {warranty} {bh} {cond} {comp}",
    "{model} {storage}gb {cond} {warranty} sinyal on bebas reset",
    "Dijual {model} {storage} {color} {comp} {bh} mulus",
    "{brand} {model} {storage}gb {screen} {warranty}",
    "{model} {storage}gb {dp_trap} promo murah cuci gudang"
]

def generate_realistic_market_dataset(target_count_per_variant: int = 15):
    init_db()
    db = SessionLocal()
    matcher = SmartphoneEntityMatcher(db)

    variants = db.query(MasterVariant, MasterModel, MasterBrand).join(
        MasterModel, MasterVariant.model_id == MasterModel.id
    ).join(
        MasterBrand, MasterModel.brand_id == MasterBrand.id
    ).all()

    if not variants:
        print("[ERROR] Master catalog kosong! Jalankan seed_master_catalog terlebih dahulu.")
        return

    print(f"Generating realistic listings for {len(variants)} smartphone variants...")
    total_generated = 0
    scam_count = 0

    for var, model, brand in variants:
        msrp = float(var.official_msrp_new)
        retention = SmartphoneDepreciationEngine.calculate_theoretical_retention(
            brand.name, model.name, model.release_year, current_year=2026
        )
        base_market_price = msrp * retention

        for i in range(target_count_per_variant):
            city, prov = random.choice(CITIES)
            platform = random.choice(PLATFORMS)
            ext_id = f"{platform}_{var.id}_{i+1}_{random.randint(10000, 99999)}"

            # Tentukan tipe variasi kondisi (90% normal/wajar, 10% scam/DP trap)
            is_trap = random.random() < 0.08
            
            if is_trap:
                price = random.choice([1500000, 2000000, 2500000, 3000000])
                title = f"{brand.name} {model.name} {var.storage_gb}GB DP Ringan Angsuran Kredivo/Akulaku Murah"
                desc = f"Promo cuci gudang {model.name}. Cukup bayar DP {price:,}, cicilan ringan sebulan."
                is_scam = True
                scam_count += 1
            else:
                # Harga wajar pasar sekunder dengan variasi deviasi +- 12%
                price_deviation = random.uniform(-0.15, 0.12)
                price = base_market_price * (1.0 + price_deviation)

                # Kondisi atribut pasar
                is_apple = "apple" in brand.name.lower()
                warranty = random.choices(
                    ["iBox Resmi", "Digimap", "SEIN Resmi", "Ex-Inter All Op", "Ex-Inter Non Pajak (Smartfren)"],
                    weights=[40, 20, 20, 15, 5] if is_apple else [10, 5, 60, 20, 5]
                )[0]
                
                bh_str = f"BH {random.randint(82, 100)}%" if is_apple else ""
                cond = random.choice(["Mulus 99% Like New", "Mulus 95% No Minus", "Lecet Pemakaian Wajar", "Dent Sudut Tipis"])
                comp = random.choice(["Fullset Original Box Bawaan", "Fullset OEM", "Batangan Unit Only"])
                color = random.choice(["Titanium", "Black", "Blue", "White", "Silver", "Green", "Gold"])
                
                # Masukkan diskon jika kondisi tidak sempurna
                if "Batangan" in comp:
                    price *= 0.88
                if "Ex-Inter Non Pajak" in warranty:
                    price *= 0.78
                if "Dent" in cond:
                    price *= 0.90

                title = f"{brand.name} {model.name} {var.storage_gb}GB {color} {warranty} {bh_str} {cond} {comp}"
                desc = f"Jual santai {model.name} {var.storage_gb}GB {warranty}. Pemakaian pribadi, mesin 100% normal, {bh_str}, layar bening no shadow. Minat COD {city}."
                is_scam = False

            # Normalisasi & Pipeline
            norm = SmartphoneListingNormalizer.normalize_listing({
                "source_platform": platform,
                "external_id": ext_id,
                "title": title,
                "description": desc,
                "price": price,
                "storage_gb": var.storage_gb,
                "ram_gb": var.ram_gb,
                "year": model.release_year,
                "province": prov,
                "city": city,
                "seller_name": f"User_{city.split()[0]}_{random.randint(100, 999)}",
                "seller_type": random.choice(["Individual", "Store / Toko HP"])
            })

            var_id, conf, matched_name, _ = matcher.match(norm["title"], norm["storage_gb"])
            if not var_id:
                var_id = var.id

            is_scam_eval, _, _ = SmartphoneScamDetector.evaluate_listing(
                norm["price"], norm["title"], norm["raw_description"], expected_msrp=msrp
            )

            listing = ScrapedListing(
                source_platform=platform,
                external_id=ext_id,
                url=f"https://www.{platform}.com/item/{ext_id}",
                title=norm["title"],
                raw_description=norm["raw_description"],
                matched_variant_id=var_id,
                claimed_year=model.release_year,
                price=norm["price"],
                is_dp_price=is_scam_eval or is_scam,
                warranty_type=norm["warranty_type"],
                warranty_status=norm["warranty_status"],
                imei_status=norm["imei_status"],
                battery_health_pct=norm["battery_health_pct"],
                completeness=norm["completeness"],
                physical_grade=norm["physical_grade"],
                screen_condition=norm["screen_condition"],
                biometrics_status=norm["biometrics_status"],
                truetone_status=norm["truetone_status"],
                province=norm["province"],
                city=norm["city"],
                seller_name=norm["seller_name"],
                seller_type=norm["seller_type"],
                posted_at=datetime.utcnow() - timedelta(days=random.randint(0, 30))
            )
            db.add(listing)
            total_generated += 1

    db.commit()
    db.close()
    print(f"[SUCCESS] Berhasil mengenerate {total_generated} listing smartphone realistis ({scam_count} DP Trap terfilter).")

if __name__ == "__main__":
    generate_realistic_market_dataset()
