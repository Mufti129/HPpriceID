# PhonePrice ID — Smartphone Market Intelligence & Hedonic Valuation Engine

PhonePrice ID adalah platform data harvesting, pembersihan cerdas (AI & NLP), dan valuasi ekonometrik harga smartphone bekas & baru di pasar Indonesia (2010 - 2026).

---

## Fitur Utama

- **NLP & Slang Normalizer:** Ekstraksi otomatis istilah pasar smartphone Indonesia (iBox, SEIN, Inter, IMEI Kemenperin vs Bea Cukai, All Operator, Wifi Only, BH 85%, Layar Shadow, Green Line, True Tone On/Off, Face ID).
- **DP Scam & HDC Trap Filter:** Mengeliminasi listing DP/cicilan paylater palsu (misal iPhone 15 Pro Max dipasang Rp 1.5jt) dan HP tiruan/HDC.
- **RapidFuzz Entity Resolution:** Memetakan teks judul liar ke katalog master model & varian RAM/ROM 16 tahun (2010 - 2026).
- **Hedonic Quality Valuation:** Penyesuaian nilai wajar berbasis kondisi riil baterai, bodi, layar, garansi, dan legalitas IMEI.
- **3-Tier Price Corridors (Tukey IQR):** Agregasi kuartil P25 (Bargain Buy Target), Median (FMV), dan P75 (Pristine Grade).
- **Arbitrage & Hot Deals Radar:** Memindai unit dengan selisih harga signifikan untuk margin keuntungan reseller.
- **Interactive Enterprise Streamlit UI:** Dashboard analitik modern berbasis Plotly dengan visualisasi lengkap.

---

## Panduan Memulai Cepat

```bash
# 1. Masuk ke direktori
cd "Scrape Data HP"

# 2. Aktifkan virtual environment
source venv/bin/activate

# 3. Jalankan pipeline setup data
python3 main.py

# 4. Jalankan aplikasi Streamlit
streamlit run app.py
```

---

## Dokumentasi Lengkap
Lihat [DOKUMENTASI_SISTEM_HP.md](DOKUMENTASI_SISTEM_HP.md) untuk kamus data 46+ parameter, formula matematika, dan landasan teori ekonometrik.
