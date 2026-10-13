"""
Generator Aset Visual Smartphone & Sinkronisasi Database PhonePrice ID.
Menghasilkan representasi visual SVG resolusi tinggi untuk seluruh 315 model smartphone di 16 brand
dan memperbarui kolom image_url pada tabel master_models dan master_variants.
"""
import os
import re
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "assets" / "phones"
DB_PATH = ROOT_DIR / "smartphone_bekas.db"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)

BRAND_PALETTES = {
    "Apple": {"primary": "#38bdf8", "accent": "#94a3b8", "badge": "#0ea5e9", "bg": "#0f172a"},
    "Samsung": {"primary": "#60a5fa", "accent": "#3b82f6", "badge": "#2563eb", "bg": "#0b1329"},
    "Xiaomi": {"primary": "#f97316", "accent": "#fb923c", "badge": "#ea580c", "bg": "#1c140e"},
    "Poco": {"primary": "#eab308", "accent": "#fde047", "badge": "#ca8a04", "bg": "#1c190a"},
    "Redmi": {"primary": "#ef4444", "accent": "#f87171", "badge": "#dc2626", "bg": "#1c0d0d"},
    "Oppo": {"primary": "#10b981", "accent": "#34d399", "badge": "#059669", "bg": "#091c16"},
    "Vivo": {"primary": "#06b6d4", "accent": "#22d3ee", "badge": "#0891b2", "bg": "#081a20"},
    "Realme": {"primary": "#facc15", "accent": "#fde047", "badge": "#d97706", "bg": "#1c1809"},
    "Infinix": {"primary": "#22c55e", "accent": "#4ade80", "badge": "#16a34a", "bg": "#0a1e12"},
    "Tecno": {"primary": "#38bdf8", "accent": "#818cf8", "badge": "#4f46e5", "bg": "#0f152b"},
    "Google Pixel": {"primary": "#4285f4", "accent": "#34a853", "badge": "#ea4335", "bg": "#0f1626"},
    "Asus": {"primary": "#ef4444", "accent": "#f43f5e", "badge": "#be123c", "bg": "#1e0b11"},
    "Sony": {"primary": "#a855f7", "accent": "#c084fc", "badge": "#9333ea", "bg": "#180d24"},
    "Huawei": {"primary": "#f43f5e", "accent": "#fb7185", "badge": "#e11d48", "bg": "#1f0d14"},
    "Nokia": {"primary": "#38bdf8", "accent": "#67e8f9", "badge": "#0284c7", "bg": "#0b1825"},
    "BlackBerry": {"primary": "#94a3b8", "accent": "#cbd5e1", "badge": "#64748b", "bg": "#14171f"},
    "iQOO": {"primary": "#eab308", "accent": "#f59e0b", "badge": "#d97706", "bg": "#1c160b"},
    "Nothing": {"primary": "#ffffff", "accent": "#e2e8f0", "badge": "#ef4444", "bg": "#111827"},
}

def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    return s.strip('_')

def generate_phone_svg(brand: str, model: str, year: int, chipset: str, display: str, camera: str) -> str:
    palette = BRAND_PALETTES.get(brand, {"primary": "#38bdf8", "accent": "#94a3b8", "badge": "#0ea5e9", "bg": "#0f172a"})
    is_bb = (brand == "BlackBerry")
    is_fold = "fold" in model.lower() or "flip" in model.lower()
    is_ultra = "ultra" in model.lower() or "pro max" in model.lower() or "rog" in model.lower()
    
    # Model shape parameters
    corner_radius = "8" if ("ultra" in model.lower() or "note" in model.lower()) else "26"
    notch_type = "dynamic_island" if ("iphone 1" in model.lower() and int(year) >= 2022) else "punch_hole"
    
    # BlackBerry QWERTY layout
    bb_keyboard = ""
    if is_bb:
        bb_keyboard = """
        <!-- Physical QWERTY Keyboard Mockup -->
        <g transform="translate(45, 235)">
            <rect x="0" y="0" width="150" height="90" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
            <!-- Key rows -->
            <rect x="10" y="8" width="130" height="15" rx="3" fill="#334155"/>
            <text x="75" y="19" font-family="'JetBrains Mono', monospace" font-size="8" fill="#94a3b8" text-anchor="middle">Q W E R T Y U I O P</text>
            <rect x="15" y="28" width="120" height="15" rx="3" fill="#334155"/>
            <text x="75" y="39" font-family="'JetBrains Mono', monospace" font-size="8" fill="#94a3b8" text-anchor="middle">A S D F G H J K L</text>
            <rect x="22" y="48" width="106" height="15" rx="3" fill="#334155"/>
            <text x="75" y="59" font-family="'JetBrains Mono', monospace" font-size="8" fill="#94a3b8" text-anchor="middle">Z X C V B N M ↵</text>
            <rect x="35" y="68" width="80" height="14" rx="3" fill="#475569"/>
            <text x="75" y="78" font-family="'JetBrains Mono', monospace" font-size="7" fill="#cbd5e1" text-anchor="middle">SPACE</text>
        </g>
        """

    # Top Notch / Camera Cutout
    notch_svg = ""
    if is_bb:
        notch_svg = """<circle cx="120" cy="48" r="3.5" fill="#0f172a" stroke="#334155" stroke-width="1"/>"""
    elif notch_type == "dynamic_island":
        notch_svg = """<rect x="104" y="42" width="32" height="10" rx="5" fill="#020617"/>"""
    else:
        # Centered punch hole
        notch_svg = """<circle cx="120" cy="46" r="3.5" fill="#020617" stroke="#1e293b" stroke-width="1"/>"""

    # Screen height adjusts if physical keyboard exists
    screen_height = "170" if is_bb else "280"

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 400" width="100%" height="100%">
    <defs>
        <linearGradient id="bodyGrad_{slugify(model)}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1e293b"/>
            <stop offset="50%" stop-color="#0f172a"/>
            <stop offset="100%" stop-color="{palette['bg']}"/>
        </linearGradient>
        <linearGradient id="screenGrad_{slugify(model)}" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#090d16"/>
            <stop offset="100%" stop-color="#111827"/>
        </linearGradient>
        <linearGradient id="accentGrad_{slugify(model)}" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{palette['primary']}"/>
            <stop offset="100%" stop-color="{palette['accent']}"/>
        </linearGradient>
        <filter id="shadow_{slugify(model)}" x="-10%" y="-10%" width="125%" height="125%">
            <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000000" flood-opacity="0.45"/>
        </filter>
    </defs>

    <!-- Outer Studio Background -->
    <rect width="320" height="400" rx="14" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

    <!-- Device Frame Shadow & Body -->
    <g filter="url(#shadow_{slugify(model)})">
        <!-- Outer Chassis / Frame -->
        <rect x="35" y="24" width="170" height="348" rx="{corner_radius}" 
              fill="url(#bodyGrad_{slugify(model)})" stroke="#334155" stroke-width="2.5"/>
        <!-- Inner Bezel -->
        <rect x="40" y="29" width="160" height="338" rx="{max(4, int(corner_radius)-3)}" 
              fill="#020617" stroke="#1e293b" stroke-width="1.5"/>
        <!-- Active Screen Glass -->
        <rect x="43" y="32" width="154" height="{screen_height}" rx="{max(2, int(corner_radius)-5)}" 
              fill="url(#screenGrad_{slugify(model)})"/>
    </g>

    <!-- Notch / Island / Speaker Earpiece -->
    {notch_svg}
    <line x1="110" y1="27" x2="130" y2="27" stroke="#475569" stroke-width="1.5" stroke-linecap="round"/>

    <!-- Screen Content: Minimalist Lockscreen / UI -->
    <g transform="translate(43, 62)">
        <!-- Brand & Model Name on Screen -->
        <text x="77" y="38" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" 
              fill="{palette['primary']}" text-anchor="middle" letter-spacing="1.5">{brand.upper()}</text>
        <text x="77" y="58" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800" 
              fill="#f8fafc" text-anchor="middle">{model[:20]}</text>
        <text x="77" y="74" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" 
              fill="#94a3b8" text-anchor="middle">{year}</text>

        <!-- Dynamic Visual Pulse Wave -->
        <path d="M 22 105 Q 45 85 77 105 T 132 105" fill="none" stroke="url(#accentGrad_{slugify(model)})" stroke-width="2.5" opacity="0.85"/>
        <circle cx="77" cy="105" r="3.5" fill="{palette['primary']}"/>

        <!-- Hardware Spec Badge -->
        <rect x="18" y="125" width="118" height="20" rx="10" fill="rgba(30, 41, 59, 0.8)" stroke="#334155" stroke-width="1"/>
        <text x="77" y="139" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="700" 
              fill="#cbd5e1" text-anchor="middle">{chipset[:18] if chipset else 'Octa-Core'}</text>
    </g>

    {bb_keyboard}

    <!-- Side Button Renders -->
    <rect x="32" y="90" width="3" height="24" rx="1.5" fill="#475569"/>
    <rect x="32" y="124" width="3" height="38" rx="1.5" fill="#475569"/>
    <rect x="205" y="105" width="3" height="48" rx="1.5" fill="#475569"/>

    <!-- Right-Hand Side Info Cards -->
    <g transform="translate(216, 26)">
        <!-- Brand Badge -->
        <rect x="0" y="0" width="92" height="26" rx="6" fill="{palette['bg']}" stroke="{palette['primary']}" stroke-width="1.2"/>
        <text x="46" y="17" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="800" 
              fill="{palette['primary']}" text-anchor="middle">{brand}</text>

        <!-- Spec Pill 1: Camera -->
        <g transform="translate(0, 36)">
            <rect x="0" y="0" width="92" height="54" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="8" y="15" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="700" fill="#94a3b8" letter-spacing="0.5">CAMERA</text>
            <text x="8" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="800" fill="#f8fafc">{(camera or '48 MP')[:12]}</text>
            <text x="8" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="600" fill="#38bdf8">OIS Optical</text>
        </g>

        <!-- Spec Pill 2: Screen -->
        <g transform="translate(0, 98)">
            <rect x="0" y="0" width="92" height="54" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="8" y="15" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="700" fill="#94a3b8" letter-spacing="0.5">DISPLAY</text>
            <text x="8" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="800" fill="#f8fafc">{(display or 'OLED')[:12]}</text>
            <text x="8" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="600" fill="#10b981">120Hz Fast</text>
        </g>

        <!-- Spec Pill 3: Authentic Status -->
        <g transform="translate(0, 160)">
            <rect x="0" y="0" width="92" height="42" rx="6" fill="rgba(16, 185, 129, 0.12)" stroke="rgba(16, 185, 129, 0.35)" stroke-width="1"/>
            <circle cx="12" cy="16" r="3.5" fill="#10b981"/>
            <text x="20" y="19" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="700" fill="#34d399">VERIFIED</text>
            <text x="8" y="33" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="700" fill="#cbd5e1">SEIN/iBox/ID</text>
        </g>

        <!-- Catalog Seal -->
        <g transform="translate(0, 212)">
            <rect x="0" y="0" width="92" height="134" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
            <text x="46" y="24" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="700" fill="#64748b" text-anchor="middle">CATALOG ID</text>
            <text x="46" y="46" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800" fill="{palette['primary']}" text-anchor="middle">#{year}</text>
            <line x1="12" y1="58" x2="80" y2="58" stroke="#334155" stroke-width="1"/>
            <text x="46" y="76" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="600" fill="#94a3b8" text-anchor="middle">PhonePrice ID</text>
            <text x="46" y="92" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="600" fill="#64748b" text-anchor="middle">Master Spec</text>
            <rect x="14" y="104" width="64" height="18" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="46" y="116" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="700" fill="#38bdf8" text-anchor="middle">OFFICIAL</text>
        </g>
    </g>
</svg>"""
    return svg_content

def populate_images():
    print(f"[INFO] Connecting to SQLite at: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT m.id, b.name as brand_name, m.name as model_name, m.release_year, 
               m.chipset, m.display_type, m.main_camera_mp
        FROM master_models m
        JOIN master_brands b ON m.brand_id = b.id
    """)
    models = cursor.fetchall()
    print(f"[INFO] Fetched {len(models)} models from database.")

    updated_count = 0
    for mid, brand, model_name, year, chipset, display, camera in models:
        slug = f"{slugify(brand)}_{slugify(model_name)}"
        filename = f"{slug}.svg"
        file_path = ASSETS_DIR / filename
        rel_path = f"assets/phones/{filename}"

        svg_code = generate_phone_svg(
            brand=brand,
            model=model_name,
            year=year or 2024,
            chipset=chipset or "SoC Architecture",
            display=display or "AMOLED Display",
            camera=camera or "Main Camera"
        )
        file_path.write_text(svg_code, encoding="utf-8")

        # Update master_models
        cursor.execute("UPDATE master_models SET image_url = ? WHERE id = ?", (rel_path, mid))

        # Update all variants of this model
        cursor.execute("UPDATE master_variants SET image_url = ? WHERE model_id = ?", (rel_path, mid))
        updated_count += 1

    conn.commit()

    # Verify counts
    cursor.execute("SELECT COUNT(*), COUNT(image_url) FROM master_models WHERE image_url IS NOT NULL")
    models_with_img = cursor.fetchone()
    cursor.execute("SELECT COUNT(*), COUNT(image_url) FROM master_variants WHERE image_url IS NOT NULL")
    variants_with_img = cursor.fetchone()
    conn.close()

    print(f"[SUCCESS] Generated {len(models)} SVG assets in: {ASSETS_DIR}")
    print(f"[SUCCESS] master_models with image_url: {models_with_img}")
    print(f"[SUCCESS] master_variants with image_url: {variants_with_img}")

if __name__ == "__main__":
    populate_images()
