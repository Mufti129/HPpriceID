"""
Model Depresiasi Smartphone Multi-Tier Indonesia.
Menghitung laju penyusutan nilai smartphone terhadap harga peluncuran baru (MSRP).
Berbasis riset ekonometrik depresiasi consumer electronics:
- Tier Apple iOS: Depresiasi lambat (~16-18% th-1, ~8% th berikutnya)
- Tier Android Flagship: Depresiasi moderat (~24-28% th-1, ~12% th berikutnya)
- Tier Android Value/Mid: Depresiasi cepat (~32-38% th-1, ~15% th berikutnya)
"""

class SmartphoneDepreciationEngine:

    TIER_RATES = {
        "Apple": {"year_1": 0.17, "annual_decay": 0.08, "max_cap": 0.70},
        "Samsung_Flagship": {"year_1": 0.25, "annual_decay": 0.11, "max_cap": 0.78},
        "Android_Flagship": {"year_1": 0.28, "annual_decay": 0.12, "max_cap": 0.80},
        "Android_Midrange": {"year_1": 0.35, "annual_decay": 0.15, "max_cap": 0.85},
    }

    @classmethod
    def get_tier_for_model(cls, brand_name: str, model_name: str) -> str:
        brand_low = brand_name.lower()
        model_low = model_name.lower()

        if "apple" in brand_low or "iphone" in model_low:
            return "Apple"
        if "samsung" in brand_low and ("ultra" in model_low or "fold" in model_low or "s2" in model_low):
            return "Samsung_Flagship"
        if any(kw in model_low for kw in ["pro", "ultra", "gt", "rog", "x100", "magic"]):
            return "Android_Flagship"
        return "Android_Midrange"

    @classmethod
    def calculate_theoretical_retention(
        cls,
        brand_name: str,
        model_name: str,
        release_year: int,
        current_year: int = 2026
    ) -> float:
        """
        Menghitung persentase retensi nilai teoritis (0.0 - 1.0).
        """
        tier = cls.get_tier_for_model(brand_name, model_name)
        params = cls.TIER_RATES.get(tier, cls.TIER_RATES["Android_Midrange"])

        age = max(0, current_year - release_year)
        if age == 0:
            total_depreciation = params["year_1"] * 0.5  # Model tahun berjalan
        else:
            total_depreciation = params["year_1"] + ((age - 1) * params["annual_decay"])

        total_depreciation = min(params["max_cap"], total_depreciation)
        retention_rate = 1.0 - total_depreciation
        return retention_rate

    @classmethod
    def calculate_real_depreciation(
        cls,
        msrp_new: float,
        current_market_price: float
    ) -> float:
        """
        Menghitung persentase depresiasi riil dari MSRP Baru ke Harga Pasar Saat Ini.
        """
        if msrp_new <= 0:
            return 0.0
        depr = ((msrp_new - current_market_price) / msrp_new) * 100.0
        return max(0.0, round(depr, 2))
