from typing import Optional, List, Dict, Any, Tuple
from rapidfuzz import fuzz
from sqlalchemy.orm import Session
from models.catalog import MasterVariant, MasterModel, MasterBrand

class SmartphoneEntityMatcher:
    """
    Fuzzy Entity Matcher & Disambiguation Engine untuk Smartphone.
    Menghubungkan teks judul & spesifikasi listing marketplace ke Master Variant ID.
    """

    def __init__(self, db_session: Session):
        self.db = db_session
        self._variants_cache = self._load_variants()

    def _load_variants(self) -> List[Dict[str, Any]]:
        """Pre-cache master variants dengan metadata dan alias lengkap."""
        variants = self.db.query(
            MasterVariant, MasterModel, MasterBrand
        ).join(
            MasterModel, MasterVariant.model_id == MasterModel.id
        ).join(
            MasterBrand, MasterModel.brand_id == MasterBrand.id
        ).all()

        cache = []
        import re
        for var, model, brand in variants:
            alias_list = [a.strip().lower() for a in (var.aliases or "").split(",") if a.strip()]
            raw_codes = getattr(model, "factory_model_code", "") or ""
            model_codes = [c.strip().lower() for c in raw_codes.split(", ") if len(c.strip()) >= 3 and not c.strip().isdigit()]
            search_corpus = [
                f"{brand.name} {model.name} {var.variant_name}".lower(),
                f"{model.name} {var.storage_gb}gb".lower(),
                f"{model.name} {var.variant_name}".lower(),
                var.variant_name.lower()
            ] + alias_list + model_codes

            cache.append({
                "variant_id": var.id,
                "variant_name": var.variant_name,
                "model_name": model.name,
                "brand_name": brand.name,
                "storage_gb": var.storage_gb,
                "ram_gb": var.ram_gb,
                "release_year": model.release_year,
                "official_msrp": float(var.official_msrp_new) if var.official_msrp_new else None,
                "aliases_list": alias_list,
                "model_codes": model_codes,
                "search_corpus": search_corpus
            })
        return cache

    def match(
        self,
        title: str,
        storage_gb: Optional[int] = None
    ) -> Tuple[Optional[int], float, Optional[str], Optional[float]]:
        """
        Mencocokkan judul listing ke Master Variant ID.
        Returns: (variant_id, confidence_score, matched_name, official_msrp)
        """
        import re
        title_str = str(title or "")
        clean_title = title_str.lower()
        # Normalisasi singkatan umum smartphone di Indonesia
        clean_title = clean_title.replace("ip ", "iphone ").replace("ipone", "iphone").replace("ip.", "iphone ")
        clean_title = clean_title.replace("pmax", "pro max").replace("pm ", "pro max ")
        clean_title = clean_title.replace("sam ", "samsung ").replace("ss ", "samsung ")

        best_match_id = None
        best_score = 0.0
        best_name = None
        best_msrp = None

        for item in self._variants_cache:
            # 1. Cek kecocokan storage jika diekstrak
            if storage_gb and item["storage_gb"] != storage_gb:
                continue

            # 2. Cek apakah ada keyword model / brand / alias / kode model pabrikan
            brand_kw = item["brand_name"].lower()
            model_kw = item["model_name"].lower()
            code_in_title = any(re.search(rf"\b{re.escape(c)}\b", clean_title) for c in item.get("model_codes", []))
            
            # Cek relevansi awal: harus mengandung brand/alias/kode model DAN token model pembeda
            brand_in_title = brand_kw in clean_title or any(alias in clean_title for alias in item["aliases_list"])
            if not brand_in_title and model_kw not in clean_title and not code_in_title:
                continue

            model_tokens = [w for w in model_kw.replace("(", "").replace(")", "").split() if w not in {"samsung", "galaxy", "apple", "iphone", "xiaomi", "redmi", "poco", "oppo", "vivo", "realme", "infinix", "asus", "rog", "huawei", "sony", "xperia", "tecno", "nokia", "blackberry", "nothing", "phone"} and len(w) > 1]
            if model_tokens and not any(tok in clean_title for tok in model_tokens):
                continue

            # 3. Hitung score fuzzy matching
            for corpus_text in item["search_corpus"]:
                score_token = fuzz.token_set_ratio(corpus_text, clean_title)
                score_partial = fuzz.partial_ratio(corpus_text, clean_title)
                final_score = (score_token * 0.7) + (score_partial * 0.3)

                # Bonus jika storage tepat
                if str(item["storage_gb"]) in clean_title:
                    final_score += 5.0

                # High-Confidence Anchor Bonus jika kode model pabrikan tertera
                if code_in_title:
                    final_score += 15.0

                if final_score > best_score:
                    best_score = final_score
                    best_match_id = item["variant_id"]
                    best_name = f"{item['brand_name']} {item['model_name']} - {item['variant_name']}"
                    best_msrp = item["official_msrp"]

        if best_score >= 58.0:
            return best_match_id, best_score, best_name, best_msrp

        return None, 0.0, None, None
