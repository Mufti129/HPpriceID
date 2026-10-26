"""
Skrip Migrasi dan Backfill Kolom Generasi Smartphone ke SQLite Database.
Menambahkan kolom:
- generation (Generasi Riil / Hardware Lineage)
- commercial_generation (Generasi Komersial / Marketing Branding)
- lineage_generation (Keterangan Silsilah Historis Penetapan Generasi)
Sesuai Panduan & Aturan Penetapan Generasi Smartphone (datahptambahgenerasi.csv).
"""

import sys
import sqlite3
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "smartphone_bekas.db"
CSV_PATH = ROOT_DIR / "data" / "datahptambahgenerasi.csv"

def run_migration():
    print(f"[*] Menghubungkan ke database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Periksa kolom yang sudah ada di tabel master_models
    cursor.execute("PRAGMA table_info(master_models);")
    existing_cols = [row[1] for row in cursor.fetchall()]

    # 2. Tambahkan kolom jika belum ada
    new_cols = [
        ("generation", "VARCHAR(50)"),
        ("commercial_generation", "VARCHAR(50)"),
        ("lineage_generation", "TEXT")
    ]

    for col_name, col_type in new_cols:
        if col_name not in existing_cols:
            print(f"[*] Menambahkan kolom '{col_name}' ({col_type}) ke tabel master_models...")
            cursor.execute(f"ALTER TABLE master_models ADD COLUMN {col_name} {col_type};")
        else:
            print(f"[i] Kolom '{col_name}' sudah ada di tabel master_models.")

    conn.commit()

    # 3. Baca datahptambahgenerasi.csv dan lakukan backfill
    if not CSV_PATH.exists():
        print(f"[!] Error: Berkas CSV tidak ditemukan di {CSV_PATH}")
        conn.close()
        return

    print(f"[*] Membaca data generasi dari: {CSV_PATH}")
    df = pd.read_csv(CSV_PATH)
    print(f"[*] Total baris data generasi pada CSV: {len(df)}")

    # Ambil pemetaan brand_id dan brand name
    cursor.execute("SELECT id, name FROM master_brands;")
    brand_map = {name.lower().strip(): b_id for b_id, name in cursor.fetchall()}

    updated_count = 0
    not_found = []

    for idx, row in df.iterrows():
        b_name = str(row["Brand"]).strip()
        m_name = str(row["Model"]).strip()
        gen_riil = str(row["Generasi"]).strip() if pd.notna(row["Generasi"]) else None
        gen_kom = str(row["Generasi Komersial"]).strip() if pd.notna(row["Generasi Komersial"]) else None
        ket_silsilah = str(row["Keterangan Silsilah"]).strip() if pd.notna(row["Keterangan Silsilah"]) else None

        b_id = brand_map.get(b_name.lower())
        if not b_id:
            not_found.append((b_name, m_name))
            continue

        cursor.execute("""
            UPDATE master_models
            SET generation = ?, commercial_generation = ?, lineage_generation = ?
            WHERE brand_id = ? AND LOWER(name) = LOWER(?);
        """, (gen_riil, gen_kom, ket_silsilah, b_id, m_name))

        if cursor.rowcount > 0:
            updated_count += cursor.rowcount
        else:
            not_found.append((b_name, m_name))

    conn.commit()

    # 4. Verifikasi hasil
    cursor.execute("""
        SELECT COUNT(*),
               COUNT(generation),
               COUNT(commercial_generation),
               COUNT(lineage_generation)
        FROM master_models;
    """)
    total_m, count_gen, count_com, count_lin = cursor.fetchone()

    print("\n" + "=" * 65)
    print("HASIL MIGRASI & BACKFILL GENERASI SMARTPHONE:")
    print(f"Total Model di DB           : {total_m}")
    print(f"Model Terupdate dari CSV    : {updated_count}")
    print(f"Model dengan Generasi Riil  : {count_gen} / {total_m}")
    print(f"Model dengan Gen Komersial  : {count_com} / {total_m}")
    print(f"Model dengan Ket. Silsilah  : {count_lin} / {total_m}")
    if not_found:
        print(f"[!] Perhatian: {len(not_found)} model tidak ditemukan di DB: {not_found[:5]}")
    else:
        print("[✓] 100% Model di Master Database berhasil diperbarui dengan data generasi!")
    print("=" * 65)

    conn.close()

if __name__ == "__main__":
    run_migration()
