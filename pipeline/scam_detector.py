import re
from typing import Optional, Tuple
from pipeline.slang_dictionary import DP_SCAM_PATTERNS

class SmartphoneScamDetector:
    """
    Detektor Iklan Penipuan, Perangkap DP/Cicilan, dan Replika HDC pada Pasar Smartphone.
    """

    MIN_PLAUSIBLE_CASH_PRICE = 400_000 # Di bawah 400rb untuk smartphone modern adalah rongsokan/DP semu
    
    FAKE_HDC_PATTERNS = [
        r"\bhdc\b", r"\breplika\b", r"\bsupercopy\b", r"\bclone\b",
        r"\bgrade\s*aaa\b", r"\bcopy\s*1:1\b", r"\bdummy\b"
    ]

    BYPASS_LOCK_PATTERNS = [
        r"\bbypass\s*icloud\b", r"\bmdm\s*locked\b", r"\bfrp\s*lock\b",
        r"\bakun\s*nyangkut\b", r"\blupa\s*sandi\s*icloud\b"
    ]

    @classmethod
    def evaluate_listing(
        cls,
        price: Optional[float],
        title: str,
        description: str = "",
        expected_msrp: Optional[float] = None
    ) -> Tuple[bool, str, str]:
        """
        Mengevaluasi apakah listing valid, penipuan DP, HDC palsu, atau locked device.
        Returns: (is_scam_or_dp: bool, category: str, reason: str)
        """
        try:
            price = float(price) if price is not None else None
        except (ValueError, TypeError):
            return True, "INVALID_PRICE", "Format harga tidak valid"

        if price is None or price <= 0:
            return True, "INVALID_PRICE", "Harga kosong atau 0"

        title_str = str(title or "")
        desc_str = str(description or "")
        text_corpus = f"{title_str} {desc_str}".lower()

        # 1. Cek HP Replika / HDC / Clone
        for pat in cls.FAKE_HDC_PATTERNS:
            if re.search(pat, text_corpus):
                return True, "FAKE_HDC_REPLICA", f"Terdeteksi indikasi barang replika/HDC: '{pat}'"

        # 2. Cek Akun Terkunci / Bypass Liar
        for pat in cls.BYPASS_LOCK_PATTERNS:
            if re.search(pat, text_corpus):
                return True, "LOCKED_OR_BYPASS", f"Unit mengalami bypass / lock akun: '{pat}'"

        # 3. Cek Kata Kunci DP di Judul dengan Harga Tidak Wajar
        for pat in DP_SCAM_PATTERNS:
            if re.search(pat, title_str.lower()):
                if price < 5_000_000:
                    return True, "DP_CLICKBAIT", f"Mengandung kata kunci DP/Kredit di judul: '{pat}'"

        # 4. Anomali Harga Ekstrim Terhadap MSRP Baru
        if expected_msrp and expected_msrp > 0:
            # Jika harga di bawah 15% dari MSRP baru untuk HP modern (misal iPhone 15 Pro 20jt dijual 2jt)
            if price < (expected_msrp * 0.15) and price < 4_000_000:
                for pat in DP_SCAM_PATTERNS:
                    if re.search(pat, text_corpus):
                        return True, "DP_CLICKBAIT", f"Harga anomali ({price:,.0f}) dengan keyword cicilan: '{pat}'"
                return True, "SUSPICIOUS_ANOMALY", f"Harga sangat tidak wajar ({price:,.0f} vs MSRP {expected_msrp:,.0f})"

        # 5. Batas Minimum Absolut Adaptif
        # Untuk perangkat modern/flagship, harga tunai di bawah 400rb adalah rongsokan/DP semu.
        # Namun untuk perangkat vintage (2010-2014) atau ultra-budget entry level, harga wajar pasar bisa Rp 100k - Rp 350k.
        min_threshold = cls.MIN_PLAUSIBLE_CASH_PRICE
        if expected_msrp and expected_msrp > 0:
            if expected_msrp < 2_500_000:
                min_threshold = 100_000
            elif expected_msrp < 5_000_000:
                min_threshold = 200_000
            else:
                min_threshold = 400_000
        else:
            min_threshold = 150_000

        if price < min_threshold:
            return True, "UNREALISTIC_LOW", f"Harga (Rp {price:,.0f}) di bawah batas minimum kewajaran Rp {min_threshold:,.0f}"

        return False, "VALID_CASH", "Listing Tunai Valid"
