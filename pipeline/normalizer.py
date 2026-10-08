import re
from typing import Dict, Any, Optional, Tuple
from pipeline.slang_dictionary import (
    WARRANTY_PATTERNS, IMEI_SIGNAL_PATTERNS, BATTERY_PATTERNS,
    COMPLETENESS_PATTERNS, PHYSICAL_GRADE_PATTERNS, SCREEN_PATTERNS,
    BIOMETRICS_PATTERNS, TRUETONE_PATTERNS, PRICE_SLANG_PATTERNS
)

class SmartphoneListingNormalizer:
    """
    NLP & Rule-based Normalizer untuk Ekstraksi Spesifikasi & Metadata Pasar Smartphone Indonesia.
    """

    @staticmethod
    def parse_price(raw_val: Any) -> Optional[float]:
        """Konversi representasi string/angka harga ke float bersih."""
        if raw_val is None:
            return None
        if isinstance(raw_val, (int, float)):
            return float(raw_val)

        text = str(raw_val).strip().lower()
        text = re.sub(r"^(?:rp\.?|idr|harga:?)\s*", "", text)

        for pattern, multiplier in PRICE_SLANG_PATTERNS:
            match = re.search(pattern, text)
            if match:
                num_str = match.group(1).replace(",", ".")
                try:
                    return float(num_str) * multiplier
                except ValueError:
                    pass

        clean_num = re.sub(r"[^\d]", "", text)
        if clean_num:
            try:
                return float(clean_num)
            except ValueError:
                return None
        return None

    @staticmethod
    def extract_storage(text: str) -> Optional[int]:
        """Ekstraksi kapasitas ROM / Internal Storage dalam GB."""
        lower = text.lower()
        if "1tb" in lower or "1 tb" in lower or "1024gb" in lower:
            return 1024
        
        # Cek format RAM/ROM misal 8/256, 12/512
        ram_rom_match = re.search(r"\b\d{1,2}\s*[/,]\s*(\d{2,4})\s*(?:gb)?\b", lower)
        if ram_rom_match:
            try:
                val = int(ram_rom_match.group(1))
                if val in [32, 64, 128, 256, 512, 1024]:
                    return val
            except ValueError:
                pass

        match = re.search(r"\b(512|256|128|64|32|16)\s*(?:gb|gigabyte|g)?\b", lower)
        if match:
            try:
                return int(match.group(1))
            except ValueError:
                pass
        return None

    @staticmethod
    def extract_ram(text: str) -> Optional[int]:
        """Ekstraksi kapasitas RAM dalam GB."""
        lower = text.lower()
        ram_rom_match = re.search(r"\b(\d{1,2})\s*[/,]\s*\d{2,4}\s*(?:gb)?\b", lower)
        if ram_rom_match:
            try:
                val = int(ram_rom_match.group(1))
                if val in [2, 3, 4, 6, 8, 12, 16, 24]:
                    return val
            except ValueError:
                pass

        ram_match = re.search(r"\bram\s*(\d{1,2})\s*(?:gb)?\b", lower)
        if ram_match:
            try:
                return int(ram_match.group(1))
            except ValueError:
                pass
        return None

    @staticmethod
    def extract_warranty(text: str) -> Tuple[str, str]:
        """
        Ekstraksi asal garansi dan status aktif/habis.
        Returns: (warranty_type, warranty_status)
        """
        lower = text.lower()
        w_type = "Resmi Indonesia (iBox/SEIN/TAM)"
        w_status = "Habis (Ex-Resmi)"

        if any(re.search(pat, lower) for pat in WARRANTY_PATTERNS["resmi_indonesia"]):
            w_type = "Resmi Indonesia (iBox/SEIN/TAM)"
        elif any(re.search(pat, lower) for pat in WARRANTY_PATTERNS["ex_inter_pajak"]):
            w_type = "Ex-Inter Pajak Bea Cukai"
        elif any(re.search(pat, lower) for pat in WARRANTY_PATTERNS["ex_inter_non_pajak"]):
            w_type = "Ex-Inter Non-Pajak"
        elif any(re.search(pat, lower) for pat in WARRANTY_PATTERNS["distributor"]):
            w_type = "Garansi Distributor"

        # Cek status keaktifan garansi
        if re.search(r"\b(?:garansi\s*aktif|garansi\s*panjang|masih\s*garansi|applecare\+|on\s*garansi)\b", lower):
            w_status = "Aktif (Masih Garansi)"
        elif re.search(r"\b(?:garansi\s*toko|garansi\s*1\s*minggu|garansi\s*1\s*bulan)\b", lower):
            w_status = "Garansi Toko 1 Bulan"

        return w_type, w_status

    @staticmethod
    def extract_imei_status(text: str, warranty_type: str) -> str:
        """Ekstraksi status sinyal & registrasi IMEI di Indonesia."""
        lower = text.lower()
        if any(re.search(pat, lower) for pat in IMEI_SIGNAL_PATTERNS["wifi_only"]):
            return "Wifi Only / Sinyal Blokir"
        if any(re.search(pat, lower) for pat in IMEI_SIGNAL_PATTERNS["smartfren_temp"]):
            return "IMEI 3 Bulan / Smartfren Only"
        if any(re.search(pat, lower) for pat in IMEI_SIGNAL_PATTERNS["kemenperin_resmi"]):
            return "IMEI Kemenperin Permanen"
        if any(re.search(pat, lower) for pat in IMEI_SIGNAL_PATTERNS["all_operator"]):
            return "IMEI Bea Cukai All Operator"

        # Default fallback berdasarkan garansi
        if "Resmi Indonesia" in warranty_type:
            return "IMEI Kemenperin Permanen"
        elif "Ex-Inter Non-Pajak" in warranty_type:
            return "IMEI 3 Bulan / Smartfren Only"
        return "IMEI Bea Cukai All Operator"

    @staticmethod
    def extract_battery_health(text: str) -> Optional[int]:
        """Ekstraksi Battery Health (BH %) untuk iPhone."""
        lower = text.lower()
        for pat in BATTERY_PATTERNS:
            match = re.search(pat, lower)
            if match:
                try:
                    val = int(match.group(1))
                    if 50 <= val <= 100:
                        return val
                except ValueError:
                    pass
        return None

    @staticmethod
    def extract_completeness(text: str) -> str:
        """Ekstraksi kelengkapan unit."""
        lower = text.lower()
        if any(re.search(pat, lower) for pat in COMPLETENESS_PATTERNS["batangan"]):
            return "Batangan / Unit Only"
        if any(re.search(pat, lower) for pat in COMPLETENESS_PATTERNS["fullset_oem"]):
            return "Fullset OEM"
        if any(re.search(pat, lower) for pat in COMPLETENESS_PATTERNS["fullset_original"]):
            return "Fullset Original"
        return "Fullset Original"

    @staticmethod
    def extract_physical_grade(text: str) -> str:
        """Ekstraksi kondisi fisik unit."""
        lower = text.lower()
        if any(re.search(pat, lower) for pat in PHYSICAL_GRADE_PATTERNS["grade_c"]):
            return "Grade C (Dent/Baret)"
        if any(re.search(pat, lower) for pat in PHYSICAL_GRADE_PATTERNS["grade_b"]):
            return "Grade B (Lecet Wajar)"
        if any(re.search(pat, lower) for pat in PHYSICAL_GRADE_PATTERNS["grade_a_plus"]):
            return "Grade A+ (Like New 99%)"
        if any(re.search(pat, lower) for pat in PHYSICAL_GRADE_PATTERNS["grade_a"]):
            return "Grade A (Mulus 95%)"
        return "Grade A (Mulus 95%)"

    @staticmethod
    def extract_screen_condition(text: str) -> str:
        """Ekstraksi kondisi panel layar."""
        lower = text.lower()
        if any(re.search(pat, lower) for pat in SCREEN_PATTERNS["green_line"]):
            return "Green Line / Garis"
        if any(re.search(pat, lower) for pat in SCREEN_PATTERNS["shadow_tebal"]):
            return "Shadow Tebal"
        if any(re.search(pat, lower) for pat in SCREEN_PATTERNS["shadow_tipis"]):
            return "Shadow Tipis"
        if any(re.search(pat, lower) for pat in SCREEN_PATTERNS["glass_retak"]):
            return "Retak Kaca / Glass"
        if any(re.search(pat, lower) for pat in SCREEN_PATTERNS["layar_ganti_oem"]):
            return "Layar Ganti (OLED OEM/Incell)"
        return "Normal Original"

    @staticmethod
    def extract_biometrics_and_truetone(text: str) -> Tuple[str, str]:
        """Ekstraksi Face ID/Touch ID dan True Tone."""
        lower = text.lower()
        bio = "Normal Aktif"
        if any(re.search(pat, lower) for pat in BIOMETRICS_PATTERNS["broken"]):
            bio = "Face ID / Touch ID Rusak/Off"

        tt = "Aktif"
        if any(re.search(pat, lower) for pat in TRUETONE_PATTERNS["mati"]):
            tt = "Mati / Non-Aktif"

        return bio, tt

    @classmethod
    def normalize_listing(cls, raw_listing: Dict[str, Any]) -> Dict[str, Any]:
        """Menjalankan pipeline normalisasi menyeluruh untuk 1 raw listing HP."""
        title = raw_listing.get("title", "")
        desc = raw_listing.get("description", "")
        combined = f"{title} {desc}"

        clean_price = cls.parse_price(raw_listing.get("price"))
        storage = raw_listing.get("storage_gb") or cls.extract_storage(combined)
        ram = raw_listing.get("ram_gb") or cls.extract_ram(combined)
        w_type, w_status = cls.extract_warranty(combined)
        imei = cls.extract_imei_status(combined, w_type)
        bh = raw_listing.get("battery_health") or cls.extract_battery_health(combined)
        completeness = cls.extract_completeness(combined)
        grade = cls.extract_physical_grade(combined)
        screen = cls.extract_screen_condition(combined)
        bio, tt = cls.extract_biometrics_and_truetone(combined)

        return {
            "source_platform": raw_listing.get("source_platform", "olx"),
            "external_id": str(raw_listing.get("external_id", "")),
            "url": raw_listing.get("url", ""),
            "title": title.strip(),
            "raw_description": desc.strip(),
            "price": clean_price,
            "claimed_year": raw_listing.get("year"),
            "storage_gb": storage,
            "ram_gb": ram,
            "warranty_type": w_type,
            "warranty_status": w_status,
            "imei_status": imei,
            "battery_health_pct": bh,
            "completeness": completeness,
            "physical_grade": grade,
            "screen_condition": screen,
            "biometrics_status": bio,
            "truetone_status": tt,
            "account_lock_status": "Clean",
            "province": raw_listing.get("province", "DKI Jakarta"),
            "city": raw_listing.get("city", "Jakarta Selatan"),
            "seller_name": raw_listing.get("seller_name", "Individual Seller"),
            "seller_type": raw_listing.get("seller_type", "Individual")
        }
