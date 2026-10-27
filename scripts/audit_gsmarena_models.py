import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from scrapers.gsmarena_sync import HEADERS, BASE_URL, GSMARENA_BRAND_SLUGS, parse_gsmarena_device_page

session = requests.Session()
session.headers.update(HEADERS)

conn = sqlite3.connect('smartphone_bekas.db')
c = conn.cursor()
c.execute('''
    SELECT m.id, b.name, m.name, m.factory_model_code
    FROM master_models m
    JOIN master_brands b ON m.brand_id = b.id
    WHERE m.source_platform = 'GSMArena'
    ORDER BY b.name, m.name
''')
db_models = c.fetchall()
conn.close()

# Brand -> list of (dev_title, href)
brand_devices = {}
unique_brands = sorted(list(set(b[1] for b in db_models)))

for b_name in unique_brands:
    slug = GSMARENA_BRAND_SLUGS.get(b_name)
    if not slug: continue
    url = f"{BASE_URL}/{slug}"
    try:
        resp = session.get(url, timeout=15)
        soup = BeautifulSoup(resp.text, 'html.parser')
        makers = soup.select('.makers li a')
        brand_devices[b_name] = []
        for a in makers:
            dev_title = a.get_text(strip=True)
            href = a['href']
            brand_devices[b_name].append((dev_title, href))
        time.sleep(0.5)
    except Exception as e:
        print(f"Error fetching {b_name}: {e}")

print("=== AUDIT GSMARENA MODEL CODES ===")
results = []
for m_id, b_name, m_name, curr_code in db_models:
    devices = brand_devices.get(b_name, [])
    # Find exact or best match
    best_href = None
    best_title = None
    # 1. Exact match
    for title, href in devices:
        t_clean = title
        if t_clean.lower().startswith(b_name.lower()):
            t_clean = t_clean[len(b_name):].strip()
        if t_clean.lower() == m_name.lower() or title.lower() == m_name.lower():
            best_href = href
            best_title = title
            break
    
    # 2. Substring match if not found
    if not best_href:
        for title, href in devices:
            if m_name.lower() in title.lower():
                best_href = href
                best_title = title
                break
                
    if best_href:
        dev_url = f"{BASE_URL}/{best_href}"
        parsed = parse_gsmarena_device_page(dev_url, session)
        web_models = parsed.get("factory_model_code") if parsed else None
        results.append({
            "id": m_id,
            "brand": b_name,
            "db_name": m_name,
            "web_title": best_title,
            "current_code": curr_code,
            "web_code": web_models,
            "url": dev_url
        })
        time.sleep(0.3)
    else:
        results.append({
            "id": m_id,
            "brand": b_name,
            "db_name": m_name,
            "web_title": "NOT FOUND ON PAGE 1",
            "current_code": curr_code,
            "web_code": None,
            "url": None
        })

print(f"Total audited: {len(results)}")
discrepancies = []
for r in results:
    match = (r["current_code"] == r["web_code"])
    status = "OK" if match else "MISMATCH / DIFF"
    if not match:
        discrepancies.append(r)
    print(f"[{status:15s}] {r['brand']:10s} | {r['db_name']:22s} | DB: {r['current_code']} | WEB: {r['web_code']}")

print(f"\nTotal Mismatches found: {len(discrepancies)} of {len(results)}")
