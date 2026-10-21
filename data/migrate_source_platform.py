import os
import sys
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "smartphone_bekas.db"

def migrate_database():
    print(f"Connecting to database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Check and add source_platform to master_models
    cursor.execute("PRAGMA table_info(master_models)")
    columns = [row[1] for row in cursor.fetchall()]
    if "source_platform" not in columns:
        print("Adding 'source_platform' column to 'master_models'...")
        cursor.execute("ALTER TABLE master_models ADD COLUMN source_platform VARCHAR(50) DEFAULT 'Official Indonesia'")
    else:
        print("'source_platform' column already exists in 'master_models'.")

    # 2. Check and add source_platform to master_variants
    cursor.execute("PRAGMA table_info(master_variants)")
    columns_var = [row[1] for row in cursor.fetchall()]
    if "source_platform" not in columns_var:
        print("Adding 'source_platform' column to 'master_variants'...")
        cursor.execute("ALTER TABLE master_variants ADD COLUMN source_platform VARCHAR(50) DEFAULT 'Official Indonesia'")
    else:
        print("'source_platform' column already exists in 'master_variants'.")

    # 3. Update existing nulls
    cursor.execute("UPDATE master_models SET source_platform = 'Official Indonesia' WHERE source_platform IS NULL")
    cursor.execute("UPDATE master_variants SET source_platform = 'Official Indonesia' WHERE source_platform IS NULL")
    conn.commit()

    # 4. Verify counts
    cursor.execute("SELECT count(*), source_platform FROM master_models GROUP BY source_platform")
    model_stats = cursor.fetchall()
    print("Master Models by Platform:", model_stats)

    cursor.execute("SELECT count(*), source_platform FROM master_variants GROUP BY source_platform")
    variant_stats = cursor.fetchall()
    print("Master Variants by Platform:", variant_stats)

    conn.close()
    print("Migration completed successfully!")

if __name__ == "__main__":
    migrate_database()
