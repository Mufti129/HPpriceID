import argparse
from models.database import init_db, SessionLocal
from data.master_catalog_seed import seed_master_catalog
from scrapers.generate_synthetic_data import generate_realistic_market_dataset
from analytics.pricing_engine import SmartphonePricingEngine

def run_pipeline():
    print("=" * 60)
    print("PHONEPRICE ID — SMARTPHONE INTELLIGENCE & VALUATION PIPELINE")
    print("=" * 60)
    
    print("\n[STEP 1] Inisialisasi Database SQLite...")
    init_db()
    
    print("\n[STEP 2] Memuat Master Katalog Brand, Model & Spesifikasi Teknis...")
    seed_master_catalog()
    
    print("\n[STEP 3] Memuat Snapshot Listing Pasar Sekunder & Menjalankan NLP Pipeline...")
    generate_realistic_market_dataset(target_count_per_variant=20)
    
    print("\n[STEP 4] Menghitung Statistik FMV & Kuartil Harga...")
    db = SessionLocal()
    engine = SmartphonePricingEngine(db)
    deals = engine.find_hot_deals(discount_threshold_pct=12.0)
    db.close()
    
    print(f"\n[DONE] Pipeline Selesai! Terdeteksi {len(deals)} Hot Deals Arbitrase Aktif.")
    print("Jalankan Dashboard Streamlit dengan: streamlit run app.py")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PhonePrice ID CLI Orchestrator")
    parser.add_argument("--all", action="store_true", help="Jalankan seluruh pipeline dari awal")
    args = parser.parse_args()
    run_pipeline()
