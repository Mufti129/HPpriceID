import math
from datetime import datetime
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from models.catalog import (
    ScrapedListing, MasterVariant, MasterModel, MasterBrand, MarketPriceStats
)

try:
    import numpy as np
    def percentile(data, p):
        return float(np.percentile(data, p))
    def median(data):
        return float(np.median(data))
except ImportError:
    def percentile(data, p):
        if not data:
            return 0.0
        sorted_data = sorted(data)
        k = (len(sorted_data) - 1) * (p / 100.0)
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return float(sorted_data[int(k)])
        d0 = sorted_data[int(f)] * (c - k)
        d1 = sorted_data[int(c)] * (k - f)
        return float(d0 + d1)
    def median(data):
        return percentile(data, 50)

class SmartphonePricingEngine:
    """
    Kalkulator Fair Market Value (FMV), Model Hedonik Kualitas HP, dan Detektor Hot Deal Arbitrase.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def calculate_variant_pricing_stats(
        self,
        variant_id: int,
        city: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Menghitung statistik harga pasar wajar untuk suatu varian smartphone.
        Menggunakan Tukey Interquartile Range (IQR) Outlier Filter.
        """
        query = self.db.query(ScrapedListing.price).filter(
            ScrapedListing.matched_variant_id == variant_id,
            ScrapedListing.is_dp_price == False,
            ScrapedListing.price > 0
        )

        if city:
            query = query.filter(ScrapedListing.city == city)

        prices = [float(p[0]) for p in query.all() if p[0] is not None]

        if len(prices) < 2:
            return None

        # 1. Outlier Filtering dengan Tukey IQR
        q25_raw = percentile(prices, 25)
        q75_raw = percentile(prices, 75)
        iqr = q75_raw - q25_raw
        lower_bound = max(0, q25_raw - (1.5 * iqr))
        upper_bound = q75_raw + (1.5 * iqr)

        filtered_prices = [p for p in prices if lower_bound <= p <= upper_bound]
        if not filtered_prices:
            filtered_prices = prices

        return {
            "variant_id": variant_id,
            "city": city,
            "sample_count": len(filtered_prices),
            "price_min": float(min(filtered_prices)),
            "price_p25": float(percentile(filtered_prices, 25)),
            "price_median": float(median(filtered_prices)),
            "price_p75": float(percentile(filtered_prices, 75)),
            "price_max": float(max(filtered_prices)),
            "calculated_at": datetime.utcnow()
        }

    def calculate_hedonic_adjusted_price(
        self,
        base_fmv: float,
        warranty_type: str = "Resmi Indonesia (iBox/SEIN/TAM)",
        warranty_status: str = "Habis (Ex-Resmi)",
        imei_status: str = "IMEI Kemenperin Permanen",
        battery_health: Optional[int] = None,
        completeness: str = "Fullset Original",
        physical_grade: str = "Grade A (Mulus 95%)",
        screen_condition: str = "Normal Original",
        biometrics: str = "Normal Aktif",
        truetone: str = "Aktif"
    ) -> Dict[str, Any]:
        """
        Menghitung Penyesuaian Harga Hedonik (Hedonic Quality Valuation).
        """
        adj_pct = 0.0
        breakdown = []

        # 1. Status Sinyal & IMEI
        if "Wifi Only" in imei_status or "Blokir" in imei_status:
            adj_pct -= 0.40
            breakdown.append(("Sinyal Blokir / Wifi Only", -0.40))
        elif "Smartfren" in imei_status or "3 Bulan" in imei_status:
            adj_pct -= 0.22
            breakdown.append(("IMEI 3 Bulan / Smartfren Only", -0.22))
        elif "Bea Cukai" in imei_status:
            adj_pct -= 0.05
            breakdown.append(("IMEI Bea Cukai All Operator", -0.05))

        # 2. Status Garansi
        if "Aktif" in warranty_status:
            adj_pct += 0.08
            breakdown.append(("Garansi Resmi Masih Aktif", +0.08))
        elif "Ex-Inter Non-Pajak" in warranty_type:
            adj_pct -= 0.12
            breakdown.append(("Unit Ex-Inter Non-Pajak", -0.12))

        # 3. Battery Health (iPhone)
        if battery_health is not None:
            if battery_health >= 95:
                adj_pct += 0.04
                breakdown.append((f"Battery Health Prima ({battery_health}%)", +0.04))
            elif battery_health < 80:
                adj_pct -= 0.12
                breakdown.append((f"Battery Health Service ({battery_health}%)", -0.12))
            elif battery_health < 85:
                adj_pct -= 0.05
                breakdown.append((f"Battery Health Menurun ({battery_health}%)", -0.05))

        # 4. Kelengkapan Unit
        if "Batangan" in completeness:
            adj_pct -= 0.12
            breakdown.append(("Unit Batangan (Tanpa Box/Charger)", -0.12))
        elif "OEM" in completeness:
            adj_pct -= 0.05
            breakdown.append(("Kelengkapan Box/Charger OEM", -0.05))

        # 5. Kondisi Fisik Bodi
        if "Grade A+" in physical_grade or "Like New" in physical_grade:
            adj_pct += 0.05
            breakdown.append(("Kondisi Fisik Like New 99%", +0.05))
        elif "Grade B" in physical_grade:
            adj_pct -= 0.08
            breakdown.append(("Lecet Pemakaian Wajar (Grade B)", -0.08))
        elif "Grade C" in physical_grade:
            adj_pct -= 0.18
            breakdown.append(("Dent / Baret Kasar (Grade C)", -0.18))

        # 6. Kondisi Layar
        if "Green Line" in screen_condition or "Garis" in screen_condition:
            adj_pct -= 0.45
            breakdown.append(("Layar Green Line / Rusak", -0.45))
        elif "Shadow Tebal" in screen_condition:
            adj_pct -= 0.30
            breakdown.append(("Layar Shadow Tebal", -0.30))
        elif "Shadow Tipis" in screen_condition:
            adj_pct -= 0.15
            breakdown.append(("Layar Shadow Tipis", -0.15))
        elif "OEM" in screen_condition or "Incell" in screen_condition:
            adj_pct -= 0.25
            breakdown.append(("Layar Ganti Non-Original (OEM/Incell)", -0.25))

        # 7. Biometrik & Sensor
        if "Rusak" in biometrics or "Off" in biometrics:
            adj_pct -= 0.20
            breakdown.append(("Face ID / Touch ID Rusak", -0.20))
        if "Mati" in truetone:
            adj_pct -= 0.06
            breakdown.append(("True Tone Non-Aktif", -0.06))

        # Batasi batas penyesuaian agar tidak negatif tidak masuk akal
        adj_pct = max(-0.75, min(0.30, adj_pct))
        adjusted_price = base_fmv * (1.0 + adj_pct)

        return {
            "base_fmv": base_fmv,
            "net_adjustment_pct": adj_pct * 100.0,
            "adjusted_price": adjusted_price,
            "adjustment_breakdown": breakdown
        }

    def find_hot_deals(self, discount_threshold_pct: float = 12.0) -> List[Dict[str, Any]]:
        """
        Mendeteksi unit smartphone dengan harga di bawah FMV (Peluang Hot Deal / Arbitrase).
        """
        listings = self.db.query(
            ScrapedListing, MasterVariant, MasterModel, MasterBrand
        ).join(
            MasterVariant, ScrapedListing.matched_variant_id == MasterVariant.id
        ).join(
            MasterModel, MasterVariant.model_id == MasterModel.id
        ).join(
            MasterBrand, MasterModel.brand_id == MasterBrand.id
        ).filter(
            ScrapedListing.is_dp_price == False,
            ScrapedListing.price > 0
        ).all()

        hot_deals = []
        for list_obj, var_obj, model_obj, brand_obj in listings:
            stats = self.calculate_variant_pricing_stats(var_obj.id)
            if not stats or stats["sample_count"] < 2:
                continue

            fmv = stats["price_median"]
            actual_price = float(list_obj.price)

            if actual_price < fmv:
                discount_pct = ((fmv - actual_price) / fmv) * 100.0
                if discount_pct >= discount_threshold_pct:
                    # Klasifikasi tingkat keuntungan
                    if discount_pct >= 22.0:
                        deal_tier = "Tier 1: Super Arbitrage (>=22%)"
                    elif discount_pct >= 15.0:
                        deal_tier = "Tier 2: High Arbitrage (15-21%)"
                    else:
                        deal_tier = "Tier 3: Moderate Arbitrage (12-14%)"

                    hot_deals.append({
                        "listing_id": list_obj.id,
                        "title": list_obj.title,
                        "brand": brand_obj.name,
                        "model": model_obj.name,
                        "variant": var_obj.variant_name,
                        "price": actual_price,
                        "fmv_price": fmv,
                        "discount_pct": round(discount_pct, 1),
                        "potential_profit": fmv - actual_price,
                        "deal_tier": deal_tier,
                        "city": list_obj.city,
                        "platform": list_obj.source_platform,
                        "url": list_obj.url,
                        "warranty_type": list_obj.warranty_type,
                        "imei_status": list_obj.imei_status,
                        "battery_health": list_obj.battery_health_pct,
                        "physical_grade": list_obj.physical_grade,
                        "screen_condition": list_obj.screen_condition
                    })

        hot_deals.sort(key=lambda x: x["discount_pct"], reverse=True)
        return hot_deals
