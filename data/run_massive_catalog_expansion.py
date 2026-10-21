"""
Massive Master Database Catalog Expansion from GSMArena.
Menambahkan puluhan model dan ratusan varian baru dari seluruh brand
yang belum memiliki data atau memiliki data minim dalam Master Database.
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

# Target brand: Brand baru yang belum ada datanya + brand utama untuk penambahan model mutakhir
EXPANSION_TARGETS = [
    # Brand baru (belum pernah ada di GSMArena catalog lokal kita)
    ("OnePlus", 5),
    ("Honor", 5),
    ("Motorola", 5),
    ("Huawei", 4),
    ("Sony", 4),
    ("Nokia", 4),
    ("ZTE", 4),
    ("Meizu", 3),
    ("Sharp", 3),
    ("Lenovo", 3),
    # Brand utama (penambahan kuota smartphone generasi terkini)
    ("Samsung", 5),
    ("Xiaomi", 5),
    ("Apple", 4),
    ("Vivo", 5),
    ("Oppo", 5),
    ("Realme", 5),
    ("Infinix", 5),
    ("Google", 4),
    ("Asus", 4),
    ("Tecno", 4)
]

def main():
    print("=" * 75)
    print("MEMULAI EKSPANSI MASSAL MASTER DATABASE KATALOG SMARTPHONE")
    print(f"Target: {len(EXPANSION_TARGETS)} Brand Smartphone dari GSMArena")
    print("=" * 75)

    db_before = SessionLocal()
    m_before = db_before.query(MasterModel).count()
    v_before = db_before.query(MasterVariant).count()
    b_before = db_before.query(MasterBrand).count()
    db_before.close()

    total_added_models = 0
    total_added_variants = 0
    total_enriched = 0
    successful_brands = 0

    for brand_name, limit in EXPANSION_TARGETS:
        print(f"\n[+] Meng-ingest brand: {brand_name} (kuota: {limit} smartphone)...")
        res = ingest_gsmarena_brand_devices(brand_name, max_devices=limit, delay_sec=0.8)
        if res.get("status") == "success":
            successful_brands += 1
            added_m = res["new_models_added"]
            added_v = res["new_variants_added"]
            enr_m = res["models_enriched"]
            print(f"    Hasil: +{added_m} Model Baru, +{added_v} Varian Baru, {enr_m} Model Diperkaya.")
            for dev in res.get("processed_devices", []):
                print(f"      - {dev['name']}: {dev['status']} ({dev['variants_count']} varian)")
            total_added_models += added_m
            total_added_variants += added_v
            total_enriched += enr_m
        else:
            print(f"    Gagal: {res.get('message')}")
        time.sleep(0.5)

    db_after = SessionLocal()
    m_after = db_after.query(MasterModel).count()
    v_after = db_after.query(MasterVariant).count()
    b_after = db_after.query(MasterBrand).count()
    gsm_count = db_after.query(MasterModel).filter(MasterModel.source_platform == "GSMArena").count()
    db_after.close()

    print("\n" + "=" * 75)
    print("RINGKASAN EKSPANSI MASSAL MASTER DATABASE KATALOG:")
    print(f"Brand : {b_before} -> {b_after} (+{b_after - b_before} brand baru terdaftar)")
    print(f"Model : {m_before} -> {m_after} (+{total_added_models} model smartphone baru)")
    print(f"Varian: {v_before} -> {v_after} (+{total_added_variants} kombinasi RAM/ROM baru)")
    print(f"Model Diperkaya (Enriched): {total_enriched}")
    print(f"Total Model Berlabel 'GSMArena': {gsm_count}")
    print("=" * 75)

if __name__ == "__main__":
    main()
