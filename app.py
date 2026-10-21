import os
import sys
import math
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import html
from contextlib import contextmanager
from sqlalchemy.orm import Session

# Setup Path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant, ScrapedListing, MarketPriceStats
from analytics.pricing_engine import SmartphonePricingEngine
from analytics.depreciation_engine import SmartphoneDepreciationEngine
from analytics.regional_index import RegionalPriceIndex, REGIONAL_HP_INDEX
from pipeline.normalizer import SmartphoneListingNormalizer
from pipeline.scam_detector import SmartphoneScamDetector
from data.master_catalog_seed import seed_master_catalog
from scrapers.real_marketplace_scraper import run_real_scraping_and_ingestion
from scrapers.gsmarena_sync import GSMARENA_BRAND_SLUGS, ingest_gsmarena_brand_devices

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

    /* Sidebar Expander & Information Cards */
    section[data-testid="stSidebar"] div[data-testid="stExpander"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        margin-top: 8px;
        margin-bottom: 8px;
        overflow: hidden;
    }
    section[data-testid="stSidebar"] div[data-testid="stExpander"] summary {
        color: #f8fafc !important;
        font-weight: 700;
        font-size: 0.82rem;
    }
    section[data-testid="stSidebar"] div[data-testid="stExpander"] summary:hover {
        color: #60a5fa !important;
    }
    section[data-testid="stSidebar"] div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
        padding: 10px 12px;
        border-top: 1px solid #334155;
        background-color: #0f172a;
        font-size: 0.78rem;
        line-height: 1.5;
        color: #cbd5e1;
    }
    .sidebar-source-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 8px 10px;
        margin-bottom: 8px;
    }
    .sidebar-source-title {
        font-size: 0.75rem;
        font-weight: 700;
        color: #60a5fa;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 3px;
    }
    .sidebar-source-body {
        font-size: 0.76rem;
        color: #cbd5e1;
        line-height: 1.4;
    }

    /* Phone Image Showcase Card */
    .phone-img-container {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }
    .phone-showcase-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
        margin-bottom: 12px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .phone-showcase-card:hover {
        border-color: #38bdf8;
        transform: translateY(-2px);
    }
    .phone-showcase-title {
        font-size: 0.88rem;
        font-weight: 800;
        color: #f8fafc;
        margin-top: 8px;
    }
    .phone-showcase-price {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.86rem;
        font-weight: 700;
        color: #38bdf8;
        margin-top: 4px;
    }
    .phone-showcase-meta {
        font-size: 0.74rem;
        color: #94a3b8;
        margin-top: 2px;
    }
</style>
""", unsafe_allow_html=True)

def get_phone_asset_path(image_url: str | None) -> str | None:
    """Mengembalikan path file gambar lokal yang valid atau None."""
    if not image_url:
        return None
    p = Path(image_url)
    if p.exists():
        return str(p)
    p_rel = ROOT_DIR / image_url
    if p_rel.exists():
        return str(p_rel)
    return None

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
            run_real_scraping_and_ingestion()
        elif db.query(ScrapedListing).count() == 0:
            run_real_scraping_and_ingestion()
    except Exception as e:
        print(f"[WARN] Error on DB init: {e}")
    finally:
        db.close()
    return True

# Ensure DB is warmed up
ensure_database_ready()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

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
        "Data Explorer & Scam Filter",
        "Master Katalog Smartphone (2010 - 2026)"
    ],
    index=0
)

with st.sidebar.expander("Inspeksi Visual Unit (Quick Preview)", expanded=False):
    try:
        with get_db() as sb_db:
            sb_brands = [b.name for b in sb_db.query(MasterBrand).order_by(MasterBrand.name).all()]
            if sb_brands:
                sb_brand = st.selectbox("Brand:", sb_brands, key="sb_quick_brand")
                sb_b_obj = sb_db.query(MasterBrand).filter(MasterBrand.name == sb_brand).first()
                sb_models = sb_db.query(MasterModel).filter(MasterModel.brand_id == sb_b_obj.id).order_by(MasterModel.release_year.desc()).all() if sb_b_obj else []
                if sb_models:
                    sb_model_names = [m.name for m in sb_models]
                    sb_model_name = st.selectbox("Model:", sb_model_names, key="sb_quick_model")
                    sb_m_obj = next((m for m in sb_models if m.name == sb_model_name), sb_models[0])
                    if sb_m_obj:
                        sb_img = get_phone_asset_path(sb_m_obj.image_url)
                        if sb_img:
                            st.image(sb_img, use_container_width=True)
                        st.markdown(f"""
                        <div style="font-size:0.75rem; color:#94a3b8; line-height:1.45; margin-top:4px;">
                            <b style="color:#f8fafc;">{html.escape(sb_brand)} {html.escape(sb_m_obj.name)}</b> ({sb_m_obj.release_year})<br>
                            Chipset: <span style="color:#60a5fa;">{html.escape(sb_m_obj.chipset or '-')}</span><br>
                            Kamera: <span style="color:#34d399;">{html.escape(sb_m_obj.main_camera_mp or '-')}</span>
                        </div>
                        """, unsafe_allow_html=True)
    except Exception as e:
        pass

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size: 0.74rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">
    Integritas & Referensi Data
</div>
""", unsafe_allow_html=True)

with st.sidebar.expander("Sumber Pengambilan & Validasi Data", expanded=False):
    st.markdown("""
<div class="sidebar-source-card">
    <div class="sidebar-source-title">1. Spesifikasi Teknis Hardware</div>
    <div class="sidebar-source-body">
        <b>GSMArena & Kimovil:</b> Arsitektur chipset, RAM/Storage SKU, tipe panel layar (LTPO/AMOLED/IPS), sensor kamera & OIS, kapasitas baterai.<br>
        <b>Portal Resmi Vendor ID:</b> Verifikasi spesifikasi SKU resmi Indonesia (Samsung, Apple iBox/Digimap, Xiaomi, Oppo, Vivo, Realme, Infinix, Tecno, Asus).
    </div>
</div>

<div class="sidebar-source-card">
    <div class="sidebar-source-title">2. MSRP Rilis Perdana Indonesia</div>
    <div class="sidebar-source-body">
        <b>Media Otoritatif:</b> Kompas Tekno, JagatReview, DroidLime untuk arsip harga rekomendasi ritel peluncuran perdana.<br>
        <b>Distributor Resmi:</b> Erajaya Swasembada / Eraspace / TAM / Digimap / iBox untuk verifikasi harga unit bergaransi nasional.
    </div>
</div>

<div class="sidebar-source-card">
    <div class="sidebar-source-title">3. Listing Pasar Sekunder Aktual & Terverifikasi</div>
    <div class="sidebar-source-body">
        <b>Platform Re-Commerce Terverifikasi:</b> Web scraping data pasar aktual dari Maujual / Laku6 (operator resmi trade-in Samsung Indonesia & e-commerce nasional) serta arsip terverifikasi transaksi pasar sekunder OLX Indonesia.<br>
        <b>Cakupan Wilayah:</b> 13 kota sentra perdagangan HP bekas (Jabodetabek, Bandung, Surabaya, Semarang, Yogyakarta, Malang, Medan, Makassar, Denpasar, Balikpapan).
    </div>
</div>

<div class="sidebar-source-card">
    <div class="sidebar-source-title">4. Validasi & Filter Kualitas</div>
    <div class="sidebar-source-body">
        <b>NLP Normalizer:</b> Verifikasi IMEI Kemenperin/Bea Cukai, garansi resmi vs inter, Battery Health %, dan kelengkapan.<br>
        <b>Tukey IQR Filter:</b> Eliminasi harga anomali ekstrem dan perangkap uang muka (DP trap semu).<br>
        <b>Lancaster Hedonic Model:</b> Penyesuaian harga pasar riil berdasarkan grade fisik dan fungsi komponen.
    </div>
</div>
""", unsafe_allow_html=True)

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

            st.markdown("### Visual Showcase Perangkat Flagship & Best-Seller Pasar")
            showcase_targets = [
                ("Apple", "iPhone 15 Pro Max"),
                ("Samsung", "Galaxy S24 Ultra"),
                ("Xiaomi", "Xiaomi 14"),
                ("Google Pixel", "Pixel 8 Pro")
            ]
            cols_showcase = st.columns(4)
            for idx, (sh_col, (sh_brand, sh_name)) in enumerate(zip(cols_showcase, showcase_targets)):
                with sh_col:
                    sh_m = db.query(MasterModel).join(MasterBrand).filter(MasterBrand.name == sh_brand, MasterModel.name == sh_name).first()
                    if sh_m:
                        sh_img = get_phone_asset_path(sh_m.image_url)
                        if sh_img:
                            st.image(sh_img, use_container_width=True)
                        sh_var = db.query(MasterVariant).filter(MasterVariant.model_id == sh_m.id).first()
                        msrp_val = float(sh_var.official_msrp_new) if sh_var else 0
                        st.markdown(f"""
                        <div class="phone-showcase-card">
                            <div class="phone-showcase-title">{html.escape(sh_brand)} {html.escape(sh_m.name)}</div>
                            <div class="phone-showcase-price">MSRP Rp {msrp_val:,.0f}</div>
                            <div class="phone-showcase-meta">{html.escape(sh_m.chipset or '-')} | {sh_m.release_year}</div>
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
                    img_path = get_phone_asset_path(model_obj.image_url)
                    if img_path:
                        st.image(img_path, caption=f"{selected_brand} {model_obj.name} ({model_obj.release_year})", use_container_width=True)
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
                        city_list = list(REGIONAL_HP_INDEX.keys())
                        selected_city = st.selectbox("Kota Transaksi / Domisili:", city_list, index=0)

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

                city_mult = RegionalPriceIndex.get_multiplier(selected_city)
                final_val = hedonic_res['adjusted_price'] * city_mult
                regional_diff_pct = (city_mult - 1.0) * 100.0
                regional_diff_nominal = final_val - hedonic_res['adjusted_price']

                st.markdown(f"""
                <div class="val-hero-container">
                    <div class="val-hero-title">Rekomendasi Valuasi Nilai Pasar Wajar (Final Adjusted)</div>
                    <div class="val-price-hero">Rp {final_val:,.0f}</div>
                    <div class="val-hero-meta">Base FMV: Rp {base_fmv:,.0f} ({sample_txt}) | Hedonik: {hedonic_res['net_adjustment_pct']:+.1f}% | Wilayah ({selected_city}): x{city_mult:.2f} ({regional_diff_pct:+.1f}%)</div>
                </div>
                """, unsafe_allow_html=True)

                res_c1, res_c2, res_c3, res_c4 = st.columns(4)
                with res_c1:
                    st.metric("Base Fair Market Value", f"Rp {base_fmv:,.0f}")
                with res_c2:
                    st.metric("Net Penyesuaian Hedonik", f"{hedonic_res['net_adjustment_pct']:+.1f}%", f"Rp {(hedonic_res['adjusted_price'] - base_fmv):,.0f}")
                with res_c3:
                    st.metric(f"Indeks Wilayah ({selected_city})", f"x{city_mult:.2f}", f"{regional_diff_pct:+.1f}% (Rp {regional_diff_nominal:,.0f})")
                with res_c4:
                    depr_final = SmartphoneDepreciationEngine.calculate_real_depreciation(msrp, final_val)
                    st.metric("Penyusutan Nilai dari MSRP", f"{depr_final:.1f}%")

                if hedonic_res["adjustment_breakdown"] or city_mult != 1.0:
                    st.markdown("##### Rincian Penyesuaian Atribut & Wilayah:")
                    for desc, pct in hedonic_res["adjustment_breakdown"]:
                        st.write(f"- {desc}: **{pct*100:+.1f}%**")
                    if city_mult != 1.0:
                        st.write(f"- Indeks Disparitas Wilayah ({selected_city}): **{regional_diff_pct:+.1f}%** (Rp {regional_diff_nominal:+,.0f})")
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

            all_brands = sorted(list(set([v.brand_name for v in variants])))
            sel_brand_filter = st.selectbox("Filter Merk Smartphone:", ["Semua Merk"] + all_brands)
            if sel_brand_filter != "Semua Merk":
                variants = [v for v in variants if v.brand_name == sel_brand_filter]
                brand_lead_model = db.query(MasterModel).join(MasterBrand).filter(MasterBrand.name == sel_brand_filter).order_by(MasterModel.release_year.desc()).first()
                if brand_lead_model:
                    lead_img = get_phone_asset_path(brand_lead_model.image_url)
                    if lead_img:
                        col_l1, col_l2 = st.columns([1, 4])
                        with col_l1:
                            st.image(lead_img, caption=f"{sel_brand_filter} {brand_lead_model.name}", use_container_width=True)
                        with col_l2:
                            st.markdown(f"""
                            <div class="info-box-blue" style="margin-top:10px;">
                                <div class="info-box-title">Model Referensi Utama: {sel_brand_filter} {brand_lead_model.name} ({brand_lead_model.release_year})</div>
                                <div class="info-box-desc">SoC: {brand_lead_model.chipset or '-'} | Layar: {brand_lead_model.display_type or '-'} | Kamera: {brand_lead_model.main_camera_mp or '-'}</div>
                            </div>
                            """, unsafe_allow_html=True)

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

                top_deals = deals[:3]
                if top_deals:
                    st.markdown("### Top Peluang Arbitrase Unggulan")
                    cols_deal = st.columns(min(len(top_deals), 3))
                    for cd, deal_item in zip(cols_deal, top_deals):
                        with cd:
                            d_model = db.query(MasterModel).filter(MasterModel.name == deal_item["model"]).first()
                            if d_model:
                                d_img = get_phone_asset_path(d_model.image_url)
                                if d_img:
                                    st.image(d_img, use_container_width=True)
                            st.markdown(f"""
                            <div class="phone-showcase-card">
                                <div class="phone-showcase-title">{html.escape(str(deal_item['brand']))} {html.escape(str(deal_item['model']))}</div>
                                <div class="phone-showcase-price">Rp {deal_item['price']:,.0f} <span style="color:#ef4444; font-size:0.75rem;">(-{deal_item['discount_pct']:.1f}%)</span></div>
                                <div class="phone-showcase-meta">FMV: Rp {deal_item['fmv_price']:,.0f} | Margin: Rp {deal_item['potential_profit']:,.0f}</div>
                                <div style="margin-top:6px;"><span class="status-pill" style="font-size:0.65rem;">{html.escape(str(deal_item['deal_tier']))}</span></div>
                            </div>
                            """, unsafe_allow_html=True)

                df_deals = pd.DataFrame(deals)
                
                display_df = df_deals[[
                    "deal_tier", "brand", "model", "variant", "price", "fmv_price", "discount_pct", "potential_profit", "city", "platform", "warranty_type", "imei_status", "url"
                ]].copy()
                
                display_df.columns = [
                    "Tier Peluang", "Brand", "Model", "Varian", "Harga Listing", "FMV Pasar", "Diskon (%)", "Potensi Margin (IDR)", "Kota", "Platform", "Garansi", "IMEI / Sinyal", "Tautan Listing"
                ]
                
                display_df["Harga Listing"] = display_df["Harga Listing"].apply(lambda x: f"Rp {x:,.0f}")
                display_df["FMV Pasar"] = display_df["FMV Pasar"].apply(lambda x: f"Rp {x:,.0f}")
                display_df["Potensi Margin (IDR)"] = display_df["Potensi Margin (IDR)"].apply(lambda x: f"Rp {x:,.0f}")
                display_df["Diskon (%)"] = display_df["Diskon (%)"].apply(lambda x: f"{x:.1f}%")

                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Tautan Listing": st.column_config.LinkColumn(
                            "Tautan Listing",
                            display_text="Buka Listing"
                        )
                    }
                )
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
                    col_img1, col_img2 = st.columns(2)
                    with col_img1:
                        img1 = get_phone_asset_path(m1.image_url)
                        if img1:
                            st.image(img1, caption=dev1_key, use_container_width=True)
                    with col_img2:
                        img2 = get_phone_asset_path(m2.image_url)
                        if img2:
                            st.image(img2, caption=dev2_key, use_container_width=True)

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

    with st.expander("Audit Protokol: Sumber Pengambilan & Validasi Data", expanded=False):
        st.markdown("""
        <div class="info-box-blue">
            <div class="info-box-title">Sumber Pengambilan & Tata Kelola Data Katalog (2010 - 2026)</div>
            <div class="info-box-desc">
                Seluruh data spesifikasi teknis dan histori pasar dikurasi dan divalidasi silang melalui sumber-sumber otoritatif berikut:
            </div>
        </div>
        """, unsafe_allow_html=True)
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            st.markdown("""
            **1. Spesifikasi Teknis Hardware:**
            - **GSMArena Database** (`gsmarena.com`): Verifikasi chipset, arsitektur CPU, tipe display (LTPO/AMOLED/IPS), sensor kamera & OIS, baterai, IP rating.
            - **Kimovil Benchmark** (`kimovil.com`): Validasi AnTuTu benchmark v9/v10, screen-to-body ratio.
            - **Portal Resmi Vendor ID**: Samsung, Apple (iBox/Digimap), Xiaomi, Oppo, Vivo, Realme, Infinix, Tecno, Asus.
            """)
        with col_s2:
            st.markdown("""
            **2. MSRP Rilis Perdana Indonesia:**
            - **Kompas Tekno** (`tekno.kompas.com`): Arsip pers peluncuran resmi dan MSRP ritel perdana di Indonesia.
            - **JagatReview / JagatGadget** (`jagatreview.com`): Dokumentasi pengujian lab & verifikasi SKU resmi.
            - **DroidLime** (`droidlime.com`): Arsip unboxing ritel resmi & harga rilis perdana.
            - **Erajaya / Eraspace / TAM / Digimap**: Arsip katalog ritel nasional bergaransi resmi.
            """)
        with col_s3:
            st.markdown("""
            **3. Pasar Sekunder & Validasi:**
            - **Platform Re-Commerce**: Maujual / Laku6 (Trade-in & C2B Re-commerce Engine Indonesia), OLX Indonesia.
            - **13 Sentra Perdagangan**: Jakarta, Tangerang, Bekasi, Bandung, Surabaya, Semarang, Yogya, Malang, Medan, Makassar, Denpasar, Balikpapan.
            - **Filter & Model**: Normalisasi NLP + Filter Outlier Tukey IQR + Model Lancaster Hedonic.
            """)

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

# ==============================================================================
# 7. MASTER KATALOG SMARTPHONE (2010 - 2026)
# ==============================================================================
elif menu == "Master Katalog Smartphone (2010 - 2026)":
    st.markdown("""
    <div class="hero-appbar">
        <div class="hero-title">Master Katalog Smartphone Indonesia (2010 - 2026)</div>
        <div class="hero-subtitle">
            Basis data katalog resmi terverifikasi: 16 Brand, 315 Model, dan 465 Varian smartphone di pasar Indonesia lengkap dengan spesifikasi teknis hardware, MSRP rilis perdana, dan aset visual produk.
        </div>
        <div class="hero-tags">
            <span class="hero-tag-pill">16 Brand Terdaftar</span>
            <span class="hero-tag-pill">315 Model Terverifikasi</span>
            <span class="hero-tag-pill">465 Varian RAM & Storage</span>
            <span class="hero-tag-pill">Arsip 2010 - 2026</span>
            <span class="hero-tag-pill">Export Ready</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    try:
        with get_db() as db:
            total_m = db.query(MasterModel).count()
            total_v = db.query(MasterVariant).count()
            total_b = db.query(MasterBrand).count()

            st.markdown(f"""
            <div class="kpi-grid">
                <div class="pro-metric-card">
                    <div class="pro-metric-label">Total Model HP Terdaftar</div>
                    <div class="pro-metric-val">{total_m} Model</div>
                    <div class="pro-metric-sub">Katalog Terverifikasi</div>
                </div>
                <div class="pro-metric-card emerald">
                    <div class="pro-metric-label">Total Konfigurasi Varian</div>
                    <div class="pro-metric-val">{total_v} Varian</div>
                    <div class="pro-metric-sub emerald">Kombinasi RAM & Storage</div>
                </div>
                <div class="pro-metric-card purple">
                    <div class="pro-metric-label">Cakupan Merk / Brand</div>
                    <div class="pro-metric-val">{total_b} Brand</div>
                    <div class="pro-metric-sub purple">Pasar Resmi Indonesia</div>
                </div>
                <div class="pro-metric-card rose">
                    <div class="pro-metric-label">Rentang Periode Rilis</div>
                    <div class="pro-metric-val">2010 - 2026</div>
                    <div class="pro-metric-sub rose">16 Tahun Sejarah Gadget ID</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Auto-Ingestion GSMArena Tool
            with st.expander("Sinkronisasi & Auto-Ingestion Model Baru dari GSMArena (Skenario B)", expanded=False):
                st.markdown("""
                <div style="font-size:0.85rem; color:#94a3b8; margin-bottom:12px; line-height:1.5;">
                    Pindai dan tambahkan model smartphone terbaru beserta varian RAM & Storage secara otomatis langsung dari database <b>GSMArena</b>.
                    Data yang di-ingest akan diberi label <span class="status-pill" style="font-size:0.70rem; color:#38bdf8;">Platform: GSMArena</span>.
                </div>
                """, unsafe_allow_html=True)
                c_sync1, c_sync2, c_sync3 = st.columns([1.5, 1.2, 1.5])
                with c_sync1:
                    sync_brand_choice = st.selectbox("Pilih Brand Target:", list(GSMARENA_BRAND_SLUGS.keys()), key="sync_brand_sel")
                with c_sync2:
                    sync_limit = st.slider("Batas Maksimal Unit:", min_value=1, max_value=10, value=3, key="sync_limit_sel")
                with c_sync3:
                    st.write("")
                    st.write("")
                    btn_sync = st.button("Jalankan Auto-Ingestion", type="primary", key="btn_run_gsmarena_sync")

                if btn_sync:
                    with st.spinner(f"Menghubungi GSMArena dan meng-ingest model baru untuk {sync_brand_choice}..."):
                        sync_res = ingest_gsmarena_brand_devices(sync_brand_choice, max_devices=sync_limit)
                        if sync_res.get("status") == "success":
                            st.success(f"Sinkronisasi Berhasil! Ditambahkan: {sync_res['new_models_added']} Model Baru, {sync_res['new_variants_added']} Varian Baru, {sync_res['models_enriched']} Model Diperkaya.")
                            st.rerun()
                        else:
                            st.error(f"Gagal Sinkronisasi: {sync_res.get('message')}")

            # Filter Controls
            col_f1, col_f2, col_f3, col_f4 = st.columns([1.2, 1.3, 1.3, 1.7])
            with col_f1:
                all_b_names = ["Semua Brand"] + [b.name for b in db.query(MasterBrand).order_by(MasterBrand.name).all()]
                filter_brand = st.selectbox("Filter Brand:", all_b_names, key="katalog_brand")

            with col_f2:
                all_platforms = ["Semua Platform", "Official Indonesia", "GSMArena"]
                filter_platform = st.selectbox("Filter Sumber Platform:", all_platforms, key="katalog_platform")

            with col_f3:
                year_range = st.slider("Rentang Tahun Rilis:", min_value=2010, max_value=2026, value=(2010, 2026), key="katalog_year")

            with col_f4:
                search_query = st.text_input("Cari Model, Seri, atau Chipset:", placeholder="e.g. Pro Max, Snapdragon, Dimensity...", key="katalog_search")

            # Build query
            q = db.query(MasterModel, MasterBrand).join(MasterBrand, MasterModel.brand_id == MasterBrand.id)
            if filter_brand != "Semua Brand":
                q = q.filter(MasterBrand.name == filter_brand)
            if filter_platform != "Semua Platform":
                q = q.filter(MasterModel.source_platform == filter_platform)
            q = q.filter(MasterModel.release_year >= year_range[0], MasterModel.release_year <= year_range[1])

            if search_query:
                pattern = f"%{search_query.strip()}%"
                q = q.filter(
                    (MasterModel.name.ilike(pattern)) |
                    (MasterModel.chipset.ilike(pattern)) |
                    (MasterModel.series.ilike(pattern)) |
                    (MasterBrand.name.ilike(pattern))
                )

            filtered_models = q.order_by(MasterModel.release_year.desc(), MasterBrand.name, MasterModel.name).all()

            view_mode = st.radio("Pilih Format Tampilan:", ["Tampilan Galeri Visual Produk", "Tabel Database Spesifikasi Lengkap"], horizontal=True, key="katalog_view_mode")

            st.markdown(f"**Menampilkan {len(filtered_models)} model smartphone yang sesuai filter:**")

            if not filtered_models:
                st.info("Tidak ada model smartphone yang cocok dengan filter yang dipilih.")
            elif view_mode == "Tampilan Galeri Visual Produk":
                items_per_page = 18
                total_items = len(filtered_models)
                total_pages = max(1, math.ceil(total_items / items_per_page))

                col_page_sel, col_page_info = st.columns([1.5, 2.5])
                with col_page_sel:
                    selected_page = st.selectbox(
                        "Pilih Halaman:",
                        range(1, total_pages + 1),
                        format_func=lambda p: f"Halaman {p} dari {total_pages}",
                        key="katalog_page_selector"
                    )
                with col_page_info:
                    start_idx = (selected_page - 1) * items_per_page
                    end_idx = min(start_idx + items_per_page, total_items)
                    st.markdown(f"""
                    <div style="padding-top:28px; font-size:0.85rem; color:#94a3b8; font-family:'JetBrains Mono', monospace;">
                        Menampilkan unit <b style="color:#f8fafc;">{start_idx + 1} - {end_idx}</b> dari total <b style="color:#38bdf8;">{total_items}</b> model.
                    </div>
                    """, unsafe_allow_html=True)

                page_models = filtered_models[start_idx:end_idx]

                grid_cols = st.columns(3)
                for idx, (m_item, b_item) in enumerate(page_models):
                    col_target = grid_cols[idx % 3]
                    with col_target:
                        img_path = get_phone_asset_path(m_item.image_url)
                        if img_path:
                            st.image(img_path, use_container_width=True)

                        vars_m = db.query(MasterVariant).filter(MasterVariant.model_id == m_item.id).order_by(MasterVariant.storage_gb).all()
                        msrp_strs = []
                        for v in vars_m:
                            msrp_strs.append(f"• {v.variant_name}: Rp {float(v.official_msrp_new):,.0f}")
                        msrp_block = "<br>".join(msrp_strs) if msrp_strs else "MSRP belum terdata"

                        st.markdown(f"""
                        <div class="phone-showcase-card" style="text-align:left; margin-bottom:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <div style="display:flex; gap:6px; align-items:center;">
                                    <span class="status-pill" style="font-size:0.65rem;">{html.escape(str(b_item.name))}</span>
                                    <span class="status-pill" style="font-size:0.65rem; background:rgba(56, 189, 248, 0.15); color:#38bdf8; border:1px solid rgba(56, 189, 248, 0.3);">{html.escape(str(m_item.source_platform or "Official Indonesia"))}</span>
                                </div>
                                <span style="font-family:'JetBrains Mono', monospace; font-size:0.80rem; color:#94a3b8; font-weight:700;">{m_item.release_year}</span>
                            </div>
                            <div class="phone-showcase-title" style="font-size:1.05rem; margin-top:6px;">{html.escape(str(b_item.name))} {html.escape(str(m_item.name))}</div>
                            <div style="font-size:0.78rem; color:#cbd5e1; margin-top:6px; line-height:1.5;">
                                <b>SoC:</b> <span style="color:#60a5fa;">{html.escape(str(m_item.chipset or '-'))}</span><br>
                                <b>Display:</b> {html.escape(str(m_item.display_type or '-'))} ({m_item.refresh_rate_hz}Hz)<br>
                                <b>Kamera:</b> {html.escape(str(m_item.main_camera_mp or '-'))} (OIS: {'Ya' if m_item.has_ois else 'Tidak'})<br>
                                <b>Baterai:</b> {m_item.battery_capacity_mah or '-'} mAh ({m_item.fast_charging_watt}W)<br>
                                <b>Konektivitas:</b> {html.escape(str(m_item.network_gen))} | NFC: {'Ya' if m_item.has_nfc else 'Tidak'} | {html.escape(str(m_item.ip_rating))}
                            </div>
                            <div style="margin-top:10px; padding-top:8px; border-top:1px solid #334155; font-size:0.75rem; color:#94a3b8;">
                                <b style="color:#f8fafc;">Varian & MSRP Peluncuran Resmi:</b><br>
                                <span style="color:#38bdf8;">{msrp_block}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                rows_db = []
                for m_item, b_item in filtered_models:
                    vars_m = db.query(MasterVariant).filter(MasterVariant.model_id == m_item.id).order_by(MasterVariant.storage_gb).all()
                    min_msrp = min([float(v.official_msrp_new) for v in vars_m]) if vars_m else 0
                    max_msrp = max([float(v.official_msrp_new) for v in vars_m]) if vars_m else 0
                    var_summary = ", ".join([f"{v.storage_gb}GB" for v in vars_m]) if vars_m else "-"
                    msrp_str = f"Rp {min_msrp:,.0f}" if min_msrp == max_msrp else f"Rp {min_msrp:,.0f} - Rp {max_msrp:,.0f}"

                    rows_db.append({
                        "Brand": b_item.name,
                        "Model": m_item.name,
                        "Platform Sumber": m_item.source_platform or "Official Indonesia",
                        "Seri": m_item.series or "-",
                        "Tahun Rilis": m_item.release_year,
                        "MSRP Rilis Perdana": msrp_str,
                        "Varian Storage": var_summary,
                        "Chipset / SoC": m_item.chipset or "-",
                        "Antutu v10": f"{m_item.antutu_benchmark_score:,}" if m_item.antutu_benchmark_score else "-",
                        "Tipe Layar": m_item.display_type or "-",
                        "Ukuran Layar": f"{m_item.screen_size_inch} inch" if m_item.screen_size_inch else "-",
                        "Refresh Rate": f"{m_item.refresh_rate_hz} Hz",
                        "Resolusi": m_item.resolution or "-",
                        "Kamera Utama": m_item.main_camera_mp or "-",
                        "Kamera Depan": m_item.selfie_camera_mp or "-",
                        "Baterai": f"{m_item.battery_capacity_mah} mAh" if m_item.battery_capacity_mah else "-",
                        "Fast Charging": f"{m_item.fast_charging_watt}W",
                        "Wireless Charge": f"{m_item.wireless_charging_watt}W" if m_item.has_wireless_charging else "Tidak",
                        "Jaringan": m_item.network_gen,
                        "NFC": "Ya" if m_item.has_nfc else "Tidak",
                        "IP Rating": m_item.ip_rating or "-",
                        "Berat": f"{m_item.weight_grams}g" if m_item.weight_grams else "-",
                        "OS Awal": m_item.os_at_launch or "-"
                    })

                df_catalog = pd.DataFrame(rows_db)
                st.dataframe(df_catalog, use_container_width=True, hide_index=True)

                csv_data = df_catalog.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Data Master Katalog (CSV)",
                    data=csv_data,
                    file_name="master_katalog_smartphone_indonesia.csv",
                    mime="text/csv"
                )
    except Exception as e:
        st.error(f"Terjadi kesalahan pada modul Master Katalog: {e}")

