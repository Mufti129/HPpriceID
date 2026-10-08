import os
import sys
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy.orm import Session

# Setup Path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant, ScrapedListing, MarketPriceStats
from analytics.pricing_engine import SmartphonePricingEngine
from analytics.depreciation_engine import SmartphoneDepreciationEngine
from pipeline.normalizer import SmartphoneListingNormalizer
from pipeline.scam_detector import SmartphoneScamDetector
from data.master_catalog_seed import seed_master_catalog
from scrapers.generate_synthetic_data import generate_realistic_market_dataset

# Page Config
st.set_page_config(
    page_title="PhonePrice ID — Smartphone Intelligence & Valuation Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Responsive & Clean Styling
st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 100%;
    }
    .main-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: -0.02em;
        margin-bottom: 4px;
    }
    .sub-header {
        font-size: 0.95rem;
        color: #475569;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    /* Responsive Metric Card Grid */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 16px;
        margin-bottom: 24px;
    }
    .metric-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        justifyContent: space-between;
    }
    .metric-box-title {
        font-size: 0.82rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }
    .metric-box-val {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.2;
    }
    .metric-box-sub {
        font-size: 0.8rem;
        color: #2563EB;
        font-weight: 500;
        margin-top: 4px;
    }
    
    /* Spec Card */
    .spec-card {
        background: #F8FAFC;
        border: 1px solid #CBD5E1;
        border-radius: 8px;
        padding: 18px;
        height: 100%;
    }
    .spec-card h4 {
        margin-top: 0;
        color: #1E293B;
        font-size: 1.05rem;
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 8px;
    }
    
    /* Valuation Banner */
    .valuation-banner {
        background: linear-gradient(135deg, #1E3A8A 0%, #0F172A 100%);
        color: #FFFFFF;
        padding: 20px 24px;
        border-radius: 8px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .valuation-banner h3 {
        color: #93C5FD;
        margin: 0;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .valuation-banner .price-main {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
        margin: 6px 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource(show_spinner="Inisialisasi Database & Master Katalog...")
def ensure_database_ready():
    """Memastikan database terinisialisasi dan terisi data."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(MasterVariant).count() == 0:
            seed_master_catalog()
            generate_realistic_market_dataset(target_count_per_variant=15)
        elif db.query(ScrapedListing).count() == 0:
            generate_realistic_market_dataset(target_count_per_variant=15)
    except Exception as e:
        print(f"[WARN] Error on DB init: {e}")
    finally:
        db.close()
    return True

# Ensure DB is warmed up
ensure_database_ready()

def get_db():
    return SessionLocal()

# Sidebar Navigation
st.sidebar.title("PhonePrice ID")
st.sidebar.caption("System Version 2.0 • Smartphone Valuation & Market Intelligence")

menu = st.sidebar.radio(
    "PILIH MODUL ANALISIS:",
    [
        "Market Overview & Dashboard",
        "FMV & Hedonic Calculator",
        "3-Tier Price Corridors & Quantiles",
        "Arbitrage & Hot Deals Radar",
        "Spec Matrix & Model Comparison",
        "Data Explorer & Scam Filter"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **Metodologi Valuasi:**
    1. **NLP Text Extractor:** Ekstraksi spesifikasi, legalitas IMEI Kemenperin/Bea Cukai, garansi iBox/SEIN/Inter, Battery Health %, dan kelengkapan.
    2. **Tukey IQR Filter:** Eliminasi harga outlier dan perangkap iklan cicilan/DP semu.
    3. **Lancaster Hedonic Valuation:** Penyesuaian nilai wajar berbasis kondisi riil fisik, panel display, baterai, dan sinyal.
    """
)

# ==========================================
# 1. MARKET OVERVIEW & DASHBOARD
# ==========================================
if menu == "Market Overview & Dashboard":
    st.markdown('<div class="main-header">Smartphone Market Intelligence Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Analisis komprehensif pasar smartphone sekunder Indonesia (Harga Pasar Wajar, Depresiasi, dan Distribusi Merk 2010-2026).</div>', unsafe_allow_html=True)

    try:
        with get_db() as db:
            total_listings = db.query(ScrapedListing).count()
            valid_cash_listings = db.query(ScrapedListing).filter(ScrapedListing.is_dp_price == False).count()
            scam_listings = total_listings - valid_cash_listings
            total_brands = db.query(MasterBrand).count()
            total_models = db.query(MasterModel).count()
            total_variants = db.query(MasterVariant).count()

            pct_valid = (valid_cash_listings / max(1, total_listings)) * 100
            pct_scam = (scam_listings / max(1, total_listings)) * 100

            st.markdown(f"""
            <div class="metric-grid">
                <div class="metric-box">
                    <div class="metric-box-title">Total Database Listing</div>
                    <div class="metric-box-val">{total_listings:,}</div>
                    <div class="metric-box-sub">Snapshot Pasar Aktif</div>
                </div>
                <div class="metric-box">
                    <div class="metric-box-title">Listing Tunai Valid</div>
                    <div class="metric-box-val">{valid_cash_listings:,}</div>
                    <div class="metric-box-sub" style="color:#16A34A;">{pct_valid:.1f}% Bebas Anomali</div>
                </div>
                <div class="metric-box">
                    <div class="metric-box-title">DP Trap & HDC Filtered</div>
                    <div class="metric-box-val">{scam_listings:,}</div>
                    <div class="metric-box-sub" style="color:#DC2626;">{pct_scam:.1f}% Iklan Semu Tersaring</div>
                </div>
                <div class="metric-box">
                    <div class="metric-box-title">Katalog 2010-2026</div>
                    <div class="metric-box-val">{total_models} Model</div>
                    <div class="metric-box-sub">{total_variants} Varian Terdaftar</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("---")

            col_left, col_right = st.columns(2)

            with col_left:
                st.subheader("Distribusi Listing per Merk")
                query_brand = db.query(
                    MasterBrand.name,
                    ScrapedListing.price
                ).join(MasterModel, MasterModel.brand_id == MasterBrand.id)\
                 .join(MasterVariant, MasterVariant.model_id == MasterModel.id)\
                 .join(ScrapedListing, ScrapedListing.matched_variant_id == MasterVariant.id)\
                 .filter(ScrapedListing.is_dp_price == False).all()

                if query_brand:
                    df_brand = pd.DataFrame(query_brand, columns=["Brand", "Price"])
                    brand_summary = df_brand.groupby("Brand").agg(
                        Count=("Price", "count"),
                        Avg_Price=("Price", "mean")
                    ).reset_index()

                    fig_brand = px.pie(
                        brand_summary, values="Count", names="Brand",
                        title="Pangsa Pasar Volume Listing Berdasarkan Brand",
                        hole=0.4,
                        color_discrete_sequence=px.colors.qualitative.Safe
                    )
                    fig_brand.update_layout(margin=dict(t=40, b=20, l=20, r=20))
                    st.plotly_chart(fig_brand, use_container_width=True)
                else:
                    st.info("Data listing sedang dipersiapkan.")

            with col_right:
                st.subheader("Kurva Depresiasi Nilai Pasar (MSRP vs Resale)")
                variants = db.query(
                    MasterVariant.id,
                    MasterVariant.variant_name,
                    MasterVariant.official_msrp_new,
                    MasterModel.name.label("model_name"),
                    MasterBrand.name.label("brand_name"),
                    MasterModel.release_year
                ).join(MasterModel, MasterVariant.model_id == MasterModel.id)\
                 .join(MasterBrand, MasterModel.brand_id == MasterBrand.id).all()

                pricing_engine = SmartphonePricingEngine(db)
                depr_rows = []
                for var in variants:
                    stats = pricing_engine.calculate_variant_pricing_stats(var.id)
                    msrp = float(var.official_msrp_new)
                    if stats and stats["sample_count"] >= 2:
                        fmv = stats["price_median"]
                    else:
                        ret = SmartphoneDepreciationEngine.calculate_theoretical_retention(
                            var.brand_name, var.model_name, var.release_year, current_year=2026
                        )
                        fmv = msrp * ret

                    depr_pct = SmartphoneDepreciationEngine.calculate_real_depreciation(msrp, fmv)
                    depr_rows.append({
                        "Brand": var.brand_name,
                        "Model": var.model_name,
                        "Variant": var.variant_name,
                        "Year": var.release_year,
                        "MSRP": msrp,
                        "FMV": fmv,
                        "Depreciation_Pct": depr_pct
                    })

                if depr_rows:
                    df_depr = pd.DataFrame(depr_rows)
                    fig_depr = px.scatter(
                        df_depr, x="MSRP", y="FMV", color="Brand", size="Depreciation_Pct",
                        hover_data=["Variant", "Year", "Depreciation_Pct"],
                        title="Perbandingan MSRP Peluncuran Baru vs Fair Market Value Saat Ini",
                        labels={"MSRP": "Harga MSRP Baru (IDR)", "FMV": "Harga Pasar Wajar (FMV IDR)"}
                    )
                    fig_depr.update_layout(margin=dict(t=40, b=20, l=20, r=20))
                    st.plotly_chart(fig_depr, use_container_width=True)
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Dashboard: {e}")

# ==========================================
# 2. FMV & HEDONIC CALCULATOR
# ==========================================
elif menu == "FMV & Hedonic Calculator":
    st.markdown('<div class="main-header">Fair Market Value & Hedonic Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Perhitungan valuasi harga pasar wajar dengan penyesuaian kualitas riil: Status IMEI, Garansi Resmi vs Inter, Battery Health, Layar & Biometrik.</div>', unsafe_allow_html=True)

    try:
        with get_db() as db:
            brands = [b.name for b in db.query(MasterBrand).order_by(MasterBrand.name).all()]
            if not brands:
                brands = ["Apple"]

            col_select1, col_select2, col_select3 = st.columns(3)
            with col_select1:
                selected_brand = st.selectbox("Pilih Merk Smartphone:", brands)

            brand_obj = db.query(MasterBrand).filter(MasterBrand.name == selected_brand).first()
            models = db.query(MasterModel).filter(MasterModel.brand_id == brand_obj.id).order_by(MasterModel.release_year.desc()).all() if brand_obj else []
            model_names = [m.name for m in models] if models else ["-"]

            with col_select2:
                selected_model_name = st.selectbox("Pilih Model:", model_names)

            model_obj = next((m for m in models if m.name == selected_model_name), models[0] if models else None)
            variants = db.query(MasterVariant).filter(MasterVariant.model_id == model_obj.id).all() if model_obj else []
            variant_dict = {v.variant_name: v for v in variants}

            with col_select3:
                selected_variant_name = st.selectbox("Pilih Varian Storage/RAM:", list(variant_dict.keys()) if variant_dict else ["-"])

            st.markdown("---")

            selected_var_obj = variant_dict.get(selected_variant_name)

            if selected_var_obj and model_obj:
                col_specs, col_inputs = st.columns([1.1, 1.9])

                with col_specs:
                    st.markdown(f"""
                    <div class="spec-card">
                        <h4>Spesifikasi Bawaan Pabrik</h4>
                        <p><strong>Merk & Model:</strong> {selected_brand} {model_obj.name}</p>
                        <p><strong>Tahun Peluncuran:</strong> {model_obj.release_year}</p>
                        <p><strong>Harga Rilis Resmi (MSRP):</strong> Rp {float(selected_var_obj.official_msrp_new):,.0f}</p>
                        <p><strong>Chipset / SoC:</strong> {model_obj.chipset or '-'}</p>
                        <p><strong>Kapasitas Memori:</strong> {selected_var_obj.ram_gb or '-'} GB RAM / {selected_var_obj.storage_gb} GB ROM</p>
                        <p><strong>Display Panel:</strong> {model_obj.display_type or '-'} ({model_obj.refresh_rate_hz}Hz)</p>
                        <p><strong>Resolusi Layar:</strong> {model_obj.resolution or '-'}</p>
                        <p><strong>Kamera Utama:</strong> {model_obj.main_camera_mp or '-'}</p>
                        <p><strong>Baterai & Charging:</strong> {model_obj.battery_capacity_mah or '-'} mAh ({model_obj.fast_charging_watt}W)</p>
                        <p><strong>Konektivitas & IP:</strong> {model_obj.network_gen} | NFC: {'Ya' if model_obj.has_nfc else 'Tidak'} | {model_obj.ip_rating}</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col_inputs:
                    st.markdown("### Atribut Kualitas & Kondisi Fisik Unit")
                    
                    c_in1, c_in2 = st.columns(2)
                    with c_in1:
                        w_type = st.selectbox("Asal Distribusi & Garansi:", [
                            "Resmi Indonesia (iBox/SEIN/TAM)",
                            "Ex-Inter Pajak Bea Cukai",
                            "Ex-Inter Non-Pajak",
                            "Garansi Distributor"
                        ])
                        w_status = st.selectbox("Status Garansi Pabrik:", [
                            "Habis (Ex-Resmi)",
                            "Aktif (Masih Garansi)",
                            "Garansi Toko 1 Bulan"
                        ])
                        imei_status = st.selectbox("Status Sinyal & IMEI:", [
                            "IMEI Kemenperin Permanen",
                            "IMEI Bea Cukai All Operator",
                            "IMEI 3 Bulan / Smartfren Only",
                            "Wifi Only / Sinyal Blokir"
                        ])
                        comp = st.selectbox("Kelengkapan Unit:", [
                            "Fullset Original (Box+Kabel+Nota)",
                            "Fullset OEM",
                            "Batangan / Unit Only"
                        ])

                    with c_in2:
                        grade = st.selectbox("Grade Fisik Bodi:", [
                            "Grade A+ (Like New 99%)",
                            "Grade A (Mulus 95%)",
                            "Grade B (Lecet Wajar)",
                            "Grade C (Dent/Baret)"
                        ])
                        screen = st.selectbox("Kondisi Layar Display:", [
                            "Normal Original",
                            "Layar Ganti (OLED OEM/Incell)",
                            "Shadow Tipis",
                            "Shadow Tebal",
                            "Green Line / Garis"
                        ])
                        bio = st.selectbox("Sensor Biometrik (Face ID / Touch ID):", [
                            "Normal Aktif",
                            "Face ID / Touch ID Rusak/Off"
                        ])
                        tt = st.selectbox("Sensor True Tone / Auto-Brightness:", [
                            "Aktif",
                            "Mati / Non-Aktif"
                        ])
                        
                        bh = None
                        if selected_brand == "Apple":
                            bh = st.slider("Battery Health (BH %):", min_value=50, max_value=100, value=88)

                # Kalkulasi
                engine = SmartphonePricingEngine(db)
                stats = engine.calculate_variant_pricing_stats(selected_var_obj.id)
                msrp = float(selected_var_obj.official_msrp_new)

                if stats and stats["sample_count"] >= 2:
                    base_fmv = stats["price_median"]
                    sample_txt = f"{stats['sample_count']} listing aktif di pasar sekunder"
                else:
                    retention = SmartphoneDepreciationEngine.calculate_theoretical_retention(
                        selected_brand, model_obj.name, model_obj.release_year, current_year=2026
                    )
                    base_fmv = msrp * retention
                    sample_txt = "Estimasi Model Retensi Ekonometrik (N < 2)"

                hedonic_res = engine.calculate_hedonic_adjusted_price(
                    base_fmv=base_fmv,
                    warranty_type=w_type,
                    warranty_status=w_status,
                    imei_status=imei_status,
                    battery_health=bh,
                    completeness=comp,
                    physical_grade=grade,
                    screen_condition=screen,
                    biometrics=bio,
                    truetone=tt
                )

                st.markdown(f"""
                <div class="valuation-banner">
                    <h3>Rekomendasi Valuasi Nilai Pasar Wajar (Final Adjusted)</h3>
                    <div class="price-main">Rp {hedonic_res['adjusted_price']:,.0f}</div>
                    <div>Base FMV: Rp {base_fmv:,.0f} ({sample_txt}) | Penyesuaian Hedonik: {hedonic_res['net_adjustment_pct']:+.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

                res_c1, res_c2, res_c3 = st.columns(3)
                with res_c1:
                    st.metric("Base Fair Market Value", f"Rp {base_fmv:,.0f}")
                with res_c2:
                    st.metric("Net Penyesuaian Hedonik", f"{hedonic_res['net_adjustment_pct']:+.1f}%", f"Rp {(hedonic_res['adjusted_price'] - base_fmv):,.0f}")
                with res_c3:
                    depr_final = SmartphoneDepreciationEngine.calculate_real_depreciation(msrp, hedonic_res['adjusted_price'])
                    st.metric("Penyusutan Nilai dari MSRP", f"{depr_final:.1f}%")

                if hedonic_res["adjustment_breakdown"]:
                    st.markdown("##### Rincian Penyesuaian Atribut:")
                    for desc, pct in hedonic_res["adjustment_breakdown"]:
                        st.write(f"- {desc}: **{pct*100:+.1f}%**")
            else:
                st.warning("Silakan pilih model dan varian smartphone yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul FMV Calculator: {e}")

# ==========================================
# 3. 3-TIER PRICE CORRIDORS & QUANTILES
# ==========================================
elif menu == "3-Tier Price Corridors & Quantiles":
    st.markdown('<div class="main-header">3-Tier Price Corridors & Quantiles</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Monitoring koridor harga 3-tingkat (P25 Target Beli Murah, FMV Median, dan P75 Unit Pristine) untuk seluruh varian smartphone.</div>', unsafe_allow_html=True)

    try:
        with get_db() as db:
            variants = db.query(
                MasterVariant.id,
                MasterVariant.variant_name,
                MasterVariant.official_msrp_new,
                MasterModel.name.label("model_name"),
                MasterBrand.name.label("brand_name"),
                MasterModel.release_year
            ).join(MasterModel, MasterVariant.model_id == MasterModel.id)\
             .join(MasterBrand, MasterModel.brand_id == MasterBrand.id)\
             .order_by(MasterModel.release_year.desc(), MasterBrand.name).all()

            engine = SmartphonePricingEngine(db)
            table_rows = []

            for var in variants:
                stats = engine.calculate_variant_pricing_stats(var.id)
                msrp = float(var.official_msrp_new)
                
                if stats and stats["sample_count"] >= 2:
                    p25 = stats["price_p25"]
                    fmv = stats["price_median"]
                    p75 = stats["price_p75"]
                    sample_n = stats["sample_count"]
                else:
                    ret = SmartphoneDepreciationEngine.calculate_theoretical_retention(
                        var.brand_name, var.model_name, var.release_year, current_year=2026
                    )
                    fmv = msrp * ret
                    p25 = fmv * 0.92
                    p75 = fmv * 1.08
                    sample_n = 0

                depr = SmartphoneDepreciationEngine.calculate_real_depreciation(msrp, fmv)

                table_rows.append({
                    "Brand": var.brand_name,
                    "Model": var.model_name,
                    "Varian & Storage": var.variant_name,
                    "Tahun": var.release_year,
                    "Sampel": f"{sample_n} Unit" if sample_n > 0 else "Model Parametrik",
                    "MSRP Baru (IDR)": f"Rp {msrp:,.0f}",
                    "P25 Bargain (IDR)": f"Rp {p25:,.0f}",
                    "FMV Median (IDR)": f"Rp {fmv:,.0f}",
                    "P75 Pristine (IDR)": f"Rp {p75:,.0f}",
                    "Depresiasi (%)": f"{depr:.1f}%",
                    "P25_num": p25,
                    "FMV_num": fmv,
                    "P75_num": p75
                })

            if table_rows:
                df_corridor = pd.DataFrame(table_rows)
                st.dataframe(
                    df_corridor[["Brand", "Model", "Varian & Storage", "Tahun", "Sampel", "MSRP Baru (IDR)", "P25 Bargain (IDR)", "FMV Median (IDR)", "P75 Pristine (IDR)", "Depresiasi (%)"]],
                    use_container_width=True,
                    hide_index=True
                )

                st.markdown("### Visualisasi Rentang Koridor Harga Pasar")
                fig_cor = go.Figure()
                subset = df_corridor.head(15)

                fig_cor.add_trace(go.Bar(
                    name="P25 Target Beli Murah",
                    x=subset["Varian & Storage"],
                    y=subset["P25_num"],
                    marker_color="#93C5FD"
                ))
                fig_cor.add_trace(go.Bar(
                    name="FMV Nilai Pasar Wajar",
                    x=subset["Varian & Storage"],
                    y=subset["FMV_num"],
                    marker_color="#2563EB"
                ))
                fig_cor.add_trace(go.Bar(
                    name="P75 Unit Pristine",
                    x=subset["Varian & Storage"],
                    y=subset["P75_num"],
                    marker_color="#1E3A8A"
                ))
                fig_cor.update_layout(barmode="group", xaxis_tickangle=-45, height=480, margin=dict(t=20, b=100, l=20, r=20))
                st.plotly_chart(fig_cor, use_container_width=True)
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Price Corridors: {e}")

# ==========================================
# 4. ARBITRAGE & HOT DEALS RADAR
# ==========================================
elif menu == "Arbitrage & Hot Deals Radar":
    st.markdown('<div class="main-header">Smartphone Arbitrage & Hot Deals Radar</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Pemindai listing smartphone sekunder dengan diskon di atas batas normal pasar (Peluang Arbitrase Reseller).</div>', unsafe_allow_html=True)

    try:
        with get_db() as db:
            disc_thresh = st.slider("Ambang Batas Minimum Diskon Arbitrase (%):", min_value=8, max_value=30, value=12)
            engine = SmartphonePricingEngine(db)
            deals = engine.find_hot_deals(discount_threshold_pct=float(disc_thresh))

            if deals:
                st.success(f"Terverifikasi {len(deals)} unit peluang hot deals & arbitrase aktif.")
                df_deals = pd.DataFrame(deals)
                
                display_df = df_deals[[
                    "deal_tier", "brand", "model", "variant", "price", "fmv_price", "discount_pct", "potential_profit", "city", "platform", "warranty_type", "imei_status"
                ]].copy()
                
                display_df.columns = [
                    "Tier Peluang", "Brand", "Model", "Varian", "Harga Listing", "FMV Pasar", "Diskon (%)", "Potensi Margin (IDR)", "Kota", "Platform", "Garansi", "IMEI / Sinyal"
                ]
                
                display_df["Harga Listing"] = display_df["Harga Listing"].apply(lambda x: f"Rp {x:,.0f}")
                display_df["FMV Pasar"] = display_df["FMV Pasar"].apply(lambda x: f"Rp {x:,.0f}")
                display_df["Potensi Margin (IDR)"] = display_df["Potensi Margin (IDR)"].apply(lambda x: f"Rp {x:,.0f}")
                display_df["Diskon (%)"] = display_df["Diskon (%)"].apply(lambda x: f"{x:.1f}%")

                st.dataframe(display_df, use_container_width=True, hide_index=True)
            else:
                st.info(f"Tidak ada listing yang memenuhi kriteria diskon >= {disc_thresh}%.")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Arbitrage Radar: {e}")

# ==========================================
# 5. SPEC MATRIX & MODEL COMPARISON
# ==========================================
elif menu == "Spec Matrix & Model Comparison":
    st.markdown('<div class="main-header">Smartphone Hardware Spec Matrix</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Bandingkan spesifikasi teknis mendalam antar model smartphone secara berdampingan (2010 - 2026).</div>', unsafe_allow_html=True)

    try:
        with get_db() as db:
            all_models = db.query(MasterModel, MasterBrand).join(MasterBrand, MasterModel.brand_id == MasterBrand.id).order_by(MasterModel.release_year.desc(), MasterBrand.name).all()
            
            model_choice_map = {
                f"{b.name} {m.name} ({m.release_year})": m.id
                for m, b in all_models
            }
            choice_keys = list(model_choice_map.keys())

            col_c1, col_c2 = st.columns(2)
            with col_c1:
                dev1_key = st.selectbox("Pilih Smartphone 1:", choice_keys, index=0 if choice_keys else 0)
            with col_c2:
                dev2_key = st.selectbox("Pilih Smartphone 2:", choice_keys, index=min(1, len(choice_keys)-1) if choice_keys else 0)

            if dev1_key and dev2_key:
                id1 = model_choice_map[dev1_key]
                id2 = model_choice_map[dev2_key]
                
                m1 = db.query(MasterModel).filter(MasterModel.id == id1).first()
                m2 = db.query(MasterModel).filter(MasterModel.id == id2).first()

                if m1 and m2:
                    spec_data = {
                        "Parameter Spesifikasi Hardware": [
                            "Tahun Peluncuran", "Chipset / SoC", "CPU Cores & Arch", "GPU Grafis", "Antutu Benchmark Score",
                            "Tipe Layar", "Ukuran Layar", "Refresh Rate", "Resolusi Display", "Peak Brightness",
                            "Kamera Belakang Utama", "Konfigurasi Kamera", "OIS & Zoom Optik", "Kamera Depan (Selfie)",
                            "Kapasitas Baterai", "Fast Charging Kabel", "Wireless Charging", "Konektivitas & NFC", "Sertifikasi IP Rating", "Berat Bodi"
                        ],
                        dev1_key: [
                            m1.release_year, m1.chipset or "-", m1.cpu_architecture or "-", m1.gpu or "-", f"{m1.antutu_benchmark_score:,}" if m1.antutu_benchmark_score else "-",
                            m1.display_type or "-", f"{m1.screen_size_inch} inci" if m1.screen_size_inch else "-", f"{m1.refresh_rate_hz} Hz", m1.resolution or "-", f"{m1.peak_brightness_nits} nits" if m1.peak_brightness_nits else "-",
                            m1.main_camera_mp or "-", m1.camera_setup or "-", f"OIS: {'Ya' if m1.has_ois else 'Tidak'} | {m1.optical_zoom_level or 'None'}", m1.selfie_camera_mp or "-",
                            f"{m1.battery_capacity_mah} mAh" if m1.battery_capacity_mah else "-", f"{m1.fast_charging_watt} Watt", f"{'Ya (' + str(m1.wireless_charging_watt) + 'W)' if m1.has_wireless_charging else 'Tidak'}",
                            f"{m1.network_gen} | NFC: {'Ya' if m1.has_nfc else 'Tidak'}", m1.ip_rating or "-", f"{m1.weight_grams} gram" if m1.weight_grams else "-"
                        ],
                        dev2_key: [
                            m2.release_year, m2.chipset or "-", m2.cpu_architecture or "-", m2.gpu or "-", f"{m2.antutu_benchmark_score:,}" if m2.antutu_benchmark_score else "-",
                            m2.display_type or "-", f"{m2.screen_size_inch} inci" if m2.screen_size_inch else "-", f"{m2.refresh_rate_hz} Hz", m2.resolution or "-", f"{m2.peak_brightness_nits} nits" if m2.peak_brightness_nits else "-",
                            m2.main_camera_mp or "-", m2.camera_setup or "-", f"OIS: {'Ya' if m2.has_ois else 'Tidak'} | {m2.optical_zoom_level or 'None'}", m2.selfie_camera_mp or "-",
                            f"{m2.battery_capacity_mah} mAh" if m2.battery_capacity_mah else "-", f"{m2.fast_charging_watt} Watt", f"{'Ya (' + str(m2.wireless_charging_watt) + 'W)' if m2.has_wireless_charging else 'Tidak'}",
                            f"{m2.network_gen} | NFC: {'Ya' if m2.has_nfc else 'Tidak'}", m2.ip_rating or "-", f"{m2.weight_grams} gram" if m2.weight_grams else "-"
                        ]
                    }

                    df_spec = pd.DataFrame(spec_data)
                    st.dataframe(df_spec.set_index("Parameter Spesifikasi Hardware"), use_container_width=True)
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Spec Matrix: {e}")

# ==========================================
# 6. DATA EXPLORER & SCAM FILTER
# ==========================================
elif menu == "Data Explorer & Scam Filter":
    st.markdown('<div class="main-header">Live Data Explorer & Scam Filter Monitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Jelajahi seluruh raw listing dan evaluasi performa filter anti-penipuan DP & HDC Palsu.</div>', unsafe_allow_html=True)

    try:
        with get_db() as db:
            filter_mode = st.radio("Status Listing:", ["Semua Listing Tunai Valid", "Hanya Terindikasi Perangkap DP / Scam", "Semua Data Mentah"], horizontal=True)

            query = db.query(ScrapedListing)
            if filter_mode == "Semua Listing Tunai Valid":
                query = query.filter(ScrapedListing.is_dp_price == False)
            elif filter_mode == "Hanya Terindikasi Perangkap DP / Scam":
                query = query.filter(ScrapedListing.is_dp_price == True)

            raw_items = query.limit(250).all()

            if raw_items:
                data_rows = []
                for it in raw_items:
                    data_rows.append({
                        "Platform": it.source_platform.upper(),
                        "Judul Iklan": it.title,
                        "Harga (IDR)": f"Rp {float(it.price):,.0f}",
                        "Status DP/Scam": "DP TRAP / ANOMALI" if it.is_dp_price else "CASH VALID",
                        "Garansi Asal": it.warranty_type,
                        "Status IMEI": it.imei_status,
                        "BH (%)": f"{it.battery_health_pct}%" if it.battery_health_pct else "-",
                        "Kelengkapan": it.completeness,
                        "Fisik": it.physical_grade,
                        "Layar": it.screen_condition,
                        "Kota": it.city
                    })
                st.dataframe(pd.DataFrame(data_rows), use_container_width=True, hide_index=True)
            else:
                st.info("Tidak ada data listing yang cocok.")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Data Explorer: {e}")
