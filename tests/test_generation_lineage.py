import unittest
import pandas as pd
from pathlib import Path
from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel

class TestGenerationLineage(unittest.TestCase):

    def setUp(self):
        init_db()
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()

    def test_schema_has_generation_columns(self):
        """Memastikan kolom generation, commercial_generation, dan lineage_generation ada pada MasterModel."""
        model_cols = [c.name for c in MasterModel.__table__.columns]
        self.assertIn("generation", model_cols)
        self.assertIn("commercial_generation", model_cols)
        self.assertIn("lineage_generation", model_cols)

    def test_all_models_have_generation_data(self):
        """Memastikan seluruh model di database memiliki data silsilah generasi terisi lengkap."""
        total_models = self.db.query(MasterModel).count()
        self.assertGreaterEqual(total_models, 400, "Database harus memuat minimal 400 model")

        null_gen = self.db.query(MasterModel).filter(MasterModel.generation.is_(None)).count()
        null_com = self.db.query(MasterModel).filter(MasterModel.commercial_generation.is_(None)).count()
        null_lin = self.db.query(MasterModel).filter(MasterModel.lineage_generation.is_(None)).count()

        self.assertEqual(null_gen, 0, "Tidak boleh ada model dengan generation NULL")
        self.assertEqual(null_com, 0, "Tidak boleh ada model dengan commercial_generation NULL")
        self.assertEqual(null_lin, 0, "Tidak boleh ada model dengan lineage_generation NULL")

    def test_verified_sample_rules_from_pdf(self):
        """
        Memvalidasi sampel aturan silsilah yang tercantum pada Bagian 4 dokumen
        Panduan & Aturan Penetapan Generasi Smartphone.
        """
        test_samples = [
            ("Apple", "iPhone 18 Pro", "Gen 20", "Gen 18"),
            ("Apple", "iPhone 11", "Gen 13", "Gen 11"),
            ("Samsung", "Galaxy S24", "Gen 15", "Gen 24"),
            ("Samsung", "Galaxy S20", "Gen 11", "Gen 20"),
            ("Samsung", "Galaxy A55", "Gen 6", "Gen 55"),
            ("Samsung", "Galaxy A54", "Gen 5", "Gen 54"),
            ("Oppo", "Reno 12 Pro 5G", "Gen 12", "Gen 12"),
            ("Oppo", "Find X5 Pro", "Gen 4", "Gen 5"),
            ("Xiaomi", "Xiaomi 14", "Gen 13", "Gen 14"),
            ("Xiaomi", "Redmi Note 13 Pro 5G", "Gen 13", "Gen 13"),
            ("Xiaomi", "Poco F6", "Gen 6", "Gen 6"),
            ("Vivo", "X100 Pro", "Gen 6", "Gen 100"),
            ("Vivo", "V30 Pro", "Gen 16", "Gen 30"),
            ("Google", "Pixel 9 Pro XL", "Gen 9", "Gen 9"),
            ("Asus", "ROG Phone 8 Pro", "Gen 7", "Gen 8"),
            ("Sony", "Xperia 1 VI", "Gen 6", "Gen 6"),
            ("Huawei", "Pura 70 Ultra", "Gen 13", "Gen 70"),
            ("Infinix", "Hot 40 Pro", "Gen 14", "Gen 40"),
            ("Nothing", "Phone (2)", "Gen 2", "Gen 2")
        ]

        for b_name, m_keyword, expected_riil, expected_kom in test_samples:
            model = self.db.query(MasterModel).join(
                MasterBrand, MasterModel.brand_id == MasterBrand.id
            ).filter(
                MasterBrand.name.ilike(b_name),
                MasterModel.name.ilike(f"%{m_keyword}%")
            ).first()

            self.assertIsNotNone(model, f"Model {b_name} {m_keyword} harus ada di database")
            self.assertEqual(model.generation, expected_riil, f"Generasi riil {model.name} harus {expected_riil}")
            self.assertEqual(model.commercial_generation, expected_kom, f"Generasi komersial {model.name} harus {expected_kom}")
            self.assertTrue(len(model.lineage_generation) > 5, "Keterangan silsilah harus memuat deskripsi")

    def test_csv_file_integrity(self):
        """Memastikan file datahptambahgenerasi.csv valid dan memiliki 26 kolom lengkap."""
        csv_file = Path("data/datahptambahgenerasi.csv")
        self.assertTrue(csv_file.exists(), "File data/datahptambahgenerasi.csv harus ada di folder data")

        df = pd.read_csv(csv_file)
        self.assertEqual(len(df), 402, "CSV harus memiliki 402 baris model")
        self.assertIn("Generasi", df.columns)
        self.assertIn("Generasi Komersial", df.columns)
        self.assertIn("Keterangan Silsilah", df.columns)
        self.assertIn("Kode Model Pabrikan", df.columns)

    def test_scraped_discrepancies_and_factory_codes(self):
        """Memastikan perbaikan diskrepansi scraping dan kode model pabrikan valid."""
        csv_file = Path("data/datahptambahgenerasi.csv")
        df = pd.read_csv(csv_file)

        # 1. Verifikasi Realme 16x
        r_16x = df[df["Model"] == "16x"].iloc[0]
        self.assertEqual(int(r_16x["Tahun Rilis"]), 2026)
        self.assertIn("Dimensity 6300", r_16x["Chipset / SoC"])
        self.assertEqual(r_16x["Jaringan"], "5G")
        self.assertEqual(r_16x["Kode Model Pabrikan"], "RMX5270")

        # 2. Verifikasi Tecno Camon Air
        t_camon = df[df["Model"] == "Camon Air"].iloc[0]
        self.assertEqual(int(t_camon["Tahun Rilis"]), 2026)
        self.assertIn("Helio G200", t_camon["Chipset / SoC"])
        self.assertEqual(t_camon["Kode Model Pabrikan"], "CN6c")

        # 3. Verifikasi Ponsel 5G (seperti Honor Magic9 dan Oppo K15x)
        h_magic = df[df["Model"] == "Magic9"].iloc[0]
        self.assertEqual(h_magic["Jaringan"], "5G")

        o_k15x = df[df["Model"] == "K15x"].iloc[0]
        self.assertEqual(o_k15x["Jaringan"], "5G")
        self.assertEqual(o_k15x["Kode Model Pabrikan"], "CPH2913, PMX110")

        # 4. Verifikasi Apple iPhone Duo selfie camera sanitasi
        i_duo = df[df["Model"] == "iPhone Duo"].iloc[0]
        self.assertNotIn("XX MP", str(i_duo["Kamera Depan"]))
        self.assertIn("12 MP", str(i_duo["Kamera Depan"]))

        # 5. Verifikasi 100% kelengkapan Kode Model Pabrikan & 0 NaN di CSV
        self.assertEqual((df["Kode Model Pabrikan"] != "-").sum(), 402, "Seluruh 402 model harus memiliki Kode Model Pabrikan")
        self.assertEqual(df.isna().sum().sum(), 0, "CSV tidak boleh memiliki sel NaN")

if __name__ == "__main__":
    unittest.main()
