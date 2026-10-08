import math
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from collections import defaultdict
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
    Dioptimalkan dengan in-memory batch aggregation untuk performa sub-milidetik.
    """

    def __init__(self, db_session: Session):
        self.db = db_session
        self._cached_stats_map = None

    def get_all_variant_stats_map(self) -> Dict[int, Dict[str, Any]]:
        """
        Menghitung statistik FMV, P25, P75 untuk seluruh varian dalam 1 kali batch query.
        """
        if self._cached_stats_map is not None:
            return self._cached_stats_map

        rows = self.db.query(
            ScrapedListing.matched_variant_id,
            ScrapedListing.price
        ).filter(
            ScrapedListing.matched_variant_id.isnot(None),
            ScrapedListing.is_dp_price == False,
            ScrapedListing.price > 0
        ).all()

        variant_prices = defaultdict(list)
        for var_id, price in rows:
            if price is not None and float(price) > 0:
                variant_prices[var_id].append(float(price))

        stats_map = {}
        now = datetime.now(timezone.utc)

        for var_id, prices in variant_prices.items():
            if len(prices) < 2:
                continue

            # Tukey IQR Outlier Filtering
            q25_raw = percentile(prices, 25)
            q75_raw = percentile(prices, 75)
            iqr = q75_raw - q25_raw
            lower_bound = max(0, q25_raw - (1.5 * iqr))
            upper_bound = q75_raw + (1.5 * iqr)

            filtered_prices = [p for p in prices if lower_bound <= p <= upper_bound]
            if not filtered_prices:
                filtered_prices = prices

            stats_map[var_id] = {
                "variant_id": var_id,
                "sample_count": len(filtered_prices),
                "price_min": float(min(filtered_prices)),
                "price_p25": float(percentile(filtered_prices, 25)),
                "price_median": float(median(filtered_prices)),
                "price_p75": float(percentile(filtered_prices, 75)),
                "price_max": float(max(filtered_prices)),
                "calculated_at": now
            }

        self._cached_stats_map = stats_map
        return stats_map

    def calculate_variant_pricing_stats(
        self,
        variant_id: int,
        city: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Menghitung statistik harga pasar wajar untuk suatu varian smartphone.
        """
        if not city:
            stats_map = self.get_all_variant_stats_map()
            return stats_map.get(variant_id)

        query = self.db.query(ScrapedListing.price).filter(
            ScrapedListing.matched_variant_id == variant_id,
            ScrapedListing.is_dp_price == False,
            ScrapedListing.price > 0,
            ScrapedListing.city == city
        )

        prices = [float(p[0]) for p in query.all() if p[0] is not None]
        if len(prices) < 2:
            return None

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
            "calculated_at": datetime.now(timezone.utc)
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

        # Batasi batas penyesuaian agar wajar (-75% s/d +30%)
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
        Menggunakan in-memory pre-computed batch stats untuk kecepatan ultra instan.
        """
        stats_map = self.get_all_variant_stats_map()

        listings = self.db.query(
            ScrapedListing.id,
            ScrapedListing.title,
            ScrapedListing.price,
            ScrapedListing.matched_variant_id,
            ScrapedListing.city,
            ScrapedListing.source_platform,
            ScrapedListing.url,
            ScrapedListing.warranty_type,
            ScrapedListing.imei_status,
            ScrapedListing.battery_health_pct,
            ScrapedListing.physical_grade,
            ScrapedListing.screen_condition,
            MasterVariant.variant_name,
            MasterModel.name.label("model_name"),
            MasterBrand.name.label("brand_name")
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
        for (l_id, title, price, var_id, city, platform, url,
             w_type, imei, bh, p_grade, s_cond,
             var_name, model_name, brand_name) in listings:

            stats = stats_map.get(var_id)
            if not stats or stats["sample_count"] < 2:
                continue

            fmv = stats["price_median"]
            actual_price = float(price)

            if actual_price < fmv:
                discount_pct = ((fmv - actual_price) / fmv) * 100.0
                if discount_pct >= discount_threshold_pct:
                    if discount_pct >= 22.0:
                        deal_tier = "Tier 1: Super Arbitrage (>=22%)"
                    elif discount_pct >= 15.0:
                        deal_tier = "Tier 2: High Arbitrage (15-21%)"
                    else:
                        deal_tier = "Tier 3: Moderate Arbitrage (12-14%)"

                    hot_deals.append({
                        "listing_id": l_id,
                        "title": title,
                        "brand": brand_name,
                        "model": model_name,
                        "variant": var_name,
                        "price": actual_price,
                        "fmv_price": fmv,
                        "discount_pct": round(discount_pct, 1),
                        "potential_profit": fmv - actual_price,
                        "deal_tier": deal_tier,
                        "city": city,
                        "platform": platform,
                        "url": url,
                        "warranty_type": w_type,
                        "imei_status": imei,
                        "battery_health": bh,
                        "physical_grade": p_grade,
                        "screen_condition": s_cond
                    })

        hot_deals.sort(key=lambda x: x["discount_pct"], reverse=True)
        return hot_deals
