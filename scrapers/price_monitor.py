"""
Periodic Smartphone Price Monitoring & Drift Detection Engine.
Dirancang untuk dijalankan terjadwal (cron / task scheduler) guna memantau pergerakan harga
smartphone sekunder secara berkala, mendeteksi penurunan harga (price drops),
dan mencatat histori fluktuasi nilai pasar.
"""

import os
import sys
import time
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from models.database import SessionLocal, init_db
from models.catalog import MasterVariant, MasterModel, MasterBrand, ScrapedListing
from scrapers.real_marketplace_scraper import fetch_real_maujual_data, BRANDS_MAP
from pipeline.entity_matcher import SmartphoneEntityMatcher

MONITORING_LOG_PATH = ROOT_DIR / "data" / "price_drift_history.json"

def run_periodic_price_check(alert_threshold_pct: float = 7.0) -> Dict[str, Any]:
    """
    Menjalankan audit harga berkala, membandingkan harga pasar terkini
    dengan snapshot sebelumnya di database, dan mencatat pergeseran (drift).
    """
    init_db()
    db = SessionLocal()
    matcher = SmartphoneEntityMatcher(db)

    print("=" * 70)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] MEMULAI AUDIT MONITORING HARGA BERKALA")
    print("=" * 70)

    # 1. Ambil snapshot harga rata-rata saat ini per varian di database
    variant_prices_db = {}
    variants = db.query(MasterVariant, MasterModel, MasterBrand).join(
        MasterModel, MasterVariant.model_id == MasterModel.id
    ).join(
        MasterBrand, MasterModel.brand_id == MasterBrand.id
    ).all()

    for v, m, b in variants:
        listings = db.query(ScrapedListing.price).filter(
            ScrapedListing.matched_variant_id == v.id,
            ScrapedListing.price > 0
        ).all()
        if listings:
            avg_p = sum(float(l[0]) for l in listings) / len(listings)
            variant_prices_db[v.id] = {
                "name": f"{b.name} {m.name} {v.variant_name}",
                "brand": b.name,
                "model": m.name,
                "current_avg_price": avg_p,
                "sample_count": len(listings)
            }

    # 2. Polling data live terkini dari platform re-commerce
    price_drops = []
    price_hikes = []
    checked_count = 0

    for brand_name, brand_slug in BRANDS_MAP.items():
        print(f"Monitoring pergerakan harga brand: {brand_name}...")
        products = fetch_real_maujual_data(brand_slug)

        for prod in products:
            for v in prod.get("variant_combinations", []):
                var_name = v.get("name", "")
                max_p = float(v.get("max_price", 0))
                min_p = float(v.get("min_price", 0))
                if max_p <= 0:
                    continue

                live_market_p = (min_p + max_p) / 2.0 if min_p > 0 else max_p * 0.85
                storage_str = next((c["value"] for c in v.get("components", []) if c["code"] == "storage"), "0")
                storage_gb = int("".join(filter(str.isdigit, storage_str))) if any(c.isdigit() for c in storage_str) else None

                var_id, conf, m_name, msrp = matcher.match(var_name, storage_gb=storage_gb)
                if var_id and var_id in variant_prices_db:
                    checked_count += 1
                    old_p = variant_prices_db[var_id]["current_avg_price"]
                    diff_pct = ((live_market_p - old_p) / old_p) * 100.0

                    if diff_pct <= -alert_threshold_pct:
                        price_drops.append({
                            "variant_id": var_id,
                            "product": variant_prices_db[var_id]["name"],
                            "old_avg": old_p,
                            "new_live": live_market_p,
                            "change_pct": round(diff_pct, 2)
                        })
                    elif diff_pct >= alert_threshold_pct:
                        price_hikes.append({
                            "variant_id": var_id,
                            "product": variant_prices_db[var_id]["name"],
                            "old_avg": old_p,
                            "new_live": live_market_p,
                            "change_pct": round(diff_pct, 2)
                        })
        time.sleep(0.2)

    db.close()

    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_variants_audited": checked_count,
        "price_drops_count": len(price_drops),
        "price_hikes_count": len(price_hikes),
        "alert_threshold_pct": alert_threshold_pct,
        "significant_drops": price_drops[:15],
        "significant_hikes": price_hikes[:15]
    }

    # Simpan riwayat monitoring
    os.makedirs(MONITORING_LOG_PATH.parent, exist_ok=True)
    history = []
    if MONITORING_LOG_PATH.exists():
        try:
            with open(MONITORING_LOG_PATH, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []

    history.append(summary)
    with open(MONITORING_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(history[-30:], f, indent=2, ensure_ascii=False) # simpan 30 audit terakhir

    print("\n" + "=" * 70)
    print(f"AUDIT MONITORING SELESAI: {checked_count} varian diperiksa.")
    print(f"Penurunan Harga Signifikan (Drops): {len(price_drops)} item.")
    print(f"Kenaikan Harga Signifikan (Hikes): {len(price_hikes)} item.")
    print("=" * 70)

    return summary

if __name__ == "__main__":
    run_periodic_price_check()
