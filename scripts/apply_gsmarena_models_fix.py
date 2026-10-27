import sqlite3
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "smartphone_bekas.db"
CSV_PATH = ROOT_DIR / "data" / "datahptambahgenerasi.csv"

# Verified Live GSMArena Model Codes for Scraped Models
VERIFIED_GSMARENA_MODELS = {
    # Apple
    ("Apple", "iPhone 17e"): "A3634, A3575, A3635, iPhone18,5",
    ("Apple", "iPhone 18 Pro"): "A3714, A3472, A3713, A3715, iPhone19,2",
    ("Apple", "iPhone 18 Pro Max"): "A3717, A3473, A3716, A3718, iPhone19,3",
    ("Apple", "iPhone Duo"): "A3720, A3721, A3447, A3719, iPhone19,4",
    
    # Asus
    ("Asus", "ROG Phone 9"): "AI2501-12G256G-BK, AI2501-12G256G-WH, AI2501-16G512G-WH, AI2501-16G512G-BK",
    ("Asus", "ROG Phone 9 FE"): "AI2401",
    ("Asus", "ROG Phone 9 Pro"): "AI2501-16G512G-BK, AI2501-24G1T-BK",
    ("Asus", "Zenfone 12 Ultra"): "AI2501, AI2501H, I2501C, AI2501B",
    
    # Google
    ("Google", "Pixel 11"): "GUJ0N, GPQQ7",
    ("Google", "Pixel 11 Pro"): "GM45K, G7SWN",
    ("Google", "Pixel 11 Pro Fold"): "GZDQ6",
    ("Google", "Pixel 11 Pro XL"): "G4HCD, GBC0H",
    
    # Honor
    ("Honor", "Magic9"): "MLY-AN00",
    ("Honor", "Magic9 Pro Max"): "WKL-AN20",
    ("Honor", "Magic9 Super"): "MLM-AN00",
    
    # Huawei
    ("Huawei", "Mate 90"): "HLS-AL00",
    ("Huawei", "Mate 90 Pro"): "CMS-AL20",
    ("Huawei", "Mate 90 Pro Max"): "CMM-AL00, CMM-AL10",
    ("Huawei", "Mate 90 RS Ultimate"): "CMU-AL10",
    
    # Infinix
    ("Infinix", "GT 50 Pro"): "X6891",
    ("Infinix", "Hot 70"): "X6895B",
    ("Infinix", "Hot 70 Pro"): "X6896",
    ("Infinix", "Note 60 Ultra"): "X6877",
    ("Infinix", "Xpad 30 Pro"): "X1103",
    
    # Lenovo
    ("Lenovo", "Legion Y700 AI"): "TB324ZC",
    ("Lenovo", "Legion Y900 11"): "TB711FU",
    ("Lenovo", "Legion Y900 13"): "TB522FU",
    
    # Nokia
    ("Nokia", "123 Shield"): "TA-1748",
    
    # Nothing
    ("Nothing", "Phone (4a) Pro"): "A069P",
    ("Nothing", "Phone (4b)"): "A009P",
    
    # Oppo
    ("Oppo", "F35"): "CPH2931",
    ("Oppo", "Find X10 Pro Max"): "CPH2913, PMX110",
    ("Oppo", "K15s"): "PYE130",
    ("Oppo", "K15x"): "PLT150",
    
    # Samsung
    ("Samsung", "Galaxy A08 4G"): "SM-A085F, SM-A085F/DS",
    ("Samsung", "Galaxy A18 4G"): "SM-A185F, SM-A185F/DS, SM-A185M, SM-A185M/DS, SM-A185F/DSB",
    ("Samsung", "Galaxy F08"): "SM-E085F, SM-E085F/DS",
    ("Samsung", "Galaxy F70"): "SM-E176E, SM-E476B, SM-E476B/DS",
    ("Samsung", "Galaxy M08"): "SM-M085F, SM-M085F/DS",
    
    # Sharp
    ("Sharp", "Aquos wish5"): "SH-AC05, SH-M32, SH-54E",
    ("Sharp", "Aquos R11"): "SH-51G, SH-M35",
    
    # Sony
    ("Sony", "Xperia 1 VII"): "XQ-FS54, PDX256",
    ("Sony", "Xperia 1 VIII"): "XQ-GE54, XQ-GE74, XQ-GE44",
    ("Sony", "Xperia 10 VII"): "XQ-FE72, XQ-FE54",
    ("Sony", "Xperia 10 VIII"): "XQ-GH54, XQ-GE54",
    
    # Tecno
    ("Tecno", "Camon Air"): "CN6c",
    
    # Realme
    ("Realme", "16x"): "RMX5270",
    ("Realme", "C01"): "RMX5399",
    ("Realme", "P4s Lite"): "RMX5398",
    ("Realme", "P4s"): "RMX5397",
    ("Realme", "C100i (India)"): "RMX5399",
    
    # Vivo
    ("Vivo", "Y600i"): "V2617A",
    ("Vivo", "V80"): "V2648",
    
    # ZTE
    ("ZTE", "nubia NaviX Ultra"): "NX888J"
}

def apply_fixes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("[*] Mengoreksi Kode Model Pabrikan pada master_models...")
    updated_count = 0
    for (b_name, m_name), code in VERIFIED_GSMARENA_MODELS.items():
        cursor.execute("""
            UPDATE master_models
            SET factory_model_code = ?
            WHERE id IN (
                SELECT m.id FROM master_models m JOIN master_brands b ON m.brand_id = b.id
                WHERE LOWER(b.name) = LOWER(?) AND LOWER(m.name) = LOWER(?)
            )
        """, (code, b_name, m_name))
        if cursor.rowcount > 0:
            updated_count += cursor.rowcount
            print(f"[✓] {b_name} {m_name} -> {code}")
            
    conn.commit()
    print(f"\n[✓] Berhasil memperbarui {updated_count} model di database.")
    
    # Verifikasi langsung iPhone 17e
    cursor.execute("""
        SELECT b.name, m.name, m.factory_model_code, m.source_platform
        FROM master_models m JOIN master_brands b ON m.brand_id = b.id
        WHERE m.name LIKE '%17e%'
    """)
    check_17e = cursor.fetchall()
    print("Verifikasi iPhone 17e di DB:", check_17e)

    # Sinkronisasi ke data/datahptambahgenerasi.csv
    print(f"\n[*] Sinkronisasi ke {CSV_PATH}...")
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
            (
                SELECT 'Rp ' || printf('%,d', CAST(MIN(v.official_msrp_new) AS INT)) || ' - Rp ' || printf('%,d', CAST(MAX(v.official_msrp_new) AS INT))
                FROM master_variants v WHERE v.model_id = m.id
            ) AS "Kisaran Harga Baru Peluncuran",
            (
                SELECT GROUP_CONCAT(DISTINCT 
                    CASE 
                        WHEN v.storage_gb >= 1024 THEN (v.storage_gb / 1024) || 'TB'
                        ELSE v.storage_gb || 'GB'
                    END
                )
                FROM master_variants v WHERE v.model_id = m.id
            ) AS "Kapasitas Tersedia",
            m.chipset AS "Chipset / SoC",
            CASE 
                WHEN m.antutu_benchmark_score IS NOT NULL AND m.antutu_benchmark_score > 0 
                THEN printf('%,d', m.antutu_benchmark_score)
                ELSE '-'
            END AS "Antutu v10",
            m.display_type AS "Tipe Layar",
            printf('%.1f inch', m.screen_size_inch) AS "Ukuran Layar",
            m.refresh_rate_hz || ' Hz' AS "Refresh Rate",
            m.resolution AS Resolusi,
            m.main_camera_mp AS "Kamera Utama",
            m.selfie_camera_mp AS "Kamera Depan",
            m.battery_capacity_mah || ' mAh' AS Baterai,
            m.fast_charging_watt || 'W' AS "Fast Charging",
            CASE WHEN m.has_wireless_charging = 1 THEN m.wireless_charging_watt || 'W' ELSE 'Tidak' END AS "Wireless Charging",
            m.network_gen AS Jaringan,
            CASE WHEN m.has_nfc = 1 THEN 'Ya' ELSE 'Tidak' END AS NFC,
            m.ip_rating AS "Rating IP",
            m.weight_grams || 'g' AS Bobot,
            m.os_at_launch AS "OS Saat Rilis"
        FROM master_models m
        JOIN master_brands b ON m.brand_id = b.id
        ORDER BY b.name, m.release_year DESC, m.name;
    """)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    
    # Clean any None or 'None' strings
    for col in df.columns:
        df[col] = df[col].apply(lambda x: '-' if pd.isna(x) or str(x).strip().lower() in ['none', 'nan', ''] else str(x).strip())
        
    df.to_csv(CSV_PATH, index=False)
    print(f"[✓] File CSV tersinkronisasi: {len(df)} baris, {len(df.columns)} kolom.")
    print(f"NaN count di CSV: {df.isna().sum().sum()}")
    
    # Check row for iPhone 17e in CSV
    row_17e = df[df['Model'].str.contains('17e', case=False, na=False)]
    print("\niPhone 17e di CSV:")
    print(row_17e[['Brand', 'Model', 'Platform Sumber', 'Kode Model Pabrikan']])
    
    conn.close()

if __name__ == '__main__':
    apply_fixes()
