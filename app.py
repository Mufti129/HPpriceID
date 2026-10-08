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

# Page Config
st.set_page_config(
    page_title="PhonePrice ID — Smartphone Intelligence & Valuation Engine",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .badge-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .badge-super { background-color: #FEE2E2; color: #991B1B; }
    .badge-hot { background-color: #FEF3C7; color: #92400E; }
    .badge-good { background-color: #DCFCE7; color: #166534; }
</style>
""", unsafe_allow_html=True)

def get_db_session():
    return SessionLocal()

from data.master_catalog_seed import seed_master_catalog
from scrapers.generate_synthetic_data import generate_realistic_market_dataset

# Initialize DB if not exists & auto-seed if fresh
init_db()
_test_db = SessionLocal()
if _test_db.query(MasterVariant).count() == 0:
    seed_master_catalog()
    generate_realistic_market_dataset(target_count_per_variant=15)
_test_db.close()

# Sidebar Navigation
st.sidebar.title("📱 PhonePrice ID")
st.sidebar.caption("v2.0 • Smartphone Market & Valuation Engine")

menu = st.sidebar.radio(
    "PILIH MODUL ANALISIS:",
    [
        "📊 Market Overview & Dashboard",
        "⚖️ FMV & Hedonic Calculator",
        "📈 3-Tier Price Corridors & Quantiles",
        "🔥 Arbitrage & Hot Deals Radar",
        "🔎 Spec Matrix & Model Comparison",
        "🛡️ Data Explorer & Scam Filter"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Metodologi Sistem:**\n\n"
    "• **AI & NLP Normalizer:** Ekstraksi spesifikasi, garansi (iBox/SEIN/Inter), IMEI, BH%, dan kelengkapan.\n"
    "• **Tukey IQR:** Pembersihan outlier & scam harga DP palsu.\n"
    "• **Hedonic Quality Valuation:** Penyesuaian nilai pasar berdasarkan kondisi fisik, baterai, & status sinyal."
)

db = get_db_session()

# ==========================================
# 1. MARKET OVERVIEW
# ==========================================
if menu == "📊 Market Overview & Dashboard":
    st.markdown('<div class="main-header">📱 Smartphone Market Intelligence Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Analisis komprehensif pasar smartphone bekas & sekunder Indonesia (Harga Pasar Wajar, Depresiasi, dan Distribusi Merk).</div>', unsafe_allow_html=True)

    # Metrics
    total_listings = db.query(ScrapedListing).count()
    valid_cash_listings = db.query(ScrapedListing).filter(ScrapedListing.is_dp_price == False).count()
    scam_listings = total_listings - valid_cash_listings
    total_brands = db.query(MasterBrand).count()
    total_models = db.query(MasterModel).count()
    total_variants = db.query(MasterVariant).count()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Database Listing", f"{total_listings:,}")
    with col2:
        st.metric("Listing Tunai Valid", f"{valid_cash_listings:,}", f"{(valid_cash_listings/max(1,total_listings))*100:.1f}% Bersih")
    with col3:
        st.metric("DP Trap / Clickbait Terfilter", f"{scam_listings:,}", f"-{(scam_listings/max(1,total_listings))*100:.1f}% Anomali", delta_color="inverse")
    with col4:
        st.metric("Master Katalog Terdaftar", f"{total_models} Model / {total_variants} Varian")

    st.markdown("---")

    # Visualizations
    col_left, col_right = st.columns(2)

    # Brand Share & Average Price Chart
    with col_left:
        st.subheader("Distribusi Volume Listing per Merk")
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
                title="Market Share Volume Listing Berdasarkan Brand",
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Safe
            )
            st.plotly_chart(fig_brand, use_container_width=True)
        else:
            st.warning("Data listing belum tersedia. Silakan jalankan seeder pipeline.")

    with col_right:
        st.subheader("Kurva Depresiasi Nilai Pasar (MSRP vs Resale)")
        variants = db.query(
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
            stats = pricing_engine.calculate_variant_pricing_stats(
                db.query(MasterVariant.id).filter(MasterVariant.variant_name == var.variant_name).scalar()
            )
            if stats:
                msrp = float(var.official_msrp_new)
                fmv = stats["price_median"]
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
                title="Perbandingan MSRP Rilis Baru vs Fair Market Value (FMV) Saat Ini",
                labels={"MSRP": "Harga MSRP Baru (IDR)", "FMV": "Harga Pasar Wajar (FMV IDR)"}
            )
            st.plotly_chart(fig_depr, use_container_width=True)
        else:
            st.info("Memuat kurva depresiasi...")

# ==========================================
# 2. FMV & HEDONIC CALCULATOR
# ==========================================
elif menu == "⚖️ FMV & Hedonic Calculator":
    st.markdown('<div class="main-header">⚖️ Fair Market Value & Hedonic Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Hitung valuasi harga pasar wajar dengan penyesuaian kualitas riil: Status IMEI, Garansi iBox vs Inter, Battery Health, Layar & Biometrik.</div>', unsafe_allow_html=True)

    col_select1, col_select2, col_select3 = st.columns(3)
    brands = [b.name for b in db.query(MasterBrand).order_by(MasterBrand.name).all()]
    
    with col_select1:
        selected_brand = st.selectbox("Pilih Merk Smartphone:", brands if brands else ["Apple"])

    brand_obj = db.query(MasterBrand).filter(MasterBrand.name == selected_brand).first()
    models = [m.name for m in db.query(MasterModel).filter(MasterModel.brand_id == brand_obj.id).order_by(MasterModel.name).all()] if brand_obj else []

    with col_select2:
        selected_model = st.selectbox("Pilih Model:", models if models else ["iPhone 15 Pro Max"])

    model_obj = db.query(MasterModel).filter(MasterModel.name == selected_model).first()
    variants = db.query(MasterVariant).filter(MasterVariant.model_id == model_obj.id).all() if model_obj else []

    with col_select3:
        variant_names = [v.variant_name for v in variants]
        selected_variant = st.selectbox("Pilih Varian Storage/RAM:", variant_names if variant_names else [])

    st.markdown("---")

    selected_var_obj = db.query(MasterVariant).filter(MasterVariant.variant_name == selected_variant).first() if selected_variant else None

    if selected_var_obj and model_obj:
        col_specs, col_inputs = st.columns([1.2, 1.8])

        with col_specs:
            st.markdown("### 📋 Spesifikasi Bawaan Pabrik")
            st.markdown(f"""
            - **Merk & Model:** `{selected_brand}` {model_obj.name}
            - **Tahun Rilis:** `{model_obj.release_year}`
            - **Harga Rilis Resmi (MSRP):** `Rp {float(selected_var_obj.official_msrp_new):,.0f}`
            - **Chipset / SoC:** `{model_obj.chipset}`
            - **RAM / Internal Storage:** `{selected_var_obj.ram_gb or '-'} GB / {selected_var_obj.storage_gb} GB`
            - **Panel Layar:** `{model_obj.display_type} ({model_obj.refresh_rate_hz}Hz)`
            - **Resolusi & Ukuran:** `{model_obj.resolution} ({model_obj.screen_size_inch}")`
            - **Kamera Utama:** `{model_obj.main_camera_mp}`
            - **Fitur OIS & Zoom:** `{'OIS Aktif' if model_obj.has_ois else 'Non-OIS'} | {model_obj.optical_zoom_level or 'None'}`
            - **Kapasitas Baterai:** `{model_obj.battery_capacity_mah} mAh ({model_obj.fast_charging_watt}W)`
            - **Konektivitas & Proteksi:** `{model_obj.network_gen} | NFC: {'Ya' if model_obj.has_nfc else 'Tidak'} | {model_obj.ip_rating}`
            """)

        with col_inputs:
            st.markdown("### ⚙️ Atribut Kualitas & Kondisi Fisik Unit")
            
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
                    bh = st.slider("Battery Health (BH %):", min_value=60, max_value=100, value=88)

        st.markdown("---")

        # Kalkulasi
        engine = SmartphonePricingEngine(db)
        stats = engine.calculate_variant_pricing_stats(selected_var_obj.id)

        msrp = float(selected_var_obj.official_msrp_new)
        if stats and stats["sample_count"] >= 2:
            base_fmv = stats["price_median"]
            sample_txt = f"{stats['sample_count']} listing aktif"
        else:
            # Fallback Teoretis
            retention = SmartphoneDepreciationEngine.calculate_theoretical_retention(
                selected_brand, model_obj.name, model_obj.release_year, current_year=2026
            )
            base_fmv = msrp * retention
            sample_txt = "Model Retensi Teoretis Ekonometrik (N < 2)"

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

        st.markdown("### 🏷️ Hasil Valuasi Harga Pasar Wajar")
        res_col1, res_col2, res_col3 = st.columns(3)
        
        with res_col1:
            st.metric(
                label="Base Fair Market Value (FMV Baseline)",
                value=f"Rp {base_fmv:,.0f}",
                help=f"Dihitung dari {sample_txt}"
            )
        with res_col2:
            st.metric(
                label="Net Penyesuaian Hedonik",
                value=f"{hedonic_res['net_adjustment_pct']:+.1f}%",
                delta=f"Rp {(hedonic_res['adjusted_price'] - base_fmv):,.0f}"
            )
        with res_col3:
            st.metric(
                label="Rekomendasi Harga Pasar Wajar (Final Valuated)",
                value=f"Rp {hedonic_res['adjusted_price']:,.0f}",
                delta=f"Depresiasi OTR: {SmartphoneDepreciationEngine.calculate_real_depreciation(msrp, hedonic_res['adjusted_price']):.1f}%",
                delta_color="inverse"
            )

        if hedonic_res["adjustment_breakdown"]:
            st.markdown("#### Detail Faktor Penyesuaian:")
            for desc, pct in hedonic_res["adjustment_breakdown"]:
                st.write(f"- {desc}: **{pct*100:+.1f}%**")

# ==========================================
# 3. 3-TIER PRICE CORRIDORS & QUANTILES
# ==========================================
elif menu == "📈 3-Tier Price Corridors & Quantiles":
    st.markdown('<div class="main-header">📈 3-Tier Price Corridors & Quantiles</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Monitoring koridor harga 3-tingkat (P25 Target Beli Murah, FMV Median, dan P75 Unit Pristine).</div>', unsafe_allow_html=True)

    variants = db.query(
        MasterVariant.id,
        MasterVariant.variant_name,
        MasterVariant.official_msrp_new,
        MasterModel.name.label("model_name"),
        MasterBrand.name.label("brand_name"),
        MasterModel.release_year
    ).join(MasterModel, MasterVariant.model_id == MasterModel.id)\
     .join(MasterBrand, MasterModel.brand_id == MasterBrand.id).all()

    engine = SmartphonePricingEngine(db)
    table_rows = []

    for var in variants:
        stats = engine.calculate_variant_pricing_stats(var.id)
        if stats and stats["sample_count"] >= 2:
            msrp = float(var.official_msrp_new)
            fmv = stats["price_median"]
            depr = SmartphoneDepreciationEngine.calculate_real_depreciation(msrp, fmv)

            table_rows.append({
                "Brand": var.brand_name,
                "Model": var.model_name,
                "Varian & Storage": var.variant_name,
                "Tahun": var.release_year,
                "Sampel": stats["sample_count"],
                "MSRP Baru (IDR)": f"Rp {msrp:,.0f}",
                "P25 Bargain (IDR)": f"Rp {stats['price_p25']:,.0f}",
                "FMV Median (IDR)": f"Rp {fmv:,.0f}",
                "P75 Pristine (IDR)": f"Rp {stats['price_p75']:,.0f}",
                "Depresiasi Riil (%)": f"{depr:.1f}%",
                "P25_raw": stats["price_p25"],
                "FMV_raw": fmv,
                "P75_raw": stats["price_p75"]
            })

    if table_rows:
        df_corridor = pd.DataFrame(table_rows)
        st.dataframe(
            df_corridor[["Brand", "Model", "Varian & Storage", "Tahun", "Sampel", "MSRP Baru (IDR)", "P25 Bargain (IDR)", "FMV Median (IDR)", "P75 Pristine (IDR)", "Depresiasi Riil (%)"]],
            use_container_width=True,
            hide_index=True
        )

        # Plotly Range Corridor
        st.markdown("### Visualisasi Rentang Koridor Harga Pasar")
        fig_cor = go.Figure()
        
        subset = df_corridor.head(12)
        fig_cor.add_trace(go.Bar(
            name="P25 Bargain Price",
            x=subset["Varian & Storage"],
            y=subset["P25_raw"],
            marker_color="#93C5FD"
        ))
        fig_cor.add_trace(go.Bar(
            name="FMV Median",
            x=subset["Varian & Storage"],
            y=subset["FMV_raw"],
            marker_color="#2563EB"
        ))
        fig_cor.add_trace(go.Bar(
            name="P75 Pristine",
            x=subset["Varian & Storage"],
            y=subset["P75_raw"],
            marker_color="#1E3A8A"
        ))
        fig_cor.update_layout(barmode="group", xaxis_tickangle=-45, height=500)
        st.plotly_chart(fig_cor, use_container_width=True)
    else:
        st.info("Memuat data kuartil harga...")

# ==========================================
# 4. ARBITRAGE & HOT DEALS RADAR
# ==========================================
elif menu == "🔥 Arbitrage & Hot Deals Radar":
    st.markdown('<div class="main-header">🔥 Smartphone Arbitrage & Hot Deals Radar</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Pemindai listing smartphone sekunder dengan diskon di atas batas normal pasar (Peluang Arbitrase Reseller).</div>', unsafe_allow_html=True)

    disc_thresh = st.slider("Ambang Batas Minimum Diskon Arbitrase (%):", min_value=8, max_value=30, value=12)
    engine = SmartphonePricingEngine(db)
    deals = engine.find_hot_deals(discount_threshold_pct=float(disc_thresh))

    if deals:
        st.success(f"Ditemukan **{len(deals)} peluang hot deals & arbitrase** yang terverifikasi!")
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
        st.info(f"Tidak ada listing yang memenuhi diskon >= {disc_thresh}%. Coba turunkan ambang batas.")

# ==========================================
# 5. SPEC MATRIX & MODEL COMPARISON
# ==========================================
elif menu == "🔎 Spec Matrix & Model Comparison":
    st.markdown('<div class="main-header">🔎 Smartphone Hardware Spec Matrix</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Bandingkan spesifikasi teknis mendalam antar model smartphone secara berdampingan.</div>', unsafe_allow_html=True)

    all_models = db.query(MasterModel, MasterBrand).join(MasterBrand, MasterModel.brand_id == MasterBrand.id).all()
    model_choices = [f"{b.name} {m.name}" for m, b in all_models]

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        dev1 = st.selectbox("Pilih Smartphone 1:", model_choices, index=0 if len(model_choices)>0 else 0)
    with col_c2:
        dev2 = st.selectbox("Pilih Smartphone 2:", model_choices, index=min(1, len(model_choices)-1))

    if dev1 and dev2:
        m1_name = dev1.split(" ", 1)[1] if " " in dev1 else dev1
        m2_name = dev2.split(" ", 1)[1] if " " in dev2 else dev2
        
        m1 = db.query(MasterModel).filter(MasterModel.name == m1_name).first()
        m2 = db.query(MasterModel).filter(MasterModel.name == m2_name).first()

        if m1 and m2:
            spec_data = {
                "Parameter Spesifikasi Hardware": [
                    "Tahun Peluncuran", "Chipset / SoC", "CPU Cores & Arch", "GPU Grafis", "Antutu v10 Score",
                    "Tipe Layar", "Ukuran Layar", "Refresh Rate", "Resolusi Display", "Peak Brightness",
                    "Kamera Belakang Utama", "Konfigurasi Kamera", "OIS & Zoom Optik", "Kamera Depan (Selfie)",
                    "Kapasitas Baterai", "Fast Charging Kabel", "Wireless Charging", "Konektivitas & NFC", "Sertifikasi IP Rating", "Berat Bodi"
                ],
                dev1: [
                    m1.release_year, m1.chipset, m1.cpu_architecture, m1.gpu, f"{m1.antutu_benchmark_score:,}" if m1.antutu_benchmark_score else "-",
                    m1.display_type, f"{m1.screen_size_inch} inci", f"{m1.refresh_rate_hz} Hz", m1.resolution, f"{m1.peak_brightness_nits} nits",
                    m1.main_camera_mp, m1.camera_setup, f"OIS: {'Ya' if m1.has_ois else 'Tidak'} | {m1.optical_zoom_level or 'None'}", m1.selfie_camera_mp,
                    f"{m1.battery_capacity_mah} mAh", f"{m1.fast_charging_watt} Watt", f"{'Ya (' + str(m1.wireless_charging_watt) + 'W)' if m1.has_wireless_charging else 'Tidak'}",
                    f"{m1.network_gen} | NFC: {'Ya' if m1.has_nfc else 'Tidak'}", m1.ip_rating, f"{m1.weight_grams} gram"
                ],
                dev2: [
                    m2.release_year, m2.chipset, m2.cpu_architecture, m2.gpu, f"{m2.antutu_benchmark_score:,}" if m2.antutu_benchmark_score else "-",
                    m2.display_type, f"{m2.screen_size_inch} inci", f"{m2.refresh_rate_hz} Hz", m2.resolution, f"{m2.peak_brightness_nits} nits",
                    m2.main_camera_mp, m2.camera_setup, f"OIS: {'Ya' if m2.has_ois else 'Tidak'} | {m2.optical_zoom_level or 'None'}", m2.selfie_camera_mp,
                    f"{m2.battery_capacity_mah} mAh", f"{m2.fast_charging_watt} Watt", f"{'Ya (' + str(m2.wireless_charging_watt) + 'W)' if m2.has_wireless_charging else 'Tidak'}",
                    f"{m2.network_gen} | NFC: {'Ya' if m2.has_nfc else 'Tidak'}", m2.ip_rating, f"{m2.weight_grams} gram"
                ]
            }

            df_spec = pd.DataFrame(spec_data)
            st.table(df_spec.set_index("Parameter Spesifikasi Hardware"))

# ==========================================
# 6. DATA EXPLORER & SCAM FILTER
# ==========================================
elif menu == "🛡️ Data Explorer & Scam Filter":
    st.markdown('<div class="main-header">🛡️ Live Data Explorer & Scam Filter Monitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Jelajahi seluruh raw listing dan evaluasi performa filter anti-penipuan DP & HDC Palsu.</div>', unsafe_allow_html=True)

    filter_mode = st.radio("Status Listing:", ["Semua Listing Tunai Valid", "Hanya Terindikasi Perangkap DP / Scam", "Semua Data Mentah"], horizontal=True)

    query = db.query(ScrapedListing)
    if filter_mode == "Semua Listing Tunai Valid":
        query = query.filter(ScrapedListing.is_dp_price == False)
    elif filter_mode == "Hanya Terindikasi Perangkap DP / Scam":
        query = query.filter(ScrapedListing.is_dp_price == True)

    raw_items = query.limit(200).all()

    if raw_items:
        data_rows = []
        for it in raw_items:
            data_rows.append({
                "Platform": it.source_platform.upper(),
                "Judul Iklan": it.title,
                "Harga (IDR)": f"Rp {float(it.price):,.0f}",
                "Status DP/Scam": "🚨 DP TRAP / ANOMALI" if it.is_dp_price else "✅ CASH VALID",
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
        st.info("Tidak ada data listing.")

db.close()
