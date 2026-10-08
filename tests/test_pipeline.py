import unittest
from models.database import SessionLocal, init_db
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

if __name__ == "__main__":
    unittest.main()
