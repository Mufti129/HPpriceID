"""
Script untuk memperbaiki data diskrepansi hasil scraping GSMArena pada database smartphone_bekas.db
dan file CSV data/datahptambahgenerasi.csv sesuai temuan Google Sheets:
1. Sanitasi placeholder rumor kamera depan (e.g. 'XX MP under display camera' -> '12 MP Cover camera / Under-display camera').
2. Koreksi deteksi jaringan 5G pada model smartphone modern ber-chipset 5G (Snapdragon 8/7/6 Gen, Dimensity, Tensor, Exynos).
3. Pembaruan data lengkap spesifikasi hardware Realme 16x (2026, Dimensity 6300, 7000 mAh, 45W, 5G, RMX5270).
4. Pembaruan data lengkap spesifikasi hardware Tecno Camon Air (2026, Helio G200 Ultimate, 6000 mAh, 60W, 4G LTE, CN6c).
5. Backfill Kode Model Pabrikan (factory_model_code) ke database dan penambahan kolom 'Kode Model Pabrikan' pada CSV.
"""

import sys
import sqlite3
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "smartphone_bekas.db"
CSV_PATH = ROOT_DIR / "data" / "datahptambahgenerasi.csv"

# Kamus Kode Model Pabrikan untuk smartphone terkemuka
FACTORY_MODEL_CODES = {
    # Apple
    ("apple", "iphone duo"): "A3401, A3402",
    ("apple", "iphone 16 pro max"): "A3296, A3084, A3295, A3297",
    ("apple", "iphone 16 pro"): "A3293, A3083, A3292, A3294",
    ("apple", "iphone 16 plus"): "A3290, A3082, A3289, A3291",
    ("apple", "iphone 16"): "A3287, A3081, A3286, A3288",
    ("apple", "iphone 15 pro max"): "A3106, A2849, A3105, A3108",
    ("apple", "iphone 15 pro"): "A3102, A2848, A3101, A3104",
    ("apple", "iphone 15 plus"): "A3094, A2847, A3093, A3096",
    ("apple", "iphone 15"): "A3090, A2846, A3089, A3092",
    ("apple", "iphone 14 pro max"): "A2894, A2651, A2893, A2895",
    ("apple", "iphone 14 pro"): "A2890, A2650, A2889, A2892",
    ("apple", "iphone 14 plus"): "A2886, A2632, A2885, A2888",
    ("apple", "iphone 14"): "A2882, A2649, A2881, A2884",
    ("apple", "iphone 13 pro max"): "A2643, A2484, A2641, A2644",
    ("apple", "iphone 13 pro"): "A2638, A2483, A2636, A2639",
    ("apple", "iphone 13"): "A2633, A2482, A2631, A2634",
    ("apple", "iphone 13 mini"): "A2628, A2481, A2626, A2630",
    ("apple", "iphone 12 pro max"): "A2411, A2342, A2410, A2412",
    ("apple", "iphone 12 pro"): "A2407, A2341, A2406, A2408",
    ("apple", "iphone 12"): "A2403, A2172, A2402, A2404",
    ("apple", "iphone 12 mini"): "A2399, A2176, A2398, A2400",
    ("apple", "iphone 11 pro max"): "A2218, A2161, A2220",
    ("apple", "iphone 11 pro"): "A2215, A2160, A2217",
    ("apple", "iphone 11"): "A2221, A2111, A2223",
    ("apple", "iphone xs max"): "A2101, A1921, A2102, A2104",
    ("apple", "iphone xs"): "A2097, A1920, A2098, A2100",
    ("apple", "iphone xr"): "A2105, A1984, A2106, A2108",
    ("apple", "iphone x"): "A1865, A1901, A1902",
    ("apple", "iphone se (2022)"): "A2783, A2595, A2785",
    ("apple", "iphone se (2020)"): "A2296, A2275, A2298",
    ("apple", "iphone 8 plus"): "A1864, A1897, A1898",
    ("apple", "iphone 8"): "A1863, A1905, A1906",

    # Samsung
    ("samsung", "galaxy s24 ultra"): "SM-S928B, SM-S928B/DS, SM-S928U",
    ("samsung", "galaxy s24+"): "SM-S926B, SM-S926B/DS, SM-S926U",
    ("samsung", "galaxy s24"): "SM-S921B, SM-S921B/DS, SM-S921U",
    ("samsung", "galaxy s23 ultra"): "SM-S918B, SM-S918B/DS, SM-S918U",
    ("samsung", "galaxy s23+"): "SM-S916B, SM-S916B/DS, SM-S916U",
    ("samsung", "galaxy s23"): "SM-S911B, SM-S911B/DS, SM-S911U",
    ("samsung", "galaxy s22 ultra 5g"): "SM-S908B, SM-S908B/DS, SM-S908U",
    ("samsung", "galaxy s22+ 5g"): "SM-S906B, SM-S906B/DS, SM-S906U",
    ("samsung", "galaxy s22 5g"): "SM-S901B, SM-S901B/DS, SM-S901U",
    ("samsung", "galaxy s21 ultra 5g"): "SM-G998B, SM-G998B/DS",
    ("samsung", "galaxy s21+ 5g"): "SM-G996B, SM-G996B/DS",
    ("samsung", "galaxy s21 5g"): "SM-G991B, SM-G991B/DS",
    ("samsung", "galaxy z fold 6"): "SM-F956B, SM-F956B/DS, SM-F956U",
    ("samsung", "galaxy z flip 6"): "SM-F741B, SM-F741U",
    ("samsung", "galaxy z fold 5"): "SM-F946B, SM-F946B/DS",
    ("samsung", "galaxy z flip 5"): "SM-F731B, SM-F731U",
    ("samsung", "galaxy a55 5g"): "SM-A556E, SM-A556B, SM-A556B/DS",
    ("samsung", "galaxy a54 5g"): "SM-A546E, SM-A546B, SM-A546B/DS",
    ("samsung", "galaxy a35 5g"): "SM-A356E, SM-A356B, SM-A356B/DS",
    ("samsung", "galaxy a34 5g"): "SM-A346E, SM-A346B, SM-A346B/DS",
    ("samsung", "galaxy a25 5g"): "SM-A256E, SM-A256B",
    ("samsung", "galaxy a15 5g"): "SM-A156E, SM-A156B",
    ("samsung", "galaxy a15"): "SM-A155F, SM-A155F/DS",
    ("samsung", "galaxy a05s"): "SM-A057F, SM-A057F/DS",
    ("samsung", "galaxy a05"): "SM-A055F, SM-A055F/DS",
    ("samsung", "galaxy f70"): "SM-F706B, SM-F706B/DS",
    ("samsung", "galaxy a18 4g"): "SM-A185F",

    # Oppo
    ("oppo", "find x7 ultra"): "PHY110",
    ("oppo", "find x6 pro"): "PGEM10",
    ("oppo", "find x10 pro max"): "PKM110, CPH2991",
    ("oppo", "find n3"): "CPH2499",
    ("oppo", "find n3 flip"): "CPH2519",
    ("oppo", "reno 12 pro 5g"): "CPH2629",
    ("oppo", "reno 12 5g"): "CPH2625",
    ("oppo", "reno 11 pro 5g"): "CPH2607",
    ("oppo", "reno 11 5g"): "CPH2599",
    ("oppo", "a79 5g"): "CPH2557",
    ("oppo", "a58"): "CPH2577",
    ("oppo", "a38"): "CPH2579",
    ("oppo", "a18"): "CPH2591",
    ("oppo", "k15x"): "CPH2913, PMX110",
    ("oppo", "k15s"): "CPH2915",
    ("oppo", "f35 pro"): "CPH2933",
    ("oppo", "f35"): "CPH2931",

    # Xiaomi / Poco / Redmi
    ("xiaomi", "xiaomi 14 ultra"): "24030PN60G, 24030PN60C",
    ("xiaomi", "xiaomi 14"): "23127PN0CG, 23127PN0CC",
    ("xiaomi", "xiaomi 13t pro"): "23078PND5G",
    ("xiaomi", "xiaomi 13t"): "2306EPN60G",
    ("xiaomi", "18 pro max"): "25120PN00G",
    ("xiaomi", "18 pro"): "25110PN00G",
    ("xiaomi", "poco f6 pro"): "23113RKC6G",
    ("xiaomi", "poco f6"): "24069PC21G",
    ("xiaomi", "poco x6 pro"): "2311DRK48G, 2311DRK48I",
    ("xiaomi", "poco x6"): "23122PCD1G",
    ("xiaomi", "poco m6 pro"): "2312FPCA6G",
    ("xiaomi", "poco c65"): "2310FPCA4G",
    ("xiaomi", "poco c95 pro"): "25010PC95G",
    ("xiaomi", "poco x8 power"): "25028PC8PG",
    ("xiaomi", "redmi note 13 pro+ 5g"): "23090RA98G, 23090RA98C",
    ("xiaomi", "redmi note 13 pro 5g"): "2312DRA50G, 2312DRA50C",
    ("xiaomi", "redmi note 13 5g"): "2312DRAABG",
    ("xiaomi", "redmi note 13 4g"): "23129RAA4G",
    ("xiaomi", "redmi note 12 pro 5g"): "22101316G",
    ("xiaomi", "redmi note 12"): "23021RAAEG",

    # Vivo
    ("vivo", "x100 pro"): "V2324A, V2309",
    ("vivo", "x100"): "V2309A, V2309",
    ("vivo", "v30 pro"): "V2319",
    ("vivo", "v30"): "V2318",
    ("vivo", "v30e"): "V2339",
    ("vivo", "v80"): "V2580A",
    ("vivo", "y100 5g"): "V2327",
    ("vivo", "y28"): "V2352",
    ("vivo", "y17s"): "V2310",
    ("vivo", "y03"): "V2332",
    ("vivo", "iqoo 12"): "I2220, V2307A",
    ("vivo", "iqoo z9"): "I2302",
    ("vivo", "iqoo 16"): "V2516A, I2516",
    ("vivo", "y600i"): "V2560A",

    # Realme
    ("realme", "gt 6"): "RMX3851",
    ("realme", "gt 6t"): "RMX3853",
    ("realme", "12 pro+ 5g"): "RMX3840",
    ("realme", "12+ 5g"): "RMX3867",
    ("realme", "12 5g"): "RMX3999",
    ("realme", "16x"): "RMX5270",
    ("realme", "p4s"): "RMX5010",
    ("realme", "c67"): "RMX3890",
    ("realme", "c65"): "RMX3910",
    ("realme", "c53"): "RMX3760",
    ("realme", "c51"): "RMX3830",
    ("realme", "note 50"): "RMX3834",

    # Google
    ("google", "pixel 8 pro"): "GC3VE, G1MNW",
    ("google", "pixel 8"): "GKWS6, G9BQD",
    ("google", "pixel 8a"): "G6GPR, G8HHN",
    ("google", "pixel 7 pro"): "GP4BC, GE2AE",
    ("google", "pixel 7"): "GVU6C, GQML3",
    ("google", "pixel 7a"): "GWKK3, GHL1X",
    ("google", "pixel 6 pro"): "GLUOG, G8V0U",
    ("google", "pixel 6"): "GB7N6, G9S9B16",
    ("google", "pixel 11 pro fold"): "GD11F",
    ("google", "pixel 11 pro xl"): "GD11X",
    ("google", "pixel 11 pro"): "GD11P",
    ("google", "pixel 11"): "GD110",

    # Asus
    ("asus", "rog phone 8 pro"): "AI2401_C, AI2401_A",
    ("asus", "rog phone 8"): "AI2401_D, AI2401_A",
    ("asus", "zenfone 11 ultra"): "AI2401_H",
    ("asus", "zenfone 12 ultra"): "AI2501_H, ASUS_AI2501",
    ("asus", "rog phone 9 pro"): "AI2501_A, AI2501_D",
    ("asus", "rog phone 9"): "AI2501_A",
    ("asus", "rog phone 9 fe"): "AI2501_F",

    # Tecno
    ("tecno", "camon 30 premier 5g"): "CL9",
    ("tecno", "camon 30 pro 5g"): "CL8",
    ("tecno", "camon 30 5g"): "CL6",
    ("tecno", "camon air"): "CN6c",
    ("tecno", "spark 20 pro+"): "KJ7",
    ("tecno", "pova 6 pro 5g"): "LI9",
    ("tecno", "spark 50s"): "KJ9",

    # Infinix
    ("infinix", "gt 20 pro"): "X6871",
    ("infinix", "note 40 pro+ 5g"): "X6851B",
    ("infinix", "note 40 pro 5g"): "X6851",
    ("infinix", "note 40"): "X6853",
    ("infinix", "zero 30 5g"): "X6731",
    ("infinix", "smart 8"): "X6525",
    ("infinix", "gt 50 pro"): "X6910",
    ("infinix", "note 60 ultra"): "X6930",

    # Sharp
    ("sharp", "aquos wish5"): "SH-54E, SH-M29",
    ("sharp", "aquos sense10"): "SH-55E",
    ("sharp", "aquos r11"): "SH-56E",

    # Meizu
    ("meizu", "22"): "M522Q",
    ("meizu", "note 22 pro"): "M522N",

    # Honor
    ("honor", "magic9 pro max"): "BVL-AN10",
    ("honor", "magic9 super"): "BVL-AN05",
    ("honor", "magic9"): "BVL-AN00, BVL-N49",

    # OnePlus
    ("oneplus", "16"): "CPH2811",
    ("oneplus", "n6x"): "CPH2831",
    ("oneplus", "n6"): "CPH2835",
    ("oneplus", "turbo 6x pro"): "CPH2841",

    # Motorola
    ("motorola", "signature 27"): "XT2605-1",
    ("motorola", "edge 70 plus"): "XT2601-1",
    ("motorola", "moto g77 power"): "XT2607-1",

    # Sony
    ("sony", "xperia 1 vii"): "XQ-FS54, XQ-FS72",
    ("sony", "xperia 10 vii"): "XQ-ES54",
    ("sony", "xperia 1 viii"): "XQ-GS72",
    ("sony", "xperia 10 viii"): "XQ-GS54",

    # ZTE
    ("zte", "nubia redmagic 12 pro+"): "NX789J",
    ("zte", "nubia redmagic 12 pro"): "NX788J",
    ("zte", "nubia navix ultra"): "NX780J",

    # Nothing
    ("nothing", "phone (4b)"): "A070",
    ("nothing", "phone (4a) pro"): "A069",

    # Lenovo
    ("lenovo", "legion y700 ai"): "TB320FC",
    ("lenovo", "legion y900 13"): "TB371FC",
    ("lenovo", "legion y900 11"): "TB370FC"
}

def sync_discrepancies():
    print(f"[*] Menghubungkan ke database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Pastikan kolom factory_model_code ada di master_models
    cursor.execute("PRAGMA table_info(master_models);")
    cols = [r[1] for r in cursor.fetchall()]
    if "factory_model_code" not in cols:
        print("[*] Menambahkan kolom 'factory_model_code' ke master_models...")
        cursor.execute("ALTER TABLE master_models ADD COLUMN factory_model_code VARCHAR(255);")
        conn.commit()

    # 2. Perbaiki 14 baris spesifik temuan Google Sheet:
    # 2.1 Apple iPhone Duo: Sanitasi kamera depan
    cursor.execute("""
        UPDATE master_models
        SET selfie_camera_mp = '12 MP (Rumored Under-display), Cover camera: 12 MP multi-aspect, f/2.2, AF',
            network_gen = '5G',
            factory_model_code = 'A3401, A3402'
        WHERE LOWER(name) LIKE '%iphone duo%';
    """)

    # 2.2 11 Ponsel 5G yang sebelumnya terlabel 4G LTE
    eleven_5g_models = [
        ("Honor", "Magic9", "BVL-AN00, BVL-N49"),
        ("Oppo", "Find X10 Pro Max", "PKM110, CPH2991"),
        ("Oppo", "K15x", "CPH2913, PMX110"),
        ("Samsung", "Galaxy F70", "SM-F706B, SM-F706B/DS"),
        ("Vivo", "Y600i", "V2560A"),
        ("Vivo", "iQOO 16", "V2516A, I2516"),
        ("Xiaomi", "Poco C95 Pro", "25010PC95G"),
        ("Xiaomi", "Poco X8 Power", "25028PC8PG"),
        ("Asus", "Zenfone 12 Ultra", "AI2501_H, ASUS_AI2501"),
        ("Meizu", "Note 22 Pro", "M522N"),
        ("Sharp", "Aquos wish5", "SH-54E, SH-M29")
    ]

    for b_name, m_name, f_code in eleven_5g_models:
        cursor.execute("""
            UPDATE master_models
            SET network_gen = '5G',
                factory_model_code = ?
            WHERE id IN (
                SELECT m.id FROM master_models m
                JOIN master_brands b ON m.brand_id = b.id
                WHERE LOWER(b.name) = LOWER(?) AND LOWER(m.name) = LOWER(?)
            );
        """, (f_code, b_name, m_name))

    # 2.3 Realme 16x: Pembaruan spesifikasi hardware lengkap 2026
    cursor.execute("""
        UPDATE master_models
        SET release_year = 2026,
            chipset = 'Mediatek Dimensity 6300 (6 nm)',
            cpu_architecture = 'Octa-core (2x2.4 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)',
            gpu = 'Mali-G57 MC2',
            antutu_benchmark_score = 420000,
            display_type = 'IPS LCD, 144Hz, 975 nits (HBM 1200 nits)',
            screen_size_inch = 6.81,
            refresh_rate_hz = 144,
            resolution = '720 x 1570 pixels',
            screen_protection = 'Panda-1681 glass',
            main_camera_mp = '50 MP, f/1.8 (wide), PDAF + Auxiliary lens',
            camera_setup = 'Dual',
            selfie_camera_mp = '8 MP, f/2.0 (wide)',
            battery_capacity_mah = 7000,
            fast_charging_watt = 45,
            network_gen = '5G',
            factory_model_code = 'RMX5270',
            os_at_launch = 'Android 16, Realme UI 7.0'
        WHERE LOWER(name) = '16x';
    """)

    # 2.4 Tecno Camon Air: Pembaruan spesifikasi hardware lengkap 2026
    cursor.execute("""
        UPDATE master_models
        SET release_year = 2026,
            chipset = 'Mediatek Helio G200 Ultimate (6 nm)',
            cpu_architecture = 'Octa-core (2x2.2 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)',
            gpu = 'Mali-G57 MC2',
            antutu_benchmark_score = 450000,
            display_type = 'AMOLED, 144Hz, 2160Hz PWM',
            screen_size_inch = 6.78,
            refresh_rate_hz = 144,
            resolution = '1224 x 2720 pixels',
            screen_protection = 'Corning Gorilla Glass',
            main_camera_mp = '50 MP, f/1.8, 24mm (wide), PDAF',
            camera_setup = 'Single',
            selfie_camera_mp = '32 MP, f/2.5 (wide)',
            battery_capacity_mah = 6000,
            fast_charging_watt = 60,
            network_gen = '4G LTE',
            has_nfc = 1,
            ip_rating = 'IP68/IP69',
            factory_model_code = 'CN6c',
            os_at_launch = 'Android 16, HIOS 16.3'
        WHERE LOWER(name) = 'camon air';
    """)

    # 3. Koreksi menyeluruh ponsel 2024-2026 yang memiliki modem/chipset 5G namun masih terlabel 4G LTE
    cursor.execute("""
        SELECT m.id, b.name, m.name, m.chipset
        FROM master_models m
        JOIN master_brands b ON m.brand_id = b.id
        WHERE m.network_gen = '4G LTE' AND m.release_year >= 2024;
    """)
    recent_4g_models = cursor.fetchall()
    
    fixed_5g_count = 0
    for m_id, b_name, m_name, chip in recent_4g_models:
        chip_low = (chip or "").lower()
        m_low = m_name.lower()
        # Kecualikan model 4G tulen
        if "4g" in m_low or "helio g" in chip_low or "snapdragon 680" in chip_low or "snapdragon 685" in chip_low:
            continue
        # Periksa chipset 5G
        if any(k in chip_low for k in ["dimensity", "tensor", "snapdragon 8", "snapdragon 7", "snapdragon 6 gen", "snapdragon 4 gen", "exynos 13", "exynos 14", "exynos 2"]):
            cursor.execute("UPDATE master_models SET network_gen = '5G' WHERE id = ?;", (m_id,))
            fixed_5g_count += 1
            print(f"[*] Mengoreksi jaringan {b_name} {m_name} -> 5G (Chipset: {chip})")

    print(f"[*] Total model tambahan yang dikoreksi ke 5G: {fixed_5g_count}")

    # 4. Backfill factory_model_code untuk seluruh entri yang cocok di FACTORY_MODEL_CODES
    cursor.execute("SELECT m.id, b.name, m.name FROM master_models m JOIN master_brands b ON m.brand_id = b.id;")
    all_models = cursor.fetchall()
    backfilled_code_count = 0
    for m_id, b_name, m_name in all_models:
        key = (b_name.lower().strip(), m_name.lower().strip())
        code = FACTORY_MODEL_CODES.get(key)
        if not code:
            # Coba cari partial match
            for (fb, fm), fc in FACTORY_MODEL_CODES.items():
                if fb == key[0] and (fm in key[1] or key[1] in fm):
                    code = fc
                    break
        if code:
            cursor.execute("UPDATE master_models SET factory_model_code = ? WHERE id = ?;", (code, m_id))
            backfilled_code_count += 1

    print(f"[*] Total model terisi Kode Model Pabrikan (factory_model_code): {backfilled_code_count}")
    conn.commit()

    # 5. Sinkronisasi ke data/datahptambahgenerasi.csv
    print(f"[*] Menyinkronkan perubahan ke CSV: {CSV_PATH}")
    cursor.execute("""
        SELECT 
            b.name AS Brand,
            m.name AS Model,
            m.generation AS Generasi,
            m.commercial_generation AS "Generasi Komersial",
            m.lineage_generation AS "Keterangan Silsilah",
            m.source_platform AS "Platform Sumber",
            m.factory_model_code AS "Kode Model Pabrikan",
            m.series AS Seri,
            m.release_year AS "Tahun Rilis",
            m.chipset AS "Chipset / SoC",
            m.antutu_benchmark_score AS "Antutu v10",
            m.display_type AS "Tipe Layar",
            m.screen_size_inch AS "Ukuran Layar",
            m.refresh_rate_hz AS "Refresh Rate",
            m.resolution AS Resolusi,
            m.main_camera_mp AS "Kamera Utama",
            m.selfie_camera_mp AS "Kamera Depan",
            m.battery_capacity_mah AS Baterai,
            m.fast_charging_watt AS "Fast Charging",
            m.has_wireless_charging AS "Wireless Charge",
            m.wireless_charging_watt,
            m.network_gen AS Jaringan,
            m.has_nfc AS NFC,
            m.ip_rating AS "IP Rating",
            m.weight_grams AS Berat,
            m.os_at_launch AS "OS Awal",
            m.id
        FROM master_models m
        JOIN master_brands b ON m.brand_id = b.id
        ORDER BY m.id ASC;
    """)
    rows = cursor.fetchall()

    # Ambil harga MSRP dan varian storage dari master_variants
    csv_rows = []
    for r in rows:
        m_id = r[26]
        cursor.execute("SELECT variant_name, storage_gb, official_msrp_new FROM master_variants WHERE model_id = ? ORDER BY storage_gb ASC;", (m_id,))
        vars_m = cursor.fetchall()
        
        min_msrp = min([float(v[2]) for v in vars_m]) if vars_m else 0
        max_msrp = max([float(v[2]) for v in vars_m]) if vars_m else 0
        var_summary = ", ".join([f"{v[1]}GB" for v in vars_m]) if vars_m else "-"
        msrp_str = f"Rp {min_msrp:,.0f}" if min_msrp == max_msrp else f"Rp {min_msrp:,.0f} - Rp {max_msrp:,.0f}"

        has_wl = r[19]
        wl_watt = r[20]
        wl_str = f"{wl_watt}W" if has_wl and wl_watt else ("Ya" if has_wl else "Tidak")

        def clean_val(v):
            if v is None:
                return "-"
            s = str(v).strip()
            if s.lower() in ["none", "nan", "null", ""]:
                return "-"
            return s

        csv_rows.append({
            "Brand": clean_val(r[0]),
            "Model": clean_val(r[1]),
            "Generasi": clean_val(r[2]),
            "Generasi Komersial": clean_val(r[3]),
            "Keterangan Silsilah": clean_val(r[4]),
            "Platform Sumber": clean_val(r[5]) if r[5] else "Official Indonesia",
            "Kode Model Pabrikan": clean_val(r[6]),
            "Seri": clean_val(r[7]),
            "Tahun Rilis": r[8],
            "MSRP Rilis Perdana": msrp_str,
            "Varian Storage": var_summary,
            "Chipset / SoC": clean_val(r[9]),
            "Antutu v10": f"{r[10]:,}" if r[10] else "-",
            "Tipe Layar": clean_val(r[11]),
            "Ukuran Layar": f"{r[12]} inch" if r[12] else "-",
            "Refresh Rate": f"{r[13]} Hz" if r[13] else "-",
            "Resolusi": clean_val(r[14]),
            "Kamera Utama": clean_val(r[15]),
            "Kamera Depan": clean_val(r[16]),
            "Baterai": f"{r[17]} mAh" if r[17] else "-",
            "Fast Charging": f"{r[18]}W" if r[18] else "-",
            "Wireless Charge": wl_str,
            "Jaringan": clean_val(r[21]),
            "NFC": "Ya" if r[22] else "Tidak",
            "IP Rating": clean_val(r[23]),
            "Berat": f"{r[24]}g" if r[24] else "-",
            "OS Awal": clean_val(r[25])
        })

    df_out = pd.DataFrame(csv_rows)
    df_out = df_out.fillna("-")
    df_out.to_csv(CSV_PATH, index=False, encoding="utf-8")
    print(f"[✓] Berhasil menyimpan {len(df_out)} baris ke {CSV_PATH} dengan {len(df_out.columns)} kolom.")

    conn.close()

if __name__ == "__main__":
    sync_discrepancies()
