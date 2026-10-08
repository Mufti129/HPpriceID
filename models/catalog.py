from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Numeric, Boolean, Float, DateTime, Date, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from models.database import Base

class MasterBrand(Base):
    __tablename__ = "master_brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)  # Apple, Samsung, Xiaomi, Poco, Vivo, Oppo, Realme, Infinix, Google, Asus
    country_origin = Column(String(50), nullable=True)                 # US, South Korea, China, Taiwan
    tier_category = Column(String(50), default="Mainstream")           # Flagship-Dominant, Value-for-Money, Premium, Gaming
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    models = relationship("MasterModel", back_populates="brand", cascade="all, delete-orphan")


class MasterModel(Base):
    """
    Entitas Model Smartphone beserta Spesifikasi Teknis Hardware Utama.
    """
    __tablename__ = "master_models"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("master_brands.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False, index=True)              # e.g. iPhone 15 Pro Max, Galaxy S24 Ultra, Poco F6
    series = Column(String(50), nullable=True)                          # Number Series, Pro, Ultra, Note, S-Series, Z-Fold, ROG
    release_year = Column(Integer, nullable=False, index=True)          # 2018 - 2026
    
    # 1. Hardware: Processor & Performa
    chipset = Column(String(100), nullable=True)                        # Apple A17 Pro (3nm), Snapdragon 8 Gen 3 (4nm), Dimensity 9300
    cpu_architecture = Column(String(100), nullable=True)               # Hexa-core (2x3.78GHz + 4x2.11GHz)
    gpu = Column(String(100), nullable=True)                            # Apple GPU (6-core), Adreno 750, Immortalis-G720
    antutu_benchmark_score = Column(Integer, nullable=True)             # Estimasi Antutu v10 Score

    # 2. Hardware: Layar & Display
    display_type = Column(String(100), nullable=True)                   # LTPO Super Retina XDR OLED, Dynamic AMOLED 2X, IPS LCD
    screen_size_inch = Column(Float, nullable=True)                     # 6.1, 6.7, 6.8
    refresh_rate_hz = Column(Integer, default=60)                       # 60, 90, 120, 144, 165
    resolution = Column(String(50), nullable=True)                      # FHD+ (1080x2400), 1.5K (1220x2712), QHD+ (1440x3120)
    peak_brightness_nits = Column(Integer, nullable=True)               # 1000, 2000, 2600, 4500
    screen_protection = Column(String(100), nullable=True)              # Ceramic Shield, Gorilla Glass Victus 2

    # 3. Hardware: Kamera
    main_camera_mp = Column(String(100), nullable=True)                 # 48 MP (wide) + 12 MP (telephoto 5x) + 12 MP (ultrawide)
    camera_setup = Column(String(20), default="Triple")                 # Single, Dual, Triple, Quad
    has_ois = Column(Boolean, default=True)                             # Optical Image Stabilization
    optical_zoom_level = Column(String(30), nullable=True)              # 2x, 3x, 5x Periscope, 10x Periscope
    selfie_camera_mp = Column(String(50), nullable=True)                # 12 MP, f/1.9, PDAF
    video_recording_max = Column(String(50), nullable=True)             # 4K@60fps Dolby Vision, 8K@30fps

    # 4. Hardware: Baterai & Charging
    battery_capacity_mah = Column(Integer, nullable=True)               # 4441, 5000, 5500
    fast_charging_watt = Column(Integer, default=20)                    # 20W, 45W, 67W, 120W
    has_wireless_charging = Column(Boolean, default=False)              # Qi / MagSafe
    wireless_charging_watt = Column(Integer, default=0)                 # 15W, 50W

    # 5. Konektivitas & Proteksi
    network_gen = Column(String(20), default="5G")                      # 5G, 4G LTE
    has_nfc = Column(Boolean, default=True)
    ip_rating = Column(String(20), default="IP68")                      # IP68, IP67, IP54, None
    weight_grams = Column(Integer, nullable=True)                       # 187, 221, 232

    # 6. Sistem Operasi & Media
    os_at_launch = Column(String(50), nullable=True)                    # iOS 17, Android 14 One UI 6.1
    image_url = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    brand = relationship("MasterBrand", back_populates="models")
    variants = relationship("MasterVariant", back_populates="model", cascade="all, delete-orphan")


class MasterVariant(Base):
    """
    Varian Spesifik Berdasarkan Konfigurasi RAM, ROM (Storage), dan Harga Resmi Peluncuran (MSRP).
    """
    __tablename__ = "master_variants"

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("master_models.id", ondelete="CASCADE"), nullable=False)
    variant_name = Column(String(150), nullable=False, index=True)      # e.g. iPhone 15 Pro Max 256GB, Galaxy S24 Ultra 12GB/512GB
    ram_gb = Column(Integer, nullable=True)                             # 4, 6, 8, 12, 16
    storage_gb = Column(Integer, nullable=False)                        # 64, 128, 256, 512, 1024 (1TB)
    color_options = Column(String(200), nullable=True)                  # Natural Titanium, Black, Blue, etc.
    official_msrp_new = Column(Numeric(15, 2), nullable=False)          # Harga Baru Resmi Peluncuran OTR Indonesia (IDR)
    aliases = Column(Text, nullable=True)                               # Keyword pencarian & singkatan pasar (e.g. ip15promax, 15 pmax 256)
    image_url = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    model = relationship("MasterModel", back_populates="variants")
    scraped_listings = relationship("ScrapedListing", back_populates="matched_variant")


class ScrapedListing(Base):
    """
    Data Listing Smartphone Bekas / Sekunder yang diekstraksi dari Marketplace Indonesia.
    """
    __tablename__ = "scraped_listings"

    id = Column(Integer, primary_key=True, index=True)
    source_platform = Column(String(50), nullable=False, index=True)    # 'olx', 'tokopedia', 'facebook', 'shopee'
    external_id = Column(String(100), nullable=False, index=True)       # ID unik listing
    url = Column(Text, nullable=False)
    title = Column(String(300), nullable=False)
    raw_description = Column(Text, nullable=True)

    # Resolusi Varian oleh AI Matcher
    matched_variant_id = Column(Integer, ForeignKey("master_variants.id"), nullable=True, index=True)
    claimed_year = Column(Integer, nullable=True, index=True)

    # Harga & Filter Penipuan (DP Scam Filter)
    price = Column(Numeric(15, 2), nullable=False, index=True)
    is_dp_price = Column(Boolean, default=False, index=True)            # True jika harga hanya DP / Angsuran palsu

    # Atribut Spesifik Pasar HP Sekunder (Hasil Ekstraksi NLP)
    # 1. Asal Unit & Garansi
    warranty_type = Column(String(50), default="Resmi Indonesia")       # 'Resmi Indonesia (iBox/SEIN/TAM)', 'Ex-Inter Pajak Bea Cukai', 'Ex-Inter Non-Pajak', 'Garansi Distributor'
    warranty_status = Column(String(50), default="Habis (Ex-Resmi)")    # 'Aktif (Masih Garansi)', 'Habis (Ex-Resmi)', 'Garansi Toko 1 Bulan'
    
    # 2. Status Sinyal & Regulasi IMEI Indonesia
    imei_status = Column(String(50), default="IMEI Kemenperin Permanen")# 'IMEI Kemenperin Permanen', 'IMEI Bea Cukai All Op', 'IMEI 3 Bulan / Smartfren', 'Wifi Only / Sinyal Blokir'
    
    # 3. Kesehatan Baterai (Battery Health - BH)
    battery_health_pct = Column(Integer, nullable=True)                 # e.g. 85, 92, 100 (% untuk iPhone) / None untuk Android
    
    # 4. Kelengkapan Unit
    completeness = Column(String(50), default="Fullset Original")       # 'Fullset Original', 'Fullset OEM', 'Batangan / Unit Only'
    
    # 5. Kondisi Fisik & Layar
    physical_grade = Column(String(50), default="Grade A (Mulus 95%)")   # 'Grade A+ (Like New 99%)', 'Grade A (Mulus 95%)', 'Grade B (Lecet Wajar)', 'Grade C (Dent/Baret)'
    screen_condition = Column(String(50), default="Normal Original")    # 'Normal Original', 'Layar Ganti (OLED OEM/Incell)', 'Shadow Tipis', 'Shadow Tebal', 'Green Line / Garis'
    
    # 6. Fitur Keamanan & Biometrik
    biometrics_status = Column(String(50), default="Normal Aktif")      # 'Face ID / Touch ID Normal', 'Face ID / Touch ID Rusak/Off'
    truetone_status = Column(String(50), default="Aktif")               # 'Aktif', 'Mati / Non-Aktif'
    account_lock_status = Column(String(50), default="Clean")           # 'Clean (Bebas Reset)', 'Bypass / MDM Locked'

    # Lokasi & Profil Penjual
    province = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True, index=True)
    seller_name = Column(String(150), nullable=True)
    seller_type = Column(String(50), default="Individual")              # 'Individual', 'Store / Toko HP'

    # Timestamps
    posted_at = Column(DateTime, nullable=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="ACTIVE")

    __table_args__ = (
        UniqueConstraint("source_platform", "external_id", name="uq_hp_source_external_id"),
    )

    matched_variant = relationship("MasterVariant", back_populates="scraped_listings")


class MarketPriceStats(Base):
    """
    Agregasi Statistik Harga Pasar Smartphone Harian (Tukey IQR, FMV, Kuartil P25/P75).
    """
    __tablename__ = "market_price_stats"

    id = Column(Integer, primary_key=True, index=True)
    stat_date = Column(Date, nullable=False, index=True)
    variant_id = Column(Integer, ForeignKey("master_variants.id", ondelete="CASCADE"), nullable=False, index=True)
    city = Column(String(100), nullable=True, index=True)
    sample_count = Column(Integer, nullable=False, default=0)
    
    price_min = Column(Numeric(15, 2), nullable=False)
    price_p25 = Column(Numeric(15, 2), nullable=False)                  # Target Beli Murah (Bargain Hunter)
    price_median = Column(Numeric(15, 2), nullable=False)               # Fair Market Value (FMV Ekuilibrium)
    price_p75 = Column(Numeric(15, 2), nullable=False)                  # Unit Istimewa / Pristine Grade A+
    price_max = Column(Numeric(15, 2), nullable=False)

    calculated_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("stat_date", "variant_id", "city", name="uq_hp_stat_date_variant_city"),
    )
