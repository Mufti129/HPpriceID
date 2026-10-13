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

# ==============================================================================
# PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="PhonePrice ID | Smartphone Market Intelligence & Valuation",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# EXECUTIVE DARK SLATE THEME (HIGH CONTRAST & RESPONSIVE PROPORTIONS)
# ==============================================================================
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
    /* Global Typography & Canvas */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }

    .block-container {
        padding-top: 1.4rem;
        padding-bottom: 3rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 1440px;
    }

    /* Hero AppBar Header */
    .hero-appbar {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%);
        border-radius: 16px;
        padding: 24px 28px;
        color: #ffffff;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.25);
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .hero-appbar::after {
        content: "";
        position: absolute;
        top: -30px;
        right: -30px;
        width: 150px;
        height: 150px;
        background: rgba(255, 255, 255, 0.07);
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-title {
        font-size: 1.75rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin: 0;
        color: #ffffff !important;
        line-height: 1.25;
    }
    .hero-subtitle {
        font-size: 0.92rem;
        color: #dbeafe !important;
        margin-top: 6px;
        font-weight: 400;
        line-height: 1.45;
    }
    .hero-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 14px;
    }
    .hero-tag-pill {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        padding: 4px 12px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.22);
    }

    /* Proportional Metric Cards (Zero-Overflow, Balanced Slate Theme) */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 14px;
        margin-bottom: 22px;
    }
    .pro-metric-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        display: flex;
        flex-direction: column;
        justifyContent: center;
        min-width: 0;
        box-sizing: border-box;
        position: relative;
        overflow: hidden;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .pro-metric-card:hover {
        border-color: #60a5fa;
        transform: translateY(-2px);
    }
    .pro-metric-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
    }
    .pro-metric-card.emerald::before {
        background: linear-gradient(90deg, #10b981, #34d399);
    }
    .pro-metric-card.rose::before {
        background: linear-gradient(90deg, #ef4444, #f87171);
    }
    .pro-metric-card.purple::before {
        background: linear-gradient(90deg, #8b5cf6, #c084fc);
    }
    .pro-metric-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .pro-metric-val {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.55rem;
        font-weight: 800;
        color: #f8fafc;
        line-height: 1.2;
    }
    .pro-metric-sub {
        font-size: 0.76rem;
        color: #60a5fa;
        margin-top: 5px;
        font-weight: 600;
    }
    .pro-metric-sub.emerald {
        color: #34d399;
    }
    .pro-metric-sub.rose {
        color: #f87171;
    }
    .pro-metric-sub.purple {
        color: #c084fc;
    }

    /* Structured Information Callout Boxes */
    .info-box-blue {
        background: rgba(59, 130, 246, 0.10);
        border: 1px solid rgba(59, 130, 246, 0.35);
        border-left: 4px solid #3b82f6;
        padding: 16px 20px;
        border-radius: 0 10px 10px 0;
        margin-bottom: 18px;
        color: #e2e8f0;
    }
    .info-box-green {
        background: rgba(16, 185, 129, 0.10);
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-left: 4px solid #10b981;
        padding: 16px 20px;
        border-radius: 0 10px 10px 0;
        margin-bottom: 18px;
        color: #e2e8f0;
    }
    .info-box-title {
        font-size: 0.92rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 4px;
        letter-spacing: -0.01em;
    }
    .info-box-desc {
        font-size: 0.84rem;
        line-height: 1.5;
        color: #cbd5e1;
    }

    /* High Contrast Specification Card */
    .spec-card-container {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px 22px;
        color: #f8fafc;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
        height: 100%;
        box-sizing: border-box;
    }
    .spec-card-header {
        font-size: 1.05rem;
        font-weight: 700;
        color: #60a5fa;
        border-bottom: 1px solid #334155;
        padding-bottom: 10px;
        margin-bottom: 14px;
        letter-spacing: -0.01em;
    }
    .spec-item {
        display: flex;
        justify-content: space-between;
        padding: 6px 0;
        border-bottom: 1px solid rgba(51, 65, 85, 0.4);
        font-size: 0.85rem;
    }
    .spec-item-key {
        color: #94a3b8;
        font-weight: 500;
    }
    .spec-item-val {
        color: #f8fafc;
        font-weight: 600;
        text-align: right;
    }

    /* Valuation Hero Result Container */
    .val-hero-container {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1.5px solid #3b82f6;
        border-radius: 14px;
        padding: 24px 26px;
        margin-top: 18px;
        margin-bottom: 22px;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
    }
    .val-hero-title {
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #93c5fd;
        margin: 0;
    }
    .val-price-hero {
        font-family: 'JetBrains Mono', monospace;
        font-size: 2.2rem;
        font-weight: 800;
        color: #38bdf8;
        line-height: 1.15;
        margin: 8px 0;
    }
    .val-hero-meta {
        font-size: 0.84rem;
        color: #cbd5e1;
    }

    /* Sidebar Clean Styling */
    section[data-testid="stSidebar"] {
        background-color: #0b1120;
        border-right: 1px solid #1e293b;
    }
    .sidebar-brand-box {
        padding: 6px 0 14px 0;
    }
    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.02em;
    }
    .sidebar-desc {
        font-size: 0.78rem;
        color: #94a3b8;
        margin-top: 4px;
        line-height: 1.4;
    }
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.14);
        border: 1px solid rgba(16, 185, 129, 0.35);
        color: #34d399;
        font-size: 0.70rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding: 3px 10px;
        border-radius: 20px;
        margin-top: 8px;
    }
    .status-dot {
        width: 6px;
        height: 6px;
        background: #10b981;
        border-radius: 50%;
    }
</style>
""", unsafe_allow_html=True)

# Helper function for dark theme Plotly styling
def apply_dark_plotly_layout(fig, height=420):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font=dict(color="#f8fafc", family="Plus Jakarta Sans"),
        height=height,
        margin=dict(t=40, b=30, l=30, r=30),
        legend=dict(
            bgcolor="rgba(15, 23, 42, 0.6)",
            bordercolor="rgba(255, 255, 255, 0.1)",
            font=dict(color="#f8fafc")
        )
    )
    fig.update_xaxes(gridcolor="#334155", linecolor="#475569")
    fig.update_yaxes(gridcolor="#334155", linecolor="#475569")
    return fig

@st.cache_resource(show_spinner="Inisialisasi Database & Master Katalog...")
def ensure_database_ready():
    """Memastikan database terinisialisasi dan terisi katalog komprehensif 2010-2026."""
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

# ==============================================================================
# SIDEBAR NAVIGATION
# ==============================================================================
st.sidebar.markdown("""
<div class="sidebar-brand-box">
    <div class="sidebar-title">PhonePrice ID</div>
    <div class="sidebar-desc">Smartphone Market Intelligence & Hedonic Valuation Platform</div>
    <div class="status-pill">
        <span class="status-dot"></span>
        Enterprise Active
    </div>
</div>
""", unsafe_allow_html=True)

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
    1. **NLP Text Extractor:** Ekstraksi spesifikasi hardware, legalitas IMEI Kemenperin/Bea Cukai, garansi iBox/SEIN/Inter, Battery Health %, dan kelengkapan unit.
    2. **Tukey IQR Filter:** Eliminasi harga outlier ekstrem dan perangkap iklan cicilan/DP semu.
    3. **Lancaster Hedonic Valuation:** Penyesuaian nilai wajar berbasis kondisi riil fisik, panel display, baterai, dan sinyal.
    """
)

# ==============================================================================
# 1. MARKET OVERVIEW & DASHBOARD
# ==============================================================================
if menu == "Market Overview & Dashboard":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">Smartphone Market Intelligence Dashboard</div>
        <div class="hero-subtitle">
            Analisis makro pasar smartphone sekunder Indonesia: pemantauan harga pasar wajar, laju depresiasi tahunan, dan distribusi volume merk (2010 - 2026).
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">Katalog: 2010 - 2026</span>
            <span class="hero-tag-pill">Filter DP Trap & HDC</span>
            <span class="hero-tag-pill">Hedonic Pricing</span>
            <span class="hero-tag-pill">Data Valid Terverifikasi</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            <div class="kpi-grid">
                <div class="pro-metric-card">
                    <div class="pro-metric-label">Total Database Listing</div>
                    <div class="pro-metric-val">{total_listings:,}</div>
                    <div class="pro-metric-sub">Snapshot Pasar Aktif</div>
                </div>
                <div class="pro-metric-card emerald">
                    <div class="pro-metric-label">Listing Tunai Valid</div>
                    <div class="pro-metric-val">{valid_cash_listings:,}</div>
                    <div class="pro-metric-sub emerald">{pct_valid:.1f}% Bebas Anomali</div>
                </div>
                <div class="pro-metric-card rose">
                    <div class="pro-metric-label">DP Trap & HDC Filtered</div>
                    <div class="pro-metric-val">{scam_listings:,}</div>
                    <div class="pro-metric-sub rose">{pct_scam:.1f}% Iklan Semu Tersaring</div>
                </div>
                <div class="pro-metric-card purple">
                    <div class="pro-metric-label">Master Katalog 2010-2026</div>
                    <div class="pro-metric-val">{total_models} Model</div>
                    <div class="pro-metric-sub purple">{total_variants} Varian Terdaftar</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_left, col_right = st.columns(2)

            with col_left:
                st.markdown("### Pangsa Pasar Volume Listing")
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
                        title="Distribusi Volume Listing Berdasarkan Brand",
                        hole=0.45,
                        color_discrete_sequence=px.colors.qualitative.Prism
                    )
                    apply_dark_plotly_layout(fig_brand, height=400)
                    st.plotly_chart(fig_brand, use_container_width=True)
                else:
                    st.info("Data listing sedang dipersiapkan.")

            with col_right:
                st.markdown("### Kurva Depresiasi Nilai Pasar")
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
                        title="MSRP Peluncuran Baru vs Fair Market Value Saat Ini",
                        labels={"MSRP": "Harga MSRP Baru (IDR)", "FMV": "Harga Pasar Wajar (FMV IDR)"}
                    )
                    apply_dark_plotly_layout(fig_depr, height=400)
                    st.plotly_chart(fig_depr, use_container_width=True)
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Dashboard: {e}")

# ==============================================================================
# 2. FMV & HEDONIC CALCULATOR
# ==============================================================================
elif menu == "FMV & Hedonic Calculator":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">Fair Market Value & Hedonic Calculator</div>
        <div class="hero-subtitle">
            Kalkulator valuasi presisi tinggi dengan penyesuaian hedonik kualitas unit: legalitas IMEI, asal garansi resmi vs inter, Battery Health, kelengkapan, dan kondisi fisik layar.
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">Hedonic Quality Adjustment</span>
            <span class="hero-tag-pill">Battery Health Depr</span>
            <span class="hero-tag-pill">IMEI Whitelist Premium</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
                    <div class="spec-card-container">
                        <div class="spec-card-header">Spesifikasi Bawaan Pabrik</div>
                        <div class="spec-item">
                            <span class="spec-item-key">Merk & Model</span>
                            <span class="spec-item-val">{selected_brand} {model_obj.name}</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Tahun Peluncuran</span>
                            <span class="spec-item-val">{model_obj.release_year}</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">MSRP Baru</span>
                            <span class="spec-item-val" style="color:#60a5fa;">Rp {float(selected_var_obj.official_msrp_new):,.0f}</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Chipset / SoC</span>
                            <span class="spec-item-val">{model_obj.chipset or '-'}</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Memori RAM / Storage</span>
                            <span class="spec-item-val">{selected_var_obj.ram_gb or '-'} GB / {selected_var_obj.storage_gb} GB</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Display Panel</span>
                            <span class="spec-item-val">{model_obj.display_type or '-'} ({model_obj.refresh_rate_hz}Hz)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Kamera Utama</span>
                            <span class="spec-item-val">{model_obj.main_camera_mp or '-'}</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Baterai & Charging</span>
                            <span class="spec-item-val">{model_obj.battery_capacity_mah or '-'} mAh ({model_obj.fast_charging_watt}W)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-item-key">Konektivitas & IP</span>
                            <span class="spec-item-val">{model_obj.network_gen} | NFC: {'Ya' if model_obj.has_nfc else 'Tidak'} | {model_obj.ip_rating}</span>
                        </div>
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
                <div class="val-hero-container">
                    <div class="val-hero-title">Rekomendasi Valuasi Nilai Pasar Wajar (Final Adjusted)</div>
                    <div class="val-price-hero">Rp {hedonic_res['adjusted_price']:,.0f}</div>
                    <div class="val-hero-meta">Base FMV: Rp {base_fmv:,.0f} ({sample_txt}) | Penyesuaian Hedonik: {hedonic_res['net_adjustment_pct']:+.1f}%</div>
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

# ==============================================================================
# 3. 3-TIER PRICE CORRIDORS & QUANTILES
# ==============================================================================
elif menu == "3-Tier Price Corridors & Quantiles":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">3-Tier Price Corridors & Quantiles</div>
        <div class="hero-subtitle">
            Monitoring koridor harga 3-tingkat kuantil statistik (P25 Target Beli Murah, FMV Median, dan P75 Unit Pristine) untuk seluruh smartphone beredar.
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">P25 Bargain Price</span>
            <span class="hero-tag-pill">P50 FMV Median</span>
            <span class="hero-tag-pill">P75 Pristine Benchmark</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
                    marker_color="#93c5fd"
                ))
                fig_cor.add_trace(go.Bar(
                    name="FMV Nilai Pasar Wajar",
                    x=subset["Varian & Storage"],
                    y=subset["FMV_num"],
                    marker_color="#3b82f6"
                ))
                fig_cor.add_trace(go.Bar(
                    name="P75 Unit Pristine",
                    x=subset["Varian & Storage"],
                    y=subset["P75_num"],
                    marker_color="#1e3a8a"
                ))
                fig_cor.update_layout(barmode="group", xaxis_tickangle=-45)
                apply_dark_plotly_layout(fig_cor, height=480)
                st.plotly_chart(fig_cor, use_container_width=True)
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Price Corridors: {e}")

# ==============================================================================
# 4. ARBITRAGE & HOT DEALS RADAR
# ==============================================================================
elif menu == "Arbitrage & Hot Deals Radar":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">Smartphone Arbitrage & Hot Deals Radar</div>
        <div class="hero-subtitle">
            Radar otomatis pendeteksi peluang beli murah di bawah harga wajar pasar (Undervalued Listing) untuk margin keuntungan optimal reseller smartphone.
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">Margin Arbitrase</span>
            <span class="hero-tag-pill">Underpriced Alert</span>
            <span class="hero-tag-pill">Anti-Scam Verified</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    try:
        with get_db() as db:
            disc_thresh = st.slider("Ambang Batas Minimum Diskon Arbitrase (%):", min_value=8, max_value=30, value=12)
            engine = SmartphonePricingEngine(db)
            deals = engine.find_hot_deals(discount_threshold_pct=float(disc_thresh))

            if deals:
                st.markdown(f"""
                <div class="info-box-green">
                    <div class="info-box-title">Terverifikasi {len(deals)} Unit Peluang Arbitrase & Hot Deals Aktif</div>
                    <div class="info-box-desc">Seluruh listing telah melewati validasi non-DP dan verifikasi anti-HDC. Potensi keuntungan dihitung dari selisih harga penawaran terhadap FMV.</div>
                </div>
                """, unsafe_allow_html=True)

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

# ==============================================================================
# 5. SPEC MATRIX & MODEL COMPARISON
# ==============================================================================
elif menu == "Spec Matrix & Model Comparison":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">Smartphone Hardware Spec Matrix</div>
        <div class="hero-subtitle">
            Komparasi mendalam matriks spesifikasi hardware smartphone secara berdampingan: SoC, benchmark Antutu, panel display, setup kamera, dan pengisian daya (2010 - 2026).
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">2010 - 2026 Hardware Archive</span>
            <span class="hero-tag-pill">SoC & Benchmark</span>
            <span class="hero-tag-pill">Display & Camera Setup</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
                            str(m1.release_year), m1.chipset or "-", m1.cpu_architecture or "-", m1.gpu or "-", f"{m1.antutu_benchmark_score:,}" if m1.antutu_benchmark_score else "-",
                            m1.display_type or "-", f"{m1.screen_size_inch} inci" if m1.screen_size_inch else "-", f"{m1.refresh_rate_hz} Hz", m1.resolution or "-", f"{m1.peak_brightness_nits} nits" if m1.peak_brightness_nits else "-",
                            m1.main_camera_mp or "-", m1.camera_setup or "-", f"OIS: {'Ya' if m1.has_ois else 'Tidak'} | {m1.optical_zoom_level or 'None'}", m1.selfie_camera_mp or "-",
                            f"{m1.battery_capacity_mah} mAh" if m1.battery_capacity_mah else "-", f"{m1.fast_charging_watt} Watt", f"{'Ya (' + str(m1.wireless_charging_watt) + 'W)' if m1.has_wireless_charging else 'Tidak'}",
                            f"{m1.network_gen} | NFC: {'Ya' if m1.has_nfc else 'Tidak'}", m1.ip_rating or "-", f"{m1.weight_grams} gram" if m1.weight_grams else "-"
                        ],
                        dev2_key: [
                            str(m2.release_year), m2.chipset or "-", m2.cpu_architecture or "-", m2.gpu or "-", f"{m2.antutu_benchmark_score:,}" if m2.antutu_benchmark_score else "-",
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

# ==============================================================================
# 6. DATA EXPLORER & SCAM FILTER
# ==============================================================================
elif menu == "Data Explorer & Scam Filter":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">Live Data Explorer & Scam Filter Monitor</div>
        <div class="hero-subtitle">
            Audit langsung listing mentah dari marketplace dan verifikasi efektivitas algoritma pendeteksi iklan pancingan DP & unit replika.
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">Audit Engine</span>
            <span class="hero-tag-pill">Regex & NLP Detection</span>
            <span class="hero-tag-pill">Clean Data Pipeline</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
