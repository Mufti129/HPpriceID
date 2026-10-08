# DOKUMENTASI LENGKAP & SPESIFIKASI TEKNIS SISTEM
## PHONEPRICE ID — SMARTPHONE INTELLIGENCE & HEDONIC VALUATION ENGINE
**Penulis & Pengembang:** Mukhammad Rekza Mufti (Data & System Analyst)  
**Versi Sistem:** v2.0 (Smartphone Enterprise Intelligence Edition)  
**Rentang Historis Master Katalog:** 2010 – 2026 (16 Brand Terkemuka Indonesia)  
**Waktu Rilis:** 2026  
**Repositori GitHub:** [https://github.com/Mufti129/HPpriceID](https://github.com/Mufti129/HPpriceID)  
**Platform Deploy:** Streamlit Community Cloud (Python 3.13 Runtime)  

---

# DAFTAR ISI
1. [BAB I: Pendahuluan & Latar Belakang Masalah Pasar Smartphone](#bab-i-pendahuluan--latar-belakang-masalah-pasar-smartphone)
2. [BAB II: Arsitektur Sistem End-to-End](#bab-ii-arsitektur-sistem-end-to-end)
3. [BAB III: Kamus Data & Spesifikasi Lengkap Parameter Output](#bab-iii-kamus-data--spesifikasi-lengkap-parameter-output)
4. [BAB IV: Logika Matematis, Model Ekonometrik & Teori Valuasi](#bab-iv-logika-matematis-model-ekonometrik--teori-valuasi)
5. [BAB V: Taksonomi Master Katalog Smartphone 16 Tahun (2010–2026)](#bab-v-taksonomi-master-katalog-smartphone-16-tahun-20102026)
6. [BAB VI: Panduan Instalasi & Operasional](#bab-vi-panduan-instalasi--operasional)

---

# BAB I: Pendahuluan & Latar Belakang Masalah Pasar Smartphone

### 1.1 Kompleksitas & Asimetri Informasi Pasar Smartphone Bekas Indonesia
Pasar smartphone sekunder (bekas) di Indonesia memiliki karakteristik pasar tidak terstruktur dengan risiko asimetri informasi yang sangat tinggi:

1. **Regulasi IMEI & Pemblokiran Sinyal Seluler (Aturan Kemenperin & Bea Cukai):**
   - Unit Resmi Indonesia (iBox, Digimap, SEIN, TAM, Erajaya) terdaftar permanen pada database TPP Kemenperin.
   - Unit Ex-Inter Resmi Pajak (Lolos Bea Cukai / Kemenkeu) sinyal aktif permanen all operator.
   - Unit Ex-Inter Non-Pajak / Whitelist 3 Bulan (Smartfren Only / Tembak Sinyal Sementara) berisiko tinggi kehilangan sinyal (No Service / Sinyal Blokir / Wifi Only), menurunkan nilai aset 40% - 60%.
2. **Kesehatan Baterai & Degradasi Kimiawi (Battery Health - BH):**
   - Pada iPhone, persentase Battery Health (BH 100% vs 85% vs <80% Service) sangat menentukan valuasi jual sekunder.
3. **Kualitas Suku Cadang & Panel Layar (Display Substitution Risk):**
   - Pergantian layar original ke imitasi (Incell LCD / OLED OEM) sering mematikan fitur True Tone dan Face ID, serta memicu cacat layar (Shadow tipis/tebal, Green Line, Layar Bergaris).
4. **Praktek Iklan Clickbait DP / Paylater (DP Trap Scam):**
   - Penjual online sering mencantumkan nominal DP cicilan (misal Rp 1.500.000 untuk iPhone 15 Pro Max) pada kolom harga tunai.
5. **Kunci Keamanan & Akun (Bypass / MDM / FRP Lock):**
   - Unit yang terkunci iCloud, Mi Cloud, atau MDM perusahaan sering dijual murah dan tidak dapat direset pabrik (Clean vs Bypass).

---

# BAB II: Arsitektur Sistem End-to-End

```text
+-----------------------------------------------------------------------------------+
|                        1. DATA HARVESTING & INGESTION                             |
|  - E-Commerce & Marketplace: OLX Indonesia, Tokopedia, Shopee, FB Marketplace      |
|  - Multi-threaded Crawlers, Header Spoofing & Request Pipeline                    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                   2. AI & NLP DATA REFINEMENT PIPELINE                            |
|  - Indonesian Smartphone Slang Dictionary (iBox, SEIN, Inter, All Op, BH 88%)     |
|  - DP Scam & HDC Replica Detector                                                 |
|  - Hardware Metadata Extractor (RAM, ROM Storage, Sinyal IMEI, Panel Layar)       |
|  - RapidFuzz Entity Matcher (Multi-token resolution ke Master Varian)             |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                     3. RELATIONAL DATABASE LAYER (SQLite)                         |
|  - master_brands (Apple, Samsung, Xiaomi, Poco, Vivo, Oppo, Realme, Google, Asus) |
|  - master_models (Hardware Specs: SoC, Display, Camera MP, Battery mAh, Charging) |
|  - master_variants (Konfigurasi RAM/Storage & MSRP Baru OTR)                       |
|  - scraped_listings (Cleaned Secondary Market Listings)                           |
|  - market_price_stats (Agregasi Harian Kuartil P25, FMV, P75)                     |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                 4. ECONOMETRIC & PRICING ANALYTICS ENGINE                         |
|  - Tukey Interquartile Range (IQR) Outlier Filter                                 |
|  - Hedonic Quality Pricing Model (Penyesuaian IMEI, Garansi, BH, Layar, Bodi)    |
|  - Multi-Tier Depreciation Engine (Apple Retention vs Android Flagship vs Mid)    |
|  - Fama Arbitrage Opportunity Scanner (Super Arbitrage, High, Moderate)           |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|             5. ENTERPRISE STREAMLIT USER INTERFACE & VISUALIZATION                |
|  - Live Marketplace Explorer & Filter        - Interactive FMV Hedonic Calculator |
|  - 3-Tier Price Corridor Visualizer          - Hardware Spec Comparison Matrix    |
|  - Real Depreciation Curve Analysis          - Arbitrage & Hot Deals Radar        |
+-----------------------------------------------------------------------------------+
```

---

# BAB III: Kamus Data & Spesifikasi Lengkap Parameter Output

### 3.1 Parameter Identitas & Taksonomi Master Katalog
1. `brand_name` (String): Produsen resmi smartphone (Apple, Samsung, Xiaomi, Poco, Vivo, Oppo, Realme, Infinix, Google, Asus, Sony, Huawei, Nokia, BlackBerry, Nothing, ZTE).
2. `model_name` (String): Lini model smartphone (misal iPhone 15 Pro Max, Galaxy S24 Ultra, Poco F6).
3. `variant_name` (String): Nama lengkap varian memori (misal iPhone 15 Pro Max 256GB Natural Titanium).
4. `series` (String): Segmen lini produk (Pro Max, S-Series Flagship, Performance, Ultra, Midrange, Foldable).
5. `release_year` (Integer): Tahun peluncuran resmi di pasar (2010 - 2026).
6. `ram_gb` (Integer): Kapasitas RAM fisik dalam Gigabyte (1, 2, 3, 4, 6, 8, 12, 16, 24 GB).
7. `storage_gb` (Integer): Kapasitas internal storage dalam Gigabyte / Terabyte (8, 16, 32, 64, 128, 256, 512, 1024 GB).
8. `official_msrp_new` (Numeric IDR): Harga resmi retail On-The-Road (OTR) saat peluncuran baru di Indonesia.

### 3.2 Parameter Spesifikasi Teknis Hardware (Hardware Performance Specs)
9. `chipset` (String): Nama chipset / System-on-Chip (Apple A18 Pro 3nm, Snapdragon 8 Gen 3, Dimensity 9300).
10. `cpu_architecture` (String): Konfigurasi inti dan clock speed prosesor.
11. `gpu` (String): Unit pemrosesan grafis (Adreno 750, Apple 6-core GPU, Immortalis-G720).
12. `antutu_benchmark_score` (Integer): Skor benchmark AnTuTu.
13. `display_type` (String): Teknologi panel display (LTPO Super Retina XDR OLED, Dynamic AMOLED 2X, IPS LCD).
14. `screen_size_inch` (Float): Ukuran diagonal layar dalam inci (3.5" s/d 7.82" Fold).
15. `refresh_rate_hz` (Integer): Laju penyegaran layar (60Hz, 120Hz ProMotion, 144Hz, 165Hz).
16. `resolution` (String): Resolusi native layar (FHD+, 1.5K, QHD+ 2K).
17. `peak_brightness_nits` (Integer): Tingkat kecerahan puncak panel display (nits).
18. `screen_protection` (String): Kaca pelindung layar (Ceramic Shield, Gorilla Glass Victus 2, Gorilla Armor).
19. `main_camera_mp` (String): Konfigurasi & resolusi kamera belakang utama.
20. `camera_setup` (String): Jumlah modul kamera (Single, Dual, Triple, Quad).
21. `has_ois` (Boolean): Dukungan stabilisasi mekanis lensa (Optical Image Stabilization).
22. `optical_zoom_level` (String): Kemampuan pembesaran optik murni (2x, 3x, 5x Periscope, 10x Periscope).
23. `selfie_camera_mp` (String): Resolusi dan bukaan lensa kamera depan.
24. `video_recording_max` (String): Resolusi rekaman video tertinggi (4K@60fps ProRes HDR, 8K@30fps).
25. `battery_capacity_mah` (Integer): Kapasitas baterai dalam miliampere-hour (mAh).
26. `fast_charging_watt` (Integer): Kecepatan pengisian daya kabel (Watt).
27. `has_wireless_charging` (Boolean): Dukungan pengisian nirkabel (Qi / MagSafe).
28. `wireless_charging_watt` (Integer): Kecepatan wireless charging (Watt).
29. `network_gen` (String): Jaringan seluler yang didukung (3G / 4G LTE / 5G Ready).
30. `has_nfc` (Boolean): Ketersediaan chip NFC untuk transaksi e-money.
31. `ip_rating` (String): Sertifikasi ketahanan air dan debu (IP68, IP67, IP65, IP54, None).
32. `weight_grams` (Integer): Bobot total smartphone dalam gram.
33. `os_at_launch` (String): Versi sistem operasi saat peluncuran.

### 3.3 Parameter Atribut Pasar Sekunder (Secondary Market Condition & Legitimacy)
34. `warranty_type` (String): Asal unit dan garansi (Resmi Indonesia, Ex-Inter Pajak Bea Cukai, Ex-Inter Non-Pajak, Garansi Distributor).
35. `warranty_status` (String): Status keaktifan garansi (Aktif, Habis Ex-Resmi, Garansi Toko 1 Bulan).
36. `imei_status` (String): Status registrasi IMEI Indonesia (IMEI Kemenperin Permanen, IMEI Bea Cukai All Operator, IMEI 3 Bulan / Smartfren Only, Wifi Only / Sinyal Blokir).
37. `battery_health_pct` (Integer): Persentase Battery Health aktual (50% - 100%).
38. `completeness` (String): Kelengkapan unit jual (Fullset Original, Fullset OEM, Batangan / Unit Only).
39. `physical_grade` (String): Grade kondisi fisik bodi (Grade A+ Like New 99%, Grade A Mulus 95%, Grade B Lecet Wajar, Grade C Dent/Baret).
40. `screen_condition` (String): Kondisi layar (Normal Original, Layar Ganti OLED OEM/Incell, Shadow Tipis, Shadow Tebal, Green Line / Garis).
41. `biometrics_status` (String): Status sensor biometrik (Face ID / Touch ID Normal Aktif vs Rusak / Off).
42. `truetone_status` (String): Status sensor True Tone (Aktif vs Mati).
43. `account_lock_status` (String): Keamanan akun (Clean Bebas Reset vs Bypass / MDM Locked).
44. `is_dp_price` (Boolean): Flag deteksi perangkap iklan DP / Cicilan semu.

### 3.4 Parameter Valuasi & Ekonometrik (Econometric & Pricing Analytics)
45. `price_p25_bargain` (Numeric IDR): Kuartil 1 batas bawah harga beli murah (Bargain Hunter Target).
46. `price_median_fmv` (Numeric IDR): Nilai Pasar Wajar ekuilibrium (Fair Market Value).
47. `price_p75_pristine` (Numeric IDR): Kuartil 3 batas atas kondisi istimewa.
48. `hedonic_adjusted_price` (Numeric IDR): Nilai valuasi final setelah penyesuaian parameter kualitas riil.
49. `real_depreciation_pct` (Numeric %): Persentase depresiasi riil dari MSRP Baru terhadap FMV.
50. `arbitrage_discount_pct` (Numeric %): Persentase diskon arbitrase terhadap FMV pasar.
51. `arbitrage_deal_tier` (String): Klasifikasi arbitrase (Tier 1: Super Arbitrage >=22%, Tier 2: High Arbitrage 15-21%, Tier 3: Moderate 12-14%).

---

# BAB IV: Logika Matematis, Model Ekonometrik & Teori Valuasi

### 4.1 Model Penyesuaian Harga Hedonik (Lancaster-Rosen Hedonic Pricing)
Nilai sebuah smartphone bekas dihitung berdasarkan dekomposisi atribut kualitas intrinsik dan legalitasnya:

$$\text{FMV}_{\text{Final}} = \text{Base FMV}_{\text{Median}} \times \left(1 + \sum \Delta_{\text{Hedonik}}\right)$$

Tabel Koefisien Bobot Hedonik:
- **Status IMEI & Sinyal:**
  - IMEI Kemenperin Permanen: $\Delta = 0\%$
  - IMEI Bea Cukai All Operator: $\Delta = -5\%$
  - IMEI 3 Bulan / Smartfren Only: $\Delta = -22\%$
  - Wifi Only / Sinyal Blokir: $\Delta = -40\%$
- **Status Garansi:**
  - Garansi Resmi Aktif (>6 bln): $\Delta = +8\%$
  - Ex-Resmi (Habis): $\Delta = 0\%$
  - Ex-Inter Non-Pajak: $\Delta = -12\%$
- **Battery Health (iPhone):**
  - $\text{BH} \ge 95\%$: $\Delta = +4\%$
  - $85\% \le \text{BH} \le 94\%$: $\Delta = 0\%$
  - $80\% \le \text{BH} \le 84\%$: $\Delta = -5\%$
  - $\text{BH} < 80\%$ (Service): $\Delta = -12\%$
- **Kelengkapan Unit:**
  - Fullset Original: $\Delta = 0\%$
  - Fullset OEM: $\Delta = -5\%$
  - Batangan (Unit Only): $\Delta = -12\%$
- **Kondisi Fisik & Bodi:**
  - Grade A+ (Like New 99%): $\Delta = +5\%$
  - Grade A (Mulus 95%): $\Delta = 0\%$
  - Grade B (Lecet Pemakaian): $\Delta = -8\%$
  - Grade C (Dent/Baret): $\Delta = -18\%$
- **Kondisi Layar & Sensor:**
  - Layar Normal: $\Delta = 0\%$
  - Shadow Tipis: $\Delta = -15\%$
  - Shadow Tebal: $\Delta = -30\%$
  - Layar Green Line / Garis: $\Delta = -45\%$
  - Layar Ganti OEM / Incell: $\Delta = -25\%$
  - Face ID / Touch ID Rusak: $\Delta = -20\%$
  - True Tone Mati: $\Delta = -6\%$

---

# BAB V: Taksonomi Master Katalog Smartphone 16 Tahun (2010–2026)

Master katalog mencakup 16 produsen smartphone dengan segmentasi multi-tier sejak era 2010 hingga 2026:
1. **Apple (2010 - 2026):** iPhone 4, 5s, 6s, 7 Plus, X, XR, 11, 11 Pro Max, 12, 12 Pro Max, 13, 13 Pro, 13 Pro Max, 14, 14 Pro Max, 15, 15 Pro, 15 Pro Max, 16, 16 Pro, 16 Pro Max.
2. **Samsung (2010 - 2026):** Galaxy S I9000, S4, S8, S10+, Note 10+, S20 Ultra, Note 20 Ultra, S22 Ultra, S23 Ultra, S24 Ultra, Z Fold 6, A55 5G.
3. **Xiaomi / Poco / Redmi (2013 - 2026):** Redmi Note 3, Pocophone F1, Redmi Note 13 Pro+ 5G, Poco F6, Xiaomi 14 Leica.
4. **Vivo / iQOO (2015 - 2026):** iQOO 12, Vivo X100 Pro ZEISS.
5. **Oppo (2013 - 2026):** Find N3 Fold, Reno 12 Pro 5G.
6. **Realme (2018 - 2026):** Realme GT 6 Snapdragon 8s Gen 3.
7. **Infinix & Tecno (2015 - 2026):** Infinix GT 20 Pro Gaming.
8. **Google Pixel (2016 - 2026):** Pixel 8 Pro Tensor G3.
9. **Asus ROG & Zenfone (2015 - 2026):** Zenfone 10, ROG Phone 8 Pro 165Hz.
10. **Sony Xperia (2013 - 2026):** Xperia 1 VI Continuous Optical Zoom.
11. **Huawei (2013 - 2026):** Pura 70 Ultra Retractable XMAGE.
12. **Nothing (2022 - 2026):** Nothing Phone (2) Glyph Interface.

---

# BAB VI: Panduan Instalasi & Operasional

```bash
# 1. Masuk ke direktori
cd "Scrape Data HP"

# 2. Buat virtual environment & install dependensi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Jalankan pipeline inisialisasi & seeder data
python3 main.py

# 4. Jalankan Enterprise Streamlit Web Dashboard
streamlit run app.py
```
