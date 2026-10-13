"""
Batch 4 Master Catalog Smartphone Pasar Indonesia (2010 - 2026).
Ekspansi komprehensif 53 model smartphone dengan volume peredaran dan nilai historis tinggi di Indonesia:
- BlackBerry (Bold 9900 Dakota, Bold 9700 Onyx, Curve 8520 Gemini, Z10, Passport)
- Nokia (808 PureView, Lumia 1020, Lumia 520, Nokia 6, Nokia N8)
- Tecno (Pova 6 Pro 5G, Camon 30 Premier 5G, Spark 20 Pro+, Pova 5 Pro 5G, Camon 20 Pro 5G)
- Infinix (Zero 30 5G, Hot 40 Pro, Note 12 G96, Hot 11S, Zero 5G)
- Realme (11 Pro+ 5G, C55, 6 Pro, 3 Pro, C3)
- Xiaomi / Poco / Redmi (Poco X3 NFC, Poco F5 Pro, Redmi Note 11 Pro 5G, Redmi Note 5 Whyred, Redmi 9)
- Vivo (Vivo V30 5G, Vivo Y100 5G, Vivo X70 Pro, Vivo V20, Vivo Y20s)
- iQOO (iQOO Z9 5G, iQOO Neo 7 Pro 5G, iQOO 9 Pro)
- Oppo (Oppo Reno 7 5G, Oppo A78 4G, Oppo Find X, Oppo F7, Oppo F5)
- Samsung (Galaxy A35 5G, Galaxy A15 5G, Galaxy S21 FE 5G, Galaxy Note 4, Galaxy S7)
- Google Pixel / Sony / Asus (Google Pixel 7, Google Pixel 6, Sony Xperia Z5, Sony Xperia Z3, Asus ROG Phone 7)
"""

EXTENDED_CATALOG_MODELS_BATCH4 = [
    # ==================== 1. BLACKBERRY (INDONESIA ERA 2010 - 2015) ====================
    {
        "brand_name": "BlackBerry",
        "models": [
            {
                "name": "BlackBerry Bold 9900 (Dakota)", "series": "Bold Touch Flagship", "release_year": 2011,
                "chipset": "Qualcomm Snapdragon S2 MSM8655 (1.2GHz)", "cpu_architecture": "Single-core 1.2GHz Scorpion",
                "gpu": "Adreno 205", "antutu_benchmark_score": 12000,
                "display_type": "TFT Capacitive Touchscreen (Liquid Graphics)", "screen_size_inch": 2.8,
                "refresh_rate_hz": 60, "resolution": "640 x 480 pixels (VGA)", "peak_brightness_nits": 350,
                "screen_protection": "Corning Glass",
                "main_camera_mp": "5 MP, EDoF, LED Flash",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "None", "video_recording_max": "720p@30fps",
                "battery_capacity_mah": 1230, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA+", "has_nfc": True, "ip_rating": "None", "weight_grams": 130, "os_at_launch": "BlackBerry OS 7.0",
                "variants": [
                    {"variant_name": "BlackBerry Bold 9900 8GB", "ram_gb": 1, "storage_gb": 8, "official_msrp_new": 5999000, "aliases": "bb dakota, bold dakota, bold 9900"}
                ]
            },
            {
                "name": "BlackBerry Bold 9700 (Onyx)", "series": "Bold Classic", "release_year": 2010,
                "chipset": "Marvell PXA930 (624MHz)", "cpu_architecture": "Single-core 624MHz",
                "gpu": "Integrated", "antutu_benchmark_score": 8000,
                "display_type": "TFT 65K Colors, Optical Trackpad", "screen_size_inch": 2.44,
                "refresh_rate_hz": 60, "resolution": "480 x 360 pixels", "peak_brightness_nits": 300,
                "screen_protection": "Standard Acrylic",
                "main_camera_mp": "3.15 MP, Autofocus, LED Flash",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "None", "video_recording_max": "480p@30fps",
                "battery_capacity_mah": 1500, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSDPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 122, "os_at_launch": "BlackBerry OS 5.0 (Upgradable to OS 6)",
                "variants": [
                    {"variant_name": "BlackBerry Bold 9700 256MB", "ram_gb": 1, "storage_gb": 1, "official_msrp_new": 5499000, "aliases": "bb onyx, bold onyx, bb 9700"}
                ]
            },
            {
                "name": "BlackBerry Curve 8520 (Gemini)", "series": "Curve Mass Market", "release_year": 2010,
                "chipset": "Marvell PXA930 (512MHz)", "cpu_architecture": "Single-core 512MHz",
                "gpu": "Integrated", "antutu_benchmark_score": 5000,
                "display_type": "TFT 65K Colors, Optical Trackpad", "screen_size_inch": 2.46,
                "refresh_rate_hz": 60, "resolution": "320 x 240 pixels (QVGA)", "peak_brightness_nits": 280,
                "screen_protection": "Standard Acrylic",
                "main_camera_mp": "2.0 MP, Video Recording",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "None", "video_recording_max": "320x240 pixels",
                "battery_capacity_mah": 1150, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "2G EDGE", "has_nfc": False, "ip_rating": "None", "weight_grams": 106, "os_at_launch": "BlackBerry OS 4.6 (Upgradable to OS 5)",
                "variants": [
                    {"variant_name": "BlackBerry Curve 8520 256MB", "ram_gb": 1, "storage_gb": 1, "official_msrp_new": 3299000, "aliases": "bb gemini, curve gemini, bb 8520"}
                ]
            },
            {
                "name": "BlackBerry Z10", "series": "BlackBerry 10 Touchscreen", "release_year": 2013,
                "chipset": "Qualcomm Snapdragon S4 Plus MSM8960 (Dual-core 1.5GHz)", "cpu_architecture": "Dual-core 1.5GHz Krait",
                "gpu": "Adreno 225", "antutu_benchmark_score": 18000,
                "display_type": "Capacitive Touchscreen, 355 ppi", "screen_size_inch": 4.2,
                "refresh_rate_hz": 60, "resolution": "768 x 1280 pixels", "peak_brightness_nits": 400,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "8 MP, f/2.2, Autofocus, LED Flash",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP, 720p@30fps", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 1800, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 137, "os_at_launch": "BlackBerry 10 OS",
                "variants": [
                    {"variant_name": "BlackBerry Z10 2GB/16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 6999000, "aliases": "bb z10, blackberry z10 lte"}
                ]
            },
            {
                "name": "BlackBerry Passport", "series": "Passport Square Innovation", "release_year": 2014,
                "chipset": "Snapdragon 801 (Quad-core 2.26GHz)", "cpu_architecture": "Quad-core 2.26GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 42000,
                "display_type": "IPS LCD Square Display, 453 ppi", "screen_size_inch": 4.5,
                "refresh_rate_hz": 60, "resolution": "1440 x 1440 pixels (1:1 Ratio)", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP, f/2.0, OIS, LED Flash",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP, f/2.8", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 3450, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 196, "os_at_launch": "BlackBerry OS 10.3",
                "variants": [
                    {"variant_name": "BlackBerry Passport 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 9599000, "aliases": "bb passport, blackberry passport black"}
                ]
            }
        ]
    },

    # ==================== 2. NOKIA (INDONESIA ERA 2010 - 2020) ====================
    {
        "brand_name": "Nokia",
        "models": [
            {
                "name": "Nokia 808 PureView", "series": "PureView Imaging Pioneer", "release_year": 2012,
                "chipset": "ARM 11 1.3GHz + Broadcom BCM2763 GPU", "cpu_architecture": "Single-core 1.3GHz ARM11",
                "gpu": "Broadcom BCM2763", "antutu_benchmark_score": 15000,
                "display_type": "AMOLED, Nokia ClearBlack Display", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "360 x 640 pixels (16:9 nHD)", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "41 MP (1/1.2 inch Carl Zeiss optics, Xenon Flash)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "3x Lossless Digital",
                "selfie_camera_mp": "0.3 MP (VGA)", "video_recording_max": "1080p@30fps (Rich Recording)",
                "battery_capacity_mah": 1400, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA", "has_nfc": True, "ip_rating": "None", "weight_grams": 169, "os_at_launch": "Nokia Belle OS",
                "variants": [
                    {"variant_name": "Nokia 808 PureView 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 6999000, "aliases": "nokia 808, 808 pureview"}
                ]
            },
            {
                "name": "Nokia Lumia 1020", "series": "PureView Windows Phone", "release_year": 2013,
                "chipset": "Snapdragon S4 Plus MSM8960 (Dual-core 1.5GHz)", "cpu_architecture": "Dual-core 1.5GHz Krait",
                "gpu": "Adreno 225", "antutu_benchmark_score": 21000,
                "display_type": "AMOLED PureMotion HD+ ClearBlack", "screen_size_inch": 4.5,
                "refresh_rate_hz": 60, "resolution": "768 x 1280 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "41 MP (1/1.5 inch Carl Zeiss optics, OIS, Xenon flash)",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "3x Lossless High-Res",
                "selfie_camera_mp": "1.2 MP, 720p", "video_recording_max": "1080p@30fps Rich Recording",
                "battery_capacity_mah": 2000, "fast_charging_watt": 10, "has_wireless_charging": True, "wireless_charging_watt": 5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 158, "os_at_launch": "Microsoft Windows Phone 8",
                "variants": [
                    {"variant_name": "Nokia Lumia 1020 2GB/32GB", "ram_gb": 2, "storage_gb": 32, "official_msrp_new": 7999000, "aliases": "lumia 1020, nokia 1020, lumia 41mp"}
                ]
            },
            {
                "name": "Nokia Lumia 520", "series": "Lumia Affordable Best-Seller", "release_year": 2013,
                "chipset": "Snapdragon S4 Plus MSM8227 (Dual-core 1.0GHz)", "cpu_architecture": "Dual-core 1.0GHz Krait",
                "gpu": "Adreno 305", "antutu_benchmark_score": 11000,
                "display_type": "IPS LCD, Super Sensitive Touch", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "480 x 800 pixels (WVGA)", "peak_brightness_nits": 350,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "5 MP, f/2.4, Autofocus",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "None", "video_recording_max": "720p@30fps",
                "battery_capacity_mah": 1430, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSDPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 124, "os_at_launch": "Microsoft Windows Phone 8",
                "variants": [
                    {"variant_name": "Nokia Lumia 520 512MB/8GB", "ram_gb": 1, "storage_gb": 8, "official_msrp_new": 1999000, "aliases": "lumia 520, nokia 520"}
                ]
            },
            {
                "name": "Nokia 6", "series": "Android Rebirth Aluminum Unibody", "release_year": 2017,
                "chipset": "Snapdragon 430 (28nm)", "cpu_architecture": "Octa-core 1.4GHz Cortex-A53",
                "gpu": "Adreno 505", "antutu_benchmark_score": 58000,
                "display_type": "IPS LCD Full HD (2.5D curved glass)", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "16 MP, f/2.0, PDAF, Dual-LED flash",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 169, "os_at_launch": "Android 7.1.1 (Nougat, Pure Stock)",
                "variants": [
                    {"variant_name": "Nokia 6 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 3299000, "aliases": "nokia 6 2017, nokia 6 android"}
                ]
            },
            {
                "name": "Nokia N8", "series": "N-Series Flagship Camera", "release_year": 2010,
                "chipset": "ARM 11 680MHz + Broadcom BCM2727 GPU", "cpu_architecture": "Single-core 680MHz ARM11",
                "gpu": "Broadcom BCM2727", "antutu_benchmark_score": 9000,
                "display_type": "AMOLED capacitive touchscreen", "screen_size_inch": 3.5,
                "refresh_rate_hz": 60, "resolution": "360 x 640 pixels (16:9 nHD)", "peak_brightness_nits": 350,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "12 MP (1/1.83 inch Carl Zeiss optics, Xenon Flash, ND filter)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "0.3 MP (VGA)", "video_recording_max": "720p@25fps (Stereo Dolby Digital Plus)",
                "battery_capacity_mah": 1200, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSDPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 135, "os_at_launch": "Symbian^3 (Upgradable to Symbian Belle)",
                "variants": [
                    {"variant_name": "Nokia N8 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 4999000, "aliases": "nokia n8, n8 carl zeiss"}
                ]
            }
        ]
    },

    # ==================== 3. TECNO (INDONESIA ERA 2022 - 2024) ====================
    {
        "brand_name": "Tecno",
        "models": [
            {
                "name": "Tecno Pova 6 Pro 5G", "series": "Pova Gaming Mecha", "release_year": 2024,
                "chipset": "MediaTek Dimensity 6080 (6nm)", "cpu_architecture": "Octa-core 2.4GHz (2x Cortex-A76 + 6x Cortex-A55)",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 435000,
                "display_type": "AMOLED, 120Hz, 1300 nits, Dynamic Light Effect", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "108 MP (wide) + 2 MP (depth) + 0.08 MP (auxiliary)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "32 MP, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 70, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 198, "os_at_launch": "Android 14, HIOS 14",
                "variants": [
                    {"variant_name": "Tecno Pova 6 Pro 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 3299000, "aliases": "pova 6 pro, tecno pova 6 pro 5g"}
                ]
            },
            {
                "name": "Tecno Camon 30 Premier 5G", "series": "Camon Imaging Flagship", "release_year": 2024,
                "chipset": "MediaTek Dimensity 8200 Ultimate (4nm) + Sony Imaging Chip CXD5622GG", "cpu_architecture": "Octa-core 3.1GHz (1x Cortex-A78 + 3x Cortex-A78 + 4x Cortex-A55)",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 920000,
                "display_type": "LTPO AMOLED, 1B colors, 120Hz, HDR", "screen_size_inch": 6.77,
                "refresh_rate_hz": 120, "resolution": "1264 x 2780 pixels (1.5K)", "peak_brightness_nits": 1400,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX890, OIS) + 50 MP (3x periscope telephoto) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "50 MP, Eye-AF", "video_recording_max": "4K@60fps HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 70, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 210, "os_at_launch": "Android 14, HIOS 14",
                "variants": [
                    {"variant_name": "Tecno Camon 30 Premier 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 5999000, "aliases": "camon 30 premier, tecno camon 30 premier"}
                ]
            },
            {
                "name": "Tecno Spark 20 Pro+", "series": "Spark Curved Master", "release_year": 2024,
                "chipset": "MediaTek Helio G99 Ultimate (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 420000,
                "display_type": "Curved AMOLED, 120Hz, 1000 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP, f/1.75, 1/1.67 inch, 3x lossless zoom",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "32 MP, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 179, "os_at_launch": "Android 14, HIOS 14",
                "variants": [
                    {"variant_name": "Tecno Spark 20 Pro+ 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2699000, "aliases": "spark 20 pro plus, spark 20 pro+"}
                ]
            },
            {
                "name": "Tecno Pova 5 Pro 5G", "series": "Pova Cyber Mecha RGB", "release_year": 2023,
                "chipset": "MediaTek Dimensity 6080 (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 410000,
                "display_type": "IPS LCD, 120Hz, 580 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 580,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "50 MP, f/1.6, PDAF + 0.08 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 68, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 212, "os_at_launch": "Android 13, HIOS 13",
                "variants": [
                    {"variant_name": "Tecno Pova 5 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2999000, "aliases": "pova 5 pro, tecno pova 5 pro"}
                ]
            },
            {
                "name": "Tecno Camon 20 Pro 5G", "series": "Camon RGBW OIS", "release_year": 2023,
                "chipset": "MediaTek Dimensity 8050 (6nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 710000,
                "display_type": "AMOLED, 120Hz, Always-on display", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Glass",
                "main_camera_mp": "64 MP (RGBW sensor, OIS) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5, Dual-LED flash", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 193, "os_at_launch": "Android 13, HIOS 13",
                "variants": [
                    {"variant_name": "Tecno Camon 20 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4299000, "aliases": "camon 20 pro 5g, tecno camon 20 pro"}
                ]
            }
        ]
    },

    # ==================== 4. INFINIX BATCH 4 ====================
    {
        "brand_name": "Infinix",
        "models": [
            {
                "name": "Infinix Zero 30 5G", "series": "Zero 4K60 Vlog", "release_year": 2023,
                "chipset": "MediaTek Dimensity 8020 (6nm)", "cpu_architecture": "Octa-core 2.6GHz (4x Cortex-A78 + 4x Cortex-A55)",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 700000,
                "display_type": "Curved AMOLED, 1B colors, 144Hz, HDR10", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (Samsung ISOCELL HM6, OIS) + 13 MP (ultrawide) + 2 MP",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP, PDAF, 4K@60fps", "video_recording_max": "4K@60fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 68, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 185, "os_at_launch": "Android 13, XOS 13",
                "variants": [
                    {"variant_name": "Infinix Zero 30 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 4299000, "aliases": "zero 30 5g, infinix zero 30 5g"}
                ]
            },
            {
                "name": "Infinix Hot 40 Pro", "series": "Hot Gaming Champion", "release_year": 2023,
                "chipset": "MediaTek Helio G99 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 420000,
                "display_type": "IPS LCD, 120Hz, Magic Ring", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "108 MP, f/1.8 + 2 MP (macro) + 0.08 MP (auxiliary)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 199, "os_at_launch": "Android 13, XOS 13.5",
                "variants": [
                    {"variant_name": "Infinix Hot 40 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2199000, "aliases": "hot 40 pro, infinix hot 40 pro"}
                ]
            },
            {
                "name": "Infinix Note 12 (G96)", "series": "Note AMOLED Performance", "release_year": 2022,
                "chipset": "MediaTek Helio G96 (12nm)", "cpu_architecture": "Octa-core 2.05GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 350000,
                "display_type": "AMOLED, 1000 nits peak, 100% DCI-P3", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "50 MP, f/1.6, PDAF + 2 MP (depth) + QVGA",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, Dual-LED flash", "video_recording_max": "1440p@30fps, 1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 185, "os_at_launch": "Android 12, XOS 10.6",
                "variants": [
                    {"variant_name": "Infinix Note 12 G96 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 2799000, "aliases": "note 12 g96, infinix note 12"}
                ]
            },
            {
                "name": "Infinix Hot 11S", "series": "Hot Fast Gaming", "release_year": 2021,
                "chipset": "MediaTek Helio G88 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 MC2", "antutu_benchmark_score": 240000,
                "display_type": "IPS LCD, 90Hz Full HD+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 90, "resolution": "1080 x 2480 pixels", "peak_brightness_nits": 500,
                "screen_protection": "NEG Dinorex T2X-1",
                "main_camera_mp": "50 MP, f/1.6, PDAF + 2 MP (depth) + AI lens",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, Dual-LED flash", "video_recording_max": "1440p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 205, "os_at_launch": "Android 11, XOS 7.6",
                "variants": [
                    {"variant_name": "Infinix Hot 11S 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2099000, "aliases": "hot 11s 64gb, infinix hot 11s"},
                    {"variant_name": "Infinix Hot 11S 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2399000, "aliases": "hot 11s 128gb"}
                ]
            },
            {
                "name": "Infinix Zero 5G", "series": "Zero First 5G", "release_year": 2022,
                "chipset": "MediaTek Dimensity 900 (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 485000,
                "display_type": "IPS LCD, 120Hz, 500 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2460 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "48 MP, f/1.8 + 13 MP (2x telephoto) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "16 MP, f/2.0, Dual-LED flash", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": False, "ip_rating": "None", "weight_grams": 199, "os_at_launch": "Android 11, XOS 10",
                "variants": [
                    {"variant_name": "Infinix Zero 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3599000, "aliases": "zero 5g, infinix zero 5g"}
                ]
            }
        ]
    },

    # ==================== 5. REALME BATCH 4 ====================
    {
        "brand_name": "Realme",
        "models": [
            {
                "name": "Realme 11 Pro+ 5G", "series": "Number Flagship Design", "release_year": 2023,
                "chipset": "MediaTek Dimensity 7050 (6nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 580000,
                "display_type": "Curved AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Double-Reinforced Glass",
                "main_camera_mp": "200 MP (Samsung ISOCELL HP3, OIS, SuperZoom) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "4x In-Sensor Lossless",
                "selfie_camera_mp": "32 MP (Sony IMX615), f/2.5", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 100, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 189, "os_at_launch": "Android 13, Realme UI 4.0",
                "variants": [
                    {"variant_name": "Realme 11 Pro+ 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 6599000, "aliases": "realme 11 pro plus, realme 11 pro+ 5g"}
                ]
            },
            {
                "name": "Realme C55", "series": "C-Series Champion Mini Capsule", "release_year": 2023,
                "chipset": "MediaTek Helio G88 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 MC2", "antutu_benchmark_score": 260000,
                "display_type": "IPS LCD, 90Hz, 680 nits peak", "screen_size_inch": 6.72,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 680,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "64 MP (OmniVision OV64B) + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 189, "os_at_launch": "Android 13, Realme UI 4.0",
                "variants": [
                    {"variant_name": "Realme C55 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 2499000, "aliases": "c55 128, realme c55 128gb"},
                    {"variant_name": "Realme C55 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2999000, "aliases": "c55 256, realme c55 256gb"}
                ]
            },
            {
                "name": "Realme 6 Pro", "series": "Number Pro 6-Camera Master", "release_year": 2020,
                "chipset": "Snapdragon 720G (8nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 465",
                "gpu": "Adreno 618", "antutu_benchmark_score": 330000,
                "display_type": "IPS LCD, 90Hz Smooth Display", "screen_size_inch": 6.6,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 480,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, Samsung GW1) + 12 MP (2x telephoto) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "16 MP (Sony IMX471) + 8 MP (105 deg ultrawide)", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 4300, "fast_charging_watt": 30, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "Splash-resistant", "weight_grams": 202, "os_at_launch": "Android 10, Realme UI 1.0",
                "variants": [
                    {"variant_name": "Realme 6 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4499000, "aliases": "realme 6 pro, 6 pro 128"}
                ]
            },
            {
                "name": "Realme 3 Pro", "series": "Speed Awakens", "release_year": 2019,
                "chipset": "Snapdragon 710 (10nm)", "cpu_architecture": "Octa-core 2.2GHz Kryo 360",
                "gpu": "Adreno 616", "antutu_benchmark_score": 215000,
                "display_type": "IPS LCD Dewdrop Full HD+", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "16 MP (Sony IMX519, f/1.7) + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "25 MP, f/2.0", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 4045, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 172, "os_at_launch": "Android 9.0 (Pie), ColorOS 6",
                "variants": [
                    {"variant_name": "Realme 3 Pro 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2999000, "aliases": "realme 3 pro 64, r3 pro"},
                    {"variant_name": "Realme 3 Pro 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 3699000, "aliases": "realme 3 pro 128"}
                ]
            },
            {
                "name": "Realme C3", "series": "Triple Camera Game Monster", "release_year": 2020,
                "chipset": "MediaTek Helio G70 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 2EEMC2", "antutu_benchmark_score": 190000,
                "display_type": "IPS LCD Mini-drop", "screen_size_inch": 6.5,
                "refresh_rate_hz": 60, "resolution": "720 x 1600 pixels (HD+)", "peak_brightness_nits": 480,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12 MP (f/1.8, PDAF) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.4", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "Splash-resistant", "weight_grams": 195, "os_at_launch": "Android 10, Realme UI 1.0",
                "variants": [
                    {"variant_name": "Realme C3 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 1699000, "aliases": "c3 32gb, realme c3 3gb"}
                ]
            }
        ]
    },

    # ==================== 6. XIAOMI / REDMI / POCO BATCH 4 ====================
    {
        "brand_name": "Xiaomi",
        "models": [
            {
                "name": "Poco X3 NFC", "series": "X-Series 120Hz Midrange Benchmark", "release_year": 2020,
                "chipset": "Snapdragon 732G (8nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 470",
                "gpu": "Adreno 618", "antutu_benchmark_score": 355000,
                "display_type": "IPS LCD, 120Hz, HDR10, 450 nits", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (Sony IMX682, f/1.9) + 13 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.2", "video_recording_max": "4K@30fps, 1080p@120fps",
                "battery_capacity_mah": 5160, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 215, "os_at_launch": "Android 10, MIUI 12",
                "variants": [
                    {"variant_name": "Poco X3 NFC 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 3199000, "aliases": "poco x3 64, x3 nfc 64"},
                    {"variant_name": "Poco X3 NFC 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3599000, "aliases": "poco x3 128, x3 nfc 128"}
                ]
            },
            {
                "name": "Poco F5 Pro", "series": "F-Series WQHD+ Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8+ Gen 1 (4nm TSMC)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1300000,
                "display_type": "Flow AMOLED, 68B colors, 120Hz, WQHD+, Dolby Vision, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (WQHD+)", "peak_brightness_nits": 1400,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 5160, "fast_charging_watt": 67, "has_wireless_charging": True, "wireless_charging_watt": 30,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 204, "os_at_launch": "Android 13, MIUI 14 for POCO",
                "variants": [
                    {"variant_name": "Poco F5 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6999000, "aliases": "poco f5 pro 256, f5 pro"},
                    {"variant_name": "Poco F5 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 7999000, "aliases": "poco f5 pro 512"}
                ]
            },
            {
                "name": "Redmi Note 11 Pro 5G", "series": "Note 11 Global 5G", "release_year": 2022,
                "chipset": "Snapdragon 695 5G (6nm)", "cpu_architecture": "Octa-core 2.2GHz Kryo 660",
                "gpu": "Adreno 619", "antutu_benchmark_score": 405000,
                "display_type": "Super AMOLED, 120Hz, 1200 nits, HDR10", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (Samsung HM2, f/1.9) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 202, "os_at_launch": "Android 11, MIUI 13",
                "variants": [
                    {"variant_name": "Redmi Note 11 Pro 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4299000, "aliases": "note 11 pro 5g, rn 11 pro 5g"}
                ]
            },
            {
                "name": "Redmi Note 5 (Whyred)", "series": "Note AI Camera Legend", "release_year": 2018,
                "chipset": "Snapdragon 636 (14nm)", "cpu_architecture": "Octa-core 1.8GHz Kryo 260",
                "gpu": "Adreno 509", "antutu_benchmark_score": 115000,
                "display_type": "IPS LCD 18:9 Full Screen", "screen_size_inch": 5.99,
                "refresh_rate_hz": 60, "resolution": "1080 x 2160 pixels (FHD+)", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "12 MP (f/1.9, Dual Pixel PDAF) + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.0, LED Selfie Light", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 181, "os_at_launch": "Android 8.0 (Oreo), MIUI 9",
                "variants": [
                    {"variant_name": "Redmi Note 5 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 2499000, "aliases": "redmi note 5 whyred 32, rn5 pro 32"},
                    {"variant_name": "Redmi Note 5 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2999000, "aliases": "redmi note 5 whyred 64, rn5 pro 64"}
                ]
            },
            {
                "name": "Redmi 9", "series": "Redmi Quad Camera Pioneer", "release_year": 2020,
                "chipset": "MediaTek Helio G80 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G52 MC2", "antutu_benchmark_score": 200000,
                "display_type": "IPS LCD Full HD+ Dot Drop", "screen_size_inch": 6.53,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP (wide) + 8 MP (ultrawide) + 5 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5020, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 198, "os_at_launch": "Android 10, MIUI 11",
                "variants": [
                    {"variant_name": "Redmi 9 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 1799000, "aliases": "redmi 9 32, r9 32"},
                    {"variant_name": "Redmi 9 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 1999000, "aliases": "redmi 9 64, r9 64"}
                ]
            }
        ]
    },

    # ==================== 7. VIVO BATCH 4 ====================
    {
        "brand_name": "Vivo",
        "models": [
            {
                "name": "Vivo V30 5G", "series": "V-Series Studio Portrait", "release_year": 2024,
                "chipset": "Snapdragon 7 Gen 3 (4nm)", "cpu_architecture": "Octa-core 2.63GHz",
                "gpu": "Adreno 720", "antutu_benchmark_score": 830000,
                "display_type": "Curved AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 2800,
                "screen_protection": "Schott Xensation Alpha",
                "main_camera_mp": "50 MP (OmniVision OV50E, OIS) + 50 MP (ultrawide, AF)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP, f/2.0, AF, Dual-LED Flash", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 186, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "Vivo V30 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "v30 256, vivo v30 5g"},
                    {"variant_name": "Vivo V30 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 6999000, "aliases": "v30 512, vivo v30 512gb"}
                ]
            },
            {
                "name": "Vivo Y100 5G", "series": "Y-Series Leather Design", "release_year": 2024,
                "chipset": "Snapdragon 4 Gen 2 (4nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 613", "antutu_benchmark_score": 450000,
                "display_type": "AMOLED, 120Hz, 1200 nits, Stereo Speaker 300%", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "50 MP, f/1.8 + 8 MP (ultrawide) + Flicker sensor",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 185, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "Vivo Y100 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3899000, "aliases": "y100 5g 128, vivo y100 5g"},
                    {"variant_name": "Vivo Y100 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4199000, "aliases": "y100 5g 256"}
                ]
            },
            {
                "name": "Vivo X70 Pro", "series": "X-Series Zeiss Gimbal 3.0", "release_year": 2021,
                "chipset": "MediaTek Dimensity 1200-Vivo (6nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 720000,
                "display_type": "AMOLED, 120Hz, HDR10+, 1300 nits", "screen_size_inch": 6.56,
                "refresh_rate_hz": 120, "resolution": "1080 x 2376 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (Sony IMX766V, Gimbal OIS) + 12 MP (2x telephoto OIS) + 8 MP (5x periscope OIS) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@60fps, Gimbal Stabilization",
                "battery_capacity_mah": 4450, "fast_charging_watt": 44, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 183, "os_at_launch": "Android 11, Funtouch 12",
                "variants": [
                    {"variant_name": "Vivo X70 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 10999000, "aliases": "x70 pro, vivo x70 pro zeiss"}
                ]
            },
            {
                "name": "Vivo V20", "series": "V-Series 44MP Eye Autofocus", "release_year": 2020,
                "chipset": "Snapdragon 720G (8nm)", "cpu_architecture": "Octa-core 2.3GHz Kryo 465",
                "gpu": "Adreno 618", "antutu_benchmark_score": 330000,
                "display_type": "AMOLED, HDR10", "screen_size_inch": 6.44,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 600,
                "screen_protection": "AG Matte Glass",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide/macro) + 2 MP (mono)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "44 MP, f/2.0, Eye Autofocus, 4K@30fps", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 171, "os_at_launch": "Android 11, Funtouch 11",
                "variants": [
                    {"variant_name": "Vivo V20 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "vivo v20 128, v20 sunset melody"}
                ]
            },
            {
                "name": "Vivo Y20s", "series": "Y-Series Mega Battery Mass Market", "release_year": 2020,
                "chipset": "Snapdragon 460 (11nm)", "cpu_architecture": "Octa-core 1.8GHz Kryo 240",
                "gpu": "Adreno 610", "antutu_benchmark_score": 150000,
                "display_type": "IPS LCD Halo FullView", "screen_size_inch": 6.51,
                "refresh_rate_hz": 60, "resolution": "720 x 1600 pixels (HD+)", "peak_brightness_nits": 450,
                "screen_protection": "Reinforced Glass",
                "main_camera_mp": "13 MP (f/2.2) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/1.8", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 192, "os_at_launch": "Android 10, Funtouch 10.5",
                "variants": [
                    {"variant_name": "Vivo Y20s 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3099000, "aliases": "y20s 128, vivo y20s 8gb"}
                ]
            }
        ]
    },

    # ==================== 8. IQOO BATCH 4 ====================
    {
        "brand_name": "iQOO",
        "models": [
            {
                "name": "iQOO Z9 5G", "series": "Z-Series Battery & Performance King", "release_year": 2024,
                "chipset": "Snapdragon 7 Gen 3 (4nm)", "cpu_architecture": "Octa-core 2.63GHz",
                "gpu": "Adreno 720", "antutu_benchmark_score": 820000,
                "display_type": "AMOLED, 144Hz, 1.5K, 4500 nits peak, HDR", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 4500,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (Sony IMX882, f/1.79, OIS) + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.45", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP64", "weight_grams": 194, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "iQOO Z9 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3999000, "aliases": "iqoo z9 128, z9 5g"},
                    {"variant_name": "iQOO Z9 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4299000, "aliases": "iqoo z9 256, z9 256"},
                    {"variant_name": "iQOO Z9 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 4699000, "aliases": "iqoo z9 12gb"}
                ]
            },
            {
                "name": "iQOO Neo 7 Pro 5G", "series": "Neo Dual-Chip Gaming", "release_year": 2023,
                "chipset": "Snapdragon 8+ Gen 1 (4nm TSMC) + Independent Gaming Chip", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1280000,
                "display_type": "AMOLED, 120Hz, HDR10+, 1200Hz Instant Touch", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1500,
                "screen_protection": "Schott Xensation",
                "main_camera_mp": "50 MP (Samsung GN5, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 199, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "iQOO Neo 7 Pro 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5999000, "aliases": "iqoo neo 7 pro, neo 7 pro"},
                    {"variant_name": "iQOO Neo 7 Pro 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 6799000, "aliases": "neo 7 pro 256"}
                ]
            },
            {
                "name": "iQOO 9 Pro", "series": "Numbered Flagship Ultra Performance", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1020000,
                "display_type": "LTPO 2.0 AMOLED, 1B colors, 120Hz, 2K E5", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (2K)", "peak_brightness_nits": 1500,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (Samsung GN5, Gimbal OIS) + 16 MP (2.5x telephoto OIS) + 50 MP (150 deg fisheye ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2.5x Optical",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 4700, "fast_charging_watt": 120, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 209, "os_at_launch": "Android 12, Funtouch 12",
                "variants": [
                    {"variant_name": "iQOO 9 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 11999000, "aliases": "iqoo 9 pro 256, iqoo 9 pro bmw"}
                ]
            }
        ]
    },

    # ==================== 9. OPPO BATCH 4 ====================
    {
        "brand_name": "Oppo",
        "models": [
            {
                "name": "Oppo Reno 7 5G", "series": "Reno Portrait Expert LDI", "release_year": 2022,
                "chipset": "MediaTek Dimensity 900 (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 480000,
                "display_type": "AMOLED, 90Hz, HDR10+, 800 nits", "screen_size_inch": 6.43,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, f/1.7) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP (Sony IMX615), f/2.4", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 173, "os_at_launch": "Android 11, ColorOS 12",
                "variants": [
                    {"variant_name": "Oppo Reno 7 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 7499000, "aliases": "reno 7 5g, oppo reno 7 5g"}
                ]
            },
            {
                "name": "Oppo A78 4G", "series": "A-Series 67W SuperVOOC AMOLED", "release_year": 2023,
                "chipset": "Snapdragon 680 4G (6nm)", "cpu_architecture": "Octa-core 2.4GHz Kryo 265",
                "gpu": "Adreno 610", "antutu_benchmark_score": 310000,
                "display_type": "AMOLED, 90Hz, Dual Stereo Speakers", "screen_size_inch": 6.43,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 430,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP, f/1.8, PDAF + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 180, "os_at_launch": "Android 13, ColorOS 13.1",
                "variants": [
                    {"variant_name": "Oppo A78 4G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3599000, "aliases": "oppo a78 4g, a78 256"}
                ]
            },
            {
                "name": "Oppo Find X", "series": "Find Stealth 3D Camera Pioneer", "release_year": 2018,
                "chipset": "Snapdragon 845 (10nm)", "cpu_architecture": "Octa-core 2.8GHz Kryo 385",
                "gpu": "Adreno 630", "antutu_benchmark_score": 340000,
                "display_type": "Panoramic Curved AMOLED, 93.8% Screen-to-body", "screen_size_inch": 6.42,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "16 MP (Sony IMX519, OIS) + 20 MP (motorized pop-up module)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "25 MP (motorized pop-up 3D Structured Light)", "video_recording_max": "4K@30fps, 1080p@240fps",
                "battery_capacity_mah": 3730, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 186, "os_at_launch": "Android 8.1 (Oreo), ColorOS 5.1",
                "variants": [
                    {"variant_name": "Oppo Find X 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 12999000, "aliases": "oppo find x, find x stealth"}
                ]
            },
            {
                "name": "Oppo F7", "series": "Selfie Expert AI 25MP", "release_year": 2018,
                "chipset": "MediaTek Helio P60 (12nm)", "cpu_architecture": "Octa-core 2.0GHz (4x Cortex-A73 + 4x Cortex-A53)",
                "gpu": "Mali-G72 MP3", "antutu_benchmark_score": 140000,
                "display_type": "IPS LCD Notch Full Screen", "screen_size_inch": 6.23,
                "refresh_rate_hz": 60, "resolution": "1080 x 2280 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "16 MP, f/1.8, PDAF, LED flash",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "25 MP (Sony IMX576), f/2.0, AI Beauty 2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3400, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 158, "os_at_launch": "Android 8.1 (Oreo), ColorOS 5.0",
                "variants": [
                    {"variant_name": "Oppo F7 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 4199000, "aliases": "oppo f7 64, f7 64gb"},
                    {"variant_name": "Oppo F7 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 5499000, "aliases": "oppo f7 128, f7 128gb"}
                ]
            },
            {
                "name": "Oppo F5", "series": "Selfie Expert AI 18:9 FullView Pioneer", "release_year": 2017,
                "chipset": "MediaTek Helio P23 (16nm)", "cpu_architecture": "Octa-core 2.5GHz Cortex-A53",
                "gpu": "Mali-G71 MP2", "antutu_benchmark_score": 85000,
                "display_type": "LTPS IPS LCD 18:9 FullView", "screen_size_inch": 6.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 2160 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "16 MP, f/1.8, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.0, AI Recognition", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3200, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 152, "os_at_launch": "Android 7.1.1 (Nougat), ColorOS 3.2",
                "variants": [
                    {"variant_name": "Oppo F5 4GB/32GB", "ram_gb": 4, "storage_gb": 32, "official_msrp_new": 3999000, "aliases": "oppo f5 32, f5 32gb"},
                    {"variant_name": "Oppo F5 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 5199000, "aliases": "oppo f5 64, f5 64gb"}
                ]
            }
        ]
    },

    # ==================== 10. SAMSUNG BATCH 4 ====================
    {
        "brand_name": "Samsung",
        "models": [
            {
                "name": "Galaxy A35 5G", "series": "A-Series Key Island", "release_year": 2024,
                "chipset": "Exynos 1380 (5nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68 MP5", "antutu_benchmark_score": 590000,
                "display_type": "Super AMOLED, 120Hz, 1000 nits, Vision Booster", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus+",
                "main_camera_mp": "50 MP (wide, OIS) + 8 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.2", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 209, "os_at_launch": "Android 14, One UI 6.1",
                "variants": [
                    {"variant_name": "Galaxy A35 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "a35 128, samsung a35 128gb"},
                    {"variant_name": "Galaxy A35 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "a35 256, samsung a35 256gb"}
                ]
            },
            {
                "name": "Galaxy A15 5G", "series": "A-Series Entry 5G Value", "release_year": 2024,
                "chipset": "MediaTek Dimensity 6100+ (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 410000,
                "display_type": "Super AMOLED, 90Hz, 800 nits", "screen_size_inch": 6.5,
                "refresh_rate_hz": 90, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "50 MP (f/1.8, AF) + 5 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 200, "os_at_launch": "Android 14, One UI 6.0",
                "variants": [
                    {"variant_name": "Galaxy A15 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3599000, "aliases": "a15 5g 256, samsung a15 5g"}
                ]
            },
            {
                "name": "Galaxy S21 FE 5G", "series": "Fan Edition Flagship Value", "release_year": 2022,
                "chipset": "Exynos 2100 (5nm)", "cpu_architecture": "Octa-core 2.9GHz (1x Cortex-X1 + 3x Cortex-A78 + 4x Cortex-A55)",
                "gpu": "Mali-G78 MP14", "antutu_benchmark_score": 750000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.4,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "12 MP (wide, Dual Pixel PDAF, OIS) + 8 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@60fps, 1080p@240fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 177, "os_at_launch": "Android 12, One UI 4.0",
                "variants": [
                    {"variant_name": "Galaxy S21 FE 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 8999000, "aliases": "s21 fe 128, samsung s21 fe"},
                    {"variant_name": "Galaxy S21 FE 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "s21 fe 256, samsung s21 fe 256gb"}
                ]
            },
            {
                "name": "Galaxy Note 4", "series": "Note QHD Metal Frame Classic", "release_year": 2014,
                "chipset": "Exynos 5433 (20nm)", "cpu_architecture": "Octa-core (4x 1.9GHz Cortex-A57 + 4x 1.3GHz Cortex-A53)",
                "gpu": "Mali-T760", "antutu_benchmark_score": 68000,
                "display_type": "Super AMOLED QHD Display, 515 ppi", "screen_size_inch": 5.7,
                "refresh_rate_hz": 60, "resolution": "1440 x 2560 pixels (QHD)", "peak_brightness_nits": 550,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "16 MP, f/2.2, Smart OIS, LED flash",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "3.7 MP, f/1.9, 120 deg Wide Selfie", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 3220, "fast_charging_watt": 15, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 176, "os_at_launch": "Android 4.4.4 (KitKat), TouchWiz",
                "variants": [
                    {"variant_name": "Galaxy Note 4 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 9499000, "aliases": "note 4, samsung note 4 32gb"}
                ]
            },
            {
                "name": "Galaxy S7", "series": "S-Series Dual Pixel Pioneer", "release_year": 2016,
                "chipset": "Exynos 8890 Octa (14nm)", "cpu_architecture": "Octa-core (4x 2.3GHz Mongoose + 4x 1.6GHz Cortex-A53)",
                "gpu": "Mali-T880 MP12", "antutu_benchmark_score": 135000,
                "display_type": "Super AMOLED QHD, Always-on display", "screen_size_inch": 5.1,
                "refresh_rate_hz": 60, "resolution": "1440 x 2560 pixels (QHD)", "peak_brightness_nits": 850,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "12 MP (f/1.7, Dual Pixel PDAF, OIS)",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/1.7, Auto HDR", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 152, "os_at_launch": "Android 6.0 (Marshmallow), TouchWiz",
                "variants": [
                    {"variant_name": "Galaxy S7 4GB/32GB", "ram_gb": 4, "storage_gb": 32, "official_msrp_new": 8999000, "aliases": "s7 flat, samsung s7 32gb"}
                ]
            }
        ]
    },

    # ==================== 11. GOOGLE PIXEL / SONY / ASUS BATCH 4 ====================
    {
        "brand_name": "Google",
        "models": [
            {
                "name": "Pixel 7", "series": "Google Tensor Flagship", "release_year": 2022,
                "chipset": "Google Tensor G2 (5nm)", "cpu_architecture": "Octa-core 2.85GHz (2x Cortex-X1 + 2x Cortex-A78 + 4x Cortex-A55)",
                "gpu": "Mali-G710 MP7", "antutu_benchmark_score": 830000,
                "display_type": "AMOLED, 90Hz, HDR10+, 1400 nits peak", "screen_size_inch": 6.3,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1400,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, Octa PD, OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Super Res Zoom",
                "selfie_camera_mp": "10.8 MP, f/2.2", "video_recording_max": "4K@60fps 10-bit HDR",
                "battery_capacity_mah": 4355, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 20,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 197, "os_at_launch": "Android 13 (Pixel Experience)",
                "variants": [
                    {"variant_name": "Pixel 7 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 9999000, "aliases": "pixel 7 128, google pixel 7"},
                    {"variant_name": "Pixel 7 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 11499000, "aliases": "pixel 7 256"}
                ]
            },
            {
                "name": "Pixel 6", "series": "First Tensor Innovation", "release_year": 2021,
                "chipset": "Google Tensor (5nm)", "cpu_architecture": "Octa-core 2.8GHz (2x Cortex-X1 + 2x Cortex-A76 + 4x Cortex-A55)",
                "gpu": "Mali-G78 MP20", "antutu_benchmark_score": 750000,
                "display_type": "AMOLED, 90Hz, HDR10+", "screen_size_inch": 6.4,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1100,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Samsung GN1, OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4614, "fast_charging_watt": 21, "has_wireless_charging": True, "wireless_charging_watt": 21,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 207, "os_at_launch": "Android 12 (Material You)",
                "variants": [
                    {"variant_name": "Pixel 6 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 8999000, "aliases": "pixel 6 128, google pixel 6"}
                ]
            }
        ]
    },
    {
        "brand_name": "Sony",
        "models": [
            {
                "name": "Sony Xperia Z5", "series": "Xperia Z Frosted Glass Classic", "release_year": 2015,
                "chipset": "Snapdragon 810 (20nm)", "cpu_architecture": "Octa-core (4x 2.0GHz Cortex-A57 + 4x 1.5GHz Cortex-A53)",
                "gpu": "Adreno 430", "antutu_benchmark_score": 90000,
                "display_type": "IPS LCD, Triluminos display, X-Reality Engine", "screen_size_inch": 5.2,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 650,
                "screen_protection": "Scratch-resistant glass, oleophobic coating",
                "main_camera_mp": "23 MP (1/2.3 inch Exmor RS, f/2.0, 24mm wide)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "5x Clear Image Zoom",
                "selfie_camera_mp": "5.1 MP, f/2.4", "video_recording_max": "4K@30fps, SteadyShot",
                "battery_capacity_mah": 2900, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 154, "os_at_launch": "Android 5.1.1 (Lollipop)",
                "variants": [
                    {"variant_name": "Sony Xperia Z5 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 9999000, "aliases": "xperia z5, sony z5 32gb"}
                ]
            },
            {
                "name": "Sony Xperia Z3", "series": "Xperia Z Waterproof Benchmark", "release_year": 2014,
                "chipset": "Snapdragon 801 (28nm)", "cpu_architecture": "Quad-core 2.5GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 45000,
                "display_type": "IPS LCD, Triluminos display", "screen_size_inch": 5.2,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Shatter proof glass",
                "main_camera_mp": "20.7 MP (1/2.3 inch Exmor RS, f/2.0, ISO 12800)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2.2 MP, 1080p@30fps", "video_recording_max": "4K@30fps, 1080p@60fps",
                "battery_capacity_mah": 3100, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 152, "os_at_launch": "Android 4.4.4 (KitKat)",
                "variants": [
                    {"variant_name": "Sony Xperia Z3 3GB/16GB", "ram_gb": 3, "storage_gb": 16, "official_msrp_new": 8499000, "aliases": "xperia z3, sony z3"}
                ]
            }
        ]
    },
    {
        "brand_name": "Asus",
        "models": [
            {
                "name": "ROG Phone 7", "series": "ROG Extreme Gaming Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1600000,
                "display_type": "Samsung AMOLED, 1B colors, 165Hz, HDR10+, 1500 nits", "screen_size_inch": 6.78,
                "refresh_rate_hz": 165, "resolution": "1080 x 2448 pixels", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766) + 13 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 239, "os_at_launch": "Android 13, ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone 7 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 10999000, "aliases": "rog phone 7 256, rog 7 12gb"},
                    {"variant_name": "ROG Phone 7 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 13999000, "aliases": "rog phone 7 512, rog 7 16gb"}
                ]
            }
        ]
    }
]
