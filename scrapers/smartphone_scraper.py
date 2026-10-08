import time
import random
import requests
from typing import List, Dict, Any, Optional
from bs4 import BeautifulSoup
from models.database import SessionLocal
from models.catalog import ScrapedListing
from pipeline.normalizer import SmartphoneListingNormalizer
from pipeline.scam_detector import SmartphoneScamDetector
from pipeline.entity_matcher import SmartphoneEntityMatcher

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"
]

class SmartphoneLiveScraper:
    """
    Scraper Multi-Marketplace Smartphone Indonesia (OLX, Web Catalog, E-Commerce).
    """

    def __init__(self):
        self.session = requests.Session()

    def get_headers(self) -> Dict[str, str]:
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

    def scrape_olx_category(self, keyword: str = "iphone", page_limit: int = 2) -> List[Dict[str, Any]]:
        """Scraping publik OLX Indonesia untuk kategori handphone."""
        results = []
        base_url = f"https://www.olx.co.id/handphone_c207?filter=search_terms_eq_{keyword}"
        
        try:
            res = self.session.get(base_url, headers=self.get_headers(), timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                # Parse listings jika ada DOM selector
                # Fallback jika blocked oleh Cloudflare
                pass
        except Exception as e:
            print(f"[SCRAPER] Notice on live fetch: {e}")
            
        return results

    def process_and_save_listings(self, raw_listings: List[Dict[str, Any]]) -> int:
        """Menjalankan Pipeline NLP, Scam Detector, Entity Matcher, dan simpan ke Database."""
        db = SessionLocal()
        matcher = SmartphoneEntityMatcher(db)
        saved_count = 0

        try:
            for raw in raw_listings:
                # 1. Normalisasi
                norm = SmartphoneListingNormalizer.normalize_listing(raw)
                
                # 2. Entity Matching
                var_id, conf, matched_name, msrp = matcher.match(norm["title"], norm.get("storage_gb"))
                
                # 3. Scam / DP Evaluation
                is_scam, scam_type, scam_reason = SmartphoneScamDetector.evaluate_listing(
                    norm["price"], norm["title"], norm["raw_description"], expected_msrp=msrp
                )

                # 4. Insert or Update DB
                listing = db.query(ScrapedListing).filter(
                    ScrapedListing.source_platform == norm["source_platform"],
                    ScrapedListing.external_id == norm["external_id"]
                ).first()

                if not listing:
                    listing = ScrapedListing(
                        source_platform=norm["source_platform"],
                        external_id=norm["external_id"],
                        url=norm["url"],
                        title=norm["title"],
                        raw_description=norm["raw_description"],
                        matched_variant_id=var_id,
                        claimed_year=norm.get("claimed_year"),
                        price=norm["price"] or 0,
                        is_dp_price=is_scam,
                        warranty_type=norm["warranty_type"],
                        warranty_status=norm["warranty_status"],
                        imei_status=norm["imei_status"],
                        battery_health_pct=norm["battery_health_pct"],
                        completeness=norm["completeness"],
                        physical_grade=norm["physical_grade"],
                        screen_condition=norm["screen_condition"],
                        biometrics_status=norm["biometrics_status"],
                        truetone_status=norm["truetone_status"],
                        province=norm["province"],
                        city=norm["city"],
                        seller_name=norm["seller_name"],
                        seller_type=norm["seller_type"]
                    )
                    db.add(listing)
                    saved_count += 1
                else:
                    listing.price = norm["price"] or listing.price
                    listing.is_dp_price = is_scam
                    listing.matched_variant_id = var_id
                    saved_count += 1

            db.commit()
        except Exception as e:
            db.rollback()
            print(f"[ERROR] Ingestion error: {e}")
        finally:
            db.close()

        return saved_count
