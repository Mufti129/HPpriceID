"""
Batch 3 Master Catalog Smartphone Pasar Indonesia (2010 - 2026).
Menambahkan generasi smartphone legendaris dan volume masif lainnya:
Samsung (S20, S22, S24, Note 10, Note 20, S6, S5, A71, A72, A34, A35, Z Flip 6, Z Fold 3/4),
Apple (iPhone 12 Pro, 5c), Xiaomi (Mi 9T Pro, 11T Pro, Poco X4 Pro, Poco M6 Pro, Redmi Note 9/10/11),
Oppo (Reno 11 Pro, Reno 7 5G, Reno 5 5G, Find X2, Find X, Find 7, F11 Pro, F7, F5),
Vivo/iQOO (V40 5G, X70 Pro, X60 Pro, V23 5G, V20 Pro, V19, V17 Pro, V11 Pro, iQOO Z9 5G),
Realme (11 Pro, 10 Pro, 8 5G, 6, GT Neo 2, 3 Pro),
Infinix/Tecno (Note 11 Pro, Zero 5G, Hot 30, Camon 30 Pro, Camon 20 Pro, Phantom X2 Pro),
Google Pixel (Pixel 8, Pixel 7, Pixel 6, Pixel 5, Pixel 3 XL),
Sony (Xperia 1 IV, Xperia 1 III, Xperia 5 IV, Xperia Z5 Premium, Xperia Z1),
Huawei (P60 Pro, P50 Pro, P40 Pro, P9),
Asus (ROG Phone 6, ROG Phone 5, ROG Phone 3, Zenfone 6, Zenfone 2),
Nothing (Nothing Phone 1).
"""

EXTENDED_CATALOG_MODELS_BATCH3 = [
    # ==================== 1. SAMSUNG BATCH 3 ====================
    {
        "brand_name": "Samsung",
        "models": [
            {
                "name": "Galaxy S24", "series": "S-Series AI Flagship", "release_year": 2024,
                "chipset": "Exynos 2400 (4nm)", "cpu_architecture": "Deca-core 3.2GHz",
                "gpu": "Xclipse 940 (AMD RDNA3)", "antutu_benchmark_score": 1720000,
                "display_type": "Dynamic LTPO AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.2,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 167, "os_at_launch": "Android 14, One UI 6.1 (Galaxy AI)",
                "variants": [
                    {"variant_name": "Galaxy S24 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 13999000, "aliases": "s24 256, samsung s24 256gb"},
                    {"variant_name": "Galaxy S24 8GB/512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 15999000, "aliases": "s24 512, samsung s24 512gb"}
                ]
            },
            {
                "name": "Galaxy S24+", "series": "S-Series AI Flagship", "release_year": 2024,
                "chipset": "Exynos 2400 (4nm)", "cpu_architecture": "Deca-core 3.2GHz",
                "gpu": "Xclipse 940 (AMD RDNA3)", "antutu_benchmark_score": 1750000,
                "display_type": "Dynamic LTPO AMOLED 2X, 120Hz, QHD+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1440 x 3120 pixels (QHD+)", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 4900, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 196, "os_at_launch": "Android 14, One UI 6.1",
                "variants": [
                    {"variant_name": "Galaxy S24+ 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 16999000, "aliases": "s24 plus 256, s24+ 256"},
                    {"variant_name": "Galaxy S24+ 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 18999000, "aliases": "s24 plus 512, s24+ 512"}
                ]
            },
            {
                "name": "Galaxy S22", "series": "S-Series Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1010000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass Victus+",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 3700, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 167, "os_at_launch": "Android 12, One UI 4.1",
                "variants": [
                    {"variant_name": "Galaxy S22 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 11999000, "aliases": "s22 128, samsung s22 128gb"},
                    {"variant_name": "Galaxy S22 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 12999000, "aliases": "s22 256, samsung s22 256gb"}
                ]
            },
            {
                "name": "Galaxy S20", "series": "S-Series Flagship", "release_year": 2020,
                "chipset": "Exynos 990 (7nm+)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G77 MP11", "antutu_benchmark_score": 550000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.2,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (QHD+)", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "12 MP (wide, OIS) + 64 MP (3x hybrid telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Hybrid",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 163, "os_at_launch": "Android 10, One UI 2.0",
                "variants": [
                    {"variant_name": "Galaxy S20 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 12999000, "aliases": "s20 128, samsung s20 128gb"}
                ]
            },
            {
                "name": "Galaxy Note 20", "series": "Note S-Pen", "release_year": 2020,
                "chipset": "Exynos 990 (7nm+)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G77 MP11", "antutu_benchmark_score": 540000,
                "display_type": "Super AMOLED Plus, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1050,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP (wide, OIS) + 64 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Hybrid Optical",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4300, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 192, "os_at_launch": "Android 10, One UI 2.5",
                "variants": [
                    {"variant_name": "Galaxy Note 20 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 14499000, "aliases": "note 20 256, samsung note 20"}
                ]
            },
            {
                "name": "Galaxy Note 10", "series": "Compact Note S-Pen", "release_year": 2019,
                "chipset": "Exynos 9825 (7nm)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G76 MP12", "antutu_benchmark_score": 460000,
                "display_type": "Dynamic AMOLED, HDR10+", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2280 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "12 MP (wide, dual aperture OIS) + 12 MP (2x telephoto OIS) + 16 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3500, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 12,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 168, "os_at_launch": "Android 9 (Pie), One UI",
                "variants": [
                    {"variant_name": "Galaxy Note 10 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 13999000, "aliases": "note 10 256, samsung note 10"}
                ]
            },
            {
                "name": "Galaxy S6", "series": "Metal Glass Pioneer", "release_year": 2015,
                "chipset": "Exynos 7420 Octa (14nm)", "cpu_architecture": "Octa-core 2.1GHz",
                "gpu": "Mali-T760MP8", "antutu_benchmark_score": 110000,
                "display_type": "Super AMOLED QHD", "screen_size_inch": 5.1,
                "refresh_rate_hz": 60, "resolution": "1440 x 2560 pixels (QHD)", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "16 MP, f/1.9, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/1.9", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 2550, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 138, "os_at_launch": "Android 5.0.2 (Lollipop)",
                "variants": [
                    {"variant_name": "Galaxy S6 32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 9499000, "aliases": "samsung s6, s6 32gb"}
                ]
            },
            {
                "name": "Galaxy S5", "series": "Waterproof Heart Rate", "release_year": 2014,
                "chipset": "Snapdragon 801 (28nm)", "cpu_architecture": "Quad-core 2.5GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 45000,
                "display_type": "Super AMOLED FHD", "screen_size_inch": 5.1,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 698,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "16 MP, f/2.2, ISOCELL, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 2800, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 145, "os_at_launch": "Android 4.4.2 (KitKat)",
                "variants": [
                    {"variant_name": "Galaxy S5 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 8499000, "aliases": "samsung s5, s5 16gb"}
                ]
            },
            {
                "name": "Galaxy A71", "series": "A-Series Upper Mid", "release_year": 2020,
                "chipset": "Snapdragon 730 (8nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 618", "antutu_benchmark_score": 275000,
                "display_type": "Super AMOLED Plus Infinity-O", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "64 MP (wide) + 12 MP (ultrawide) + 5 MP (macro) + 5 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 179, "os_at_launch": "Android 10, One UI 2.0",
                "variants": [
                    {"variant_name": "Galaxy A71 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 6099000, "aliases": "samsung a71 128, a71 8/128"}
                ]
            },
            {
                "name": "Galaxy A34 5G", "series": "A-Series Value 5G", "release_year": 2023,
                "chipset": "MediaTek Dimensity 1080 (6nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 530000,
                "display_type": "Super AMOLED, 120Hz", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (wide, OIS) + 8 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 199, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy A34 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "a34 128, samsung a34 5g"},
                    {"variant_name": "Galaxy A34 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5399000, "aliases": "a34 256, samsung a34 256gb"}
                ]
            }
        ]
    },

    # ==================== 2. APPLE BATCH 3 ====================
    {
        "brand_name": "Apple",
        "models": [
            {
                "name": "iPhone 12 Pro", "series": "Pro", "release_year": 2020,
                "chipset": "Apple A14 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 1020000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1170 x 2532 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (2x telephoto OIS) + 12 MP (ultrawide) + LiDAR",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps Dolby Vision",
                "battery_capacity_mah": 2815, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 189, "os_at_launch": "iOS 14.1",
                "variants": [
                    {"variant_name": "iPhone 12 Pro 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 18499000, "aliases": "12 pro 128, ip 12 pro 128, iphone 12 pro 128gb"},
                    {"variant_name": "iPhone 12 Pro 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 20999000, "aliases": "12 pro 256, ip 12 pro 256, iphone 12 pro 256gb"}
                ]
            },
            {
                "name": "iPhone 5c", "series": "Color Polycarbonate", "release_year": 2013,
                "chipset": "Apple A6 (32nm)", "cpu_architecture": "Dual-core 1.3GHz Swift",
                "gpu": "PowerVR SGX543MP3", "antutu_benchmark_score": 90000,
                "display_type": "IPS LCD Retina Display", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "640 x 1136 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "8 MP, f/2.4, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.2 MP, f/2.4", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 1510, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 132, "os_at_launch": "iOS 7",
                "variants": [
                    {"variant_name": "iPhone 5c 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 7999000, "aliases": "ip 5c 16, iphone 5c 16gb"}
                ]
            }
        ]
    },

    # ==================== 3. XIAOMI / POCO / REDMI BATCH 3 ====================
    {
        "brand_name": "Xiaomi",
        "models": [
            {
                "name": "Xiaomi 11T Pro", "series": "HyperCharge Flagship", "release_year": 2021,
                "chipset": "Snapdragon 888 5G (5nm)", "cpu_architecture": "Octa-core 2.84GHz",
                "gpu": "Adreno 660", "antutu_benchmark_score": 810000,
                "display_type": "AMOLED, 1B colors, 120Hz, Dolby Vision, DisplayMate A+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "108 MP (wide) + 8 MP (ultrawide) + 5 MP (telemacro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 204, "os_at_launch": "Android 11, MIUI 12.5",
                "variants": [
                    {"variant_name": "Xiaomi 11T Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6999000, "aliases": "11t pro 256, xiaomi 11t pro"},
                    {"variant_name": "Xiaomi 11T Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 7499000, "aliases": "11t pro 12/256, mi 11t pro"}
                ]
            },
            {
                "name": "Poco X4 Pro 5G", "series": "Poco X", "release_year": 2022,
                "chipset": "Snapdragon 695 5G (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 619", "antutu_benchmark_score": 400000,
                "display_type": "AMOLED, 120Hz, HDR10", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (wide) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 205, "os_at_launch": "Android 11, MIUI 13 for POCO",
                "variants": [
                    {"variant_name": "Poco X4 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3999000, "aliases": "poco x4 pro 256, x4 pro 5g"}
                ]
            },
            {
                "name": "Poco M6 Pro", "series": "Poco M All-Rounder", "release_year": 2024,
                "chipset": "MediaTek Helio G99-Ultra (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 430000,
                "display_type": "Flow AMOLED, 120Hz", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 179, "os_at_launch": "Android 13, MIUI 14 for POCO",
                "variants": [
                    {"variant_name": "Poco M6 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 2999000, "aliases": "poco m6 pro 256, m6 pro 8/256"}
                ]
            },
            {
                "name": "Redmi Note 9 Pro", "series": "Redmi Note", "release_year": 2020,
                "chipset": "Snapdragon 720G (8nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Adreno 618", "antutu_benchmark_score": 280000,
                "display_type": "IPS LCD DotDisplay", "screen_size_inch": 6.67,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide) + 5 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5020, "fast_charging_watt": 30, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "Splash-proof", "weight_grams": 209, "os_at_launch": "Android 10, MIUI 11",
                "variants": [
                    {"variant_name": "Redmi Note 9 Pro 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 3499000, "aliases": "rn 9 pro 64, redmi note 9 pro 64gb"},
                    {"variant_name": "Redmi Note 9 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3899000, "aliases": "rn 9 pro 128, redmi note 9 pro 128gb"}
                ]
            }
        ]
    },

    # ==================== 4. OPPO BATCH 3 ====================
    {
        "brand_name": "Oppo",
        "models": [
            {
                "name": "Oppo Reno 11 Pro 5G", "series": "Reno Portrait Expert", "release_year": 2024,
                "chipset": "MediaTek Dimensity 8200 (4nm)", "cpu_architecture": "Octa-core 3.1GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 930000,
                "display_type": "OLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Asahi Glass AGC",
                "main_camera_mp": "50 MP (Sony IMX890, OIS) + 32 MP (telephoto 2x) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.4, AF", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4600, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 181, "os_at_launch": "Android 14, ColorOS 14",
                "variants": [
                    {"variant_name": "Oppo Reno 11 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 8999000, "aliases": "reno 11 pro 512, oppo reno 11 pro"}
                ]
            },
            {
                "name": "Oppo Reno 5 5G", "series": "Reno Video Expert", "release_year": 2021,
                "chipset": "Snapdragon 765G (7nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 620", "antutu_benchmark_score": 380000,
                "display_type": "OLED, 90Hz", "screen_size_inch": 6.43,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 750,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.4", "video_recording_max": "4K@30fps Dual-View Video",
                "battery_capacity_mah": 4300, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 172, "os_at_launch": "Android 11, ColorOS 11.1",
                "variants": [
                    {"variant_name": "Oppo Reno 5 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 6999000, "aliases": "reno 5 5g, oppo reno 5 128"}
                ]
            },
            {
                "name": "Oppo F11 Pro", "series": "Rising Camera", "release_year": 2019,
                "chipset": "MediaTek Helio P70 (12nm)", "cpu_architecture": "Octa-core 2.1GHz",
                "gpu": "Mali-G72 MP3", "antutu_benchmark_score": 190000,
                "display_type": "IPS LCD Panoramic Screen", "screen_size_inch": 6.53,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 430,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (f/1.8) + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP Motorized Pop-up, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 190, "os_at_launch": "Android 9 (Pie), ColorOS 6",
                "variants": [
                    {"variant_name": "Oppo F11 Pro 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 4999000, "aliases": "oppo f11 pro 64, f11 pro"}
                ]
            }
        ]
    },

    # ==================== 5. VIVO BATCH 3 ====================
    {
        "brand_name": "Vivo",
        "models": [
            {
                "name": "Vivo V40 5G", "series": "V-Series Zeiss Portrait", "release_year": 2024,
                "chipset": "Snapdragon 7 Gen 3 (4nm)", "cpu_architecture": "Octa-core 2.63GHz",
                "gpu": "Adreno 720", "antutu_benchmark_score": 830000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 4500,
                "screen_protection": "Schott Xensation Alpha",
                "main_camera_mp": "50 MP (Zeiss, OIS) + 50 MP (Zeiss ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP (Zeiss, f/2.0, AF)", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5500, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68/IP69", "weight_grams": 190, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "Vivo V40 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6499000, "aliases": "vivo v40 256, v40 5g 256"},
                    {"variant_name": "Vivo V40 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 7999000, "aliases": "vivo v40 512, v40 5g 512"}
                ]
            },
            {
                "name": "Vivo V23 5G", "series": "V-Series Color Changing", "release_year": 2022,
                "chipset": "MediaTek Dimensity 920 (6nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 500000,
                "display_type": "AMOLED, 90Hz, HDR10+", "screen_size_inch": 6.44,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP (wide, AF) + 8 MP (ultrawide) Dual Spotlight", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4200, "fast_charging_watt": 44, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 179, "os_at_launch": "Android 12, Funtouch 12",
                "variants": [
                    {"variant_name": "Vivo V23 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5999000, "aliases": "v23 5g 128, vivo v23 128"}
                ]
            },
            {
                "name": "Vivo V11 Pro", "series": "Screen Touch ID Debut", "release_year": 2018,
                "chipset": "Snapdragon 660 (14nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 512", "antutu_benchmark_score": 165000,
                "display_type": "Super AMOLED Halo FullView", "screen_size_inch": 6.41,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 430,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12 MP (f/1.8, Dual Pixel PDAF) + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "25 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3400, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 156, "os_at_launch": "Android 8.1 (Oreo), Funtouch 4.5",
                "variants": [
                    {"variant_name": "Vivo V11 Pro 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 4999000, "aliases": "v11 pro 64, vivo v11 pro"}
                ]
            }
        ]
    },

    # ==================== 6. GOOGLE PIXEL BATCH 3 ====================
    {
        "brand_name": "Google",
        "models": [
            {
                "name": "Pixel 8", "series": "Best-Take AI", "release_year": 2023,
                "chipset": "Google Tensor G3 (4nm)", "cpu_architecture": "Nona-core 3.0GHz",
                "gpu": "Immortalis-G715s MC10", "antutu_benchmark_score": 1150000,
                "display_type": "OLED Actua Display, 120Hz, HDR10+", "screen_size_inch": 6.2,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "10.5 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4575, "fast_charging_watt": 27, "has_wireless_charging": True, "wireless_charging_watt": 18,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 187, "os_at_launch": "Android 14",
                "variants": [
                    {"variant_name": "Pixel 8 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 11999000, "aliases": "pixel 8 128, google pixel 8"},
                    {"variant_name": "Pixel 8 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 13499000, "aliases": "pixel 8 256, google pixel 8 256gb"}
                ]
            },
            {
                "name": "Pixel 5", "series": "Bio-Resin Aluminum", "release_year": 2020,
                "chipset": "Snapdragon 765G (7nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 620", "antutu_benchmark_score": 380000,
                "display_type": "OLED, 90Hz, HDR10+", "screen_size_inch": 6.0,
                "refresh_rate_hz": 90, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 700,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "12.2 MP (wide, OIS) + 16 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.0", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4080, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 12,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 151, "os_at_launch": "Android 11",
                "variants": [
                    {"variant_name": "Pixel 5 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 10499000, "aliases": "pixel 5 128, google pixel 5"}
                ]
            }
        ]
    },

    # ==================== 7. SONY XPERIA BATCH 3 ====================
    {
        "brand_name": "Sony",
        "models": [
            {
                "name": "Xperia 1 IV", "series": "True Optical Zoom 85-125mm", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1020000,
                "display_type": "OLED, 1B colors, 120Hz, 4K HDR", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1644 x 3840 pixels (4K)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "12 MP (24mm, OIS) + 12 MP (85-125mm True Continuous Optical Zoom OIS) + 12 MP (16mm ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3.5x-5.2x Continuous Optical",
                "selfie_camera_mp": "12 MP, f/2.0", "video_recording_max": "4K@120fps all rear cameras",
                "battery_capacity_mah": 5000, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 185, "os_at_launch": "Android 12",
                "variants": [
                    {"variant_name": "Xperia 1 IV 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 18999000, "aliases": "sony xperia 1 iv, 1 iv 256"}
                ]
            },
            {
                "name": "Xperia Z1 (C6903)", "series": "G-Lens 20.7MP Pioneer", "release_year": 2013,
                "chipset": "Snapdragon 800 (28nm)", "cpu_architecture": "Quad-core 2.2GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 38000,
                "display_type": "TFT Triluminos Display, X-Reality", "screen_size_inch": 5.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 460,
                "screen_protection": "Shatter proof glass",
                "main_camera_mp": "20.7 MP, f/2.0, 1/2.3\" Sony G-Lens",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP58", "weight_grams": 170, "os_at_launch": "Android 4.2 (Jelly Bean)",
                "variants": [
                    {"variant_name": "Xperia Z1 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 8499000, "aliases": "sony xperia z1, z1 16gb, c6903"}
                ]
            }
        ]
    },

    # ==================== 8. HUAWEI BATCH 3 ====================
    {
        "brand_name": "Huawei",
        "models": [
            {
                "name": "Huawei P50 Pro", "series": "Dual-Matrix Camera", "release_year": 2021,
                "chipset": "Snapdragon 888 4G (5nm)", "cpu_architecture": "Octa-core 2.84GHz",
                "gpu": "Adreno 660", "antutu_benchmark_score": 790000,
                "display_type": "OLED, 1B colors, 120Hz", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1228 x 2700 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Aluminosilicate glass",
                "main_camera_mp": "50 MP (True-Chroma, OIS) + 64 MP (periscope 3.5x OIS) + 13 MP (ultrawide) + 40 MP (monochrome)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "3.5x Periscope & 100x Digital",
                "selfie_camera_mp": "13 MP, f/2.4", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4360, "fast_charging_watt": 66, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 195, "os_at_launch": "EMUI 12",
                "variants": [
                    {"variant_name": "Huawei P50 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 14999000, "aliases": "p50 pro 256, huawei p50 pro"}
                ]
            },
            {
                "name": "Huawei P9", "series": "First Leica Dual-Lens", "release_year": 2016,
                "chipset": "Kirin 955 (16nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-T880 MP4", "antutu_benchmark_score": 110000,
                "display_type": "IPS-NEO LCD", "screen_size_inch": 5.2,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12 MP (RGB, Leica) + 12 MP (Monochrome, Leica)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.4", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 144, "os_at_launch": "Android 6.0, EMUI 4.1",
                "variants": [
                    {"variant_name": "Huawei P9 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 6999000, "aliases": "huawei p9 32, p9 leica"}
                ]
            }
        ]
    },

    # ==================== 9. ASUS BATCH 3 ====================
    {
        "brand_name": "Asus",
        "models": [
            {
                "name": "ROG Phone 6", "series": "Gaming Monster", "release_year": 2022,
                "chipset": "Snapdragon 8+ Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.19GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1120000,
                "display_type": "AMOLED, 1B colors, 165Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 165, "resolution": "1080 x 2448 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766) + 13 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP (Sony IMX663)", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IPX4", "weight_grams": 239, "os_at_launch": "Android 12, ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone 6 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 10999000, "aliases": "rog 6 256, asus rog 6"},
                    {"variant_name": "ROG Phone 6 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 13999000, "aliases": "rog 6 12/256, rog phone 6 12gb"}
                ]
            },
            {
                "name": "Zenfone 2 (ZE551ML)", "series": "World First 4GB RAM", "release_year": 2015,
                "chipset": "Intel Atom Z3580 (22nm)", "cpu_architecture": "Quad-core 2.3GHz Moorefield",
                "gpu": "PowerVR G6430", "antutu_benchmark_score": 52000,
                "display_type": "IPS LCD Full HD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP, f/2.0, AF (PixelMaster)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 170, "os_at_launch": "Android 5.0 (Lollipop), ZenUI",
                "variants": [
                    {"variant_name": "Zenfone 2 4GB/32GB", "ram_gb": 4, "storage_gb": 32, "official_msrp_new": 3999000, "aliases": "zenfone 2 4gb, ze551ml 32gb"},
                    {"variant_name": "Zenfone 2 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 4499000, "aliases": "zenfone 2 64gb, ze551ml 64gb"}
                ]
            }
        ]
    },

    # ==================== 10. NOTHING BATCH 3 ====================
    {
        "brand_name": "Nothing",
        "models": [
            {
                "name": "Nothing Phone (1)", "series": "Glyph Pioneer", "release_year": 2022,
                "chipset": "Snapdragon 778G+ 5G (6nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Adreno 642L", "antutu_benchmark_score": 600000,
                "display_type": "OLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.55,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 700,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766, OIS) + 50 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 33, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 193, "os_at_launch": "Android 12, Nothing OS 1.0",
                "variants": [
                    {"variant_name": "Nothing Phone (1) 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 7999000, "aliases": "nothing 1 128, nothing phone 1"},
                    {"variant_name": "Nothing Phone (1) 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 8999000, "aliases": "nothing 1 256, nothing phone 1 256gb"}
                ]
            }
        ]
    }
]
