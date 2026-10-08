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
        if price is None or price <= 0:
            return True, "INVALID_PRICE", "Harga kosong atau 0"

        text_corpus = f"{title} {description}".lower()

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
            if re.search(pat, title.lower()):
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

        # 5. Batas Minimum Absolut
        if price < cls.MIN_PLAUSIBLE_CASH_PRICE:
            return True, "UNREALISTIC_LOW", f"Harga di bawah batas minimum Rp {cls.MIN_PLAUSIBLE_CASH_PRICE:,.0f}"

        return False, "VALID_CASH", "Listing Tunai Valid"
