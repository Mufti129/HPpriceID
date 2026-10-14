import unittest
from models.database import SessionLocal, init_db, get_db
from models.catalog import MasterBrand, MasterModel, MasterVariant, ScrapedListing
from pipeline.normalizer import SmartphoneListingNormalizer
from pipeline.scam_detector import SmartphoneScamDetector
from pipeline.entity_matcher import SmartphoneEntityMatcher
from analytics.pricing_engine import SmartphonePricingEngine
from analytics.depreciation_engine import SmartphoneDepreciationEngine

class TestSmartphonePipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()
        cls.db = SessionLocal()
        cls.matcher = SmartphoneEntityMatcher(cls.db)
        cls.pricing_engine = SmartphonePricingEngine(cls.db)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_nlp_normalizer_extraction(self):
        sample_title = "iPhone 13 Pro 128GB Sierra Blue iBox BH 88% mulus no minus fullset ori"
        norm = SmartphoneListingNormalizer.normalize_listing({
            "title": sample_title,
            "description": "Layar ori TrueTone on Face ID aktif sinyal aman",
            "price": "12.500.000"
        })

        self.assertEqual(norm["price"], 12500000.0)
        self.assertEqual(norm["storage_gb"], 128)
        self.assertIn("iBox", norm["warranty_type"])
        self.assertEqual(norm["battery_health_pct"], 88)
        self.assertEqual(norm["completeness"], "Fullset Original")
        self.assertEqual(norm["physical_grade"], "Grade A (Mulus 95%)")
        self.assertEqual(norm["screen_condition"], "Normal Original")
        self.assertEqual(norm["biometrics_status"], "Normal Aktif")
        self.assertEqual(norm["truetone_status"], "Aktif")

    def test_dp_scam_detector(self):
        # Test 1: DP Cicilan trap
        is_scam, cat, reason = SmartphoneScamDetector.evaluate_listing(
            price=1500000,
            title="iPhone 15 Pro Max 256GB DP Ringan Angsuran Kredivo",
            description="Promo bayar DP 1.5jt",
            expected_msrp=24999000
        )
        self.assertTrue(is_scam)
        self.assertEqual(cat, "DP_CLICKBAIT")

        # Test 2: HDC Replika
        is_scam_hdc, cat_hdc, _ = SmartphoneScamDetector.evaluate_listing(
            price=1800000,
            title="iPhone 15 Pro Max HDC Clone Supercopy 1:1",
            description="Replika mirip asli"
        )
        self.assertTrue(is_scam_hdc)
        self.assertEqual(cat_hdc, "FAKE_HDC_REPLICA")

    def test_entity_matcher(self):
        var_id, conf, name, msrp = self.matcher.match("ip 15 pro max 256gb natural titanium", storage_gb=256)
        self.assertIsNotNone(var_id)
        self.assertGreaterEqual(conf, 70.0)
        self.assertIn("iPhone 15 Pro Max", name)

    def test_hedonic_valuation_adjustments(self):
        base_fmv = 10000000.0
        
        # Test unit wifi only / sinyal blokir
        res_blocked = self.pricing_engine.calculate_hedonic_adjusted_price(
            base_fmv=base_fmv,
            imei_status="Wifi Only / Sinyal Blokir"
        )
        self.assertLess(res_blocked["adjusted_price"], base_fmv)
        self.assertAlmostEqual(res_blocked["net_adjustment_pct"], -40.0, places=1)

        # Test unit istimewa like new dengan BH 100%
        res_pristine = self.pricing_engine.calculate_hedonic_adjusted_price(
            base_fmv=base_fmv,
            battery_health=100,
            physical_grade="Grade A+ (Like New 99%)"
        )
        self.assertGreater(res_pristine["adjusted_price"], base_fmv)

    def test_depreciation_engine(self):
        retention_apple = SmartphoneDepreciationEngine.calculate_theoretical_retention(
            "Apple", "iPhone 15 Pro Max", release_year=2023, current_year=2026
        )
        retention_mid = SmartphoneDepreciationEngine.calculate_theoretical_retention(
            "Xiaomi", "Redmi Note 13", release_year=2023, current_year=2026
        )
        # Apple harus memiliki nilai retensi lebih tinggi dibanding Android midrange
        self.assertGreater(retention_apple, retention_mid)

        # Perangkat vintage (>8 tahun) harus menyusut ke nilai residu/koleksi (5-15%)
        retention_vintage_iphone = SmartphoneDepreciationEngine.calculate_theoretical_retention(
            "Apple", "iPhone 4", release_year=2010, current_year=2026
        )
        retention_vintage_samsung = SmartphoneDepreciationEngine.calculate_theoretical_retention(
            "Samsung", "Galaxy S2", release_year=2011, current_year=2026
        )
        self.assertLessEqual(retention_vintage_iphone, 0.15)
        self.assertGreaterEqual(retention_vintage_iphone, 0.05)
        self.assertLessEqual(retention_vintage_samsung, 0.10)
        self.assertGreaterEqual(retention_vintage_samsung, 0.04)

    def test_nlp_normalizer_null_safety(self):
        # Must not raise exceptions on None or empty values
        norm_none = SmartphoneListingNormalizer.normalize_listing({})
        self.assertIsNone(norm_none["price"])
        self.assertEqual(norm_none["warranty_type"], "Resmi Indonesia (iBox/SEIN/TAM)")

        # Direct function calls with None
        self.assertIsNone(SmartphoneListingNormalizer.extract_storage(None))
        self.assertIsNone(SmartphoneListingNormalizer.extract_ram(None))
        self.assertIsNone(SmartphoneListingNormalizer.extract_battery_health(None))
        w_type, w_stat = SmartphoneListingNormalizer.extract_warranty(None)
        self.assertEqual(w_type, "Resmi Indonesia (iBox/SEIN/TAM)")
        self.assertEqual(SmartphoneListingNormalizer.extract_imei_status(None, None), "IMEI Bea Cukai All Operator")
        self.assertEqual(SmartphoneListingNormalizer.extract_completeness(None), "Fullset Original")
        self.assertEqual(SmartphoneListingNormalizer.extract_physical_grade(None), "Grade A (Mulus 95%)")
        self.assertEqual(SmartphoneListingNormalizer.extract_screen_condition(None), "Normal Original")
        bio, tt = SmartphoneListingNormalizer.extract_biometrics_and_truetone(None)
        self.assertEqual(bio, "Normal Aktif")
        self.assertEqual(tt, "Aktif")

    def test_hedonic_null_safety(self):
        # Must gracefully handle None inputs without raising TypeError
        res = self.pricing_engine.calculate_hedonic_adjusted_price(
            base_fmv=None,
            warranty_type=None,
            warranty_status=None,
            imei_status=None,
            battery_health="invalid",
            completeness=None,
            physical_grade=None,
            screen_condition=None,
            biometrics=None,
            truetone=None
        )
        self.assertEqual(res["base_fmv"], 0.0)
        self.assertEqual(res["adjusted_price"], 0.0)

        # Non-zero base_fmv with None strings
        res2 = self.pricing_engine.calculate_hedonic_adjusted_price(
            base_fmv=5_000_000,
            imei_status=None,
            warranty_type=None,
            physical_grade=None
        )
        self.assertEqual(res2["base_fmv"], 5_000_000.0)
        self.assertGreater(res2["adjusted_price"], 0.0)

    def test_case_insensitive_city_pricing(self):
        # Test case insensitivity of city filter
        first_variant = self.db.query(MasterVariant).first()
        self.assertIsNotNone(first_variant)

        stats_lower = self.pricing_engine.calculate_variant_pricing_stats(first_variant.id, city="jakarta selatan")
        stats_upper = self.pricing_engine.calculate_variant_pricing_stats(first_variant.id, city="JAKARTA SELATAN")
        stats_mixed = self.pricing_engine.calculate_variant_pricing_stats(first_variant.id, city=" Jakarta Selatan ")

        if stats_lower and stats_upper:
            self.assertEqual(stats_lower["sample_count"], stats_upper["sample_count"])
            self.assertEqual(stats_lower["price_median"], stats_upper["price_median"])
        if stats_mixed and stats_lower:
            self.assertEqual(stats_mixed["sample_count"], stats_lower["sample_count"])

    def test_adaptive_scam_detector_vintage_vs_modern(self):
        # Vintage phone at Rp 250k with expected MSRP Rp 1.5jt should NOT be marked UNREALISTIC_LOW
        is_scam_vintage, cat_vintage, reason_vintage = SmartphoneScamDetector.evaluate_listing(
            price=250_000,
            title="Nokia Lumia 520 Bekas Normal",
            description="Kondisi mulus tombol oke",
            expected_msrp=1_500_000
        )
        self.assertFalse(is_scam_vintage, f"Vintage phone should not be scam: {reason_vintage}")
        self.assertEqual(cat_vintage, "VALID_CASH")

        # Modern flagship phone at Rp 250k with expected MSRP Rp 25jt MUST be marked scam
        is_scam_modern, cat_modern, _ = SmartphoneScamDetector.evaluate_listing(
            price=250_000,
            title="iPhone 15 Pro Max 256GB Mulus",
            description="Dijual cepat butuh uang",
            expected_msrp=24_999_000
        )
        self.assertTrue(is_scam_modern)
        self.assertIn(cat_modern, ["SUSPICIOUS_ANOMALY", "UNREALISTIC_LOW", "DP_CLICKBAIT"])

    def test_database_context_manager(self):
        from models.database import get_db
        # Test normal context exit
        with get_db() as session:
            count = session.query(MasterBrand).count()
            self.assertGreater(count, 0)

        # Test rollback on exception inside context
        try:
            with get_db() as session:
                dummy_brand = MasterBrand(name="TestBrandRollbackTemp", tier_category="Test")
                session.add(dummy_brand)
                raise RuntimeError("Simulated transaction error")
        except RuntimeError:
            pass

        # Verify dummy brand was rolled back
        with get_db() as session:
            found = session.query(MasterBrand).filter(MasterBrand.name == "TestBrandRollbackTemp").first()
            self.assertIsNone(found, "Rolled back brand should not exist in database")

if __name__ == "__main__":
    unittest.main()
