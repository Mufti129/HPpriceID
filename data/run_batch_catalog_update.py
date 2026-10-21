"""
Batch Master Database Catalog Update & GSMArena Ingestion.
Memperbarui dan memperkaya katalog smartphone pada database smartphone_bekas.db
dengan perangkat-perangkat generasi terbaru dari berbagai brand terkemuka.
"""

import sys
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scrapers.gsmarena_sync import ingest_gsmarena_brand_devices, GSMARENA_BRAND_SLUGS
from models.database import SessionLocal
from models.catalog import MasterBrand, MasterModel, MasterVariant

TARGET_BRANDS = [
    ("Samsung", 3),
    ("Xiaomi", 3),
    ("Apple", 2),
    ("Vivo", 3),
    ("Oppo", 3),
    ("Realme", 3),
    ("Infinix", 3),
    ("Google", 3),
    ("Asus", 2),
    ("Tecno", 2),
    ("Nothing", 2)
]

def main():
    print("=" * 70)
    print("MEMULAI PEMBARUAN & AUTO-INGESTION MASTER KATALOG SMARTPHONE")
    print("Sumber: GSMArena (Teknis Hardware & Varian RAM/ROM Lengkap)")
    print("=" * 70)

    db_before = SessionLocal()
    m_before = db_before.query(MasterModel).count()
    v_before = db_before.query(MasterVariant).count()
    db_before.close()

    total_added_models = 0
    total_added_variants = 0
    total_enriched = 0

    for brand_name, limit in TARGET_BRANDS:
        print(f"\n[+] Memproses pembaruan brand: {brand_name} (kuota: {limit} smartphone)...")
        res = ingest_gsmarena_brand_devices(brand_name, max_devices=limit, delay_sec=1.2)
        if res.get("status") == "success":
            print(f"    Berhasil: +{res['new_models_added']} Model Baru, +{res['new_variants_added']} Varian Baru, {res['models_enriched']} Model Diperkaya.")
            for dev in res.get("processed_devices", []):
                print(f"      - {dev['name']}: {dev['status']} ({dev['variants_count']} varian)")
            total_added_models += res["new_models_added"]
            total_added_variants += res["new_variants_added"]
            total_enriched += res["models_enriched"]
        else:
            print(f"    Gagal: {res.get('message')}")
        time.sleep(1.0)

    db_after = SessionLocal()
    m_after = db_after.query(MasterModel).count()
    v_after = db_after.query(MasterVariant).count()
    gsm_count = db_after.query(MasterModel).filter(MasterModel.source_platform == "GSMArena").count()
    db_after.close()

    print("\n" + "=" * 70)
    print("RINGKASAN PEMBARUAN MASTER DATABASE KATALOG:")
    print(f"Model Sebelum : {m_before} -> Sesudah: {m_after} (+{total_added_models} model baru)")
    print(f"Varian Sebelum: {v_before} -> Sesudah: {v_after} (+{total_added_variants} varian baru)")
    print(f"Model Diperkaya (Enriched Specs): {total_enriched}")
    print(f"Total Model Berlabel 'GSMArena'  : {gsm_count}")
    print("=" * 70)

if __name__ == "__main__":
    main()
