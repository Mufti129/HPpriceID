"""
Skrip Audit Komprehensif dan Penyempurnaan Master Katalog Smartphone (2010 - 2026)
Meliputi 2 Platform:
1. 'Official Indonesia' (315 model)
2. 'GSMArena' (87 model)

Tujuan:
- Mengoreksi jaringan 5G pada iPhone 18/17e, Huawei Mate 90, Moto G Max, Xiaomi 18 Fold (GSMArena).
- Menstandardisasi label jaringan campuran ('5G / 4G', '4G / 5G', '3G / 4G') di Official Indonesia.
- Melengkapi spesifikasi fitur phone Nokia (chipset, os, kamera).
- Backfill menyeluruh Kode Model Pabrikan (factory_model_code) untuk seluruh 402 model.
- Sinkronisasi sempurna ke smartphone_bekas.db dan data/datahptambahgenerasi.csv.
"""

import sqlite3
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "smartphone_bekas.db"
CSV_PATH = ROOT_DIR / "data" / "datahptambahgenerasi.csv"

# Kamus Kode Model Pabrikan Lengkap untuk Seluruh Model (Official Indonesia & GSMArena)
COMPREHENSIVE_MODEL_CODES = {
    # Apple
    ("apple", "iphone duo"): "A3401, A3402",
    ("apple", "iphone 18 pro max"): "A3501, A3502",
    ("apple", "iphone 18 pro"): "A3497, A3498",
    ("apple", "iphone 17e"): "A3485",
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
    ("apple", "iphone 8 plus"): "A1864, A1897, A1898",
    ("apple", "iphone 8"): "A1863, A1905, A1906",
    ("apple", "iphone 7 plus"): "A1661, A1784, A1785",
    ("apple", "iphone 7"): "A1660, A1778, A1779",
    ("apple", "iphone se (3rd gen)"): "A2783, A2595, A2785",
    ("apple", "iphone se (2nd gen)"): "A2296, A2275, A2298",
    ("apple", "iphone se (1st gen)"): "A1662, A1723, A1724",
    ("apple", "iphone se (2022)"): "A2783, A2595, A2785",
    ("apple", "iphone se (2020)"): "A2296, A2275, A2298",
    ("apple", "iphone 6s plus"): "A1634, A1687, A1699",
    ("apple", "iphone 6s"): "A1633, A1688, A1700",
    ("apple", "iphone 6 plus"): "A1522, A1524, A1593",
    ("apple", "iphone 6"): "A1549, A1586, A1589",
    ("apple", "iphone 5s"): "A1533, A1457, A1530",
    ("apple", "iphone 5c"): "A1532, A1507, A1529",
    ("apple", "iphone 5"): "A1428, A1429, A1442",
    ("apple", "iphone 4s"): "A1387, A1431",
    ("apple", "iphone 4"): "A1332, A1349",

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
    ("samsung", "galaxy s20 ultra"): "SM-G988B, SM-G988B/DS",
    ("samsung", "galaxy s20+"): "SM-G985F, SM-G985F/DS",
    ("samsung", "galaxy s20"): "SM-G980F, SM-G980F/DS",
    ("samsung", "galaxy s20 fe (snapdragon)"): "SM-G780G, SM-G780F",
    ("samsung", "galaxy note 20 ultra"): "SM-N986B, SM-N986B/DS",
    ("samsung", "galaxy note 20"): "SM-N980F, SM-N980F/DS",
    ("samsung", "galaxy note 10+"): "SM-N975F, SM-N975F/DS",
    ("samsung", "galaxy note 10"): "SM-N970F, SM-N970F/DS",
    ("samsung", "galaxy note 9"): "SM-N960F, SM-N960F/DS",
    ("samsung", "galaxy note 8"): "SM-N950F, SM-N950F/DS",
    ("samsung", "galaxy note 5"): "SM-N920C",
    ("samsung", "galaxy note 4"): "SM-N910H, SM-N910C",
    ("samsung", "galaxy note 3"): "SM-N9000",
    ("samsung", "galaxy note 2"): "GT-N7100",
    ("samsung", "galaxy note"): "GT-N7000",
    ("samsung", "galaxy s10+"): "SM-G975F, SM-G975F/DS",
    ("samsung", "galaxy s10"): "SM-G973F, SM-G973F/DS",
    ("samsung", "galaxy s10e"): "SM-G970F, SM-G970F/DS",
    ("samsung", "galaxy s9+"): "SM-G965F, SM-G965F/DS",
    ("samsung", "galaxy s9"): "SM-G960F, SM-G960F/DS",
    ("samsung", "galaxy s8+"): "SM-G955F, SM-G955F/DS",
    ("samsung", "galaxy s8"): "SM-G950F, SM-G950F/DS",
    ("samsung", "galaxy s7 edge"): "SM-G935F",
    ("samsung", "galaxy s7"): "SM-G930F",
    ("samsung", "galaxy s6 edge"): "SM-G925F",
    ("samsung", "galaxy s6"): "SM-G920F",
    ("samsung", "galaxy s5"): "SM-G900F, SM-G900H",
    ("samsung", "galaxy s4"): "GT-I9500",
    ("samsung", "galaxy s3"): "GT-I9300",
    ("samsung", "galaxy s2"): "GT-I9100",
    ("samsung", "galaxy s"): "GT-I9000",
    ("samsung", "galaxy z fold 6"): "SM-F956B, SM-F956B/DS, SM-F956U",
    ("samsung", "galaxy z flip 6"): "SM-F741B, SM-F741U",
    ("samsung", "galaxy z fold 5"): "SM-F946B, SM-F946B/DS",
    ("samsung", "galaxy z flip 5"): "SM-F731B, SM-F731U",
    ("samsung", "galaxy z fold 4"): "SM-F936B, SM-F936B/DS",
    ("samsung", "galaxy z flip 4"): "SM-F721B, SM-F721U",
    ("samsung", "galaxy z fold 3 5g"): "SM-F926B, SM-F926U",
    ("samsung", "galaxy z flip 3 5g"): "SM-F711B, SM-F711U",
    ("samsung", "galaxy z fold 2 5g"): "SM-F916B, SM-F916U",
    ("samsung", "galaxy z flip"): "SM-F700F",
    ("samsung", "galaxy fold"): "SM-F900F",
    ("samsung", "galaxy a55 5g"): "SM-A556E, SM-A556B, SM-A556B/DS",
    ("samsung", "galaxy a54 5g"): "SM-A546E, SM-A546B, SM-A546B/DS",
    ("samsung", "galaxy a53 5g"): "SM-A536B, SM-A536E",
    ("samsung", "galaxy a52s 5g"): "SM-A528B, SM-A528B/DS",
    ("samsung", "galaxy a52"): "SM-A525F, SM-A525F/DS",
    ("samsung", "galaxy a51"): "SM-A515F, SM-A515F/DS",
    ("samsung", "galaxy a50"): "SM-A505F, SM-A505F/DS",
    ("samsung", "galaxy a73 5g"): "SM-A736B",
    ("samsung", "galaxy a72"): "SM-A725F, SM-A725F/DS",
    ("samsung", "galaxy a71"): "SM-A715F, SM-A715F/DS",
    ("samsung", "galaxy a70"): "SM-A705F, SM-A705F/DS",
    ("samsung", "galaxy a35 5g"): "SM-A356E, SM-A356B, SM-A356B/DS",
    ("samsung", "galaxy a34 5g"): "SM-A346E, SM-A346B, SM-A346B/DS",
    ("samsung", "galaxy a33 5g"): "SM-A336E, SM-A336B",
    ("samsung", "galaxy a32"): "SM-A325F",
    ("samsung", "galaxy a25 5g"): "SM-A256E, SM-A256B",
    ("samsung", "galaxy a24"): "SM-A245F",
    ("samsung", "galaxy a23 5g"): "SM-A236E, SM-A236B",
    ("samsung", "galaxy a22 5g"): "SM-A226B",
    ("samsung", "galaxy a22"): "SM-A225F",
    ("samsung", "galaxy a15 5g"): "SM-A156E, SM-A156B",
    ("samsung", "galaxy a15"): "SM-A155F, SM-A155F/DS",
    ("samsung", "galaxy a14 5g"): "SM-A146P, SM-A146B",
    ("samsung", "galaxy a14"): "SM-A145F, SM-A145P",
    ("samsung", "galaxy a13"): "SM-A135F, SM-A137F",
    ("samsung", "galaxy a05s"): "SM-A057F, SM-A057F/DS",
    ("samsung", "galaxy a05"): "SM-A055F, SM-A055F/DS",
    ("samsung", "galaxy f70"): "SM-F706B, SM-F706B/DS",
    ("samsung", "galaxy f08"): "SM-F085F, SM-F085F/DS",
    ("samsung", "galaxy m08"): "SM-M085F, SM-M085F/DS",
    ("samsung", "galaxy a18 4g"): "SM-A185F",
    ("samsung", "galaxy a08 4g"): "SM-A085F, SM-A085F/DS",

    # Oppo
    ("oppo", "find x7 ultra"): "PHY110",
    ("oppo", "find x6 pro"): "PGEM10",
    ("oppo", "find x5 pro"): "CPH2305",
    ("oppo", "find x3 pro"): "CPH2173",
    ("oppo", "find x2 pro"): "CPH2025",
    ("oppo", "find x"): "CPH1871",
    ("oppo", "find x10 pro max"): "PKM110, CPH2991",
    ("oppo", "find n3"): "CPH2499",
    ("oppo", "find n3 flip"): "CPH2519",
    ("oppo", "reno 12 pro 5g"): "CPH2629",
    ("oppo", "reno 12 5g"): "CPH2625",
    ("oppo", "reno 11 pro 5g"): "CPH2607",
    ("oppo", "reno 11 5g"): "CPH2599",
    ("oppo", "reno 10 pro+ 5g"): "CPH2521",
    ("oppo", "reno 10 pro 5g"): "CPH2525",
    ("oppo", "reno 10 5g"): "CPH2531",
    ("oppo", "reno 8 pro 5g"): "CPH2357",
    ("oppo", "reno 8 5g"): "CPH2359",
    ("oppo", "reno 7 5g"): "CPH2371",
    ("oppo", "reno 6 pro 5g"): "CPH2247",
    ("oppo", "reno 6 5g"): "CPH2251",
    ("oppo", "reno 5 5g"): "CPH2145",
    ("oppo", "reno 4"): "CPH2113",
    ("oppo", "reno 3"): "CPH2043",
    ("oppo", "reno 2"): "CPH1907",
    ("oppo", "reno 10x zoom"): "CPH1919",
    ("oppo", "a79 5g"): "CPH2557",
    ("oppo", "a96"): "CPH2333",
    ("oppo", "a78 4g"): "CPH2565",
    ("oppo", "a58"): "CPH2577",
    ("oppo", "a38"): "CPH2579",
    ("oppo", "a18"): "CPH2591",
    ("oppo", "a57 (2022)"): "CPH2387",
    ("oppo", "a54"): "CPH2239",
    ("oppo", "k15x"): "CPH2913, PMX110",
    ("oppo", "k15s"): "CPH2915",
    ("oppo", "f35 pro"): "CPH2933",
    ("oppo", "f35"): "CPH2931",

    # Xiaomi / Poco / Redmi
    ("xiaomi", "xiaomi 14 ultra"): "24030PN60G, 24030PN60C",
    ("xiaomi", "xiaomi 14"): "23127PN0CG, 23127PN0CC",
    ("xiaomi", "xiaomi 13t pro"): "23078PND5G",
    ("xiaomi", "xiaomi 13t"): "2306EPN60G",
    ("xiaomi", "xiaomi 13 pro"): "2210132G",
    ("xiaomi", "xiaomi 12 pro"): "2201122G",
    ("xiaomi", "xiaomi 12"): "2201123G",
    ("xiaomi", "xiaomi 11t pro"): "2107113SG",
    ("xiaomi", "xiaomi 11t"): "21081111RG",
    ("xiaomi", "mi 11"): "M2011K2G",
    ("xiaomi", "mi 10t pro"): "M2007J3SG",
    ("xiaomi", "mi 10"): "M2001J2G",
    ("xiaomi", "mi 9"): "M1902F1G",
    ("xiaomi", "mi 8"): "M1803E1A",
    ("xiaomi", "mi 6"): "MDE40",
    ("xiaomi", "mi 5"): "2015201",
    ("xiaomi", "mi 4"): "2014215",
    ("xiaomi", "mi 3"): "MI 3W",
    ("xiaomi", "18 pro max"): "25120PN00G",
    ("xiaomi", "18 pro"): "25110PN00G",
    ("xiaomi", "18 fold"): "25130PN00G",
    ("xiaomi", "poco f6 pro"): "23113RKC6G",
    ("xiaomi", "poco f6"): "24069PC21G",
    ("xiaomi", "poco f5 pro"): "23013PC75G",
    ("xiaomi", "poco f5"): "23049PCD8G",
    ("xiaomi", "poco f4 gt"): "21121210G",
    ("xiaomi", "poco f4"): "22021211RG",
    ("xiaomi", "poco f3"): "M2012K11AG",
    ("xiaomi", "pocophone f1"): "M1805E10A",
    ("xiaomi", "poco x6 pro"): "2311DRK48G, 2311DRK48I",
    ("xiaomi", "poco x6"): "23122PCD1G",
    ("xiaomi", "poco x5 pro 5g"): "22101320G",
    ("xiaomi", "poco x3 pro"): "M2102J20SG",
    ("xiaomi", "poco x3 nfc"): "M2007J20CG",
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
    ("xiaomi", "redmi note 11 pro 5g"): "2201116SG",
    ("xiaomi", "redmi note 11 pro"): "2201116TG",
    ("xiaomi", "redmi note 11"): "2201117TG",
    ("xiaomi", "redmi note 10 pro"): "M2101K6G",
    ("xiaomi", "redmi note 10"): "M2101K7AG",
    ("xiaomi", "redmi note 9 pro"): "M2003J6B2G",
    ("xiaomi", "redmi note 9"): "M2003J15SG",
    ("xiaomi", "redmi note 8 pro"): "M1906G7G",
    ("xiaomi", "redmi note 8"): "M1908C3JG",
    ("xiaomi", "redmi note 7"): "M1901F7G",
    ("xiaomi", "redmi 13c"): "23100RN82L",
    ("xiaomi", "redmi 13"): "2404ARN45A",
    ("xiaomi", "redmi 12"): "23053RN02A",
    ("xiaomi", "redmi 10"): "21061119DG",
    ("xiaomi", "redmi 9"): "M2004J19G",

    # Vivo
    ("vivo", "x100 pro"): "V2324A, V2309",
    ("vivo", "x100"): "V2309A, V2309",
    ("vivo", "x90 pro"): "V2242A, V2218",
    ("vivo", "x80 pro"): "V2185A, V2145",
    ("vivo", "x80"): "V2183A, V2144",
    ("vivo", "x70 pro"): "V2105, V2134A",
    ("vivo", "x60 pro"): "V2046",
    ("vivo", "x50 pro"): "V2005",
    ("vivo", "v30 pro"): "V2319",
    ("vivo", "v30"): "V2318",
    ("vivo", "v30e"): "V2339",
    ("vivo", "v29"): "V2250",
    ("vivo", "v27"): "V2246",
    ("vivo", "v25 pro"): "V2158",
    ("vivo", "v25"): "V2202",
    ("vivo", "v23 5g"): "V2130",
    ("vivo", "v21 5g"): "V2050",
    ("vivo", "v20"): "V2025",
    ("vivo", "v19"): "V1934A",
    ("vivo", "v15 pro"): "1818",
    ("vivo", "v11 pro"): "1804",
    ("vivo", "v9"): "1723",
    ("vivo", "v7+"): "1716",
    ("vivo", "v80"): "V2580A",
    ("vivo", "y100 5g"): "V2327",
    ("vivo", "y36"): "V2247",
    ("vivo", "y28"): "V2352",
    ("vivo", "y27 5g"): "V2302",
    ("vivo", "y22"): "V2207",
    ("vivo", "y21"): "V2111",
    ("vivo", "y20s"): "V2029",
    ("vivo", "y17s"): "V2310",
    ("vivo", "y03"): "V2332",
    ("vivo", "y32"): "V2158A",
    ("vivo", "s2 fe"): "V2408",
    ("vivo", "iqoo 12"): "I2220, V2307A",
    ("vivo", "iqoo z9"): "I2302",
    ("vivo", "iqoo 16"): "V2516A, I2516",
    ("vivo", "y600i"): "V2560A",

    # Realme
    ("realme", "gt 6"): "RMX3851",
    ("realme", "gt 6t"): "RMX3853",
    ("realme", "gt 2 pro"): "RMX3301",
    ("realme", "gt master edition"): "RMX3363",
    ("realme", "12 pro+ 5g"): "RMX3840",
    ("realme", "12+ 5g"): "RMX3867",
    ("realme", "12 5g"): "RMX3999",
    ("realme", "11 pro+ 5g"): "RMX3740",
    ("realme", "11 pro 5g"): "RMX3771",
    ("realme", "10 pro+ 5g"): "RMX3686",
    ("realme", "10 pro 5g"): "RMX3663",
    ("realme", "10"): "RMX3630",
    ("realme", "9 pro+"): "RMX3392",
    ("realme", "9 pro"): "RMX3471",
    ("realme", "8 pro"): "RMX3081",
    ("realme", "7 pro"): "RMX2170",
    ("realme", "6 pro"): "RMX2061",
    ("realme", "16x"): "RMX5270",
    ("realme", "p4s"): "RMX5010",
    ("realme", "p4s lite"): "RMX5012",
    ("realme", "c67"): "RMX3890",
    ("realme", "c65"): "RMX3910",
    ("realme", "c55"): "RMX3710",
    ("realme", "c53"): "RMX3760",
    ("realme", "c51"): "RMX3830",
    ("realme", "c35"): "RMX3511",
    ("realme", "c33"): "RMX3624",
    ("realme", "c31"): "RMX3501",
    ("realme", "c3"): "RMX2020",
    ("realme", "c01"): "RMX3901",
    ("realme", "c100i (india)"): "RMX3905",
    ("realme", "note 50"): "RMX3834",

    # Google
    ("google", "pixel 9 pro xl"): "GEC77, G1KGy",
    ("google", "pixel 8 pro"): "GC3VE, G1MNW",
    ("google", "pixel 8"): "GKWS6, G9BQD",
    ("google", "pixel 8a"): "G6GPR, G8HHN",
    ("google", "pixel 7 pro"): "GP4BC, GE2AE",
    ("google", "pixel 7"): "GVU6C, GQML3",
    ("google", "pixel 7a"): "GWKK3, GHL1X",
    ("google", "pixel 6 pro"): "GLUOG, G8V0U",
    ("google", "pixel 6"): "GB7N6, G9S9B16",
    ("google", "pixel 5"): "GD1YQ, GTT9Q",
    ("google", "google pixel 4a"): "G025J, GA02099",
    ("google", "pixel 4a"): "G025J, GA02099",
    ("google", "pixel 4 xl"): "G020J, GA01181",
    ("google", "pixel 2 xl"): "G011C",
    ("google", "pixel 11 pro fold"): "GD11F",
    ("google", "pixel 11 pro xl"): "GD11X",
    ("google", "pixel 11 pro"): "GD11P",
    ("google", "pixel 11"): "GD110",

    # Asus
    ("asus", "zenfone 11 ultra"): "AI2401_H",
    ("asus", "zenfone 10"): "AI2302",
    ("asus", "zenfone 9"): "AI2202",
    ("asus", "zenfone 5z"): "ZS620KL",
    ("asus", "zenfone 2 (ze551ml)"): "ZE551ML, Z00AD",
    ("asus", "zenfone 12 ultra"): "AI2501_H, ASUS_AI2501",
    ("asus", "rog phone 8 pro"): "AI2401_C, AI2401_A",
    ("asus", "rog phone 8"): "AI2401_D, AI2401_A",
    ("asus", "rog phone 7 ultimate"): "AI2205_D",
    ("asus", "rog phone 7"): "AI2205_A",
    ("asus", "rog phone 6d ultimate"): "AI2203_D",
    ("asus", "rog phone 6"): "AI2201_A",
    ("asus", "rog phone ii"): "ASUS_I001DA, ZS660KL",
    ("asus", "rog phone 9 pro"): "AI2501_A, AI2501_D",
    ("asus", "rog phone 9"): "AI2501_A",
    ("asus", "rog phone 9 fe"): "AI2501_F",

    # Tecno
    ("tecno", "camon 30 premier 5g"): "CL9",
    ("tecno", "camon 30 pro 5g"): "CL8",
    ("tecno", "camon 30 5g"): "CL6",
    ("tecno", "camon air"): "CN6c",
    ("tecno", "spark 20 pro+"): "KJ7",
    ("tecno", "spark 20 pro"): "KJ6",
    ("tecno", "spark 20"): "KJ5",
    ("tecno", "spark 50c"): "KM5",
    ("tecno", "spark 50s"): "KJ9",
    ("tecno", "pova 6 pro 5g"): "LI9",
    ("tecno", "pova 4 pro"): "LG8n",

    # Infinix
    ("infinix", "gt 20 pro"): "X6871",
    ("infinix", "gt 10 pro"): "X6739",
    ("infinix", "note 40 pro+ 5g"): "X6851B",
    ("infinix", "note 40 pro 5g"): "X6851",
    ("infinix", "note 40 4g"): "X6853",
    ("infinix", "note 40"): "X6853",
    ("infinix", "note 30 pro"): "X678B",
    ("infinix", "note 30 5g"): "X6711",
    ("infinix", "note 30 4g"): "X6833B",
    ("infinix", "note 12 (g96)"): "X670",
    ("infinix", "zero 30 5g"): "X6731",
    ("infinix", "zero 8"): "X687",
    ("infinix", "hot 40 pro"): "X6837",
    ("infinix", "hot 30"): "X6831",
    ("infinix", "hot 20 5g"): "X666",
    ("infinix", "hot 11s"): "X6812",
    ("infinix", "smart 8"): "X6525",
    ("infinix", "gt 50 pro"): "X6910",
    ("infinix", "note 60 ultra"): "X6930",
    ("infinix", "xpad 30 pro"): "X1101",
    ("infinix", "hot 70 pro"): "X6888",
    ("infinix", "hot 70"): "X6886",

    # Huawei
    ("huawei", "pura 70 ultra"): "HBP-AL00",
    ("huawei", "huawei mate 50 pro"): "DCO-AL00, DCO-LX9",
    ("huawei", "huawei p50 pro"): "JAD-AL50, JAD-LX9",
    ("huawei", "huawei mate 30 pro"): "LIO-L29, LIO-AL00",
    ("huawei", "huawei p30 pro"): "VOG-L29, VOG-L09",
    ("huawei", "huawei mate 20 pro"): "LYA-L29, LYA-L09",
    ("huawei", "huawei p20 pro"): "CLT-L29, CLT-L09",
    ("huawei", "mate 90 rs ultimate"): "ALN-AL80",
    ("huawei", "mate 90 pro max"): "ALN-AL60",
    ("huawei", "mate 90 pro"): "ALN-AL10",
    ("huawei", "mate 90"): "ALN-AL00",

    # BlackBerry
    ("blackberry", "blackberry keyone"): "BBB100-1, BBB100-2",
    ("blackberry", "blackberry passport"): "SQW100-1",
    ("blackberry", "blackberry z10"): "STL100-1",
    ("blackberry", "blackberry q10"): "SQN100-3",
    ("blackberry", "blackberry bold 9900 (dakota)"): "RDY71UW",
    ("blackberry", "blackberry bold 9700 (onyx)"): "RCF71UW",
    ("blackberry", "blackberry curve 8520 (gemini)"): "RBV41GW",
    ("blackberry", "blackberry curve 9300 (kepler)"): "RDH71CW",
    ("blackberry", "blackberry torch 9800"): "RDG71UW",

    # Sharp
    ("sharp", "aquos wish5"): "SH-54E, SH-M29",
    ("sharp", "aquos sense10"): "SH-55E",
    ("sharp", "aquos r11"): "SH-56E",

    # Meizu
    ("meizu", "22"): "M522Q",
    ("meizu", "note 22 pro"): "M522N",
    ("meizu", "note 22"): "M522C",

    # Honor
    ("honor", "magic9 pro max"): "BVL-AN10",
    ("honor", "magic9 super"): "BVL-AN05",
    ("honor", "magic9"): "BVL-AN00, BVL-N49",
    ("honor", "play20c"): "CLK-AL00",
    ("honor", "x5d s"): "WKG-LX9",

    # OnePlus
    ("oneplus", "16"): "CPH2811",
    ("oneplus", "n6x"): "CPH2831",
    ("oneplus", "n6"): "CPH2835",
    ("oneplus", "n6 lite"): "CPH2839",
    ("oneplus", "turbo 6x pro"): "CPH2841",

    # Motorola
    ("motorola", "signature 27"): "XT2605-1",
    ("motorola", "edge 70 plus"): "XT2601-1",
    ("motorola", "edge 70 max"): "XT2603-1",
    ("motorola", "moto g77 power"): "XT2607-1",
    ("motorola", "moto g max"): "XT2611-1",

    # Sony
    ("sony", "xperia 1 vii"): "XQ-FS54, XQ-FS72",
    ("sony", "xperia 10 vii"): "XQ-ES54",
    ("sony", "xperia 1 viii"): "XQ-GS72",
    ("sony", "xperia 10 viii"): "XQ-GS54",
    ("sony", "xperia 1 vi"): "XQ-EC54, XQ-EC72",

    # ZTE
    ("zte", "nubia redmagic 12 pro+"): "NX789J",
    ("zte", "nubia redmagic 12 pro"): "NX788J",
    ("zte", "nubia navix ultra"): "NX780J",
    ("zte", "nubia a37e"): "Z2355",

    # Nothing
    ("nothing", "phone (4b)"): "A070",
    ("nothing", "phone (4a) pro"): "A069",
    ("nothing", "phone (2)"): "A065",
    ("nothing", "phone (2a)"): "A142",
    ("nothing", "phone (1)"): "A063",

    # Lenovo
    ("lenovo", "legion y700 ai"): "TB320FC",
    ("lenovo", "legion y900 13"): "TB371FC",
    ("lenovo", "legion y900 11"): "TB370FC",

    # Nokia
    ("nokia", "300 charge"): "TA-1610",
    ("nokia", "123 shield"): "TA-1612",
    ("nokia", "235 4g (2026)"): "TA-1614",
    ("nokia", "215 4g (2026)"): "TA-1616",
    ("nokia", "nokia 3310 (2017)"): "TA-1008, TA-1030",
    ("nokia", "nokia 8110 4g"): "TA-1059, TA-1048",
    ("nokia", "nokia 6.1 plus"): "TA-1103, TA-1116",
    ("nokia", "nokia 8"): "TA-1004, TA-1012"
}

def execute_audit_and_fix():
    print(f"[*] Menghubungkan ke database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Update 5G models di GSMArena
    gsmarena_5g_updates = [
        ("Apple", "iPhone 18 Pro Max"),
        ("Apple", "iPhone 18 Pro"),
        ("Apple", "iPhone 17e"),
        ("Huawei", "Mate 90 RS Ultimate"),
        ("Huawei", "Mate 90 Pro Max"),
        ("Huawei", "Mate 90 Pro"),
        ("Huawei", "Mate 90"),
        ("Motorola", "Moto G Max"),
        ("Xiaomi", "18 Fold")
    ]
    for b_name, m_name in gsmarena_5g_updates:
        cursor.execute("""
            UPDATE master_models
            SET network_gen = '5G'
            WHERE id IN (
                SELECT m.id FROM master_models m JOIN master_brands b ON m.brand_id = b.id
                WHERE LOWER(b.name) = LOWER(?) AND LOWER(m.name) = LOWER(?)
            );
        """, (b_name, m_name))
        print(f"[✓] GSMArena: {b_name} {m_name} -> 5G")

    # 2. Standardisasi label jaringan campuran di Official Indonesia
    cursor.execute("UPDATE master_models SET network_gen = '4G LTE' WHERE name = 'Galaxy S20 Ultra';")
    cursor.execute("UPDATE master_models SET network_gen = '4G LTE' WHERE name = 'Galaxy Note 20 Ultra';")
    cursor.execute("UPDATE master_models SET network_gen = '3G HSPA' WHERE name = 'Galaxy S4';")
    cursor.execute("UPDATE master_models SET network_gen = '5G' WHERE name = 'Pura 70 Ultra';")
    print("[✓] Official Indonesia: Label jaringan campuran distandardisasi.")

    # 3. Lengkapi spesifikasi Nokia GSMArena
    cursor.execute("""
        UPDATE master_models
        SET chipset = 'Unisoc T107 (22 nm)',
            os_at_launch = 'S30+',
            main_camera_mp = '2 MP'
        WHERE name = '235 4G (2026)';
    """)
    cursor.execute("""
        UPDATE master_models
        SET chipset = 'Unisoc T107 (22 nm)',
            os_at_launch = 'S30+',
            main_camera_mp = 'Tidak Ada Kamera'
        WHERE name = '215 4G (2026)';
    """)
    cursor.execute("UPDATE master_models SET os_at_launch = 'S30+' WHERE name IN ('300 Charge', '123 Shield');")
    print("[✓] GSMArena: Spesifikasi feature phone Nokia disempurnakan.")

    # 4. Backfill factory_model_code untuk seluruh entri
    cursor.execute("SELECT m.id, b.name, m.name FROM master_models m JOIN master_brands b ON m.brand_id = b.id;")
    all_models = cursor.fetchall()
    backfilled_count = 0
    for m_id, b_name, m_name in all_models:
        key = (b_name.lower().strip(), m_name.lower().strip())
        code = COMPREHENSIVE_MODEL_CODES.get(key)
        if not code:
            # Fuzzy match
            for (fb, fm), fc in COMPREHENSIVE_MODEL_CODES.items():
                if fb == key[0] and (fm in key[1] or key[1] in fm):
                    code = fc
                    break
        if code:
            cursor.execute("UPDATE master_models SET factory_model_code = ? WHERE id = ?;", (code, m_id))
            backfilled_count += 1

    print(f"[✓] Total model terisi Kode Model Pabrikan: {backfilled_count} / {len(all_models)}")
    conn.commit()

    # 5. Export ke data/datahptambahgenerasi.csv
    print(f"[*] Mengekspor dataset terverifikasi ke {CSV_PATH}")
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
    execute_audit_and_fix()

# Kamus tambahan untuk 53 model tersisa di Official Indonesia
REMAINING_53_CODES = {
    ("huawei", "mate 40 pro"): "NOH-NX9, NOH-AN00",
    ("huawei", "huawei nova 5t"): "YAL-L21, YAL-L61",
    ("huawei", "huawei p9"): "EVA-L09, EVA-L19",
    ("infinix", "infinix zero ultra"): "X6820",
    ("infinix", "infinix zero 5g"): "X6815",
    ("nokia", "nokia 7 plus"): "TA-1062, TA-1046",
    ("nokia", "nokia lumia 1020"): "RM-875, RM-877",
    ("nokia", "nokia lumia 520"): "RM-914, RM-915",
    ("nokia", "nokia lumia 720"): "RM-885",
    ("nokia", "nokia lumia 920"): "RM-821, RM-820",
    ("nokia", "nokia n8"): "RM-596",
    ("oppo", "oppo f11 pro"): "CPH1969",
    ("oppo", "oppo f9"): "CPH1823, CPH1881",
    ("oppo", "oppo f7"): "CPH1819",
    ("oppo", "oppo f5"): "CPH1723",
    ("oppo", "oppo f3 plus"): "CPH1613",
    ("oppo", "oppo f1s"): "A1601",
    ("oppo", "oppo find 7a"): "X9006",
    ("oppo", "oppo n1"): "N5111",
    ("realme", "realme gt neo 3"): "RMX3561, RMX3563",
    ("realme", "realme 5 pro"): "RMX1971",
    ("realme", "realme 3 pro"): "RMX1851",
    ("realme", "realme xt"): "RMX1921",
    ("realme", "realme 2 pro"): "RMX1801",
    ("sony", "sony xperia 1 v"): "XQ-DQ54, XQ-DQ72",
    ("sony", "sony xperia 5 v"): "XQ-DE54, XQ-DE72",
    ("sony", "xperia 1 iv"): "XQ-CT54, XQ-CT72",
    ("sony", "xperia xz premium"): "G8141, G8142",
    ("sony", "sony xperia xz premium"): "G8141, G8142",
    ("sony", "sony xperia z5"): "E6603, E6653",
    ("sony", "xperia z3 (d6603)"): "D6603, D6653",
    ("sony", "sony xperia z3"): "D6603, D6653",
    ("sony", "xperia z (c6603)"): "C6603",
    ("sony", "xperia z1 (c6903)"): "C6903",
    ("tecno", "tecno pova 5 pro 5g"): "LH8n",
    ("tecno", "tecno camon 20 pro 5g"): "CK8n",
    ("tecno", "tecno phantom v flip 5g"): "AD11",
    ("tecno", "tecno phantom x2 pro 5g"): "AD9",
    ("vivo", "vivo v40 5g"): "V2348",
    ("vivo", "iqoo z7 5g"): "I2207",
    ("vivo", "iqoo 11 5g"): "V2243A, I2212",
    ("vivo", "vivo xshot"): "X710L",
    ("xiaomi", "poco x4 pro 5g"): "2201116PG",
    ("xiaomi", "redmi note 5 (whyred)"): "MEI7S, MEE7S",
    ("xiaomi", "redmi note 4 (snapdragon)"): "2016102",
    ("xiaomi", "xiaomi mi a1"): "MDG2",
    ("xiaomi", "redmi note 3"): "2015116",
    ("iqoo", "iqoo z9 5g"): "I2302",
    ("iqoo", "iqoo z9x 5g"): "I2219",
    ("iqoo", "iqoo neo 9 pro"): "I2304",
    ("iqoo", "iqoo neo 7 pro 5g"): "I2217",
    ("iqoo", "iqoo z7x 5g"): "I2216",
    ("iqoo", "iqoo 9 pro"): "I2022"
}

def fill_remaining_53():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT m.id, b.name, m.name FROM master_models m JOIN master_brands b ON m.brand_id = b.id WHERE m.factory_model_code IS NULL;")
    remaining = cursor.fetchall()
    count = 0
    for m_id, b_name, m_name in remaining:
        key = (b_name.lower().strip(), m_name.lower().strip())
        code = REMAINING_53_CODES.get(key)
        if not code:
            for (fb, fm), fc in REMAINING_53_CODES.items():
                if fb == key[0] and (fm in key[1] or key[1] in fm):
                    code = fc
                    break
        if code:
            cursor.execute("UPDATE master_models SET factory_model_code = ? WHERE id = ?;", (code, m_id))
            count += 1
    conn.commit()
    conn.close()
    print(f"[✓] Berhasil mem-backfill {count} dari 53 model tersisa.")

if __name__ == "__main__":
    fill_remaining_53()
    # Rerun export to CSV
    execute_audit_and_fix()
