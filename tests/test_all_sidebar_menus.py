import unittest
from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant, ScrapedListing
from analytics.pricing_engine import SmartphonePricingEngine
from analytics.depreciation_engine import SmartphoneDepreciationEngine

class TestAllSidebarMenus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()
        cls.db = SessionLocal()
        cls.engine = SmartphonePricingEngine(cls.db)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_menu_1_market_overview(self):
        total_listings = self.db.query(ScrapedListing).count()
        valid_cash = self.db.query(ScrapedListing).filter(ScrapedListing.is_dp_price == False).count()
        self.assertGreater(total_listings, 0)
        self.assertGreater(valid_cash, 0)

        # Query Brand share
        query_brand = self.db.query(
            MasterBrand.name,
            ScrapedListing.price
        ).join(MasterModel, MasterModel.brand_id == MasterBrand.id)\
         .join(MasterVariant, MasterVariant.model_id == MasterModel.id)\
         .join(ScrapedListing, ScrapedListing.matched_variant_id == MasterVariant.id)\
         .filter(ScrapedListing.is_dp_price == False).all()
        self.assertGreater(len(query_brand), 0)

    def test_menu_2_fmv_calculator(self):
        brands = [b.name for b in self.db.query(MasterBrand).order_by(MasterBrand.name).all()]
        for b_name in brands:
            brand_obj = self.db.query(MasterBrand).filter(MasterBrand.name == b_name).first()
            models = self.db.query(MasterModel).filter(MasterModel.brand_id == brand_obj.id).all()
            for m_obj in models:
                variants = self.db.query(MasterVariant).filter(MasterVariant.model_id == m_obj.id).all()
                for v_obj in variants:
                    stats = self.engine.calculate_variant_pricing_stats(v_obj.id)
                    msrp = float(v_obj.official_msrp_new)
                    base_fmv = stats["price_median"] if stats else msrp * 0.7
                    
                    hedonic = self.engine.calculate_hedonic_adjusted_price(
                        base_fmv=base_fmv,
                        warranty_type="Resmi Indonesia (iBox/SEIN/TAM)",
                        imei_status="IMEI Kemenperin Permanen"
                    )
                    self.assertGreater(hedonic["adjusted_price"], 0)

    def test_menu_3_price_corridors(self):
        variants = self.db.query(MasterVariant).all()
        stats_map = self.engine.get_all_variant_stats_map()
        self.assertIsInstance(stats_map, dict)
        self.assertGreater(len(stats_map), 0)

    def test_menu_4_arbitrage_radar(self):
        deals = self.engine.find_hot_deals(discount_threshold_pct=12.0)
        self.assertIsInstance(deals, list)
        self.assertGreater(len(deals), 0)

    def test_menu_5_spec_matrix(self):
        all_models = self.db.query(MasterModel, MasterBrand).join(MasterBrand, MasterModel.brand_id == MasterBrand.id).all()
        model_choice_map = {f"{b.name} {m.name} ({m.release_year})": m.id for m, b in all_models}
        
        for key, m_id in model_choice_map.items():
            model = self.db.query(MasterModel).filter(MasterModel.id == m_id).first()
            self.assertIsNotNone(model)
            self.assertIsNotNone(model.name)

    def test_menu_6_data_explorer(self):
        valid_items = self.db.query(ScrapedListing).filter(ScrapedListing.is_dp_price == False).limit(50).all()
        scam_items = self.db.query(ScrapedListing).filter(ScrapedListing.is_dp_price == True).limit(50).all()
        self.assertGreater(len(valid_items), 0)
        self.assertGreater(len(scam_items), 0)

if __name__ == "__main__":
    unittest.main()
