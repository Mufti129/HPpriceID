"""
Batch 5 Master Catalog Smartphone Pasar Indonesia (2010 - 2026).
Ekspansi besar 90 model smartphone baru dan 118 varian RAM/ROM baru:
- Samsung (Galaxy S23 FE, A53 5G, A33 5G, A25 5G, A05s, Note Edge, S9)
- Apple (iPhone 14 Plus, iPhone 6s Plus)
- Xiaomi / Poco / Redmi (Xiaomi 13T Pro, Poco F6 Pro, Poco X5 Pro 5G, Poco X6 5G, Redmi Note 13 Pro 5G, Redmi Note 12 Pro+ 5G, Redmi Note 10 5G, Redmi Note 8, Redmi 10, Xiaomi Mi 10T Pro, Xiaomi Mi 9, Xiaomi Mi A1, Xiaomi Mi 6, Xiaomi Mi 4)
- Oppo (Oppo Reno 10 5G, Oppo Reno 8 5G, Oppo Reno 4, Oppo Reno 10x Zoom, Oppo A96, Oppo A57 (2022), Oppo A54, Oppo F3 Plus, Oppo N1, Oppo Find 7a)
- Vivo (Vivo X90 Pro, Vivo X60 Pro, Vivo X50 Pro, Vivo V25 Pro 5G, Vivo V21 5G, Vivo V19, Vivo V9, Vivo V7+, Vivo Y27 5G, Vivo Y36 5G, Vivo Xshot)
- iQOO (iQOO Z9x 5G, iQOO Z7x 5G, iQOO Neo 9 Pro)
- Realme (Realme 12+ 5G, Realme 10 Pro+ 5G, Realme 8 Pro, Realme 7 Pro, Realme XT, Realme C67, Realme C53, Realme GT 2 Pro, Realme 2 Pro)
- Infinix (Infinix Note 40 Pro+ 5G, Infinix Note 40 4G, Infinix Note 30 4G, Infinix Hot 30, Infinix Hot 20 5G, Infinix Smart 8, Infinix Zero 8)
- Tecno (Tecno Camon 30 Pro 5G, Tecno Camon 30 5G, Tecno Spark 20 Pro, Tecno Spark 20, Tecno Pova 4 Pro, Tecno Phantom V Flip 5G, Tecno Phantom X2 Pro 5G)
- BlackBerry (BlackBerry Curve 9300 (Kepler), BlackBerry Torch 9800, BlackBerry Q10, BlackBerry KEYone)
- Nokia (Nokia Lumia 920, Nokia Lumia 720, Nokia 7 Plus, Nokia 8)
- Asus (ROG Phone 6D Ultimate, ROG Phone II, Zenfone 5Z)
- Sony (Sony Xperia 1 V, Sony Xperia 5 V, Sony Xperia XZ Premium)
- Google (Google Pixel 8 Pro, Google Pixel 7 Pro, Google Pixel 4a)
- Huawei (Huawei Mate 50 Pro, Huawei Nova 5T, Huawei Mate 30 Pro)

Sumber Data Spesifikasi & Pasar:
1. GSMArena (gsmarena.com) - Spesifikasi teknis SoC, Display, Kamera, Sensor, Baterai.
2. Kimovil (kimovil.com) - Benchmark AnTuTu v9/v10 dan rasio hardware.
3. Kompas Tekno (tekno.kompas.com) - Arsip peluncuran resmi dan daftar harga MSRP perdana Indonesia.
4. JagatReview / JagatGadget (jagatreview.com) - Uji daya, performa rilis pasar Indonesia.
5. Arsip Resmi Vendor (Samsung ID, Apple iBox/Digimap, Xiaomi ID, Oppo ID, Vivo ID, Realme ID, Infinix ID, Tecno ID).
"""

EXTENDED_CATALOG_MODELS_BATCH5 = [
    # ==================== 1. SAMSUNG BATCH 5 ====================
    {
        "brand_name": "Samsung",
        "models": [
            {
                "name": "Galaxy S23 FE", "series": "Fan Edition Dynamic AMOLED", "release_year": 2023,
                "chipset": "Exynos 2200 (4nm)", "cpu_architecture": "Octa-core 2.8GHz (1x Cortex-X2 + 3x Cortex-A710 + 4x Cortex-A510)",
                "gpu": "Xclipse 920 (AMD RDNA2)", "antutu_benchmark_score": 1150000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+, 1450 nits", "screen_size_inch": 6.4,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (wide, OIS) + 8 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "10 MP, f/2.4", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 209, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy S23 FE 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 8999000, "aliases": "s23 fe 128, samsung s23 fe"},
                    {"variant_name": "Galaxy S23 FE 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "s23 fe 256, samsung s23 fe 256gb"}
                ]
            },
            {
                "name": "Galaxy A53 5G", "series": "A-Series OIS Waterproof Bestseller", "release_year": 2022,
                "chipset": "Exynos 1280 (5nm)", "cpu_architecture": "Octa-core 2.4GHz (2x Cortex-A78 + 6x Cortex-A55)",
                "gpu": "Mali-G68", "antutu_benchmark_score": 430000,
                "display_type": "Super AMOLED, 120Hz, 800 nits", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 12 MP (ultrawide) + 5 MP (macro) + 5 MP (depth)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 189, "os_at_launch": "Android 12, One UI 4.1",
                "variants": [
                    {"variant_name": "Galaxy A53 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5999000, "aliases": "a53 128, samsung a53 5g"},
                    {"variant_name": "Galaxy A53 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6499000, "aliases": "a53 256, samsung a53 256gb"}
                ]
            },
            {
                "name": "Galaxy A33 5G", "series": "A-Series IP67 Value Champion", "release_year": 2022,
                "chipset": "Exynos 1280 (5nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68", "antutu_benchmark_score": 420000,
                "display_type": "Super AMOLED, 90Hz, U-Cut", "screen_size_inch": 6.4,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (wide, OIS) + 8 MP (ultrawide) + 5 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.2", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 186, "os_at_launch": "Android 12, One UI 4.1",
                "variants": [
                    {"variant_name": "Galaxy A33 5G 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 4699000, "aliases": "a33 6gb, samsung a33 128gb"},
                    {"variant_name": "Galaxy A33 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "a33 256, samsung a33 256gb"}
                ]
            },
            {
                "name": "Galaxy A25 5G", "series": "A-Series 120Hz OIS Key Island", "release_year": 2024,
                "chipset": "Exynos 1280 (5nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68", "antutu_benchmark_score": 440000,
                "display_type": "Super AMOLED, 120Hz, 1000 nits", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Glass",
                "main_camera_mp": "50 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.2", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 197, "os_at_launch": "Android 14, One UI 6.0",
                "variants": [
                    {"variant_name": "Galaxy A25 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3999000, "aliases": "a25 128, samsung a25 5g"},
                    {"variant_name": "Galaxy A25 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4399000, "aliases": "a25 256, samsung a25 256gb"}
                ]
            },
            {
                "name": "Galaxy A05s", "series": "A-Series Snapdragon Entry Hero", "release_year": 2023,
                "chipset": "Snapdragon 680 4G (6nm)", "cpu_architecture": "Octa-core 2.4GHz Kryo 265",
                "gpu": "Adreno 610", "antutu_benchmark_score": 310000,
                "display_type": "PLS LCD, 90Hz Full HD+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.8 + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.0", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 194, "os_at_launch": "Android 13, One UI Core 5.1",
                "variants": [
                    {"variant_name": "Galaxy A05s 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2299000, "aliases": "a05s 128, samsung a05s"}
                ]
            },
            {
                "name": "Galaxy Note Edge", "series": "Curved Edge Display Pioneer", "release_year": 2014,
                "chipset": "Snapdragon 805 (28nm)", "cpu_architecture": "Quad-core 2.7GHz Krait 450",
                "gpu": "Adreno 420", "antutu_benchmark_score": 69000,
                "display_type": "Curved Edge Super AMOLED QHD+", "screen_size_inch": 5.6,
                "refresh_rate_hz": 60, "resolution": "1600 x 2560 pixels", "peak_brightness_nits": 550,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "16 MP, f/2.2, Smart OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "3.7 MP, f/1.9, 120 deg Wide Selfie", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 15, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 174, "os_at_launch": "Android 4.4.4 (KitKat), TouchWiz",
                "variants": [
                    {"variant_name": "Galaxy Note Edge 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 10999000, "aliases": "note edge, samsung note edge"}
                ]
            },
            {
                "name": "Galaxy S9", "series": "S-Series Dual Aperture Compact", "release_year": 2018,
                "chipset": "Exynos 9810 (10nm)", "cpu_architecture": "Octa-core 2.7GHz (4x Mongoose M3 + 4x Cortex-A55)",
                "gpu": "Mali-G72 MP18", "antutu_benchmark_score": 320000,
                "display_type": "Super AMOLED Curved Infinity Display QHD+", "screen_size_inch": 5.8,
                "refresh_rate_hz": 60, "resolution": "1440 x 2960 pixels", "peak_brightness_nits": 1100,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP, f/1.5-2.4 variable aperture, Dual Pixel PDAF, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/1.7, AF", "video_recording_max": "4K@60fps, 720p@960fps super slow-mo",
                "battery_capacity_mah": 3000, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 163, "os_at_launch": "Android 8.0 (Oreo), Samsung Experience",
                "variants": [
                    {"variant_name": "Galaxy S9 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 11499000, "aliases": "s9 64, samsung s9"},
                    {"variant_name": "Galaxy S9 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 12499000, "aliases": "s9 128, samsung s9 128gb"}
                ]
            }
        ]
    },

    # ==================== 2. APPLE BATCH 5 ====================
    {
        "brand_name": "Apple",
        "models": [
            {
                "name": "iPhone 14 Plus", "series": "Plus Big Screen Value", "release_year": 2022,
                "chipset": "Apple A15 Bionic (5nm, 5-core GPU)", "cpu_architecture": "6-core CPU (2 performance + 4 efficiency)",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1280000,
                "display_type": "Super Retina XDR OLED, HDR10, Dolby Vision", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1284 x 2778 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide, sensor-shift OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/1.9, PDAF", "video_recording_max": "4K@60fps Dolby Vision, Cinematic Mode 4K@30fps",
                "battery_capacity_mah": 4323, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 203, "os_at_launch": "iOS 16",
                "variants": [
                    {"variant_name": "iPhone 14 Plus 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 17999000, "aliases": "14 plus 128, ip 14 plus 128gb"},
                    {"variant_name": "iPhone 14 Plus 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 20999000, "aliases": "14 plus 256, ip 14 plus 256gb"},
                    {"variant_name": "iPhone 14 Plus 512GB", "ram_gb": 6, "storage_gb": 512, "official_msrp_new": 24999000, "aliases": "14 plus 512, ip 14 plus 512gb"}
                ]
            },
            {
                "name": "iPhone 6s Plus", "series": "3D Touch Video OIS Pioneer", "release_year": 2015,
                "chipset": "Apple A9 (14nm/16nm)", "cpu_architecture": "Dual-core 1.84GHz Twister",
                "gpu": "PowerVR GT7600 (6-core)", "antutu_benchmark_score": 180000,
                "display_type": "IPS LCD Retina Full HD, 3D Touch display", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 550,
                "screen_protection": "Ion-strengthened glass, oleophobic coating",
                "main_camera_mp": "12 MP, f/2.2, PDAF, OIS hardware",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.2, Retina Flash", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 2750, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 192, "os_at_launch": "iOS 9",
                "variants": [
                    {"variant_name": "iPhone 6s Plus 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 12999000, "aliases": "6s plus 16, ip 6s plus 16gb"},
                    {"variant_name": "iPhone 6s Plus 64GB", "ram_gb": 2, "storage_gb": 64, "official_msrp_new": 14999000, "aliases": "6s plus 64, ip 6s plus 64gb"},
                    {"variant_name": "iPhone 6s Plus 128GB", "ram_gb": 2, "storage_gb": 128, "official_msrp_new": 16999000, "aliases": "6s plus 128, ip 6s plus 128gb"}
                ]
            }
        ]
    },

    # ==================== 3. XIAOMI / POCO / REDMI BATCH 5 ====================
    {
        "brand_name": "Xiaomi",
        "models": [
            {
                "name": "Xiaomi 13T Pro", "series": "Flagship Leica 144Hz 120W", "release_year": 2023,
                "chipset": "MediaTek Dimensity 9200+ (4nm)", "cpu_architecture": "Octa-core 3.35GHz (1x Cortex-X3 + 3x Cortex-A715 + 4x Cortex-A510)",
                "gpu": "Immortalis-G715 MC11", "antutu_benchmark_score": 1480000,
                "display_type": "CrystalRes AMOLED, 68B colors, 144Hz, Dolby Vision, HDR10+, 2600 nits", "screen_size_inch": 6.67,
                "refresh_rate_hz": 144, "resolution": "1220 x 2712 pixels (1.5K)", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Leica, OIS, 24mm) + 50 MP (Leica 2x telephoto, 50mm) + 12 MP (Leica ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "20 MP, f/2.2, HDR", "video_recording_max": "8K@24fps, 4K@60fps 10-bit LOG",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 206, "os_at_launch": "Android 13, MIUI 14",
                "variants": [
                    {"variant_name": "Xiaomi 13T Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "13t pro 256, xiaomi 13t pro"},
                    {"variant_name": "Xiaomi 13T Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 10999000, "aliases": "13t pro 512, xiaomi 13t pro 512gb"}
                ]
            },
            {
                "name": "Poco F6 Pro", "series": "F-Series WQHD+ 120W Extreme", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1600000,
                "display_type": "Flow AMOLED, 68B colors, 120Hz, WQHD+, Dolby Vision, 4000 nits", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (WQHD+)", "peak_brightness_nits": 4000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Light Fusion 800, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 209, "os_at_launch": "Android 14, HyperOS",
                "variants": [
                    {"variant_name": "Poco F6 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 7999000, "aliases": "f6 pro 256, poco f6 pro"},
                    {"variant_name": "Poco F6 Pro 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 8999000, "aliases": "f6 pro 512, poco f6 pro 512gb"}
                ]
            },
            {
                "name": "Poco X5 Pro 5G", "series": "X-Series 108MP 778G Slim", "release_year": 2023,
                "chipset": "Snapdragon 778G 5G (6nm)", "cpu_architecture": "Octa-core 2.4GHz Kryo 670",
                "gpu": "Adreno 642L", "antutu_benchmark_score": 545000,
                "display_type": "Flow AMOLED, 1B colors, 120Hz, Dolby Vision, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (Samsung HM2, f/1.9) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 181, "os_at_launch": "Android 12, MIUI 14 for POCO",
                "variants": [
                    {"variant_name": "Poco X5 Pro 5G 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 3799000, "aliases": "x5 pro 128, poco x5 pro"},
                    {"variant_name": "Poco X5 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4299000, "aliases": "x5 pro 256, poco x5 pro 256gb"}
                ]
            },
            {
                "name": "Poco X6 5G", "series": "X-Series 1.5K 64MP OIS", "release_year": 2024,
                "chipset": "Snapdragon 7s Gen 2 (4nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 710", "antutu_benchmark_score": 605000,
                "display_type": "AMOLED, 68B colors, 120Hz, 1.5K, Dolby Vision, 1800 nits", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1220 x 2712 pixels (1.5K)", "peak_brightness_nits": 1800,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5100, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 181, "os_at_launch": "Android 14, HyperOS",
                "variants": [
                    {"variant_name": "Poco X6 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 3999000, "aliases": "poco x6 256, poco x6 5g"}
                ]
            },
            {
                "name": "Redmi Note 13 Pro 5G", "series": "Note 13 200MP OIS 1.5K", "release_year": 2024,
                "chipset": "Snapdragon 7s Gen 2 (4nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 710", "antutu_benchmark_score": 600000,
                "display_type": "AMOLED, 68B colors, 120Hz, 1.5K, Dolby Vision, 1800 nits", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1220 x 2712 pixels", "peak_brightness_nits": 1800,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "200 MP (Samsung ISOCELL HP3, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "4x In-Sensor Lossless",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5100, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 187, "os_at_launch": "Android 13, MIUI 14",
                "variants": [
                    {"variant_name": "Redmi Note 13 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4399000, "aliases": "rn 13 pro 5g, redmi note 13 pro"},
                    {"variant_name": "Redmi Note 13 Pro 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 4999000, "aliases": "rn 13 pro 512, note 13 pro 512"}
                ]
            },
            {
                "name": "Redmi Note 12 Pro+ 5G", "series": "Note 12 200MP OIS 120W", "release_year": 2023,
                "chipset": "MediaTek Dimensity 1080 (6nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 525000,
                "display_type": "OLED, 1B colors, 120Hz, Dolby Vision, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "200 MP (Samsung ISOCELL HPX, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 208, "os_at_launch": "Android 12, MIUI 13",
                "variants": [
                    {"variant_name": "Redmi Note 12 Pro+ 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4599000, "aliases": "rn 12 pro plus, redmi note 12 pro+"}
                ]
            },
            {
                "name": "Redmi Note 10 5G", "series": "Jawara 5G Affordable Pioneer", "release_year": 2021,
                "chipset": "MediaTek Dimensity 700 (7nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 320000,
                "display_type": "IPS LCD, 90Hz AdaptiveSync, 500 nits", "screen_size_inch": 6.5,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "48 MP, f/1.8 + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 190, "os_at_launch": "Android 11, MIUI 12",
                "variants": [
                    {"variant_name": "Redmi Note 10 5G 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 2799000, "aliases": "rn 10 5g 128, redmi note 10 5g"},
                    {"variant_name": "Redmi Note 10 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3099000, "aliases": "rn 10 5g 8gb"}
                ]
            },
            {
                "name": "Redmi Note 8", "series": "Note 48MP Quad Camera Super-Seller", "release_year": 2019,
                "chipset": "Snapdragon 665 (11nm)", "cpu_architecture": "Octa-core 2.0GHz Kryo 260",
                "gpu": "Adreno 610", "antutu_benchmark_score": 175000,
                "display_type": "IPS LCD Dot Drop Full HD+", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (Samsung GM1, f/1.8) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "Splash-resistant coating", "weight_grams": 190, "os_at_launch": "Android 9.0 (Pie), MIUI 10",
                "variants": [
                    {"variant_name": "Redmi Note 8 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2099000, "aliases": "rn 8 64, redmi note 8 64gb"},
                    {"variant_name": "Redmi Note 8 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2899000, "aliases": "rn 8 128, redmi note 8 128gb"}
                ]
            },
            {
                "name": "Redmi 10", "series": "Redmi 50MP 90Hz Budget Benchmark", "release_year": 2021,
                "chipset": "MediaTek Helio G88 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 MC2", "antutu_benchmark_score": 240000,
                "display_type": "IPS LCD, 90Hz AdaptiveSync Full HD+", "screen_size_inch": 6.5,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "50 MP, f/1.8 + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 181, "os_at_launch": "Android 11, MIUI 12.5",
                "variants": [
                    {"variant_name": "Redmi 10 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 1999000, "aliases": "redmi 10 64, r10 64"},
                    {"variant_name": "Redmi 10 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2399000, "aliases": "redmi 10 128, r10 128"}
                ]
            },
            {
                "name": "Xiaomi Mi 10T Pro", "series": "Mi 144Hz 108MP Flagship Killer", "release_year": 2020,
                "chipset": "Snapdragon 865 (7nm+)", "cpu_architecture": "Octa-core 2.84GHz Kryo 585",
                "gpu": "Adreno 650", "antutu_benchmark_score": 680000,
                "display_type": "IPS LCD, 144Hz AdaptiveSync, HDR10+, 650 nits", "screen_size_inch": 6.67,
                "refresh_rate_hz": 144, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 650,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (Samsung HMX, f/1.69, OIS) + 13 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 218, "os_at_launch": "Android 10, MIUI 12",
                "variants": [
                    {"variant_name": "Xiaomi Mi 10T Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 6999000, "aliases": "mi 10t pro 128, mi 10t pro"},
                    {"variant_name": "Xiaomi Mi 10T Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 7499000, "aliases": "mi 10t pro 256, mi 10t pro 256gb"}
                ]
            },
            {
                "name": "Xiaomi Mi 9", "series": "Mi Numbered Flagship Triple Camera", "release_year": 2019,
                "chipset": "Snapdragon 855 (7nm)", "cpu_architecture": "Octa-core 2.84GHz Kryo 485",
                "gpu": "Adreno 640", "antutu_benchmark_score": 440000,
                "display_type": "Super AMOLED, HDR10, 600 nits", "screen_size_inch": 6.39,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "48 MP (Sony IMX586, f/1.75) + 12 MP (2x telephoto) + 16 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "20 MP, f/2.0", "video_recording_max": "4K@60fps, 1080p@240fps",
                "battery_capacity_mah": 3300, "fast_charging_watt": 27, "has_wireless_charging": True, "wireless_charging_watt": 20,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 173, "os_at_launch": "Android 9.0 (Pie), MIUI 10",
                "variants": [
                    {"variant_name": "Xiaomi Mi 9 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 6999000, "aliases": "mi 9 64, mi 9"},
                    {"variant_name": "Xiaomi Mi 9 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 7999000, "aliases": "mi 9 128, mi 9 128gb"}
                ]
            },
            {
                "name": "Xiaomi Mi A1", "series": "Android One Dual Camera Pioneer", "release_year": 2017,
                "chipset": "Snapdragon 625 (14nm)", "cpu_architecture": "Octa-core 2.0GHz Cortex-A53",
                "gpu": "Adreno 506", "antutu_benchmark_score": 78000,
                "display_type": "LTPS IPS LCD Full HD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12 MP (26mm, f/2.2) + 12 MP (50mm 2x telephoto)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "5 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 3080, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 165, "os_at_launch": "Android 7.1.2 (Nougat, Pure Android One)",
                "variants": [
                    {"variant_name": "Xiaomi Mi A1 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 3099000, "aliases": "mi a1, xiaomi a1"}
                ]
            },
            {
                "name": "Xiaomi Mi 6", "series": "Stainless Steel 4-Axis OIS Flagship", "release_year": 2017,
                "chipset": "Snapdragon 835 (10nm)", "cpu_architecture": "Octa-core 2.45GHz Kryo",
                "gpu": "Adreno 540", "antutu_benchmark_score": 210000,
                "display_type": "IPS LCD Full HD, 600 nits", "screen_size_inch": 5.15,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "12 MP (f/1.8, 4-axis OIS) + 12 MP (52mm 2x telephoto)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 3350, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "Splash resistant", "weight_grams": 168, "os_at_launch": "Android 7.1.1 (Nougat), MIUI 8",
                "variants": [
                    {"variant_name": "Xiaomi Mi 6 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 5499000, "aliases": "mi 6 64, xiaomi mi 6"},
                    {"variant_name": "Xiaomi Mi 6 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 6299000, "aliases": "mi 6 128, xiaomi mi 6 128gb"}
                ]
            },
            {
                "name": "Xiaomi Mi 4", "series": "Mi Stainless Steel Launch Frenzy", "release_year": 2014,
                "chipset": "Snapdragon 801 (28nm)", "cpu_architecture": "Quad-core 2.5GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 46000,
                "display_type": "IPS LCD Full HD, 441 ppi", "screen_size_inch": 5.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Concore Glass",
                "main_camera_mp": "13 MP (Sony IMX214, f/1.8)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/1.8, 1080p", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 3080, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 149, "os_at_launch": "Android 4.4.3 (KitKat), MIUI 5",
                "variants": [
                    {"variant_name": "Xiaomi Mi 4 3GB/16GB", "ram_gb": 3, "storage_gb": 16, "official_msrp_new": 3899000, "aliases": "mi 4 16, xiaomi mi 4"},
                    {"variant_name": "Xiaomi Mi 4 3GB/64GB", "ram_gb": 3, "storage_gb": 64, "official_msrp_new": 4599000, "aliases": "mi 4 64, xiaomi mi 4 64gb"}
                ]
            }
        ]
    },

    # ==================== 4. OPPO BATCH 5 ====================
    {
        "brand_name": "Oppo",
        "models": [
            {
                "name": "Oppo Reno 10 5G", "series": "Reno Portrait Telephoto 67W", "release_year": 2023,
                "chipset": "MediaTek Dimensity 7050 (6nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 570000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+, 950 nits", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Asahi Glass AGC DT-Star2",
                "main_camera_mp": "64 MP (wide, f/1.7) + 32 MP (Sony IMX709 2x telephoto) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.4", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 185, "os_at_launch": "Android 13, ColorOS 13.1",
                "variants": [
                    {"variant_name": "Oppo Reno 10 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "reno 10 5g, oppo reno 10"}
                ]
            },
            {
                "name": "Oppo Reno 8 5G", "series": "Reno Streamlined Unibody 80W", "release_year": 2022,
                "chipset": "MediaTek Dimensity 1300 (6nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 680000,
                "display_type": "AMOLED, 90Hz, 800 nits", "screen_size_inch": 6.43,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766, f/1.8) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP (Sony IMX709 RGBW), f/2.4", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 179, "os_at_launch": "Android 12, ColorOS 12.1",
                "variants": [
                    {"variant_name": "Oppo Reno 8 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 7999000, "aliases": "reno 8 5g, oppo reno 8 5g"}
                ]
            },
            {
                "name": "Oppo Reno 4", "series": "Reno AI Color Portrait Slim", "release_year": 2020,
                "chipset": "Snapdragon 720G (8nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 465",
                "gpu": "Adreno 618", "antutu_benchmark_score": 325000,
                "display_type": "Super AMOLED, 430 nits", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 430,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "48 MP (Sony IMX586) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (mono)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.4 + Smart Sensor", "video_recording_max": "4K@30fps, 1080p@120fps, 960fps slow-mo",
                "battery_capacity_mah": 4015, "fast_charging_watt": 30, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 165, "os_at_launch": "Android 10, ColorOS 7.2",
                "variants": [
                    {"variant_name": "Oppo Reno 4 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "reno 4 128, oppo reno 4"}
                ]
            },
            {
                "name": "Oppo Reno 10x Zoom", "series": "Shark Fin Periscope Flagship", "release_year": 2019,
                "chipset": "Snapdragon 855 (7nm)", "cpu_architecture": "Octa-core 2.84GHz Kryo 485",
                "gpu": "Adreno 640", "antutu_benchmark_score": 430000,
                "display_type": "Panoramic AMOLED, HDR, DCI-P3 100%", "screen_size_inch": 6.6,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 430,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "48 MP (Sony IMX586, OIS) + 13 MP (5x periscope telephoto OIS, 10x hybrid) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope Optical",
                "selfie_camera_mp": "16 MP (Motorized Shark Fin pop-up), f/2.0", "video_recording_max": "4K@60fps, 1080p@240fps",
                "battery_capacity_mah": 4065, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 210, "os_at_launch": "Android 9.0 (Pie), ColorOS 6",
                "variants": [
                    {"variant_name": "Oppo Reno 10x Zoom 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 12999000, "aliases": "reno 10x zoom, reno periscope"}
                ]
            },
            {
                "name": "Oppo A96", "series": "A-Series Glow 33W Durable", "release_year": 2022,
                "chipset": "Snapdragon 680 4G (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 610", "antutu_benchmark_score": 310000,
                "display_type": "IPS LCD, 90Hz, 600 nits", "screen_size_inch": 6.59,
                "refresh_rate_hz": 90, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "50 MP, f/1.8 + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "IP54", "weight_grams": 191, "os_at_launch": "Android 11, ColorOS 11.1",
                "variants": [
                    {"variant_name": "Oppo A96 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4299000, "aliases": "oppo a96 256, a96 256gb"}
                ]
            },
            {
                "name": "Oppo A57 (2022)", "series": "A-Series Glow 33W Stereo Speakers", "release_year": 2022,
                "chipset": "MediaTek Helio G35 (12nm)", "cpu_architecture": "Octa-core 2.3GHz Cortex-A53",
                "gpu": "PowerVR GE8320", "antutu_benchmark_score": 135000,
                "display_type": "IPS LCD, 600 nits, Ultra-Linear Stereo Speakers", "screen_size_inch": 6.56,
                "refresh_rate_hz": 60, "resolution": "720 x 1612 pixels (HD+)", "peak_brightness_nits": 600,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "13 MP, f/2.2 + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "IP54", "weight_grams": 187, "os_at_launch": "Android 12, ColorOS 12.1",
                "variants": [
                    {"variant_name": "Oppo A57 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2399000, "aliases": "a57 64, oppo a57 2022"},
                    {"variant_name": "Oppo A57 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 2699000, "aliases": "a57 128, oppo a57 128gb"}
                ]
            },
            {
                "name": "Oppo A54", "series": "A-Series 5000mAh Massive Retailer", "release_year": 2021,
                "chipset": "MediaTek Helio P35 (12nm)", "cpu_architecture": "Octa-core 2.35GHz Cortex-A53",
                "gpu": "PowerVR GE8320", "antutu_benchmark_score": 130000,
                "display_type": "IPS LCD Punch-hole", "screen_size_inch": 6.51,
                "refresh_rate_hz": 60, "resolution": "720 x 1600 pixels (HD+)", "peak_brightness_nits": 480,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "13 MP, f/2.2 + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "IPX4", "weight_grams": 192, "os_at_launch": "Android 10, ColorOS 7.2",
                "variants": [
                    {"variant_name": "Oppo A54 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2499000, "aliases": "a54 64, oppo a54 64gb"},
                    {"variant_name": "Oppo A54 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 2699000, "aliases": "a54 128, oppo a54 128gb"}
                ]
            },
            {
                "name": "Oppo F3 Plus", "series": "Dual Selfie Wide-Angle Camera", "release_year": 2017,
                "chipset": "Snapdragon 653 (28nm)", "cpu_architecture": "Octa-core 1.95GHz (4x Cortex-A72 + 4x Cortex-A53)",
                "gpu": "Adreno 510", "antutu_benchmark_score": 95000,
                "display_type": "IPS LCD Full HD Display", "screen_size_inch": 6.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "16 MP (Sony IMX398, f/1.7, Dual PDAF)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "Dual: 16 MP (f/2.0) + 8 MP (120 deg wide-angle)", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 185, "os_at_launch": "Android 6.0 (Marshmallow), ColorOS 3.0",
                "variants": [
                    {"variant_name": "Oppo F3 Plus 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 6499000, "aliases": "oppo f3 plus, f3 plus 64"}
                ]
            },
            {
                "name": "Oppo N1", "series": "206-Degree Rotating Camera Pioneer", "release_year": 2013,
                "chipset": "Snapdragon 600 (28nm)", "cpu_architecture": "Quad-core 1.7GHz Krait 300",
                "gpu": "Adreno 320", "antutu_benchmark_score": 26000,
                "display_type": "IPS LCD Full HD, O-Touch Rear Touchpad", "screen_size_inch": 5.9,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP, f/2.0, 206-degree motorized rotating module, Dual-LED flash",
                "camera_setup": "Single Rotating", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "Uses Main Rotating 13 MP Camera", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3610, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA+", "has_nfc": True, "ip_rating": "None", "weight_grams": 213, "os_at_launch": "Android 4.2 (Jelly Bean), ColorOS / CyanogenMod",
                "variants": [
                    {"variant_name": "Oppo N1 2GB/16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 6999000, "aliases": "oppo n1, n1 rotating"},
                    {"variant_name": "Oppo N1 2GB/32GB", "ram_gb": 2, "storage_gb": 32, "official_msrp_new": 7499000, "aliases": "oppo n1 32, n1 32gb"}
                ]
            },
            {
                "name": "Oppo Find 7a", "series": "VOOC Flash Charge 50MP Super Zoom Pioneer", "release_year": 2014,
                "chipset": "Snapdragon 801 (28nm)", "cpu_architecture": "Quad-core 2.3GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 43000,
                "display_type": "IPS LCD Full HD, Skyline Notification LED", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP (Sony IMX214, f/2.0, 50MP Super Zoom composite mode)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 2800, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 170, "os_at_launch": "Android 4.3 (Jelly Bean), ColorOS 1.2",
                "variants": [
                    {"variant_name": "Oppo Find 7a 2GB/16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 6999000, "aliases": "find 7a, oppo find 7a"}
                ]
            }
        ]
    },

    # ==================== 5. VIVO BATCH 5 ====================
    {
        "brand_name": "Vivo",
        "models": [
            {
                "name": "Vivo X90 Pro", "series": "Zeiss 1-Inch Sensor Flagship", "release_year": 2022,
                "chipset": "MediaTek Dimensity 9200 (4nm) + Vivo V2 ISP", "cpu_architecture": "Octa-core 3.05GHz",
                "gpu": "Immortalis-G715 MC11", "antutu_benchmark_score": 1260000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+, 1300 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50.3 MP (1.0 inch Sony IMX989, OIS, Zeiss T*) + 50 MP (2x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4870, "fast_charging_watt": 120, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 214, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "Vivo X90 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 14999000, "aliases": "x90 pro 256, vivo x90 pro"},
                    {"variant_name": "Vivo X90 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 16999000, "aliases": "x90 pro 512, vivo x90 pro 512gb"}
                ]
            },
            {
                "name": "Vivo X60 Pro", "series": "Zeiss Gimbal Stabilization 2.0", "release_year": 2021,
                "chipset": "Snapdragon 870 5G (7nm)", "cpu_architecture": "Octa-core 3.2GHz Kryo 585",
                "gpu": "Adreno 650", "antutu_benchmark_score": 720000,
                "display_type": "AMOLED, 120Hz, HDR10+, 1300 nits", "screen_size_inch": 6.56,
                "refresh_rate_hz": 120, "resolution": "1080 x 2376 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "48 MP (Sony IMX598, Gimbal OIS 2.0, Zeiss) + 13 MP (2x telephoto) + 13 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@60fps Gimbal",
                "battery_capacity_mah": 4200, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 177, "os_at_launch": "Android 11, Funtouch 11.1",
                "variants": [
                    {"variant_name": "Vivo X60 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "x60 pro, vivo x60 pro zeiss"}
                ]
            },
            {
                "name": "Vivo X50 Pro", "series": "World First Micro-Gimbal Camera Pioneer", "release_year": 2020,
                "chipset": "Snapdragon 765G 5G (7nm)", "cpu_architecture": "Octa-core 2.4GHz Kryo 475",
                "gpu": "Adreno 620", "antutu_benchmark_score": 380000,
                "display_type": "Curved AMOLED, 90Hz, HDR10+, 1300 nits", "screen_size_inch": 6.56,
                "refresh_rate_hz": 90, "resolution": "1080 x 2376 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "48 MP (Sony IMX598, Micro-Gimbal OIS) + 8 MP (5x periscope telephoto OIS) + 13 MP (2x portrait) + 8 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@60fps Gimbal",
                "battery_capacity_mah": 4315, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 181, "os_at_launch": "Android 10, Funtouch 10.5",
                "variants": [
                    {"variant_name": "Vivo X50 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "x50 pro, vivo x50 pro gimbal"}
                ]
            },
            {
                "name": "Vivo V25 Pro 5G", "series": "V-Series Color Changing Fluorite AG Glass", "release_year": 2022,
                "chipset": "MediaTek Dimensity 1300 (6nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 700000,
                "display_type": "3D Curved AMOLED, 120Hz, HDR10+, 1300 nits", "screen_size_inch": 6.56,
                "refresh_rate_hz": 120, "resolution": "1080 x 2376 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5, Eye AF", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4830, "fast_charging_watt": 66, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 190, "os_at_launch": "Android 12, Funtouch 12",
                "variants": [
                    {"variant_name": "Vivo V25 Pro 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 8999000, "aliases": "v25 pro 256, vivo v25 pro"}
                ]
            },
            {
                "name": "Vivo V21 5G", "series": "World First 44MP OIS Dual Selfie Spotlight", "release_year": 2021,
                "chipset": "MediaTek Dimensity 800U (7nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G57 MC3", "antutu_benchmark_score": 390000,
                "display_type": "AMOLED, 90Hz, HDR10+, 500 nits", "screen_size_inch": 6.44,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Schott Xensation",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "44 MP, f/2.0, OIS hardware, Dual-LED front flash", "video_recording_max": "4K@30fps (Front & Rear OIS)",
                "battery_capacity_mah": 4000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 176, "os_at_launch": "Android 11, Funtouch 11.1",
                "variants": [
                    {"variant_name": "Vivo V21 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5799000, "aliases": "v21 5g, vivo v21 5g"}
                ]
            },
            {
                "name": "Vivo V19", "series": "V-Series Super Night Selfie E3 AMOLED", "release_year": 2020,
                "chipset": "Snapdragon 712 (10nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 360",
                "gpu": "Adreno 616", "antutu_benchmark_score": 225000,
                "display_type": "Super AMOLED E3, HDR10, 800 nits", "screen_size_inch": 6.44,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "48 MP (wide) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.1, Super Night Selfie", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 186, "os_at_launch": "Android 10, Funtouch 10.0",
                "variants": [
                    {"variant_name": "Vivo V19 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4299000, "aliases": "v19 128, vivo v19"},
                    {"variant_name": "Vivo V19 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4999000, "aliases": "v19 256, vivo v19 256gb"}
                ]
            },
            {
                "name": "Vivo V9", "series": "V-Series 24MP AI Selfie Notch Pioneer", "release_year": 2018,
                "chipset": "Snapdragon 450 (14nm)", "cpu_architecture": "Octa-core 1.8GHz Cortex-A53",
                "gpu": "Adreno 506", "antutu_benchmark_score": 76000,
                "display_type": "IPS LCD 19:9 FullView Display", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2280 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "16 MP, f/2.0 + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "24 MP, f/2.0, AI Face Beauty", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 3260, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 150, "os_at_launch": "Android 8.1 (Oreo), Funtouch 4.0",
                "variants": [
                    {"variant_name": "Vivo V9 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 3999000, "aliases": "vivo v9, v9 64gb"}
                ]
            },
            {
                "name": "Vivo V7+", "series": "24MP Moonlight Selfie 18:9 Pioneer", "release_year": 2017,
                "chipset": "Snapdragon 450 (14nm)", "cpu_architecture": "Octa-core 1.8GHz Cortex-A53",
                "gpu": "Adreno 506", "antutu_benchmark_score": 72000,
                "display_type": "IPS LCD FullView Display 18:9", "screen_size_inch": 5.99,
                "refresh_rate_hz": 60, "resolution": "720 x 1440 pixels (HD+)", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "16 MP, f/2.0, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "24 MP, f/2.0, Moonlight Glow LED", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3225, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 160, "os_at_launch": "Android 7.1.2 (Nougat), Funtouch 3.2",
                "variants": [
                    {"variant_name": "Vivo V7+ 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 4699000, "aliases": "vivo v7 plus, v7+ 64"}
                ]
            },
            {
                "name": "Vivo Y27 5G", "series": "Y-Series 44W FlashCharge Sunlight Display", "release_year": 2023,
                "chipset": "MediaTek Dimensity 6020 (7nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 380000,
                "display_type": "IPS LCD, 600 nits FHD+", "screen_size_inch": 6.64,
                "refresh_rate_hz": 60, "resolution": "1080 x 2388 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "50 MP, f/1.8 + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 44, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 190, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "Vivo Y27 5G 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2999000, "aliases": "y27 5g, vivo y27 5g"}
                ]
            },
            {
                "name": "Vivo Y36 5G", "series": "Y-Series Dynamic Design 5G Value", "release_year": 2023,
                "chipset": "MediaTek Dimensity 6020 (7nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 390000,
                "display_type": "IPS LCD, 90Hz, 650 nits", "screen_size_inch": 6.64,
                "refresh_rate_hz": 90, "resolution": "1080 x 2388 pixels", "peak_brightness_nits": 650,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.8 + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 44, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 190, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "Vivo Y36 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3999000, "aliases": "y36 5g, vivo y36 5g"}
                ]
            },
            {
                "name": "Vivo Xshot", "series": "Extreme Hi-Fi & Camera Pioneer (f/1.8 OIS)", "release_year": 2014,
                "chipset": "Snapdragon 801 (28nm)", "cpu_architecture": "Quad-core 2.5GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 42000,
                "display_type": "IPS LCD Full HD, Dual-stage Shutter Button", "screen_size_inch": 5.2,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP (Sony IMX214, f/1.8, OIS, dual-tone flash)",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.4, front LED flash", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 2600, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 148, "os_at_launch": "Android 4.3 (Jelly Bean), Funtouch OS",
                "variants": [
                    {"variant_name": "Vivo Xshot 2GB/16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 4999000, "aliases": "vivo xshot 16, xshot elite"},
                    {"variant_name": "Vivo Xshot 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 5999000, "aliases": "vivo xshot 32, xshot ultimate"}
                ]
            }
        ]
    },

    # ==================== 6. IQOO BATCH 5 ====================
    {
        "brand_name": "iQOO",
        "models": [
            {
                "name": "iQOO Z9x 5G", "series": "Z-Series 6000mAh Value Gaming", "release_year": 2024,
                "chipset": "Snapdragon 6 Gen 1 (4nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 710", "antutu_benchmark_score": 510000,
                "display_type": "IPS LCD, 120Hz, 1000 nits peak, Stereo Speakers 300%", "screen_size_inch": 6.72,
                "refresh_rate_hz": 120, "resolution": "1080 x 2408 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.8, PDAF + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.1", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 44, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP64", "weight_grams": 199, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "iQOO Z9x 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 2999000, "aliases": "z9x 128, iqoo z9x"},
                    {"variant_name": "iQOO Z9x 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3299000, "aliases": "z9x 256, iqoo z9x 256"}
                ]
            },
            {
                "name": "iQOO Z7x 5G", "series": "Z-Series 6000mAh 80W Battery Beast", "release_year": 2023,
                "chipset": "Snapdragon 695 5G (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 619", "antutu_benchmark_score": 410000,
                "display_type": "IPS LCD, 120Hz, 5-layer liquid cooling", "screen_size_inch": 6.64,
                "refresh_rate_hz": 120, "resolution": "1080 x 2388 pixels", "peak_brightness_nits": 480,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.8 + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 205, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "iQOO Z7x 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3299000, "aliases": "z7x 128, iqoo z7x"},
                    {"variant_name": "iQOO Z7x 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3699000, "aliases": "z7x 256, iqoo z7x 256"}
                ]
            },
            {
                "name": "iQOO Neo 9 Pro", "series": "Neo Dual-Chip Flagship Killer", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 2 (4nm) + Q1 Supercomputing Chip", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1650000,
                "display_type": "LTPO AMOLED, 1B colors, 144Hz, HDR10+, 3000 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 3000,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (Sony IMX920 VCS, OIS) + 8 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5160, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 190, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "iQOO Neo 9 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 7499000, "aliases": "neo 9 pro, iqoo neo 9 pro"},
                    {"variant_name": "iQOO Neo 9 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 8499000, "aliases": "neo 9 pro 512"}
                ]
            }
        ]
    },

    # ==================== 7. REALME BATCH 5 ====================
    {
        "brand_name": "Realme",
        "models": [
            {
                "name": "Realme 12+ 5G", "series": "Luxury Watch Design Sony LYT-600 OIS", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7050 (6nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 580000,
                "display_type": "AMOLED, 120Hz, HDR10+, 2000 nits peak, Rainwater Smart Touch", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Double-Reinforced Glass",
                "main_camera_mp": "50 MP (Sony LYT-600, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x In-Sensor",
                "selfie_camera_mp": "16 MP, f/2.45", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 190, "os_at_launch": "Android 14, Realme UI 5.0",
                "variants": [
                    {"variant_name": "Realme 12+ 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4199000, "aliases": "realme 12 plus, realme 12+ 5g"},
                    {"variant_name": "Realme 12+ 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 4999000, "aliases": "realme 12+ 512"}
                ]
            },
            {
                "name": "Realme 10 Pro+ 5G", "series": "120Hz Curved AMOLED 108MP ProLight", "release_year": 2023,
                "chipset": "MediaTek Dimensity 920 5G (6nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 510000,
                "display_type": "61-degree Curved AMOLED, 1B colors, 120Hz, 800 nits, 2160Hz PWM", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Double-Reinforced Glass",
                "main_camera_mp": "108 MP (Samsung HM6, f/1.75) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "16 MP, f/2.45", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 173, "os_at_launch": "Android 13, Realme UI 4.0",
                "variants": [
                    {"variant_name": "Realme 10 Pro+ 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5999000, "aliases": "realme 10 pro plus 128, 10 pro+ 5g"},
                    {"variant_name": "Realme 10 Pro+ 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 6999000, "aliases": "realme 10 pro plus 256"}
                ]
            },
            {
                "name": "Realme 8 Pro", "series": "108MP Infinite Starry Camera", "release_year": 2021,
                "chipset": "Snapdragon 720G (8nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 465",
                "gpu": "Adreno 618", "antutu_benchmark_score": 330000,
                "display_type": "Super AMOLED, 1000 nits peak", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Glass",
                "main_camera_mp": "108 MP (Samsung HM2, f/1.88) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "3x Ultra-zoom",
                "selfie_camera_mp": "16 MP (Sony IMX471), f/2.45", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 50, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 176, "os_at_launch": "Android 11, Realme UI 2.0",
                "variants": [
                    {"variant_name": "Realme 8 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4499000, "aliases": "realme 8 pro, 8 pro 128"}
                ]
            },
            {
                "name": "Realme 7 Pro", "series": "65W SuperDart Mirror Design", "release_year": 2020,
                "chipset": "Snapdragon 720G (8nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 465",
                "gpu": "Adreno 618", "antutu_benchmark_score": 325000,
                "display_type": "Super AMOLED, 600 nits", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 3+",
                "main_camera_mp": "64 MP (Sony IMX682, f/1.8) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "Water-repellent coating", "weight_grams": 182, "os_at_launch": "Android 10, Realme UI 1.0",
                "variants": [
                    {"variant_name": "Realme 7 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "realme 7 pro, 7 pro 128"}
                ]
            },
            {
                "name": "Realme XT", "series": "World First 64MP Quad Camera Pioneer", "release_year": 2019,
                "chipset": "Snapdragon 712 (10nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 360",
                "gpu": "Adreno 616", "antutu_benchmark_score": 220000,
                "display_type": "Super AMOLED Dewdrop Full HD+", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (Samsung GW1, f/1.8) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP (Sony IMX471), f/2.0", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 183, "os_at_launch": "Android 9.0 (Pie), ColorOS 6",
                "variants": [
                    {"variant_name": "Realme XT 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4499000, "aliases": "realme xt, xt 128"}
                ]
            },
            {
                "name": "Realme C67", "series": "108MP 3x In-Sensor Champion Snapdragon", "release_year": 2023,
                "chipset": "Snapdragon 685 (6nm)", "cpu_architecture": "Octa-core 2.8GHz Kryo 265",
                "gpu": "Adreno 610", "antutu_benchmark_score": 330000,
                "display_type": "IPS LCD, 90Hz, 950 nits peak, Mini Capsule 2.0", "screen_size_inch": 6.72,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "108 MP (Samsung HM6, 3x lossless zoom) + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "8 MP, f/2.05", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 185, "os_at_launch": "Android 14, Realme UI",
                "variants": [
                    {"variant_name": "Realme C67 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 2599000, "aliases": "realme c67 128, c67 128gb"},
                    {"variant_name": "Realme C67 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2999000, "aliases": "realme c67 256, c67 256gb"}
                ]
            },
            {
                "name": "Realme C53", "series": "C-Series 33W Champion Ultra Slim", "release_year": 2023,
                "chipset": "Unisoc Tiger T612 (12nm)", "cpu_architecture": "Octa-core 1.8GHz",
                "gpu": "Mali-G57", "antutu_benchmark_score": 250000,
                "display_type": "IPS LCD, 90Hz, 560 nits, Mini Capsule", "screen_size_inch": 6.74,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 560,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.8 + 0.08 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 182, "os_at_launch": "Android 13, Realme UI T Edition",
                "variants": [
                    {"variant_name": "Realme C53 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2099000, "aliases": "realme c53 128, c53 128gb"},
                    {"variant_name": "Realme C53 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2399000, "aliases": "realme c53 256, c53 256gb"}
                ]
            },
            {
                "name": "Realme GT 2 Pro", "series": "Paper Tech 2K LTPO2 AMOLED Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1020000,
                "display_type": "LTPO2 AMOLED, 1B colors, 120Hz, 2K WQHD+, HDR10+, 1400 nits", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1440 x 3216 pixels (2K)", "peak_brightness_nits": 1400,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766, OIS) + 50 MP (150 deg fisheye ultrawide) + 3 MP (40x microscope lens)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP (Sony IMX615), f/2.4", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 189, "os_at_launch": "Android 12, Realme UI 3.0",
                "variants": [
                    {"variant_name": "Realme GT 2 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "gt 2 pro, realme gt 2 pro"}
                ]
            },
            {
                "name": "Realme 2 Pro", "series": "Debut Dewdrop Snapdragon 660 Benchmark", "release_year": 2018,
                "chipset": "Snapdragon 660 AIE (14nm)", "cpu_architecture": "Octa-core 2.0GHz Kryo 260",
                "gpu": "Adreno 512", "antutu_benchmark_score": 140000,
                "display_type": "IPS LCD Dewdrop Full HD+", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "16 MP (Sony IMX398, f/1.7) + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@30fps",
                "battery_capacity_mah": 3500, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 174, "os_at_launch": "Android 8.1 (Oreo), ColorOS 5.2",
                "variants": [
                    {"variant_name": "Realme 2 Pro 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2899000, "aliases": "realme 2 pro 64, r2 pro"},
                    {"variant_name": "Realme 2 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3699000, "aliases": "realme 2 pro 128, r2 pro 128"}
                ]
            }
        ]
    },

    # ==================== 8. INFINIX BATCH 5 ====================
    {
        "brand_name": "Infinix",
        "models": [
            {
                "name": "Infinix Note 40 Pro+ 5G", "series": "100W All-Round 2.0 Wireless MagCharge", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7020 (6nm) + Cheetah X1 Chip", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "IMG BXM-8-256", "antutu_benchmark_score": 470000,
                "display_type": "Curved AMOLED, 1B colors, 120Hz, 1300 nits peak, Active Halo Light", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (f/1.75, OIS, 3x lossless zoom) + 2 MP + 2 MP",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "32 MP, f/2.2, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@60fps",
                "battery_capacity_mah": 4600, "fast_charging_watt": 100, "has_wireless_charging": True, "wireless_charging_watt": 20,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 190, "os_at_launch": "Android 14, XOS 14",
                "variants": [
                    {"variant_name": "Infinix Note 40 Pro+ 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 4499000, "aliases": "note 40 pro plus, infinix note 40 pro+"}
                ]
            },
            {
                "name": "Infinix Note 40 4G", "series": "AMOLED 120Hz Wireless MagCharge 20W", "release_year": 2024,
                "chipset": "MediaTek Helio G99 Ultimate (6nm) + Cheetah X1 Chip", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 425000,
                "display_type": "AMOLED, 120Hz, 1300 nits peak, Active Halo Lighting", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "108 MP, f/1.9 + 2 MP + 0.08 MP",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "1440p@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 20,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 190, "os_at_launch": "Android 14, XOS 14",
                "variants": [
                    {"variant_name": "Infinix Note 40 4G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2799000, "aliases": "note 40 4g, infinix note 40"}
                ]
            },
            {
                "name": "Infinix Note 30 4G", "series": "Note 45W FastCharge JBL Audio", "release_year": 2023,
                "chipset": "MediaTek Helio G99 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 415000,
                "display_type": "IPS LCD, 120Hz, 580 nits peak, Dual JBL Stereo", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 580,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "64 MP (OmniVision OV64B) + 2 MP + 0.08 MP",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0", "video_recording_max": "1440p@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 219, "os_at_launch": "Android 13, XOS 13",
                "variants": [
                    {"variant_name": "Infinix Note 30 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 2399000, "aliases": "note 30 128, infinix note 30"},
                    {"variant_name": "Infinix Note 30 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2599000, "aliases": "note 30 256, infinix note 30 256gb"}
                ]
            },
            {
                "name": "Infinix Hot 30", "series": "Hot Gaming 33W Fast Charge", "release_year": 2023,
                "chipset": "MediaTek Helio G88 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 MC2", "antutu_benchmark_score": 260000,
                "display_type": "IPS LCD, 90Hz, 600 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 90, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.6 + 0.08 MP",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 196, "os_at_launch": "Android 13, XOS 12.6",
                "variants": [
                    {"variant_name": "Infinix Hot 30 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 1899000, "aliases": "hot 30 128, infinix hot 30"}
                ]
            },
            {
                "name": "Infinix Hot 20 5G", "series": "Affordable 120Hz 5G Gaming", "release_year": 2022,
                "chipset": "MediaTek Dimensity 810 (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 390000,
                "display_type": "IPS LCD, 120Hz Full HD+", "screen_size_inch": 6.58,
                "refresh_rate_hz": 120, "resolution": "1080 x 2408 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.6 + QVGA",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, LED flash", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 204, "os_at_launch": "Android 12, XOS 10.6",
                "variants": [
                    {"variant_name": "Infinix Hot 20 5G 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 2499000, "aliases": "hot 20 5g, infinix hot 20 5g"}
                ]
            },
            {
                "name": "Infinix Smart 8", "series": "Magic Ring Budget Best Value", "release_year": 2023,
                "chipset": "Unisoc Tiger T606 (12nm)", "cpu_architecture": "Octa-core 1.6GHz",
                "gpu": "Mali-G57 MP1", "antutu_benchmark_score": 220000,
                "display_type": "IPS LCD, 90Hz, 500 nits, Magic Ring", "screen_size_inch": 6.6,
                "refresh_rate_hz": 90, "resolution": "720 x 1612 pixels (HD+)", "peak_brightness_nits": 500,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "13 MP, f/1.8 + 0.08 MP",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 184, "os_at_launch": "Android 13 (Go edition), XOS 13",
                "variants": [
                    {"variant_name": "Infinix Smart 8 3GB/64GB", "ram_gb": 3, "storage_gb": 64, "official_msrp_new": 1099000, "aliases": "smart 8 64, infinix smart 8"},
                    {"variant_name": "Infinix Smart 8 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 1249000, "aliases": "smart 8 128, infinix smart 8 128gb"}
                ]
            },
            {
                "name": "Infinix Zero 8", "series": "Gem Cut Dual Selfie 64MP Quad", "release_year": 2020,
                "chipset": "MediaTek Helio G90T (12nm)", "cpu_architecture": "Octa-core 2.05GHz",
                "gpu": "Mali-G76 MC4", "antutu_benchmark_score": 330000,
                "display_type": "IPS LCD, 90Hz Full HD+", "screen_size_inch": 6.85,
                "refresh_rate_hz": 90, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 480,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "64 MP (Sony IMX686) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "Dual: 48 MP (wide) + 8 MP (ultrawide)", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 205, "os_at_launch": "Android 10, XOS 7",
                "variants": [
                    {"variant_name": "Infinix Zero 8 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3799000, "aliases": "zero 8, infinix zero 8"}
                ]
            }
        ]
    },

    # ==================== 9. TECNO BATCH 5 ====================
    {
        "brand_name": "Tecno",
        "models": [
            {
                "name": "Tecno Camon 30 Pro 5G", "series": "Dual 50MP Sony OIS 144Hz AMOLED", "release_year": 2024,
                "chipset": "MediaTek Dimensity 8200 Ultimate (4nm)", "cpu_architecture": "Octa-core 3.1GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 930000,
                "display_type": "AMOLED, 144Hz, HDR, 1000 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX890, 1/1.56 inch, OIS) + 50 MP (ultrawide) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP, Eye-tracking AF, Dual-LED flash", "video_recording_max": "4K@60fps HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 70, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 189, "os_at_launch": "Android 14, HIOS 14",
                "variants": [
                    {"variant_name": "Tecno Camon 30 Pro 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "camon 30 pro 5g, tecno camon 30 pro"},
                    {"variant_name": "Tecno Camon 30 Pro 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 5999000, "aliases": "camon 30 pro 512"}
                ]
            },
            {
                "name": "Tecno Camon 30 5G", "series": "Camon 50MP OIS 70W FastCharge", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7020 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "IMG BXM-8-256", "antutu_benchmark_score": 480000,
                "display_type": "AMOLED, 120Hz, Always-on display", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP (wide, OIS) + 2 MP (depth) + 0.08 MP",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP, Eye-AF", "video_recording_max": "1440p@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 70, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 199, "os_at_launch": "Android 14, HIOS 14",
                "variants": [
                    {"variant_name": "Tecno Camon 30 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3799000, "aliases": "camon 30 5g, tecno camon 30"}
                ]
            },
            {
                "name": "Tecno Spark 20 Pro", "series": "108MP Flagship Sensor Helio G99", "release_year": 2023,
                "chipset": "MediaTek Helio G99 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 420000,
                "display_type": "IPS LCD, 120Hz Full HD+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "108 MP, f/1.75, 3x in-sensor zoom + 0.08 MP",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "32 MP, f/2.2, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 200, "os_at_launch": "Android 13, HIOS 13.5",
                "variants": [
                    {"variant_name": "Tecno Spark 20 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2099000, "aliases": "spark 20 pro, tecno spark 20 pro"}
                ]
            },
            {
                "name": "Tecno Spark 20", "series": "Magic Skin 50MP Stereo Speakers", "release_year": 2023,
                "chipset": "MediaTek Helio G85 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 MC2", "antutu_benchmark_score": 250000,
                "display_type": "IPS LCD, 90Hz, Dynamic Port", "screen_size_inch": 6.56,
                "refresh_rate_hz": 90, "resolution": "720 x 1612 pixels (HD+)", "peak_brightness_nits": 480,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.6 + 0.08 MP",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2, Dual-LED flash", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 190, "os_at_launch": "Android 13, HIOS 13",
                "variants": [
                    {"variant_name": "Tecno Spark 20 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 1749000, "aliases": "spark 20 128, tecno spark 20"},
                    {"variant_name": "Tecno Spark 20 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 1999000, "aliases": "spark 20 256, tecno spark 20 256gb"}
                ]
            },
            {
                "name": "Tecno Pova 4 Pro", "series": "6000mAh 90Hz AMOLED Gaming", "release_year": 2022,
                "chipset": "MediaTek Helio G99 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 400000,
                "display_type": "AMOLED, 90Hz Full HD+", "screen_size_inch": 6.66,
                "refresh_rate_hz": 90, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "50 MP, f/1.6, PDAF + 0.08 MP",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 212, "os_at_launch": "Android 12, HIOS 12",
                "variants": [
                    {"variant_name": "Tecno Pova 4 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 2899000, "aliases": "pova 4 pro 128, tecno pova 4 pro"},
                    {"variant_name": "Tecno Pova 4 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3199000, "aliases": "pova 4 pro 256, tecno pova 4 pro 256gb"}
                ]
            },
            {
                "name": "Tecno Phantom V Flip 5G", "series": "Clamshell Foldable Planet Cover Screen", "release_year": 2023,
                "chipset": "MediaTek Dimensity 8050 (6nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 750000,
                "display_type": "Foldable LTPO AMOLED, 120Hz, 1000 nits + 1.32 inch Circular Cover AMOLED", "screen_size_inch": 6.9,
                "refresh_rate_hz": 120, "resolution": "1080 x 2640 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Schott UTG (Ultra Thin Glass)",
                "main_camera_mp": "64 MP (RGBW, f/1.7) + 13 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5, Dual-LED flash", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 194, "os_at_launch": "Android 13, HIOS 13.5 Fold",
                "variants": [
                    {"variant_name": "Tecno Phantom V Flip 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 8999000, "aliases": "phantom v flip, tecno flip"}
                ]
            },
            {
                "name": "Tecno Phantom X2 Pro 5G", "series": "World First Retractable Portrait Lens", "release_year": 2022,
                "chipset": "MediaTek Dimensity 9000 (4nm)", "cpu_architecture": "Octa-core 3.05GHz",
                "gpu": "Mali-G710 MC10", "antutu_benchmark_score": 1010000,
                "display_type": "AMOLED, 120Hz, Curved Display, 500 nits", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, f/1.9) + 50 MP (motorized retractable 2.5x portrait lens, f/1.5) + 13 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "2.5x Optical Retractable",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@60fps, 1080p@60fps",
                "battery_capacity_mah": 5160, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 201, "os_at_launch": "Android 12, HIOS 12",
                "variants": [
                    {"variant_name": "Tecno Phantom X2 Pro 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "phantom x2 pro, tecno phantom x2 pro"}
                ]
            }
        ]
    },

    # ==================== 10. BLACKBERRY BATCH 5 ====================
    {
        "brand_name": "BlackBerry",
        "models": [
            {
                "name": "BlackBerry Curve 9300 (Kepler)", "series": "Curve 3G Mass Pioneer", "release_year": 2010,
                "chipset": "Marvell PXA930 (624MHz)", "cpu_architecture": "Single-core 624MHz",
                "gpu": "Integrated", "antutu_benchmark_score": 7500,
                "display_type": "TFT 65K Colors, Optical Trackpad", "screen_size_inch": 2.46,
                "refresh_rate_hz": 60, "resolution": "320 x 240 pixels (QVGA)", "peak_brightness_nits": 280,
                "screen_protection": "Standard Acrylic",
                "main_camera_mp": "2.0 MP, Video Recording",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "None", "video_recording_max": "320x240 pixels",
                "battery_capacity_mah": 1150, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSDPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 104, "os_at_launch": "BlackBerry OS 5.0 (Upgradable to OS 6)",
                "variants": [
                    {"variant_name": "BlackBerry Curve 9300 256MB", "ram_gb": 1, "storage_gb": 1, "official_msrp_new": 3499000, "aliases": "bb kepler, curve kepler, bb 9300"}
                ]
            },
            {
                "name": "BlackBerry Torch 9800", "series": "Slider Touch & QWERTY Hybrid", "release_year": 2010,
                "chipset": "Marvell 624MHz", "cpu_architecture": "Single-core 624MHz",
                "gpu": "Integrated", "antutu_benchmark_score": 9000,
                "display_type": "TFT Capacitive Touchscreen + Slide-out QWERTY Keyboard", "screen_size_inch": 3.2,
                "refresh_rate_hz": 60, "resolution": "360 x 480 pixels", "peak_brightness_nits": 300,
                "screen_protection": "Reinforced Plastic",
                "main_camera_mp": "5 MP, Autofocus, LED flash, image stabilization",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "None", "video_recording_max": "480p@30fps",
                "battery_capacity_mah": 1300, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSDPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 161, "os_at_launch": "BlackBerry OS 6.0",
                "variants": [
                    {"variant_name": "BlackBerry Torch 9800 4GB", "ram_gb": 1, "storage_gb": 4, "official_msrp_new": 6499000, "aliases": "bb torch, torch 9800, bb torch 1"}
                ]
            },
            {
                "name": "BlackBerry Q10", "series": "BB10 Super AMOLED Physical QWERTY", "release_year": 2013,
                "chipset": "Snapdragon S4 Plus MSM8960 (Dual-core 1.5GHz)", "cpu_architecture": "Dual-core 1.5GHz Krait",
                "gpu": "Adreno 225", "antutu_benchmark_score": 19000,
                "display_type": "Super AMOLED 1:1 Square Touchscreen, 328 ppi", "screen_size_inch": 3.1,
                "refresh_rate_hz": 60, "resolution": "720 x 720 pixels (1:1 Ratio)", "peak_brightness_nits": 400,
                "screen_protection": "Corning Glass",
                "main_camera_mp": "8 MP, f/2.2, Autofocus, LED flash",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP, 720p", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 2100, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 139, "os_at_launch": "BlackBerry 10 OS",
                "variants": [
                    {"variant_name": "BlackBerry Q10 2GB/16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 7499000, "aliases": "bb q10, blackberry q10 black"}
                ]
            },
            {
                "name": "BlackBerry KEYone", "series": "Smart Keyboard Android Spacebar Fingerprint", "release_year": 2017,
                "chipset": "Snapdragon 625 (14nm)", "cpu_architecture": "Octa-core 2.0GHz Cortex-A53",
                "gpu": "Adreno 506", "antutu_benchmark_score": 85000,
                "display_type": "IPS LCD 3:2 Aspect Ratio, Touch-sensitive physical keyboard", "screen_size_inch": 4.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1620 pixels (3:2 Ratio)", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "12 MP (Sony IMX378, 1/2.3 inch, f/2.0, PDAF)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.2", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 3505, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 180, "os_at_launch": "Android 7.1 (Nougat)",
                "variants": [
                    {"variant_name": "BlackBerry KEYone 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 7399000, "aliases": "bb keyone, blackberry keyone 32"},
                    {"variant_name": "BlackBerry KEYone 4GB/64GB (Black Edition)", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 8999000, "aliases": "keyone black edition, keyone 64"}
                ]
            }
        ]
    },

    # ==================== 11. NOKIA BATCH 5 ====================
    {
        "brand_name": "Nokia",
        "models": [
            {
                "name": "Nokia Lumia 920", "series": "World First Smartphone OIS PureMotion HD+", "release_year": 2012,
                "chipset": "Snapdragon S4 Plus MSM8960 (Dual-core 1.5GHz)", "cpu_architecture": "Dual-core 1.5GHz Krait",
                "gpu": "Adreno 225", "antutu_benchmark_score": 22000,
                "display_type": "IPS LCD PureMotion HD+ ClearBlack 60Hz", "screen_size_inch": 4.5,
                "refresh_rate_hz": 60, "resolution": "768 x 1280 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass 2",
                "main_camera_mp": "8.7 MP (Carl Zeiss optics, Optical Image Stabilization OIS, f/2.0)",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.3 MP, 720p@30fps", "video_recording_max": "1080p@30fps (Floating Lens OIS)",
                "battery_capacity_mah": 2000, "fast_charging_watt": 10, "has_wireless_charging": True, "wireless_charging_watt": 5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 185, "os_at_launch": "Microsoft Windows Phone 8",
                "variants": [
                    {"variant_name": "Nokia Lumia 920 1GB/32GB", "ram_gb": 1, "storage_gb": 32, "official_msrp_new": 6499000, "aliases": "lumia 920, nokia 920"}
                ]
            },
            {
                "name": "Nokia Lumia 720", "series": "Sleek Unibody f/1.9 Carl Zeiss", "release_year": 2013,
                "chipset": "Snapdragon S4 Plus MSM8227 (Dual-core 1.0GHz)", "cpu_architecture": "Dual-core 1.0GHz Krait",
                "gpu": "Adreno 305", "antutu_benchmark_score": 12000,
                "display_type": "IPS LCD ClearBlack Display, Super Sensitive Touch", "screen_size_inch": 4.3,
                "refresh_rate_hz": 60, "resolution": "480 x 800 pixels (WVGA)", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass 2",
                "main_camera_mp": "6.7 MP (Carl Zeiss optics, f/1.9 wide aperture, LED flash)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.3 MP, 720p", "video_recording_max": "720p@30fps",
                "battery_capacity_mah": 2000, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSDPA", "has_nfc": True, "ip_rating": "None", "weight_grams": 128, "os_at_launch": "Microsoft Windows Phone 8",
                "variants": [
                    {"variant_name": "Nokia Lumia 720 512MB/8GB", "ram_gb": 1, "storage_gb": 8, "official_msrp_new": 3499000, "aliases": "lumia 720, nokia 720"}
                ]
            },
            {
                "name": "Nokia 7 Plus", "series": "Aluminum 6000 Ceramic Feel Android One", "release_year": 2018,
                "chipset": "Snapdragon 660 (14nm)", "cpu_architecture": "Octa-core 2.2GHz Kryo 260",
                "gpu": "Adreno 512", "antutu_benchmark_score": 142000,
                "display_type": "IPS LCD 18:9 Full HD+, 500 nits", "screen_size_inch": 6.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 2160 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "Dual: 12 MP (Carl Zeiss, f/1.75, Dual Pixel) + 13 MP (Carl Zeiss 2x telephoto)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "16 MP (Carl Zeiss), f/2.0", "video_recording_max": "4K@30fps, OZO Spatial Audio",
                "battery_capacity_mah": 3800, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 183, "os_at_launch": "Android 8.1 (Oreo, Pure Android One)",
                "variants": [
                    {"variant_name": "Nokia 7 Plus 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 6999000, "aliases": "nokia 7 plus, n7 plus"}
                ]
            },
            {
                "name": "Nokia 8", "series": "Dual Zeiss Bothie OZO Audio Flagship", "release_year": 2017,
                "chipset": "Snapdragon 835 (10nm)", "cpu_architecture": "Octa-core 2.5GHz Kryo",
                "gpu": "Adreno 540", "antutu_benchmark_score": 215000,
                "display_type": "IPS LCD QHD, 700 nits peak, Always-on Glance", "screen_size_inch": 5.3,
                "refresh_rate_hz": 60, "resolution": "1440 x 2560 pixels (QHD)", "peak_brightness_nits": 700,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "Dual: 13 MP (Color, OIS, Zeiss) + 13 MP (Monochrome, Zeiss)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP (Carl Zeiss), f/2.0, PDAF", "video_recording_max": "4K@30fps Bothie Dual-Sight, OZO Audio",
                "battery_capacity_mah": 3090, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 160, "os_at_launch": "Android 7.1.1 (Nougat, Pure Android)",
                "variants": [
                    {"variant_name": "Nokia 8 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 6499000, "aliases": "nokia 8, n8 zeiss 2017"},
                    {"variant_name": "Nokia 8 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 7499000, "aliases": "nokia 8 128, nokia 8 polished blue"}
                ]
            }
        ]
    },

    # ==================== 12. ASUS BATCH 5 ====================
    {
        "brand_name": "Asus",
        "models": [
            {
                "name": "ROG Phone 6D Ultimate", "series": "AeroActive Portal Dimensity 9000+", "release_year": 2022,
                "chipset": "MediaTek Dimensity 9000+ (4nm)", "cpu_architecture": "Octa-core 3.35GHz",
                "gpu": "Mali-G710 MC10", "antutu_benchmark_score": 1150000,
                "display_type": "AMOLED, 1B colors, 165Hz, HDR10+, 1200 nits peak + ROG Vision PMOLED Rear", "screen_size_inch": 6.78,
                "refresh_rate_hz": 165, "resolution": "1080 x 2448 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766, f/1.9) + 13 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IPX4", "weight_grams": 247, "os_at_launch": "Android 12, ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone 6D Ultimate 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 16999000, "aliases": "rog 6d ultimate, rog phone 6d"}
                ]
            },
            {
                "name": "ROG Phone II", "series": "120Hz 1ms AMOLED 6000mAh AirTrigger II", "release_year": 2019,
                "chipset": "Snapdragon 855+ (7nm)", "cpu_architecture": "Octa-core 2.96GHz Kryo 485",
                "gpu": "Adreno 640 (700MHz)", "antutu_benchmark_score": 510000,
                "display_type": "AMOLED, 120Hz 1ms, HDR10, 240Hz touch sampling, 600 nits", "screen_size_inch": 6.59,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "48 MP (Sony IMX586, f/1.8) + 13 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "24 MP, f/2.2", "video_recording_max": "4K@60fps, 1080p@240fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 30, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 240, "os_at_launch": "Android 9.0 (Pie), ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone II 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 8499000, "aliases": "rog phone 2 128, rog 2"},
                    {"variant_name": "ROG Phone II 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 12499000, "aliases": "rog phone 2 512, rog 2 ultimate"}
                ]
            },
            {
                "name": "Zenfone 5Z", "series": "Snapdragon 845 Flagship Killer Under 7 Juta", "release_year": 2018,
                "chipset": "Snapdragon 845 (10nm)", "cpu_architecture": "Octa-core 2.8GHz Kryo 385",
                "gpu": "Adreno 630", "antutu_benchmark_score": 340000,
                "display_type": "Super IPS+, DCI-P3 96%, 550 nits", "screen_size_inch": 6.2,
                "refresh_rate_hz": 60, "resolution": "1080 x 2246 pixels", "peak_brightness_nits": 550,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12 MP (Sony IMX363, f/1.8, 4-axis OIS) + 8 MP (120 deg ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "4K@60fps, 1080p@240fps",
                "battery_capacity_mah": 3300, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 165, "os_at_launch": "Android 8.0 (Oreo), ZenUI 5",
                "variants": [
                    {"variant_name": "Zenfone 5Z 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 6699000, "aliases": "zenfone 5z, asus 5z 128"},
                    {"variant_name": "Zenfone 5Z 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 7799000, "aliases": "zenfone 5z 256, asus 5z 256gb"}
                ]
            }
        ]
    },

    # ==================== 13. SONY BATCH 5 ====================
    {
        "brand_name": "Sony",
        "models": [
            {
                "name": "Sony Xperia 1 V", "series": "4K 120Hz Exmor T 2-Layer Transistor Sensor", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1550000,
                "display_type": "4K OLED, 1B colors, 120Hz, HDR BT.2020, 21:9 CinemaWide", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1644 x 3840 pixels (4K)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "48 MP (Exmor T, 1/1.35 inch, OIS, 24mm) + 12 MP (3.5x-5.2x continuous optical zoom OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5.2x Continuous Optical",
                "selfie_camera_mp": "12 MP, f/2.0", "video_recording_max": "4K@120fps HDR all rear lenses",
                "battery_capacity_mah": 5000, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 187, "os_at_launch": "Android 13",
                "variants": [
                    {"variant_name": "Sony Xperia 1 V 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 19999000, "aliases": "xperia 1 v, sony 1 v 256"},
                    {"variant_name": "Sony Xperia 1 V 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 22999000, "aliases": "xperia 1 v 512, sony 1 v 512gb"}
                ]
            },
            {
                "name": "Sony Xperia 5 V", "series": "Compact Exmor T High-End Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1530000,
                "display_type": "OLED, 1B colors, 120Hz, HDR BT.2020, 21:9 Aspect", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1080 x 2520 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "48 MP (Exmor T, 1/1.35 inch, OIS, 24mm/48mm 2x lossless) + 12 MP (16mm ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Lossless In-Sensor",
                "selfie_camera_mp": "12 MP, f/2.0", "video_recording_max": "4K@120fps HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 182, "os_at_launch": "Android 13",
                "variants": [
                    {"variant_name": "Sony Xperia 5 V 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 14999000, "aliases": "xperia 5 v, sony 5 v 128"},
                    {"variant_name": "Sony Xperia 5 V 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 16499000, "aliases": "xperia 5 v 256, sony 5 v 256gb"}
                ]
            },
            {
                "name": "Sony Xperia XZ Premium", "series": "World First 4K HDR & 960fps Motion Eye", "release_year": 2017,
                "chipset": "Snapdragon 835 (10nm)", "cpu_architecture": "Octa-core 2.45GHz Kryo",
                "gpu": "Adreno 540", "antutu_benchmark_score": 210000,
                "display_type": "4K HDR IPS LCD (807 ppi, Triluminos display, X-Reality Engine)", "screen_size_inch": 5.46,
                "refresh_rate_hz": 60, "resolution": "2160 x 3840 pixels (4K)", "peak_brightness_nits": 700,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "19 MP (1/2.3 inch Exmor RS with stacked DRAM, f/2.0, Predictive AF, 5-axis gyro EIS)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.0, 22mm wide", "video_recording_max": "4K@30fps, 720p@960fps super slow-motion",
                "battery_capacity_mah": 3230, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 195, "os_at_launch": "Android 7.1 (Nougat)",
                "variants": [
                    {"variant_name": "Sony Xperia XZ Premium 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 8999000, "aliases": "xz premium, sony xz premium"}
                ]
            }
        ]
    },

    # ==================== 14. GOOGLE BATCH 5 ====================
    {
        "brand_name": "Google",
        "models": [
            {
                "name": "Google Pixel 8 Pro", "series": "Super Actua LTPO 120Hz Thermometer Sensor", "release_year": 2023,
                "chipset": "Google Tensor G3 (4nm)", "cpu_architecture": "Nona-core (1x Cortex-X3 + 4x Cortex-A715 + 4x Cortex-A510)",
                "gpu": "Immortalis-G715s MC10", "antutu_benchmark_score": 1120000,
                "display_type": "LTPO OLED, 120Hz, HDR10+, 2400 nits peak Super Actua", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1344 x 2992 pixels", "peak_brightness_nits": 2400,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (5x telephoto OIS) + 48 MP (ultrawide, macro) + Object Thermometer",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope Optical",
                "selfie_camera_mp": "10.5 MP, f/2.2, PDAF", "video_recording_max": "4K@60fps 10-bit HDR, Video Boost",
                "battery_capacity_mah": 5050, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 213, "os_at_launch": "Android 14 (7 Years OS Support)",
                "variants": [
                    {"variant_name": "Google Pixel 8 Pro 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 14999000, "aliases": "pixel 8 pro 128, google pixel 8 pro"},
                    {"variant_name": "Google Pixel 8 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 16499000, "aliases": "pixel 8 pro 256, google pixel 8 pro 256gb"},
                    {"variant_name": "Google Pixel 8 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 18999000, "aliases": "pixel 8 pro 512"}
                ]
            },
            {
                "name": "Google Pixel 7 Pro", "series": "Tensor G2 5x Telephoto Visor Flagship", "release_year": 2022,
                "chipset": "Google Tensor G2 (5nm)", "cpu_architecture": "Octa-core 2.85GHz",
                "gpu": "Mali-G710 MP7", "antutu_benchmark_score": 850000,
                "display_type": "LTPO AMOLED, 120Hz, HDR10+, 1500 nits peak QHD+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1440 x 3120 pixels (QHD+)", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (5x telephoto OIS) + 12 MP (ultrawide, AF macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope Optical",
                "selfie_camera_mp": "10.8 MP, f/2.2, ultrawide", "video_recording_max": "4K@60fps 10-bit HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 23, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 212, "os_at_launch": "Android 13",
                "variants": [
                    {"variant_name": "Google Pixel 7 Pro 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 13499000, "aliases": "pixel 7 pro 128, google pixel 7 pro"},
                    {"variant_name": "Google Pixel 7 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 14999000, "aliases": "pixel 7 pro 256, google pixel 7 pro 256gb"}
                ]
            },
            {
                "name": "Google Pixel 4a", "series": "Compact Computational Photography Champion", "release_year": 2020,
                "chipset": "Snapdragon 730G (8nm)", "cpu_architecture": "Octa-core 2.2GHz Kryo 470",
                "gpu": "Adreno 618", "antutu_benchmark_score": 320000,
                "display_type": "OLED, HDR, Always-on display", "screen_size_inch": 5.81,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 700,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12.2 MP (Sony IMX363, f/1.7, Dual Pixel PDAF, OIS)",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 3140, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 143, "os_at_launch": "Android 10 (Upgradable to Android 13)",
                "variants": [
                    {"variant_name": "Google Pixel 4a 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 6999000, "aliases": "pixel 4a, google pixel 4a"}
                ]
            }
        ]
    },

    # ==================== 15. HUAWEI BATCH 5 ====================
    {
        "brand_name": "Huawei",
        "models": [
            {
                "name": "Huawei Mate 50 Pro", "series": "Ultra Aperture XMAGE 10-Speed Physical Variable Aperture", "release_year": 2022,
                "chipset": "Snapdragon 8+ Gen 1 4G (4nm)", "cpu_architecture": "Octa-core 3.19GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1080000,
                "display_type": "OLED, 1B colors, 120Hz, HDR, 1440Hz PWM", "screen_size_inch": 6.74,
                "refresh_rate_hz": 120, "resolution": "1212 x 2616 pixels (1.5K)", "peak_brightness_nits": 1000,
                "screen_protection": "Huawei Kunlun Glass",
                "main_camera_mp": "50 MP (Ultra Aperture f/1.4-f/4.0 10-speed physical variable aperture, OIS, RYYB) + 64 MP (3.5x periscope telephoto OIS) + 13 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3.5x Periscope Optical",
                "selfie_camera_mp": "13 MP (ultrawide) + 3D ToF depth sensor", "video_recording_max": "4K@60fps, 1080p@480fps",
                "battery_capacity_mah": 4700, "fast_charging_watt": 66, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 205, "os_at_launch": "EMUI 13",
                "variants": [
                    {"variant_name": "Huawei Mate 50 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 14999000, "aliases": "mate 50 pro, huawei mate 50 pro"},
                    {"variant_name": "Huawei Mate 50 Pro 8GB/512GB (Orange Kunlun)", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 16999000, "aliases": "mate 50 pro kunlun, mate 50 pro 512"}
                ]
            },
            {
                "name": "Huawei Nova 5T", "series": "Kirin 980 Flagship Killer Under 7 Juta", "release_year": 2019,
                "chipset": "Kirin 980 (7nm, Dual-NPU)", "cpu_architecture": "Octa-core 2.6GHz (2x Cortex-A76 + 2x Cortex-A76 + 4x Cortex-A55)",
                "gpu": "Mali-G76 MP10", "antutu_benchmark_score": 380000,
                "display_type": "IPS LCD Punch-hole Full HD+", "screen_size_inch": 6.26,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Glass",
                "main_camera_mp": "48 MP (Sony IMX586, f/1.8) + 16 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@60fps gyro-EIS",
                "battery_capacity_mah": 3750, "fast_charging_watt": 22, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 174, "os_at_launch": "Android 9.0 (Pie), EMUI 9.1 (with Google Services)",
                "variants": [
                    {"variant_name": "Huawei Nova 5T 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 6899000, "aliases": "nova 5t, huawei nova 5t"}
                ]
            },
            {
                "name": "Huawei Mate 30 Pro", "series": "88-Degree Horizon OLED Dual 40MP Cine Camera", "release_year": 2019,
                "chipset": "Kirin 990 (7nm)", "cpu_architecture": "Octa-core 2.86GHz (2x Cortex-A76 + 2x Cortex-A76 + 4x Cortex-A55)",
                "gpu": "Mali-G76 MP16", "antutu_benchmark_score": 480000,
                "display_type": "OLED, 88-degree Horizon Curved Display, HDR10, DCI-P3", "screen_size_inch": 6.53,
                "refresh_rate_hz": 60, "resolution": "1176 x 2400 pixels", "peak_brightness_nits": 650,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "40 MP (SuperSensing f/1.6, OIS, RYYB) + 40 MP (Cine Camera f/1.8, 1/1.54 inch ultrawide) + 8 MP (3x telephoto OIS) + 3D ToF",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "32 MP, f/2.0 + 3D ToF depth/gesture camera", "video_recording_max": "4K@60fps, 7680fps ultra slow-motion, 4K HDR time-lapse",
                "battery_capacity_mah": 4500, "fast_charging_watt": 40, "has_wireless_charging": True, "wireless_charging_watt": 27,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 198, "os_at_launch": "Android 10, EMUI 10",
                "variants": [
                    {"variant_name": "Huawei Mate 30 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 12499000, "aliases": "mate 30 pro, huawei mate 30 pro"}
                ]
            }
        ]
    }
]
