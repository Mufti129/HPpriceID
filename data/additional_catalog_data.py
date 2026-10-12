"""
Dataset Tambahan Komprehensif Smartphone Pasar Indonesia (2010 - 2026).
Menambahkan puluhan model ikonik dan volume tinggi dari berbagai generasi:
Samsung (S, Note, Z, A series), Xiaomi/Poco/Redmi, Oppo, Vivo/iQOO, Realme, Infinix/Tecno, Google Pixel, Sony Xperia, Huawei.
"""

ADDITIONAL_CATALOG_MODELS = [
    # ==================== APPLE EXPANSION ====================
    {
        "brand_name": "Apple",
        "models": [
            {
                "name": "iPhone 16 Plus", "series": "Plus", "release_year": 2024,
                "chipset": "Apple A18 (3nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1680000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1290 x 2796 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Sensor",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4674, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 25,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 199, "os_at_launch": "iOS 18",
                "variants": [
                    {"variant_name": "iPhone 16 Plus 128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 18499000, "aliases": "ip 16 plus 128, iphone 16 plus 128gb"},
                    {"variant_name": "iPhone 16 Plus 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 21499000, "aliases": "ip 16 plus 256, iphone 16 plus 256gb"}
                ]
            },
            {
                "name": "iPhone 15 Plus", "series": "Plus", "release_year": 2023,
                "chipset": "Apple A16 Bionic (4nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1390000,
                "display_type": "Super Retina XDR OLED (Dynamic Island)", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1290 x 2796 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Sensor",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4383, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 201, "os_at_launch": "iOS 17",
                "variants": [
                    {"variant_name": "iPhone 15 Plus 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 18499000, "aliases": "ip 15 plus 128, iphone 15 plus 128gb"},
                    {"variant_name": "iPhone 15 Plus 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 21499000, "aliases": "ip 15 plus 256, iphone 15 plus 256gb"}
                ]
            },
            {
                "name": "iPhone 14 Pro", "series": "Pro", "release_year": 2022,
                "chipset": "Apple A16 Bionic (4nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1410000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1179 x 2556 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3200, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 206, "os_at_launch": "iOS 16",
                "variants": [
                    {"variant_name": "iPhone 14 Pro 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 19999000, "aliases": "14 pro 128, ip 14 pro 128, iphone 14 pro 128gb"},
                    {"variant_name": "iPhone 14 Pro 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 22999000, "aliases": "14 pro 256, ip 14 pro 256, iphone 14 pro 256gb"}
                ]
            },
            {
                "name": "iPhone 13 mini", "series": "Mini", "release_year": 2021,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 1150000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 5.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2438, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 12,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 141, "os_at_launch": "iOS 15",
                "variants": [
                    {"variant_name": "iPhone 13 mini 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 12999000, "aliases": "13 mini 128, ip 13 mini 128"}
                ]
            },
            {
                "name": "iPhone 12 mini", "series": "Mini", "release_year": 2020,
                "chipset": "Apple A14 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 960000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 5.4,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2227, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 12,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 135, "os_at_launch": "iOS 14",
                "variants": [
                    {"variant_name": "iPhone 12 mini 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 12999000, "aliases": "12 mini 64, ip 12 mini 64"},
                    {"variant_name": "iPhone 12 mini 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 14499000, "aliases": "12 mini 128, ip 12 mini 128"}
                ]
            },
            {
                "name": "iPhone SE (3rd Gen)", "series": "SE", "release_year": 2022,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 1100000,
                "display_type": "Retina IPS LCD", "screen_size_inch": 4.7,
                "refresh_rate_hz": 60, "resolution": "750 x 1334 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP, f/1.8, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2018, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 144, "os_at_launch": "iOS 15.4",
                "variants": [
                    {"variant_name": "iPhone SE 3 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 7999000, "aliases": "se 3 64, se 2022 64, ip se 3 64"},
                    {"variant_name": "iPhone SE 3 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 9499000, "aliases": "se 3 128, se 2022 128, ip se 3 128"}
                ]
            },
            {
                "name": "iPhone SE (2nd Gen)", "series": "SE", "release_year": 2020,
                "chipset": "Apple A13 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 750000,
                "display_type": "Retina IPS LCD", "screen_size_inch": 4.7,
                "refresh_rate_hz": 60, "resolution": "750 x 1334 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP, f/1.8, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 1821, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 148, "os_at_launch": "iOS 13",
                "variants": [
                    {"variant_name": "iPhone SE 2 64GB", "ram_gb": 3, "storage_gb": 64, "official_msrp_new": 7999000, "aliases": "se 2 64, se 2020 64, ip se 2 64"},
                    {"variant_name": "iPhone SE 2 128GB", "ram_gb": 3, "storage_gb": 128, "official_msrp_new": 8999000, "aliases": "se 2 128, se 2020 128, ip se 2 128"}
                ]
            },
            {
                "name": "iPhone 8 Plus", "series": "Plus", "release_year": 2017,
                "chipset": "Apple A11 Bionic (10nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (3-core)", "antutu_benchmark_score": 500000,
                "display_type": "Retina IPS LCD, True Tone", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (telephoto 2x)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2691, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 202, "os_at_launch": "iOS 11",
                "variants": [
                    {"variant_name": "iPhone 8 Plus 64GB", "ram_gb": 3, "storage_gb": 64, "official_msrp_new": 14499000, "aliases": "8 plus 64, ip 8 plus 64, iphone 8 plus 64gb"},
                    {"variant_name": "iPhone 8 Plus 128GB", "ram_gb": 3, "storage_gb": 128, "official_msrp_new": 16499000, "aliases": "8 plus 128, ip 8 plus 128, iphone 8 plus 128gb"}
                ]
            },
            {
                "name": "iPhone 8", "series": "Standard", "release_year": 2017,
                "chipset": "Apple A11 Bionic (10nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (3-core)", "antutu_benchmark_score": 490000,
                "display_type": "Retina IPS LCD", "screen_size_inch": 4.7,
                "refresh_rate_hz": 60, "resolution": "750 x 1334 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP, f/1.8, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 1821, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 148, "os_at_launch": "iOS 11",
                "variants": [
                    {"variant_name": "iPhone 8 64GB", "ram_gb": 2, "storage_gb": 64, "official_msrp_new": 12599000, "aliases": "ip 8 64, iphone 8 64gb"}
                ]
            },
            {
                "name": "iPhone 7", "series": "Standard", "release_year": 2016,
                "chipset": "Apple A10 Fusion (16nm)", "cpu_architecture": "Quad-core 2.34GHz",
                "gpu": "PowerVR Series7XT Plus", "antutu_benchmark_score": 360000,
                "display_type": "Retina IPS LCD", "screen_size_inch": 4.7,
                "refresh_rate_hz": 60, "resolution": "750 x 1334 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP, f/1.8, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 1960, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 138, "os_at_launch": "iOS 10",
                "variants": [
                    {"variant_name": "iPhone 7 32GB", "ram_gb": 2, "storage_gb": 32, "official_msrp_new": 11999000, "aliases": "ip 7 32, iphone 7 32gb"},
                    {"variant_name": "iPhone 7 128GB", "ram_gb": 2, "storage_gb": 128, "official_msrp_new": 13699000, "aliases": "ip 7 128, iphone 7 128gb"}
                ]
            },
            {
                "name": "iPhone 6", "series": "Standard", "release_year": 2014,
                "chipset": "Apple A8 (20nm)", "cpu_architecture": "Dual-core 1.4GHz Typhoon",
                "gpu": "PowerVR GX6450", "antutu_benchmark_score": 180000,
                "display_type": "IPS LCD", "screen_size_inch": 4.7,
                "refresh_rate_hz": 60, "resolution": "750 x 1334 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "8 MP, f/2.2, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.2 MP, f/2.2", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 1810, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 129, "os_at_launch": "iOS 8",
                "variants": [
                    {"variant_name": "iPhone 6 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 10799000, "aliases": "ip 6 16, iphone 6 16gb"},
                    {"variant_name": "iPhone 6 64GB", "ram_gb": 1, "storage_gb": 64, "official_msrp_new": 12399000, "aliases": "ip 6 64, iphone 6 64gb"}
                ]
            },
            {
                "name": "iPhone 5", "series": "Standard", "release_year": 2012,
                "chipset": "Apple A6 (32nm)", "cpu_architecture": "Dual-core 1.3GHz Swift",
                "gpu": "PowerVR SGX543MP3", "antutu_benchmark_score": 95000,
                "display_type": "IPS LCD", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "640 x 1136 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "8 MP, f/2.4, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.2 MP, f/2.4", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 1440, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 112, "os_at_launch": "iOS 6",
                "variants": [
                    {"variant_name": "iPhone 5 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 8999000, "aliases": "ip 5 16, iphone 5 16gb"}
                ]
            },
            {
                "name": "iPhone 4s", "series": "Siri Pioneer", "release_year": 2011,
                "chipset": "Apple A5 (45nm)", "cpu_architecture": "Dual-core 1.0GHz Cortex-A9",
                "gpu": "PowerVR SGX543MP2", "antutu_benchmark_score": 60000,
                "display_type": "IPS LCD Retina Display", "screen_size_inch": 3.5,
                "refresh_rate_hz": 60, "resolution": "640 x 960 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "8 MP, f/2.4, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "VGA (0.3 MP)", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 1432, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 140, "os_at_launch": "iOS 5",
                "variants": [
                    {"variant_name": "iPhone 4s 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 7799000, "aliases": "ip 4s 16, iphone 4s 16gb"}
                ]
            }
        ]
    },

    # ==================== SAMSUNG EXPANSION ====================
    {
        "brand_name": "Samsung",
        "models": [
            {
                "name": "Galaxy S23", "series": "S-Series Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.36GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1520000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1750,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 3900, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 168, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy S23 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 12999000, "aliases": "s23 128, samsung s23 128gb"},
                    {"variant_name": "Galaxy S23 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 13999000, "aliases": "s23 256, samsung s23 256gb"}
                ]
            },
            {
                "name": "Galaxy S21 Ultra 5G", "series": "S-Series Flagship", "release_year": 2021,
                "chipset": "Exynos 2100 (5nm)", "cpu_architecture": "Octa-core 2.9GHz",
                "gpu": "Mali-G78 MP14", "antutu_benchmark_score": 750000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels (QHD+)", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "108 MP (wide, OIS) + 10 MP (10x periscope) + 10 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "10x Periscope",
                "selfie_camera_mp": "40 MP, f/2.2, PDAF", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 227, "os_at_launch": "Android 11, One UI 3.1",
                "variants": [
                    {"variant_name": "Galaxy S21 Ultra 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 18999000, "aliases": "s21 ultra 128, s21u 128"},
                    {"variant_name": "Galaxy S21 Ultra 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 19999000, "aliases": "s21 ultra 256, s21u 256"}
                ]
            },
            {
                "name": "Galaxy Z Flip 5", "series": "Z-Flip Foldable", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.36GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1500000,
                "display_type": "Foldable Dynamic AMOLED 2X, 120Hz", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2640 pixels", "peak_brightness_nits": 1750,
                "screen_protection": "Gorilla Glass Victus 2 (Cover)",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3700, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IPX8", "weight_grams": 187, "os_at_launch": "Android 13, One UI 5.1.1",
                "variants": [
                    {"variant_name": "Galaxy Z Flip 5 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 15999000, "aliases": "flip 5 256, z flip 5 256gb"},
                    {"variant_name": "Galaxy Z Flip 5 8GB/512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 17999000, "aliases": "flip 5 512, z flip 5 512gb"}
                ]
            },
            {
                "name": "Galaxy A54 5G", "series": "A-Series Midrange", "release_year": 2023,
                "chipset": "Exynos 1380 (5nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Mali-G68 MP5", "antutu_benchmark_score": 580000,
                "display_type": "Super AMOLED, 120Hz, HDR10+", "screen_size_inch": 6.4,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (wide, OIS) + 12 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 202, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy A54 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 5999000, "aliases": "a54 128, samsung a54 128gb"},
                    {"variant_name": "Galaxy A54 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6399000, "aliases": "a54 256, samsung a54 256gb"}
                ]
            },
            {
                "name": "Galaxy A52s 5G", "series": "A-Series Midrange", "release_year": 2021,
                "chipset": "Snapdragon 778G 5G (6nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 642L", "antutu_benchmark_score": 590000,
                "display_type": "Super AMOLED, 120Hz", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 12 MP (ultrawide) + 5 MP (macro) + 5 MP (depth)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 189, "os_at_launch": "Android 11, One UI 3.1",
                "variants": [
                    {"variant_name": "Galaxy A52s 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6499000, "aliases": "a52s 256, samsung a52s 5g"}
                ]
            },
            {
                "name": "Galaxy Note 9", "series": "Note-Series S-Pen", "release_year": 2018,
                "chipset": "Exynos 9810 (10nm)", "cpu_architecture": "Octa-core 2.7GHz",
                "gpu": "Mali-G72 MP18", "antutu_benchmark_score": 340000,
                "display_type": "Super AMOLED, HDR10", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1440 x 2960 pixels (QHD+)", "peak_brightness_nits": 1050,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP (wide, dual aperture f/1.5-2.4, OIS) + 12 MP (2x telephoto, OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "8 MP, f/1.7, AF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 201, "os_at_launch": "Android 8.1 (Oreo)",
                "variants": [
                    {"variant_name": "Galaxy Note 9 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 13499000, "aliases": "note 9 128, samsung note 9 128gb"}
                ]
            },
            {
                "name": "Galaxy S7 edge", "series": "S-Series Flagship", "release_year": 2016,
                "chipset": "Exynos 8890 Octa (14nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Mali-T880 MP12", "antutu_benchmark_score": 180000,
                "display_type": "Super AMOLED Dual-Edge Curved", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1440 x 2560 pixels (QHD)", "peak_brightness_nits": 855,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "12 MP, f/1.7, Dual Pixel PDAF, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/1.7", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3600, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 157, "os_at_launch": "Android 6.0 (Marshmallow)",
                "variants": [
                    {"variant_name": "Galaxy S7 edge 32GB", "ram_gb": 4, "storage_gb": 32, "official_msrp_new": 10499000, "aliases": "s7 edge 32, s7 edge"}
                ]
            },
            {
                "name": "Galaxy Note II (N7100)", "series": "Note Pioneer", "release_year": 2012,
                "chipset": "Exynos 4412 Quad (32nm)", "cpu_architecture": "Quad-core 1.6GHz Cortex-A9",
                "gpu": "Mali-400MP4", "antutu_benchmark_score": 38000,
                "display_type": "Super AMOLED HD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "720 x 1280 pixels", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass 2",
                "main_camera_mp": "8 MP, f/2.6, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.9 MP", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3100, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA", "has_nfc": True, "ip_rating": "None", "weight_grams": 183, "os_at_launch": "Android 4.1 (Jelly Bean)",
                "variants": [
                    {"variant_name": "Galaxy Note II 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 7499000, "aliases": "note 2, note ii 16gb"}
                ]
            },
            {
                "name": "Galaxy S II (I9100)", "series": "S Pioneer", "release_year": 2011,
                "chipset": "Exynos 4210 Dual (45nm)", "cpu_architecture": "Dual-core 1.2GHz Cortex-A9",
                "gpu": "Mali-400MP4", "antutu_benchmark_score": 19000,
                "display_type": "Super AMOLED Plus", "screen_size_inch": 4.3,
                "refresh_rate_hz": 60, "resolution": "480 x 800 pixels", "peak_brightness_nits": 350,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "8 MP, f/2.65, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 1650, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA", "has_nfc": True, "ip_rating": "None", "weight_grams": 116, "os_at_launch": "Android 2.3 (Gingerbread)",
                "variants": [
                    {"variant_name": "Galaxy S II 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 5499000, "aliases": "galaxy s2, s2 16gb"}
                ]
            }
        ]
    },

    # ==================== XIAOMI / POCO / REDMI EXPANSION ====================
    {
        "brand_name": "Xiaomi",
        "models": [
            {
                "name": "Poco F5", "series": "Poco F", "release_year": 2023,
                "chipset": "Snapdragon 7+ Gen 2 (4nm)", "cpu_architecture": "Octa-core 2.91GHz",
                "gpu": "Adreno 725", "antutu_benchmark_score": 1130000,
                "display_type": "AMOLED, 68B colors, 120Hz, Dolby Vision, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 181, "os_at_launch": "Android 13, MIUI 14 for POCO",
                "variants": [
                    {"variant_name": "Poco F5 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4999000, "aliases": "poco f5 256, f5 256gb"},
                    {"variant_name": "Poco F5 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 5499000, "aliases": "poco f5 12/256, f5 12gb"}
                ]
            },
            {
                "name": "Poco X6 Pro 5G", "series": "Poco X", "release_year": 2024,
                "chipset": "MediaTek Dimensity 8300 Ultra (4nm)", "cpu_architecture": "Octa-core 3.35GHz",
                "gpu": "Mali-G615-MC6", "antutu_benchmark_score": 1400000,
                "display_type": "AMOLED, 68B colors, 120Hz, Dolby Vision, HDR10+", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1220 x 2712 pixels (1.5K)", "peak_brightness_nits": 1800,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "64 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 186, "os_at_launch": "Android 14, HyperOS",
                "variants": [
                    {"variant_name": "Poco X6 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 4999000, "aliases": "x6 pro 512, poco x6 pro"}
                ]
            },
            {
                "name": "Poco X3 Pro", "series": "Poco X", "release_year": 2021,
                "chipset": "Snapdragon 860 (7nm)", "cpu_architecture": "Octa-core 2.96GHz",
                "gpu": "Adreno 640", "antutu_benchmark_score": 560000,
                "display_type": "IPS LCD, 120Hz, HDR10", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "48 MP (wide) + 8 MP (ultrawide) + 2 MP + 2 MP",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5160, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 215, "os_at_launch": "Android 11, MIUI 12 for POCO",
                "variants": [
                    {"variant_name": "Poco X3 Pro 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 3599000, "aliases": "x3 pro 128, poco x3 pro 128gb"},
                    {"variant_name": "Poco X3 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4099000, "aliases": "x3 pro 256, poco x3 pro 256gb"}
                ]
            },
            {
                "name": "Redmi Note 10 Pro", "series": "Redmi Note", "release_year": 2021,
                "chipset": "Snapdragon 732G (8nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Adreno 618", "antutu_benchmark_score": 340000,
                "display_type": "AMOLED, 120Hz, HDR10", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "108 MP (wide) + 8 MP (ultrawide) + 5 MP (telemacro) + 2 MP (depth)",
                "camera_setup": "Quad", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5020, "fast_charging_watt": 33, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 193, "os_at_launch": "Android 11, MIUI 12",
                "variants": [
                    {"variant_name": "Redmi Note 10 Pro 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 3499000, "aliases": "rn 10 pro 64, redmi note 10 pro 64gb"},
                    {"variant_name": "Redmi Note 10 Pro 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 3899000, "aliases": "rn 10 pro 128, redmi note 10 pro 128gb"}
                ]
            },
            {
                "name": "Redmi Note 7", "series": "Redmi Note", "release_year": 2019,
                "chipset": "Snapdragon 660 AIE (14nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "Adreno 512", "antutu_benchmark_score": 170000,
                "display_type": "IPS LCD", "screen_size_inch": 6.3,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "48 MP (Samsung GM1) + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "13 MP, f/2.2", "video_recording_max": "1080p@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 186, "os_at_launch": "Android 9 (Pie), MIUI 10",
                "variants": [
                    {"variant_name": "Redmi Note 7 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 2599000, "aliases": "rn 7 64, redmi note 7 64gb"}
                ]
            },
            {
                "name": "Xiaomi 13T", "series": "T-Series Flagship Killer", "release_year": 2023,
                "chipset": "MediaTek Dimensity 8200 Ultra (4nm)", "cpu_architecture": "Octa-core 3.1GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 900000,
                "display_type": "CrystalRes AMOLED, 68B colors, 144Hz, Leica Optic", "screen_size_inch": 6.67,
                "refresh_rate_hz": 144, "resolution": "1220 x 2712 pixels (1.5K)", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Leica, OIS) + 50 MP (Leica 2x telephoto) + 12 MP (Leica ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "20 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 197, "os_at_launch": "Android 13, MIUI 14",
                "variants": [
                    {"variant_name": "Xiaomi 13T 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 6499000, "aliases": "mi 13t 256, xiaomi 13t 12/256"}
                ]
            }
        ]
    },

    # ==================== VIVO / IQOO EXPANSION ====================
    {
        "brand_name": "Vivo",
        "models": [
            {
                "name": "Vivo V30 Pro", "series": "V-Series Portrait", "release_year": 2024,
                "chipset": "MediaTek Dimensity 8200 (4nm)", "cpu_architecture": "Octa-core 3.1GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 960000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 2800,
                "screen_protection": "Schott Alpha Glass",
                "main_camera_mp": "50 MP (Zeiss, OIS) + 50 MP (Zeiss 2x telephoto) + 50 MP (Zeiss ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "50 MP, f/2.0, AF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 188, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "Vivo V30 Pro 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 8999000, "aliases": "v30 pro 512, vivo v30 pro"}
                ]
            },
            {
                "name": "Vivo V27 5G", "series": "V-Series Aura Light", "release_year": 2023,
                "chipset": "MediaTek Dimensity 7200 (4nm)", "cpu_architecture": "Octa-core 2.8GHz",
                "gpu": "Mali-G610 MC4", "antutu_benchmark_score": 620000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Schott Xensation Up",
                "main_camera_mp": "50 MP (Sony IMX766V, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "50 MP, f/2.5, AF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4600, "fast_charging_watt": 66, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 180, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "Vivo V27 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "v27 256, vivo v27 5g"}
                ]
            },
            {
                "name": "iQOO Z7 5G", "series": "iQOO Performance", "release_year": 2023,
                "chipset": "Snapdragon 782G (6nm)", "cpu_architecture": "Octa-core 2.7GHz",
                "gpu": "Adreno 642L", "antutu_benchmark_score": 670000,
                "display_type": "IPS LCD, 120Hz, HDR10", "screen_size_inch": 6.64,
                "refresh_rate_hz": 120, "resolution": "1080 x 2388 pixels", "peak_brightness_nits": 650,
                "screen_protection": "Panda Glass",
                "main_camera_mp": "64 MP (wide, OIS) + 2 MP (depth)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 201, "os_at_launch": "Android 13, Funtouch 13",
                "variants": [
                    {"variant_name": "iQOO Z7 5G 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 4299000, "aliases": "iqoo z7 128, z7 5g 128gb"},
                    {"variant_name": "iQOO Z7 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 4899000, "aliases": "iqoo z7 256, z7 5g 256gb"}
                ]
            }
        ]
    },

    # ==================== OPPO EXPANSION ====================
    {
        "brand_name": "Oppo",
        "models": [
            {
                "name": "Oppo Find X5 Pro", "series": "Find X Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1020000,
                "display_type": "LTPO2 AMOLED, 1B colors, 120Hz, Hasselblad", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1440 x 3216 pixels (QHD+)", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Sony IMX766, 5-axis OIS) + 13 MP (telephoto 2x) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.4", "video_recording_max": "4K@60fps (MariSilicon X)",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 218, "os_at_launch": "Android 12, ColorOS 12.1",
                "variants": [
                    {"variant_name": "Oppo Find X5 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 14999000, "aliases": "find x5 pro, oppo x5 pro 256gb"}
                ]
            },
            {
                "name": "Oppo Reno 10 Pro+ 5G", "series": "Reno Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8+ Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1290000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.74,
                "refresh_rate_hz": 120, "resolution": "1240 x 2772 pixels (1.5K)", "peak_brightness_nits": 1400,
                "screen_protection": "Asahi Glass AGC DT-Star2",
                "main_camera_mp": "50 MP (Sony IMX890, OIS) + 64 MP (periscope 3x OIS) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Periscope",
                "selfie_camera_mp": "32 MP, f/2.4, AF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4700, "fast_charging_watt": 100, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 194, "os_at_launch": "Android 13, ColorOS 13.1",
                "variants": [
                    {"variant_name": "Oppo Reno 10 Pro+ 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 10999000, "aliases": "reno 10 pro+ 256, reno 10 pro plus"}
                ]
            },
            {
                "name": "Oppo F1s", "series": "Selfie Expert", "release_year": 2016,
                "chipset": "MediaTek MT6750 (28nm)", "cpu_architecture": "Octa-core 1.5GHz Cortex-A53",
                "gpu": "Mali-T860MP2", "antutu_benchmark_score": 55000,
                "display_type": "IPS LCD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "720 x 1280 pixels", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass 4",
                "main_camera_mp": "13 MP, f/2.2, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.0 (Selfie Expert)", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 3075, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 160, "os_at_launch": "Android 5.1 (Lollipop), ColorOS 3.0",
                "variants": [
                    {"variant_name": "Oppo F1s 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 3799000, "aliases": "oppo f1s, f1s 32gb"}
                ]
            }
        ]
    },

    # ==================== REALME EXPANSION ====================
    {
        "brand_name": "Realme",
        "models": [
            {
                "name": "Realme 12 Pro+ 5G", "series": "Pro+ Series", "release_year": 2024,
                "chipset": "Snapdragon 7s Gen 2 (4nm)", "cpu_architecture": "Octa-core 2.4GHz",
                "gpu": "Adreno 710", "antutu_benchmark_score": 600000,
                "display_type": "AMOLED, 1B colors, 120Hz", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 950,
                "screen_protection": "Curved Glass",
                "main_camera_mp": "50 MP (Sony IMX890, OIS) + 64 MP (periscope 3x OIS) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Periscope",
                "selfie_camera_mp": "32 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP65", "weight_grams": 196, "os_at_launch": "Android 14, Realme UI 5.0",
                "variants": [
                    {"variant_name": "Realme 12 Pro+ 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "realme 12 pro+ 256, 12 pro plus 256"},
                    {"variant_name": "Realme 12 Pro+ 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 6999000, "aliases": "realme 12 pro+ 512, 12 pro plus 512"}
                ]
            },
            {
                "name": "Realme GT Neo 3", "series": "GT Performance", "release_year": 2022,
                "chipset": "MediaTek Dimensity 8100 (5nm)", "cpu_architecture": "Octa-core 2.85GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 820000,
                "display_type": "AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "50 MP (Sony IMX766, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 188, "os_at_launch": "Android 12, Realme UI 3.0",
                "variants": [
                    {"variant_name": "Realme GT Neo 3 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6999000, "aliases": "gt neo 3 256, realme neo 3"}
                ]
            }
        ]
    },

    # ==================== INFINIX / TECNO EXPANSION ====================
    {
        "brand_name": "Infinix",
        "models": [
            {
                "name": "Infinix Note 40 Pro 5G", "series": "Note Pro", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7020 (6nm)", "cpu_architecture": "Octa-core 2.2GHz",
                "gpu": "IMG BXM-8-256", "antutu_benchmark_score": 460000,
                "display_type": "AMOLED, 1B colors, 120Hz, 3D Curved", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "108 MP (wide, OIS) + 2 MP + 2 MP",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x In-Sensor",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "1440p@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 20,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP53", "weight_grams": 190, "os_at_launch": "Android 14, XOS 14",
                "variants": [
                    {"variant_name": "Infinix Note 40 Pro 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 3799000, "aliases": "note 40 pro 5g, infinix 40 pro 256"}
                ]
            },
            {
                "name": "Infinix Zero Ultra", "series": "Zero Flagship", "release_year": 2022,
                "chipset": "MediaTek Dimensity 920 (6nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-G68 MC4", "antutu_benchmark_score": 500000,
                "display_type": "AMOLED, 120Hz Curved Display", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 900,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "200 MP (wide, OIS) + 13 MP (ultrawide) + 2 MP",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.0", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 180, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "None", "weight_grams": 213, "os_at_launch": "Android 12, XOS 12",
                "variants": [
                    {"variant_name": "Infinix Zero Ultra 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 6599000, "aliases": "zero ultra 256, infinix zero ultra"}
                ]
            }
        ]
    },

    # ==================== GOOGLE PIXEL EXPANSION ====================
    {
        "brand_name": "Google",
        "models": [
            {
                "name": "Pixel 7 Pro", "series": "Pixel Flagship", "release_year": 2022,
                "chipset": "Google Tensor G2 (5nm)", "cpu_architecture": "Octa-core 2.85GHz",
                "gpu": "Mali-G710 MP7", "antutu_benchmark_score": 830000,
                "display_type": "LTPO AMOLED, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1440 x 3120 pixels (QHD+)", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (5x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "10.8 MP, f/2.2", "video_recording_max": "4K@60fps 10-bit HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 212, "os_at_launch": "Android 13",
                "variants": [
                    {"variant_name": "Pixel 7 Pro 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 13999000, "aliases": "pixel 7 pro 128, p7p 128"},
                    {"variant_name": "Pixel 7 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 15499000, "aliases": "pixel 7 pro 256, p7p 256"}
                ]
            },
            {
                "name": "Pixel 4 XL", "series": "Soli Radar Flagship", "release_year": 2019,
                "chipset": "Snapdragon 855 (7nm)", "cpu_architecture": "Octa-core 2.84GHz",
                "gpu": "Adreno 640", "antutu_benchmark_score": 460000,
                "display_type": "P-OLED, 90Hz, HDR", "screen_size_inch": 6.3,
                "refresh_rate_hz": 90, "resolution": "1440 x 3040 pixels (QHD+)", "peak_brightness_nits": 450,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12.2 MP (wide, OIS) + 16 MP (2x telephoto, OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "8 MP, f/2.0 + TOF 3D (Face Unlock)", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3700, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 11,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 193, "os_at_launch": "Android 10",
                "variants": [
                    {"variant_name": "Pixel 4 XL 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 12499000, "aliases": "pixel 4 xl 64, p4xl 64"},
                    {"variant_name": "Pixel 4 XL 6GB/128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 13999000, "aliases": "pixel 4 xl 128, p4xl 128"}
                ]
            }
        ]
    },

    # ==================== SONY XPERIA EXPANSION ====================
    {
        "brand_name": "Sony",
        "models": [
            {
                "name": "Xperia 1 V", "series": "Alpha Cinematography", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1550000,
                "display_type": "OLED, 1B colors, 120Hz, 4K HDR", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1644 x 3840 pixels (4K)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "48 MP (Exmor T, OIS) + 12 MP (continuous optical zoom 3.5x-5.2x OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3.5x-5.2x Continuous Optical",
                "selfie_camera_mp": "12 MP, f/2.0", "video_recording_max": "4K@120fps HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 187, "os_at_launch": "Android 13",
                "variants": [
                    {"variant_name": "Xperia 1 V 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 19999000, "aliases": "sony xperia 1 v, 1 v 256"}
                ]
            },
            {
                "name": "Xperia Z (C6603)", "series": "Waterproof Pioneer", "release_year": 2013,
                "chipset": "Snapdragon S4 Pro (28nm)", "cpu_architecture": "Quad-core 1.5GHz Krait",
                "gpu": "Adreno 320", "antutu_benchmark_score": 28000,
                "display_type": "TFT capacitive, Bravia Engine 2", "screen_size_inch": 5.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels (FHD)", "peak_brightness_nits": 440,
                "screen_protection": "Shatter proof glass",
                "main_camera_mp": "13.1 MP, f/2.4, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2.2 MP", "video_recording_max": "1080p@30fps HDR",
                "battery_capacity_mah": 2330, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP57", "weight_grams": 146, "os_at_launch": "Android 4.1.2 (Jelly Bean)",
                "variants": [
                    {"variant_name": "Xperia Z 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 7499000, "aliases": "sony xperia z, xperia z 16gb"}
                ]
            }
        ]
    },

    # ==================== HUAWEI EXPANSION ====================
    {
        "brand_name": "Huawei",
        "models": [
            {
                "name": "Mate 40 Pro", "series": "Mate Space Ring Flagship", "release_year": 2020,
                "chipset": "Kirin 9000 5G (5nm)", "cpu_architecture": "Octa-core 3.13GHz",
                "gpu": "Mali-G78 MP24", "antutu_benchmark_score": 780000,
                "display_type": "OLED, 90Hz, HDR10", "screen_size_inch": 6.76,
                "refresh_rate_hz": 90, "resolution": "1344 x 2772 pixels", "peak_brightness_nits": 800,
                "screen_protection": "Curved Glass 88 deg",
                "main_camera_mp": "50 MP (Ultra Vision, OIS) + 12 MP (periscope 5x OIS) + 20 MP (cine ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "13 MP + TOF 3D", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4400, "fast_charging_watt": 66, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 212, "os_at_launch": "EMUI 11 (Android 10)",
                "variants": [
                    {"variant_name": "Mate 40 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 15999000, "aliases": "mate 40 pro 256, huawei mate 40"}
                ]
            },
            {
                "name": "P30 Pro", "series": "P-Series Periscope Pioneer", "release_year": 2019,
                "chipset": "Kirin 980 (7nm)", "cpu_architecture": "Octa-core 2.6GHz",
                "gpu": "Mali-G76 MP10", "antutu_benchmark_score": 410000,
                "display_type": "OLED, HDR10", "screen_size_inch": 6.47,
                "refresh_rate_hz": 60, "resolution": "1080 x 2340 pixels", "peak_brightness_nits": 600,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "40 MP (SuperSpectrum, OIS) + 8 MP (5x periscope OIS) + 20 MP (ultrawide) + TOF 3D",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "32 MP, f/2.0", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 4200, "fast_charging_watt": 40, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 192, "os_at_launch": "EMUI 9.1 (GMS Official)",
                "variants": [
                    {"variant_name": "P30 Pro 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 12999000, "aliases": "p30 pro 256, huawei p30 pro"}
                ]
            }
        ]
    }
]
