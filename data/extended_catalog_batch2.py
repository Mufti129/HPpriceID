"""
Batch 2 Master Catalog Smartphone Pasar Indonesia (2010 - 2026).
Ekspansi masif mencakup Samsung, Apple, Xiaomi/Poco/Redmi, Oppo, Vivo/iQOO, Realme,
Infinix/Tecno, Google Pixel, Sony Xperia, Huawei, Asus ROG/Zenfone, dan Nothing.
Seluruh data hardware spesifik, presisi, valid, dan bebas simbol informal.
"""

EXTENDED_CATALOG_MODELS_BATCH2 = [
    # ==================== 1. SAMSUNG BATCH 2 ====================
    {
        "brand_name": "Samsung",
        "models": [
            {
                "name": "Galaxy S23+", "series": "S-Series Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.36GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1540000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1750,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 4700, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 196, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy S23+ 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 15999000, "aliases": "s23 plus 256, s23+ 256"},
                    {"variant_name": "Galaxy S23+ 8GB/512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 17999000, "aliases": "s23 plus 512, s23+ 512"}
                ]
            },
            {
                "name": "Galaxy S22+", "series": "S-Series Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1050000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1750,
                "screen_protection": "Corning Gorilla Glass Victus+",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 195, "os_at_launch": "Android 12, One UI 4.1",
                "variants": [
                    {"variant_name": "Galaxy S22+ 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 14999000, "aliases": "s22 plus 128, s22+ 128"},
                    {"variant_name": "Galaxy S22+ 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 15999000, "aliases": "s22 plus 256, s22+ 256"}
                ]
            },
            {
                "name": "Galaxy S21+ 5G", "series": "S-Series Flagship", "release_year": 2021,
                "chipset": "Exynos 2100 (5nm)", "cpu_architecture": "Octa-core 2.9GHz",
                "gpu": "Mali-G78 MP14", "antutu_benchmark_score": 740000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "12 MP (wide, OIS) + 64 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Hybrid Optical",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4800, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 200, "os_at_launch": "Android 11, One UI 3.1",
                "variants": [
                    {"variant_name": "Galaxy S21+ 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 15999000, "aliases": "s21 plus 128, s21+ 128"},
                    {"variant_name": "Galaxy S21+ 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 16999000, "aliases": "s21 plus 256, s21+ 256"}
                ]
            },
            {
                "name": "Galaxy S20 FE (Snapdragon)", "series": "Fan Edition", "release_year": 2020,
                "chipset": "Snapdragon 865 (7nm+)", "cpu_architecture": "Octa-core 2.84GHz",
                "gpu": "Adreno 650", "antutu_benchmark_score": 670000,
                "display_type": "Super AMOLED, 120Hz, HDR10+", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "12 MP (wide, OIS) + 8 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 190, "os_at_launch": "Android 10, One UI 2.5",
                "variants": [
                    {"variant_name": "Galaxy S20 FE 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 7999000, "aliases": "s20 fe 128, s20 fe snapdragon"},
                    {"variant_name": "Galaxy S20 FE 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 8999000, "aliases": "s20 fe 256, s20 fe snap"}
                ]
            },
            {
                "name": "Galaxy S10", "series": "S-Series Flagship", "release_year": 2019,
                "chipset": "Exynos 9820 (8nm)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G76 MP12", "antutu_benchmark_score": 420000,
                "display_type": "Dynamic AMOLED, HDR10+", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1440 x 3040 pixels (QHD+)", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "12 MP (wide, dual aperture f/1.5-2.4, OIS) + 12 MP (2x telephoto OIS) + 16 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "10 MP, f/1.9, Dual Pixel PDAF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3400, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 157, "os_at_launch": "Android 9 (Pie), One UI",
                "variants": [
                    {"variant_name": "Galaxy S10 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 12999000, "aliases": "s10 128, samsung s10 128gb"}
                ]
            },
            {
                "name": "Galaxy S10e", "series": "Compact Flagship", "release_year": 2019,
                "chipset": "Exynos 9820 (8nm)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G76 MP12", "antutu_benchmark_score": 415000,
                "display_type": "Dynamic AMOLED, HDR10+", "screen_size_inch": 5.8,
                "refresh_rate_hz": 60, "resolution": "1080 x 2280 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP (wide, dual aperture f/1.5-2.4, OIS) + 16 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "10 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3100, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 150, "os_at_launch": "Android 9 (Pie), One UI",
                "variants": [
                    {"variant_name": "Galaxy S10e 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 10499000, "aliases": "s10e 128, samsung s10e"}
                ]
            },
            {
                "name": "Galaxy S9+", "series": "S-Series Flagship", "release_year": 2018,
                "chipset": "Exynos 9810 (10nm)", "cpu_architecture": "Octa-core 2.7GHz",
                "gpu": "Mali-G72 MP18", "antutu_benchmark_score": 345000,
                "display_type": "Super AMOLED, HDR10", "screen_size_inch": 6.2,
                "refresh_rate_hz": 60, "resolution": "1440 x 2960 pixels (QHD+)", "peak_brightness_nits": 1050,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP (wide, dual aperture f/1.5-2.4, OIS) + 12 MP (2x telephoto OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "8 MP, f/1.7, AF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3500, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 189, "os_at_launch": "Android 8.0 (Oreo)",
                "variants": [
                    {"variant_name": "Galaxy S9+ 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 12999000, "aliases": "s9 plus 64, s9+ 64"},
                    {"variant_name": "Galaxy S9+ 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 14499000, "aliases": "s9 plus 128, s9+ 128"}
                ]
            },
            {
                "name": "Galaxy Note 8", "series": "Note S-Pen Flagship", "release_year": 2017,
                "chipset": "Exynos 8895 (10nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Mali-G71 MP20", "antutu_benchmark_score": 260000,
                "display_type": "Super AMOLED, HDR10", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1440 x 2960 pixels (QHD+)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (2x telephoto OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "8 MP, f/1.7, AF", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3300, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 195, "os_at_launch": "Android 7.1.1 (Nougat)",
                "variants": [
                    {"variant_name": "Galaxy Note 8 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 12999000, "aliases": "note 8 64, samsung note 8"}
                ]
            },
            {
                "name": "Galaxy Note 5", "series": "Note S-Pen Glass/Metal", "release_year": 2015,
                "chipset": "Exynos 7420 Octa (14nm)", "cpu_architecture": "Octa-core 2.1GHz",
                "gpu": "Mali-T760MP8", "antutu_benchmark_score": 125000,
                "display_type": "Super AMOLED", "screen_size_inch": 5.7,
                "refresh_rate_hz": 60, "resolution": "1440 x 2560 pixels (QHD)", "peak_brightness_nits": 860,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "16 MP, f/1.9, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/1.9", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 171, "os_at_launch": "Android 5.1.1 (Lollipop)",
                "variants": [
                    {"variant_name": "Galaxy Note 5 32GB", "ram_gb": 4, "storage_gb": 32, "official_msrp_new": 9999000, "aliases": "note 5 32, note 5 32gb"}
                ]
            },
            {
                "name": "Galaxy Note 3", "series": "Note Faux Leather", "release_year": 2013,
                "chipset": "Exynos 5420 Octa (28nm)", "cpu_architecture": "Octa-core (4x1.9GHz + 4x1.3GHz)",
                "gpu": "Mali-T628 MP6", "antutu_benchmark_score": 45000,
                "display_type": "Super AMOLED FHD", "screen_size_inch": 5.7,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 660,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP, f/2.2, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP, f/2.4", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 3200, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA+", "has_nfc": True, "ip_rating": "None", "weight_grams": 168, "os_at_launch": "Android 4.3 (Jelly Bean)",
                "variants": [
                    {"variant_name": "Galaxy Note 3 32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 8880000, "aliases": "note 3 32, samsung note 3"}
                ]
            },
            {
                "name": "Galaxy S III (I9300)", "series": "Designed for Humans", "release_year": 2012,
                "chipset": "Exynos 4412 Quad (32nm)", "cpu_architecture": "Quad-core 1.4GHz Cortex-A9",
                "gpu": "Mali-400MP4", "antutu_benchmark_score": 24000,
                "display_type": "Super AMOLED HD", "screen_size_inch": 4.8,
                "refresh_rate_hz": 60, "resolution": "720 x 1280 pixels", "peak_brightness_nits": 330,
                "screen_protection": "Corning Gorilla Glass 2",
                "main_camera_mp": "8 MP, f/2.6, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.9 MP", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 2100, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA+", "has_nfc": True, "ip_rating": "None", "weight_grams": 133, "os_at_launch": "Android 4.0.4 (Ice Cream Sandwich)",
                "variants": [
                    {"variant_name": "Galaxy S III 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 6499000, "aliases": "galaxy s3, s3 16gb, i9300"}
                ]
            },
            {
                "name": "Galaxy A51", "series": "A-Series Midrange", "release_year": 2020,
                "chipset": "Exynos 9611 (10nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Mali-G72 MP3", "antutu_benchmark_score": 210000,
                "display_type": "Super AMOLED Infinity-O", "screen_size_inch": 6.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "48 MP (wide) + 12 MP (ultrawide) + 5 MP (macro) + 5 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 15, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 172, "os_at_launch": "Android 10, One UI 2.0",
                "variants": [
                    {"variant_name": "Galaxy A51 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 4399000, "aliases": "samsung a51 128, a51 6/128"},
                    {"variant_name": "Galaxy A51 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4699000, "aliases": "samsung a51 8/128, a51 8gb"}
                ]
            },
            {
                "name": "Galaxy A50", "series": "A-Series Midrange", "release_year": 2019,
                "chipset": "Exynos 9610 (10nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Mali-G72 MP3", "antutu_benchmark_score": 180000,
                "display_type": "Super AMOLED Infinity-U", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 550,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "25 MP (wide) + 8 MP (ultrawide) + 5 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "25 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 15, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 166, "os_at_launch": "Android 9 (Pie), One UI",
                "variants": [
                    {"variant_name": "Galaxy A50 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 3799000, "aliases": "samsung a50 64, a50 4/64"},
                    {"variant_name": "Galaxy A50 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 4399000, "aliases": "samsung a50 128, a50 6/128"}
                ]
            }
        ]
    },

    # ==================== 2. APPLE BATCH 2 ====================
    {
        "brand_name": "Apple",
        "models": [
            {
                "name": "iPhone 11 Pro", "series": "Pro", "release_year": 2019,
                "chipset": "Apple A13 Bionic (7nm+)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 850000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 5.8,
                "refresh_rate_hz": 60, "resolution": "1125 x 2436 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (2x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3046, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 188, "os_at_launch": "iOS 13",
                "variants": [
                    {"variant_name": "iPhone 11 Pro 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 18499000, "aliases": "11 pro 64, ip 11 pro 64, iphone 11 pro 64gb"},
                    {"variant_name": "iPhone 11 Pro 256GB", "ram_gb": 4, "storage_gb": 256, "official_msrp_new": 21999000, "aliases": "11 pro 256, ip 11 pro 256, iphone 11 pro 256gb"}
                ]
            },
            {
                "name": "iPhone XS Max", "series": "XS Max", "release_year": 2018,
                "chipset": "Apple A12 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 650000,
                "display_type": "Super Retina OLED, HDR10", "screen_size_inch": 6.5,
                "refresh_rate_hz": 60, "resolution": "1242 x 2688 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (2x telephoto OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3174, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 208, "os_at_launch": "iOS 12",
                "variants": [
                    {"variant_name": "iPhone XS Max 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 22499000, "aliases": "xs max 64, ip xs max 64, iphone xs max 64gb"},
                    {"variant_name": "iPhone XS Max 256GB", "ram_gb": 4, "storage_gb": 256, "official_msrp_new": 25499000, "aliases": "xs max 256, ip xs max 256, iphone xs max 256gb"}
                ]
            },
            {
                "name": "iPhone XS", "series": "XS", "release_year": 2018,
                "chipset": "Apple A12 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 630000,
                "display_type": "Super Retina OLED, HDR10", "screen_size_inch": 5.8,
                "refresh_rate_hz": 60, "resolution": "1125 x 2436 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (2x telephoto OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2658, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 177, "os_at_launch": "iOS 12",
                "variants": [
                    {"variant_name": "iPhone XS 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 20499000, "aliases": "ip xs 64, iphone xs 64gb"},
                    {"variant_name": "iPhone XS 256GB", "ram_gb": 4, "storage_gb": 256, "official_msrp_new": 23499000, "aliases": "ip xs 256, iphone xs 256gb"}
                ]
            },
            {
                "name": "iPhone 6 Plus", "series": "Plus", "release_year": 2014,
                "chipset": "Apple A8 (20nm)", "cpu_architecture": "Dual-core 1.4GHz Typhoon",
                "gpu": "PowerVR GX6450", "antutu_benchmark_score": 190000,
                "display_type": "IPS LCD Retina HD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "8 MP, f/2.2, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.2 MP, f/2.2", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 2915, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 172, "os_at_launch": "iOS 8",
                "variants": [
                    {"variant_name": "iPhone 6 Plus 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 12399000, "aliases": "6 plus 16, ip 6 plus 16"},
                    {"variant_name": "iPhone 6 Plus 64GB", "ram_gb": 1, "storage_gb": 64, "official_msrp_new": 13999000, "aliases": "6 plus 64, ip 6 plus 64"}
                ]
            },
            {
                "name": "iPhone SE (1st Gen)", "series": "SE", "release_year": 2016,
                "chipset": "Apple A9 (14nm)", "cpu_architecture": "Dual-core 1.84GHz Twister",
                "gpu": "PowerVR GT7600", "antutu_benchmark_score": 260000,
                "display_type": "IPS LCD", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "640 x 1136 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "12 MP, f/2.2",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.2 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 1624, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 113, "os_at_launch": "iOS 9.3",
                "variants": [
                    {"variant_name": "iPhone SE 1 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 6599000, "aliases": "se 1 16, ip se 2016 16gb"},
                    {"variant_name": "iPhone SE 1 64GB", "ram_gb": 2, "storage_gb": 64, "official_msrp_new": 7999000, "aliases": "se 1 64, ip se 2016 64gb"}
                ]
            }
        ]
    },

    # ==================== 3. XIAOMI / POCO / REDMI BATCH 2 ====================
    {
        "brand_name": "Xiaomi",
        "models": [
            {
                "name": "Poco F4", "series": "Poco F", "release_year": 2022,
                "chipset": "Snapdragon 870 5G (7nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 650", "antutu_benchmark_score": 730000,
                "display_type": "AMOLED, 120Hz, Dolby Vision, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.4", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 195, "os_at_launch": "Android 12, MIUI 13 for POCO",
                "variants": [
                    {"variant_name": "Poco F4 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 5199000, "aliases": "poco f4 128, f4 128gb"},
                    {"variant_name": "Poco F4 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5699000, "aliases": "poco f4 256, f4 256gb"}
                ]
            },
            {
                "name": "Poco F3", "series": "Poco F Flagship Killer", "release_year": 2021,
                "chipset": "Snapdragon 870 5G (7nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 650", "antutu_benchmark_score": 720000,
                "display_type": "AMOLED, 120Hz, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (wide) + 8 MP (ultrawide) + 5 MP (telemacro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4520, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 196, "os_at_launch": "Android 11, MIUI 12 for POCO",
                "variants": [
                    {"variant_name": "Poco F3 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "poco f3 128, f3 128gb"},
                    {"variant_name": "Poco F3 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "poco f3 256, f3 256gb"}
                ]
            },
            {
                "name": "Redmi Note 12 Pro 5G", "series": "Redmi Note", "release_year": 2023,
                "chipset": "MediaTek Dimensity 1080 (6nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 530000,
                "display_type": "OLED, 1B colors, 120Hz, Dolby Vision", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 187, "os_at_launch": "Android 12, MIUI 14",
                "variants": [
                    {"variant_name": "Redmi Note 12 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4599000, "aliases": "rn 12 pro 5g, redmi note 12 pro"}
                ]
            },
            {
                "name": "Redmi Note 8 Pro", "series": "Redmi Note Gaming", "release_year": 2019,
                "chipset": "MediaTek Helio G90T (12nm)", "cpu_architecture": "Octa-core 2.05GHz",
                "gpu": "Mali-G76 MC4", "antutu_benchmark_score": 290000,
                "display_type": "IPS LCD, HDR", "screen_size_inch": 6.53,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.0", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP52", "weight_grams": 200, "os_at_launch": "Android 9 (Pie), MIUI 10",
                "variants": [
                    {"variant_name": "Redmi Note 8 Pro 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 3099000, "aliases": "rn 8 pro 64, redmi note 8 pro 64gb"},
                    {"variant_name": "Redmi Note 8 Pro 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 3499000, "aliases": "rn 8 pro 128, redmi note 8 pro 128gb"}
                ]
            },
            {
                "name": "Redmi Note 4 (Snapdragon)", "series": "Battery King", "release_year": 2017,
                "chipset": "Snapdragon 625 (14nm)", "cpu_architecture": "Octa-core 2.0GHz Cortex-A53",
                "gpu": "Adreno 506", "antutu_benchmark_score": 85000,
                "display_type": "IPS LCD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "2.5D Curved Glass",
                "main_camera_mp": "13 MP, f/2.0, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 4100, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 165, "os_at_launch": "Android 6.0 (Marshmallow), MIUI 8",
                "variants": [
                    {"variant_name": "Redmi Note 4 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 2399000, "aliases": "rn 4 32, redmi note 4 32gb"},
                    {"variant_name": "Redmi Note 4 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2799000, "aliases": "rn 4 64, redmi note 4 64gb"}
                ]
            },
            {
                "name": "Xiaomi 12 Pro", "series": "Xiaomi Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1010000,
                "display_type": "LTPO AMOLED, 1B colors, 120Hz, Dolby Vision", "screen_size_inch": 6.73,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (2K)", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX707, OIS) + 50 MP (2x telephoto) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4600, "fast_charging_watt": 120, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 204, "os_at_launch": "Android 12, MIUI 13",
                "variants": [
                    {"variant_name": "Xiaomi 12 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 12999000, "aliases": "mi 12 pro 256, xiaomi 12 pro"}
                ]
            }
        ]
    },

    # ==================== 4. OPPO BATCH 2 ====================
    {
        "brand_name": "Oppo",
        "models": [
            {
                "name": "Oppo Find X3 Pro", "series": "Find X Flagship", "release_year": 2021,
                "chipset": "Snapdragon 888 5G (5nm)", "cpu_architecture": "Octa-core 2.84GHz",
                "gpu": "Adreno 660", "antutu_benchmark_score": 830000,
                "display_type": "LTPO AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1440 x 3216 pixels (QHD+)", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766, OIS) + 13 MP (telephoto 2x) + 50 MP (ultrawide) + 3 MP (microscope 60x)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "2x Optical & 60x Microlens",
                "selfie_camera_mp": "32 MP, f/2.4", "video_recording_max": "4K@60fps 10-bit",
                "battery_capacity_mah": 4500, "fast_charging_watt": 65, "has_wireless_charging": True, "wireless_charging_watt": 30,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 193, "os_at_launch": "Android 11, ColorOS 11.2",
                "variants": [
                    {"variant_name": "Oppo Find X3 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 15999000, "aliases": "find x3 pro, oppo x3 pro"}
                ]
            },
            {
                "name": "Oppo Reno 8 Pro 5G", "series": "Reno Pro", "release_year": 2022,
                "chipset": "MediaTek Dimensity 8100-MAX (5nm)", "cpu_architecture": "Octa-core 2.85GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 820000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766) + 8 MP (ultrawide) + 2 MP (macro) + MariSilicon X NPU",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.4, AF", "video_recording_max": "4K@30fps (4K Ultra Night)",
                "battery_capacity_mah": 4500, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 183, "os_at_launch": "Android 12, ColorOS 12.1",
                "variants": [
                    {"variant_name": "Oppo Reno 8 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 9999000, "aliases": "reno 8 pro 256, oppo reno 8 pro"}
                ]
            },
            {
                "name": "Oppo Reno 6 5G", "series": "Reno Portrait", "release_year": 2021,
                "chipset": "MediaTek Dimensity 900 (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 480000,
                "display_type": "AMOLED, 90Hz", "screen_size_inch": 6.43,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 750,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.4", "video_recording_max": "4K@30fps (Bokeh Flare Video)",
                "battery_capacity_mah": 4300, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 182, "os_at_launch": "Android 11, ColorOS 11.3",
                "variants": [
                    {"variant_name": "Oppo Reno 6 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 7999000, "aliases": "reno 6 5g, oppo reno 6"}
                ]
            },
            {
                "name": "Oppo F9", "series": "Waterdrop VOOC", "release_year": 2018,
                "chipset": "MediaTek Helio P60 (12nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Mali-G72 MP3", "antutu_benchmark_score": 140000,
                "display_type": "IPS LCD Waterdrop Screen", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "16 MP, f/1.8 + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "25 MP, f/2.0, HDR", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3500, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 169, "os_at_launch": "Android 8.1 (Oreo), ColorOS 5.2",
                "variants": [
                    {"variant_name": "Oppo F9 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 4299000, "aliases": "oppo f9 64, f9 4/64"}
                ]
            }
        ]
    },

    # ==================== 5. VIVO & IQOO BATCH 2 ====================
    {
        "brand_name": "Vivo",
        "models": [
            {
                "name": "Vivo X80 Pro", "series": "X-Series Zeiss Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1020000,
                "display_type": "LTPO3 AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (2K)", "peak_brightness_nits": 1500,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (GNV sensor, OIS) + 8 MP (5x periscope OIS) + 12 MP (2x gimbal telephoto) + 48 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "5x Periscope & Gimbal",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@30fps, 4K@60fps Zeiss Cinematic",
                "battery_capacity_mah": 4700, "fast_charging_watt": 80, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 219, "os_at_launch": "Android 12, Funtouch 12",
                "variants": [
                    {"variant_name": "Vivo X80 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 15999000, "aliases": "x80 pro 256, vivo x80 pro"}
                ]
            },
            {
                "name": "Vivo V29 5G", "series": "V-Series Aura Light", "release_year": 2023,
                "chipset": "Snapdragon 778G 5G (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 642L", "antutu_benchmark_score": 610000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP, f/2.0, AF (Group Selfie)", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4600, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 186, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "Vivo V29 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "v29 256, vivo v29 5g"},
                    {"variant_name": "Vivo V29 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 6999000, "aliases": "v29 512, vivo v29 512gb"}
                ]
            },
            {
                "name": "Vivo V15 Pro", "series": "Elevating Camera", "release_year": 2019,
                "chipset": "Snapdragon 675 (11nm)", "cpu_architecture": "Octa-core 2.0GHz",
                "gpu": "Adreno 612", "antutu_benchmark_score": 215000,
                "display_type": "Super AMOLED Ultra FullView", "screen_size_inch": 6.39,
                "refresh_rate_hz": 60, "resolution": "1080 x 2316 pixels", "peak_brightness_nits": 430,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (wide) + 8 MP (ultrawide) + 5 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP Motorized Pop-up, f/2.0", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3700, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 185, "os_at_launch": "Android 9 (Pie), Funtouch 9",
                "variants": [
                    {"variant_name": "Vivo V15 Pro 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 5699000, "aliases": "v15 pro 128, vivo v15 pro"}
                ]
            },
            {
                "name": "iQOO 11 5G", "series": "iQOO Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1580000,
                "display_type": "LTPO4 AMOLED 2K, 1B colors, 144Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1440 x 3200 pixels (2K)", "peak_brightness_nits": 1800,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Samsung GN5, OIS) + 13 MP (2x telephoto) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 208, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "iQOO 11 5G 16GB/256GB", "ram_gb": 16, "storage_gb": 256, "official_msrp_new": 10999000, "aliases": "iqoo 11 256, iqoo 11 5g"}
                ]
            }
        ]
    },

    # ==================== 6. REALME BATCH 2 ====================
    {
        "brand_name": "Realme",
        "models": [
            {
                "name": "Realme GT Master Edition", "series": "GT Suitcase Design", "release_year": 2021,
                "chipset": "Snapdragon 778G 5G (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 642L", "antutu_benchmark_score": 580000,
                "display_type": "Super AMOLED, 120Hz", "screen_size_inch": 6.43,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Asahi Glass",
                "main_camera_mp": "64 MP (wide) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP (Sony IMX615), f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4300, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 174, "os_at_launch": "Android 11, Realme UI 2.0",
                "variants": [
                    {"variant_name": "Realme GT Master Edition 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "gt master 128, realme gt me"},
                    {"variant_name": "Realme GT Master Edition 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "gt master 256, realme gt me 256"}
                ]
            },
            {
                "name": "Realme 9 Pro+ 5G", "series": "Number Pro+ Series", "release_year": 2022,
                "chipset": "MediaTek Dimensity 920 (6nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 520000,
                "display_type": "Super AMOLED, 90Hz, HDR10", "screen_size_inch": 6.4,
                "refresh_rate_hz": 90, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 60, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 182, "os_at_launch": "Android 12, Realme UI 3.0",
                "variants": [
                    {"variant_name": "Realme 9 Pro+ 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4999000, "aliases": "realme 9 pro+ 128, 9 pro plus 128"},
                    {"variant_name": "Realme 9 Pro+ 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "realme 9 pro+ 256, 9 pro plus 256"}
                ]
            },
            {
                "name": "Realme 5 Pro", "series": "Quad Camera Speed", "release_year": 2019,
                "chipset": "Snapdragon 712 (10nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Adreno 616", "antutu_benchmark_score": 220000,
                "display_type": "IPS LCD", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 3+",
                "main_camera_mp": "48 MP (Sony IMX586) + 8 MP (ultrawide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4035, "fast_charging_watt": 20, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "Splash resistant", "weight_grams": 184, "os_at_launch": "Android 9 (Pie), ColorOS 6",
                "variants": [
                    {"variant_name": "Realme 5 Pro 4GB/128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 2999000, "aliases": "realme 5 pro 128, 5 pro 4/128"},
                    {"variant_name": "Realme 5 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3699000, "aliases": "realme 5 pro 8/128, 5 pro 8gb"}
                ]
            }
        ]
    },

    # ==================== 7. INFINIX & TECNO BATCH 2 ====================
    {
        "brand_name": "Infinix",
        "models": [
            {
                "name": "Infinix GT 10 Pro", "series": "Gaming Cyber Mecha", "release_year": 2023,
                "chipset": "MediaTek Dimensity 8050 (6nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Mali-G77 MC9", "antutu_benchmark_score": 710000,
                "display_type": "AMOLED, 1B colors, 120Hz", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "108 MP (wide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 187, "os_at_launch": "Android 13, XOS 13 for GT",
                "variants": [
                    {"variant_name": "Infinix GT 10 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3499000, "aliases": "gt 10 pro 256, infinix gt 10 pro"}
                ]
            },
            {
                "name": "Infinix Note 30 Pro", "series": "Note Pro Wireless", "release_year": 2023,
                "chipset": "MediaTek Helio G99 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Mali-G57 MC2", "antutu_benchmark_score": 410000,
                "display_type": "AMOLED, 1B colors, 120Hz", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "108 MP (wide) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "1440p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 68, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 203, "os_at_launch": "Android 13, XOS 13",
                "variants": [
                    {"variant_name": "Infinix Note 30 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3099000, "aliases": "note 30 pro 256, infinix 30 pro"}
                ]
            }
        ]
    },

    # ==================== 8. GOOGLE PIXEL BATCH 2 ====================
    {
        "brand_name": "Google",
        "models": [
            {
                "name": "Pixel 9 Pro XL", "series": "Pixel AI Flagship", "release_year": 2024,
                "chipset": "Google Tensor G4 (4nm)", "cpu_architecture": "Octa-core 3.1GHz",
                "gpu": "Mali-G715 MC7", "antutu_benchmark_score": 1350000,
                "display_type": "LTPO OLED, 120Hz, HDR10+", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1344 x 2992 pixels", "peak_brightness_nits": 3000,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (5x periscope OIS) + 48 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope Optical",
                "selfie_camera_mp": "42 MP, f/2.2, PDAF", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5060, "fast_charging_watt": 37, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 221, "os_at_launch": "Android 14 (Gemini Nano)",
                "variants": [
                    {"variant_name": "Pixel 9 Pro XL 16GB/128GB", "ram_gb": 16, "storage_gb": 128, "official_msrp_new": 19999000, "aliases": "pixel 9 pro xl 128, p9pxl 128"},
                    {"variant_name": "Pixel 9 Pro XL 16GB/256GB", "ram_gb": 16, "storage_gb": 256, "official_msrp_new": 21999000, "aliases": "pixel 9 pro xl 256, p9pxl 256"}
                ]
            },
            {
                "name": "Pixel 6 Pro", "series": "Tensor Debut", "release_year": 2021,
                "chipset": "Google Tensor (5nm)", "cpu_architecture": "Octa-core 2.8GHz",
                "gpu": "Mali-G78 MP20", "antutu_benchmark_score": 750000,
                "display_type": "LTPO AMOLED, 120Hz, HDR10+", "screen_size_inch": 6.71,
                "refresh_rate_hz": 120, "resolution": "1440 x 3120 pixels (QHD+)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (4x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "4x Optical",
                "selfie_camera_mp": "11.1 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5003, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 210, "os_at_launch": "Android 12",
                "variants": [
                    {"variant_name": "Pixel 6 Pro 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 14999000, "aliases": "pixel 6 pro 128, p6p 128"}
                ]
            },
            {
                "name": "Pixel 2 XL", "series": "Computational Legend", "release_year": 2017,
                "chipset": "Snapdragon 835 (10nm)", "cpu_architecture": "Octa-core 2.35GHz",
                "gpu": "Adreno 540", "antutu_benchmark_score": 240000,
                "display_type": "P-OLED, HDR", "screen_size_inch": 6.0,
                "refresh_rate_hz": 60, "resolution": "1440 x 2880 pixels (QHD+)", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12.2 MP, f/1.8, OIS, Dual Pixel PDAF (Pixel Visual Core)",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3520, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 175, "os_at_launch": "Android 8.0 (Oreo)",
                "variants": [
                    {"variant_name": "Pixel 2 XL 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 11499000, "aliases": "pixel 2 xl 64, p2xl 64"}
                ]
            }
        ]
    },

    # ==================== 9. SONY XPERIA BATCH 2 ====================
    {
        "brand_name": "Sony",
        "models": [
            {
                "name": "Xperia XZ Premium", "series": "4K HDR Pioneer", "release_year": 2017,
                "chipset": "Snapdragon 835 (10nm)", "cpu_architecture": "Octa-core 2.45GHz",
                "gpu": "Adreno 540", "antutu_benchmark_score": 250000,
                "display_type": "IPS LCD, 4K HDR", "screen_size_inch": 5.46,
                "refresh_rate_hz": 60, "resolution": "3840 x 2160 pixels (4K UHD)", "peak_brightness_nits": 700,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "19 MP (Motion Eye, EIS, 960fps Slow-mo)",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.0", "video_recording_max": "4K@30fps, 720p@960fps",
                "battery_capacity_mah": 3230, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 195, "os_at_launch": "Android 7.1 (Nougat)",
                "variants": [
                    {"variant_name": "Xperia XZ Premium 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 9999000, "aliases": "xz premium, sony xz premium 64gb"}
                ]
            },
            {
                "name": "Xperia Z3 (D6603)", "series": "Waterproof Legend", "release_year": 2014,
                "chipset": "Snapdragon 801 (28nm)", "cpu_architecture": "Quad-core 2.5GHz Krait 400",
                "gpu": "Adreno 330", "antutu_benchmark_score": 48000,
                "display_type": "IPS LCD Triluminos Display", "screen_size_inch": 5.2,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Shatter proof glass",
                "main_camera_mp": "20.7 MP, f/2.0, 25mm Sony G Lens",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2.2 MP", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3100, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 152, "os_at_launch": "Android 4.4.4 (KitKat)",
                "variants": [
                    {"variant_name": "Xperia Z3 16GB", "ram_gb": 3, "storage_gb": 16, "official_msrp_new": 8499000, "aliases": "sony xperia z3, z3 16gb, d6603"}
                ]
            }
        ]
    },

    # ==================== 10. HUAWEI BATCH 2 ====================
    {
        "brand_name": "Huawei",
        "models": [
            {
                "name": "Huawei P20 Pro", "series": "Leica Triple Camera", "release_year": 2018,
                "chipset": "Kirin 970 (10nm)", "cpu_architecture": "Octa-core 2.4GHz + NPU",
                "gpu": "Mali-G72 MP12", "antutu_benchmark_score": 280000,
                "display_type": "OLED, HDR10", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1080 x 2240 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "40 MP (Leica, f/1.8, OIS) + 8 MP (3x telephoto OIS) + 20 MP (monochrome)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "24 MP, f/2.0", "video_recording_max": "4K@30fps (Handheld Night Mode)",
                "battery_capacity_mah": 4000, "fast_charging_watt": 22.5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 180, "os_at_launch": "EMUI 8.1 (Android 8.1)",
                "variants": [
                    {"variant_name": "Huawei P20 Pro 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 11999000, "aliases": "p20 pro 128, huawei p20 pro"}
                ]
            },
            {
                "name": "Huawei Mate 20 Pro", "series": "Matrix Triple Camera", "release_year": 2018,
                "chipset": "Kirin 980 (7nm)", "cpu_architecture": "Octa-core 2.6GHz Dual NPU",
                "gpu": "Mali-G76 MP10", "antutu_benchmark_score": 390000,
                "display_type": "OLED, HDR10, Curved", "screen_size_inch": 6.39,
                "refresh_rate_hz": 60, "resolution": "1440 x 3120 pixels (2K)", "peak_brightness_nits": 750,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "40 MP (wide) + 8 MP (3x telephoto OIS) + 20 MP (ultrawide Leica)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "24 MP + 3D Face Unlock", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4200, "fast_charging_watt": 40, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 189, "os_at_launch": "EMUI 9.0 (Android 9)",
                "variants": [
                    {"variant_name": "Huawei Mate 20 Pro 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 11999000, "aliases": "mate 20 pro 128, huawei mate 20"}
                ]
            }
        ]
    },

    # ==================== 11. ASUS ROG & ZENFONE BATCH 2 ====================
    {
        "brand_name": "Asus",
        "models": [
            {
                "name": "ROG Phone 7 Ultimate", "series": "Gaming Ultimate", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1620000,
                "display_type": "AMOLED, 1B colors, 165Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 165, "resolution": "1080 x 2448 pixels", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766) + 13 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 6000, "fast_charging_watt": 65, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 246, "os_at_launch": "Android 13, ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone 7 Ultimate 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 18999000, "aliases": "rog 7 ultimate 512, rog 7 ultimate"}
                ]
            },
            {
                "name": "Zenfone 9", "series": "Compact Gimbal Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8+ Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.19GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1080000,
                "display_type": "Super AMOLED, 120Hz, HDR10+", "screen_size_inch": 5.9,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1100,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766, 6-axis Hybrid Gimbal OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.5, Dual PDAF", "video_recording_max": "8K@24fps, 4K@60fps Gimbal",
                "battery_capacity_mah": 4300, "fast_charging_watt": 30, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 169, "os_at_launch": "Android 12, ZenUI",
                "variants": [
                    {"variant_name": "Zenfone 9 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 7999000, "aliases": "zenfone 9 128, asus zenfone 9"}
                ]
            }
        ]
    },

    # ==================== 12. NOTHING BATCH 2 ====================
    {
        "brand_name": "Nothing",
        "models": [
            {
                "name": "Nothing Phone (2a)", "series": "Glyph Value", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7200 Pro (4nm)", "cpu_architecture": "Octa-core 2.8GHz",
                "gpu": "Mali-G610 MC4", "antutu_benchmark_score": 710000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (wide, OIS) + 50 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 190, "os_at_launch": "Android 14, Nothing OS 2.5",
                "variants": [
                    {"variant_name": "Nothing Phone (2a) 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5999000, "aliases": "nothing 2a 128, phone 2a 128"},
                    {"variant_name": "Nothing Phone (2a) 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 6999000, "aliases": "nothing 2a 256, phone 2a 256"}
                ]
            }
        ]
    }
]
