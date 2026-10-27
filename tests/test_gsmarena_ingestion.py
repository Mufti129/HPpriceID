import unittest
from unittest.mock import patch, MagicMock
from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant
from scrapers.gsmarena_sync import (
    clean_text,
    parse_price_to_idr,
    GSMARENA_BRAND_SLUGS,
    ingest_gsmarena_brand_devices
)

class TestGSMArenaIngestion(unittest.TestCase):

    def setUp(self):
        init_db()
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()

    def test_schema_has_source_platform(self):
        """Pastikan model MasterModel dan MasterVariant memiliki atribut source_platform."""
        model_cols = [c.name for c in MasterModel.__table__.columns]
        variant_cols = [c.name for c in MasterVariant.__table__.columns]

        self.assertIn("source_platform", model_cols, "MasterModel harus memiliki kolom source_platform")
        self.assertIn("source_platform", variant_cols, "MasterVariant harus memiliki kolom source_platform")

    def test_database_records_have_source_platform(self):
        """Pastikan data di DB memiliki nilai source_platform terisi."""
        sample_model = self.db.query(MasterModel).filter(MasterModel.source_platform.isnot(None)).first()
        self.assertIsNotNone(sample_model, "Harus ada minimal satu model dengan source_platform tidak null")
        self.assertIn(sample_model.source_platform, ["Official Indonesia", "GSMArena"])

        sample_variant = self.db.query(MasterVariant).filter(MasterVariant.source_platform.isnot(None)).first()
        self.assertIsNotNone(sample_variant, "Harus ada minimal satu varian dengan source_platform tidak null")
        self.assertIn(sample_variant.source_platform, ["Official Indonesia", "GSMArena"])

    def test_clean_text(self):
        """Uji fungsi sanitasi teks."""
        self.assertIsNone(clean_text(None))
        self.assertIsNone(clean_text("   "))
        self.assertEqual(clean_text("  Apple   iPhone  16   "), "Apple iPhone 16")

    def test_parse_price_to_idr(self):
        """Uji konversi mata uang GSMArena ke IDR."""
        # Test EUR
        eur_price = parse_price_to_idr("About 1000 EUR")
        self.assertGreater(eur_price, 10000000)
        self.assertLess(eur_price, 30000000)

        # Test USD
        usd_price = parse_price_to_idr("$ 999.00")
        self.assertGreater(usd_price, 10000000)
        self.assertLess(usd_price, 30000000)

        # Test INR
        inr_price = parse_price_to_idr("₹ 74,999")
        self.assertGreater(inr_price, 10000000)
        self.assertLess(inr_price, 30000000)

        # Test None fallback
        fallback = parse_price_to_idr(None)
        self.assertEqual(fallback, 7999000.0)

    def test_gsmarena_brand_slugs(self):
        """Pastikan brand-brand utama memiliki mapping slug GSMArena."""
        expected_brands = ["Apple", "Samsung", "Xiaomi", "Oppo", "Vivo", "Realme", "Infinix", "Google Pixel"]
        for b in expected_brands:
            self.assertIn(b, GSMARENA_BRAND_SLUGS, f"Brand {b} harus terdaftar di GSMARENA_BRAND_SLUGS")
            self.assertTrue(GSMARENA_BRAND_SLUGS[b].endswith(".php"))

    def test_gsmarena_ingestion_mock_flow(self):
        """Uji alur auto-ingestion dengan mock HTTP request."""
        mock_brand_html = """
        <html>
            <div class="makers">
                <ul>
                    <li><a href="test_device-1234.php"><span>Test Phone X</span></a></li>
                </ul>
            </div>
        </html>
        """

        mock_device_html = """
        <html>
            <h1 class="specs-phone-name-title">Test Brand Test Phone X</h1>
            <div class="specs-photo-main"><img src="https://fdn2.gsmarena.com/vv/bigpic/test.jpg"></div>
            <table>
                <tr><td class="nfo" data-spec="year">2025, February</td></tr>
                <tr><td class="nfo" data-spec="chipset">Snapdragon 8 Gen 4</td></tr>
                <tr><td class="nfo" data-spec="cpu">Octa-core 4.3 GHz</td></tr>
                <tr><td class="nfo" data-spec="gpu">Adreno 830</td></tr>
                <tr><td class="nfo" data-spec="displaysize">6.8 inches</td></tr>
                <tr><td class="nfo" data-spec="displaytype">LTPO AMOLED, 120Hz, 3000 nits</td></tr>
                <tr><td class="nfo" data-spec="displayresolution">1440 x 3120 pixels</td></tr>
                <tr><td class="nfo" data-spec="batdescription1">5500 mAh</td></tr>
                <tr><td class="ttl">Charging</td><td class="nfo">100W wired, 50W wireless</td></tr>
                <tr><td class="nfo" data-spec="cam1modules">50 MP + 50 MP + 50 MP</td></tr>
                <tr><td class="nfo" data-spec="cam2modules">32 MP</td></tr>
                <tr><td class="nfo" data-spec="internalmemory">256GB 12GB RAM, 512GB 16GB RAM</td></tr>
                <tr><td class="nfo" data-spec="nettech">5G / LTE / GSM</td></tr>
                <tr><td class="nfo" data-spec="nfc">Yes</td></tr>
                <tr><td class="nfo" data-spec="bodyother">IP68 dust/water resistant</td></tr>
                <tr><td class="nfo" data-spec="weight">210 g</td></tr>
                <tr><td class="nfo" data-spec="os">Android 15</td></tr>
                <tr><td class="nfo" data-spec="models">A3634, A3575, A3635, iPhone18,5</td></tr>
                <tr><td class="nfo" data-spec="colors">Titanium Black, Glacier White</td></tr>
                <tr><td class="nfo" data-spec="price">About 900 EUR</td></tr>
            </table>
        </html>
        """

        def mock_get(url, *args, **kwargs):
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            if "phones-" in url:
                mock_resp.text = mock_brand_html
            else:
                mock_resp.text = mock_device_html
            return mock_resp

        with patch("requests.Session.get", side_effect=mock_get):
            res = ingest_gsmarena_brand_devices("Apple", max_devices=1, delay_sec=0)
            self.assertEqual(res["status"], "success")

            # Verifikasi model tersimpan di DB dengan source_platform = GSMArena
            model_saved = self.db.query(MasterModel).filter(MasterModel.name == "Test Phone X").first()
            if model_saved:
                self.assertEqual(model_saved.source_platform, "GSMArena")
                self.assertEqual(model_saved.chipset, "Snapdragon 8 Gen 4")
                self.assertEqual(model_saved.release_year, 2025)
                self.assertEqual(model_saved.factory_model_code, "A3634, A3575, A3635, iPhone18,5")
                
                # Verifikasi varian tersimpan
                variants_saved = self.db.query(MasterVariant).filter(MasterVariant.model_id == model_saved.id).all()
                self.assertGreaterEqual(len(variants_saved), 1)
                for var in variants_saved:
                    self.assertEqual(var.source_platform, "GSMArena")

                # Uji enrichment: jika kode model di DB berbeda, harus di-update otomatis oleh pipeline
                model_saved.factory_model_code = "A3485" # Set ke kode lama yang salah
                self.db.commit()

                # Jalankan re-ingestion / sync ulang
                res_sync = ingest_gsmarena_brand_devices("Apple", max_devices=1, delay_sec=0)
                self.db.refresh(model_saved)
                self.assertEqual(model_saved.factory_model_code, "A3634, A3575, A3635, iPhone18,5", "Pipeline harus memperbarui kode model jika berbeda dengan GSMArena")

                # Cleanup test fixture
                self.db.delete(model_saved)
                self.db.commit()

if __name__ == "__main__":
    unittest.main()
