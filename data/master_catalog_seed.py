"""
Master Catalog Seeder Komprehensif Smartphone Pasar Indonesia (2010 - 2026).
Mencakup 16 Brand Utama: Apple, Samsung, Xiaomi, Poco, Redmi, Oppo, Vivo, iQOO,
Realme, Infinix, Tecno, Google Pixel, Asus, Sony, Huawei, Nokia, BlackBerry, ZTE/RedMagic, Nothing.
Format profesional dan bersih dari ikon/simbol informal.
"""
from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant

MASTER_CATALOG_2010_2026 = [
    # ==================== 1. APPLE (2010 - 2026) ====================
    {
        "brand": {"name": "Apple", "country_origin": "United States", "tier_category": "Flagship-Dominant"},
        "models": [
            # 2024 - 2026
            {
                "name": "iPhone 16 Pro Max", "series": "Pro Max", "release_year": 2024,
                "chipset": "Apple A18 Pro (3nm)", "cpu_architecture": "6-core CPU (2 performance + 4 efficiency)",
                "gpu": "Apple GPU (6-core graphics)", "antutu_benchmark_score": 1950000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.9,
                "refresh_rate_hz": 120, "resolution": "1320 x 2868 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield (Gen 2)",
                "main_camera_mp": "48 MP (wide, sensor-shift OIS) + 12 MP (5x periscope telephoto) + 48 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "12 MP, f/1.9, PDAF, OIS", "video_recording_max": "4K@120fps Dolby Vision HDR",
                "battery_capacity_mah": 4685, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 25,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 227, "os_at_launch": "iOS 18",
                "variants": [
                    {"variant_name": "iPhone 16 Pro Max 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 24999000, "aliases": "16 pmax 256, ip 16 pro max 256, iphone 16 pro max 256gb"},
                    {"variant_name": "iPhone 16 Pro Max 512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 29999000, "aliases": "16 pmax 512, ip 16 pro max 512, iphone 16 pro max 512gb"},
                    {"variant_name": "iPhone 16 Pro Max 1TB", "ram_gb": 8, "storage_gb": 1024, "official_msrp_new": 34999000, "aliases": "16 pmax 1tb, ip 16 pro max 1tb, iphone 16 pro max 1tb"}
                ]
            },
            {
                "name": "iPhone 16 Pro", "series": "Pro", "release_year": 2024,
                "chipset": "Apple A18 Pro (3nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (6-core)", "antutu_benchmark_score": 1920000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.3,
                "refresh_rate_hz": 120, "resolution": "1206 x 2622 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield (Gen 2)",
                "main_camera_mp": "48 MP (wide) + 12 MP (5x telephoto) + 48 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@120fps",
                "battery_capacity_mah": 3582, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 25,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 199, "os_at_launch": "iOS 18",
                "variants": [
                    {"variant_name": "iPhone 16 Pro 128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 20999000, "aliases": "16 pro 128, ip 16 pro 128, iphone 16 pro 128gb"},
                    {"variant_name": "iPhone 16 Pro 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 23999000, "aliases": "16 pro 256, ip 16 pro 256, iphone 16 pro 256gb"},
                    {"variant_name": "iPhone 16 Pro 512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 27999000, "aliases": "16 pro 512, ip 16 pro 512, iphone 16 pro 512gb"}
                ]
            },
            {
                "name": "iPhone 16", "series": "Standard", "release_year": 2024,
                "chipset": "Apple A18 (3nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1650000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1179 x 2556 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Sensor",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3561, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 25,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 170, "os_at_launch": "iOS 18",
                "variants": [
                    {"variant_name": "iPhone 16 128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 16499000, "aliases": "ip 16 128, iphone 16 128gb"},
                    {"variant_name": "iPhone 16 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 19499000, "aliases": "ip 16 256, iphone 16 256gb"}
                ]
            },
            # 2023
            {
                "name": "iPhone 15 Pro Max", "series": "Pro Max", "release_year": 2023,
                "chipset": "Apple A17 Pro (3nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (6-core)", "antutu_benchmark_score": 1580000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1290 x 2796 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (5x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps ProRes",
                "battery_capacity_mah": 4441, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 221, "os_at_launch": "iOS 17",
                "variants": [
                    {"variant_name": "iPhone 15 Pro Max 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 24999000, "aliases": "15 pmax 256, ip 15 pro max 256, iphone 15 pro max 256gb"},
                    {"variant_name": "iPhone 15 Pro Max 512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 29999000, "aliases": "15 pmax 512, ip 15 pro max 512, iphone 15 pro max 512gb"},
                    {"variant_name": "iPhone 15 Pro Max 1TB", "ram_gb": 8, "storage_gb": 1024, "official_msrp_new": 33999000, "aliases": "15 pmax 1tb, ip 15 pro max 1tb, iphone 15 pro max 1tb"}
                ]
            },
            {
                "name": "iPhone 15 Pro", "series": "Pro", "release_year": 2023,
                "chipset": "Apple A17 Pro (3nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (6-core)", "antutu_benchmark_score": 1550000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1179 x 2556 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps ProRes",
                "battery_capacity_mah": 3274, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 187, "os_at_launch": "iOS 17",
                "variants": [
                    {"variant_name": "iPhone 15 Pro 128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 20999000, "aliases": "15 pro 128, ip 15 pro 128, iphone 15 pro 128gb"},
                    {"variant_name": "iPhone 15 Pro 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 23999000, "aliases": "15 pro 256, ip 15 pro 256, iphone 15 pro 256gb"}
                ]
            },
            {
                "name": "iPhone 15", "series": "Standard", "release_year": 2023,
                "chipset": "Apple A16 Bionic (4nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1380000,
                "display_type": "Super Retina XDR OLED (Dynamic Island)", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1179 x 2556 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Sensor",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3349, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 171, "os_at_launch": "iOS 17",
                "variants": [
                    {"variant_name": "iPhone 15 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 16499000, "aliases": "ip 15 128, iphone 15 128gb"},
                    {"variant_name": "iPhone 15 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 19499000, "aliases": "ip 15 256, iphone 15 256gb"}
                ]
            },
            # 2022
            {
                "name": "iPhone 14 Pro Max", "series": "Pro Max", "release_year": 2022,
                "chipset": "Apple A16 Bionic (4nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1420000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1290 x 2796 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/1.9, PDAF", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4323, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 240, "os_at_launch": "iOS 16",
                "variants": [
                    {"variant_name": "iPhone 14 Pro Max 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 21999000, "aliases": "14 pmax 128, ip 14 pro max 128, iphone 14 pro max 128gb"},
                    {"variant_name": "iPhone 14 Pro Max 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 24999000, "aliases": "14 pmax 256, ip 14 pro max 256, iphone 14 pro max 256gb"}
                ]
            },
            {
                "name": "iPhone 14", "series": "Standard", "release_year": 2022,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1220000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1170 x 2532 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3279, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 172, "os_at_launch": "iOS 16",
                "variants": [
                    {"variant_name": "iPhone 14 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 15999000, "aliases": "ip 14 128, iphone 14 128gb"},
                    {"variant_name": "iPhone 14 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 18999000, "aliases": "ip 14 256, iphone 14 256gb"}
                ]
            },
            # 2021
            {
                "name": "iPhone 13 Pro Max", "series": "Pro Max", "release_year": 2021,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1280000,
                "display_type": "Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1284 x 2778 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4352, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 240, "os_at_launch": "iOS 15",
                "variants": [
                    {"variant_name": "iPhone 13 Pro Max 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 19999000, "aliases": "13 pmax 128, ip 13 pro max 128, iphone 13 pro max 128gb"},
                    {"variant_name": "iPhone 13 Pro Max 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 22999000, "aliases": "13 pmax 256, ip 13 pro max 256, iphone 13 pro max 256gb"}
                ]
            },
            {
                "name": "iPhone 13 Pro", "series": "Pro", "release_year": 2021,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1250000,
                "display_type": "Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1170 x 2532 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3095, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 204, "os_at_launch": "iOS 15",
                "variants": [
                    {"variant_name": "iPhone 13 Pro 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 18499000, "aliases": "13 pro 128, ip 13 pro 128, iphone 13 pro 128gb"},
                    {"variant_name": "iPhone 13 Pro 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 20999000, "aliases": "13 pro 256, ip 13 pro 256, iphone 13 pro 256gb"}
                ]
            },
            {
                "name": "iPhone 13", "series": "Standard", "release_year": 2021,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 1180000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1170 x 2532 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3240, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 174, "os_at_launch": "iOS 15",
                "variants": [
                    {"variant_name": "iPhone 13 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 14999000, "aliases": "ip 13 128, iphone 13 128gb"},
                    {"variant_name": "iPhone 13 256GB", "ram_gb": 4, "storage_gb": 256, "official_msrp_new": 17499000, "aliases": "ip 13 256, iphone 13 256gb"}
                ]
            },
            # 2020
            {
                "name": "iPhone 12 Pro Max", "series": "Pro Max", "release_year": 2020,
                "chipset": "Apple A14 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 1050000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.7,
                "refresh_rate_hz": 60, "resolution": "1284 x 2778 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (2.5x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2.5x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3687, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 228, "os_at_launch": "iOS 14",
                "variants": [
                    {"variant_name": "iPhone 12 Pro Max 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 20499000, "aliases": "12 pmax 128, ip 12 pro max 128, iphone 12 pro max 128gb"},
                    {"variant_name": "iPhone 12 Pro Max 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 22999000, "aliases": "12 pmax 256, ip 12 pro max 256, iphone 12 pro max 256gb"}
                ]
            },
            {
                "name": "iPhone 12", "series": "Standard", "release_year": 2020,
                "chipset": "Apple A14 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 980000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1170 x 2532 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2815, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 164, "os_at_launch": "iOS 14",
                "variants": [
                    {"variant_name": "iPhone 12 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 14999000, "aliases": "ip 12 64, iphone 12 64gb"},
                    {"variant_name": "iPhone 12 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 16499000, "aliases": "ip 12 128, iphone 12 128gb"}
                ]
            },
            # 2019 - 2010 (Legacy Master)
            {
                "name": "iPhone 11 Pro Max", "series": "Pro Max", "release_year": 2019,
                "chipset": "Apple A13 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 880000,
                "display_type": "Super Retina XDR OLED", "screen_size_inch": 6.5,
                "refresh_rate_hz": 60, "resolution": "1242 x 2688 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide) + 12 MP (telephoto 2x) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3969, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 226, "os_at_launch": "iOS 13",
                "variants": [
                    {"variant_name": "iPhone 11 Pro Max 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 19999000, "aliases": "11 pmax 64, ip 11 pro max 64, iphone 11 pro max 64gb"},
                    {"variant_name": "iPhone 11 Pro Max 256GB", "ram_gb": 4, "storage_gb": 256, "official_msrp_new": 23999000, "aliases": "11 pmax 256, ip 11 pro max 256, iphone 11 pro max 256gb"}
                ]
            },
            {
                "name": "iPhone 11", "series": "Standard", "release_year": 2019,
                "chipset": "Apple A13 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 820000,
                "display_type": "Liquid Retina IPS LCD", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "828 x 1792 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3110, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 194, "os_at_launch": "iOS 13",
                "variants": [
                    {"variant_name": "iPhone 11 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 12999000, "aliases": "ip 11 64, iphone 11 64gb"},
                    {"variant_name": "iPhone 11 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 14199000, "aliases": "ip 11 128, iphone 11 128gb"}
                ]
            },
            {
                "name": "iPhone XR", "series": "Value Flagship", "release_year": 2018,
                "chipset": "Apple A12 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 620000,
                "display_type": "Liquid Retina IPS LCD", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "828 x 1792 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP, f/1.8, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2942, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 194, "os_at_launch": "iOS 12",
                "variants": [
                    {"variant_name": "iPhone XR 64GB", "ram_gb": 3, "storage_gb": 64, "official_msrp_new": 15199000, "aliases": "ip xr 64, iphone xr 64gb"},
                    {"variant_name": "iPhone XR 128GB", "ram_gb": 3, "storage_gb": 128, "official_msrp_new": 16499000, "aliases": "ip xr 128, iphone xr 128gb"}
                ]
            },
            {
                "name": "iPhone X", "series": "Anniversary Flagship", "release_year": 2017,
                "chipset": "Apple A11 Bionic (10nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (3-core)", "antutu_benchmark_score": 510000,
                "display_type": "Super Retina OLED, HDR10", "screen_size_inch": 5.8,
                "refresh_rate_hz": 60, "resolution": "1125 x 2436 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (telephoto 2x, OIS)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 2716, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 174, "os_at_launch": "iOS 11",
                "variants": [
                    {"variant_name": "iPhone X 64GB", "ram_gb": 3, "storage_gb": 64, "official_msrp_new": 17999000, "aliases": "ip x 64, iphone x 64gb"},
                    {"variant_name": "iPhone X 256GB", "ram_gb": 3, "storage_gb": 256, "official_msrp_new": 20799000, "aliases": "ip x 256, iphone x 256gb"}
                ]
            },
            {
                "name": "iPhone 7 Plus", "series": "Plus", "release_year": 2016,
                "chipset": "Apple A10 Fusion (16nm)", "cpu_architecture": "Quad-core 2.34GHz",
                "gpu": "PowerVR Series7XT Plus", "antutu_benchmark_score": 380000,
                "display_type": "Retina IPS LCD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (telephoto 2x)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "7 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 2900, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 188, "os_at_launch": "iOS 10",
                "variants": [
                    {"variant_name": "iPhone 7 Plus 128GB", "ram_gb": 3, "storage_gb": 128, "official_msrp_new": 15888000, "aliases": "ip 7 plus 128, 7 plus 128gb"}
                ]
            },
            {
                "name": "iPhone 6s", "series": "Standard", "release_year": 2015,
                "chipset": "Apple A9 (14nm)", "cpu_architecture": "Dual-core 1.84GHz Twister",
                "gpu": "PowerVR GT7600", "antutu_benchmark_score": 270000,
                "display_type": "IPS LCD 3D Touch", "screen_size_inch": 4.7,
                "refresh_rate_hz": 60, "resolution": "750 x 1334 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Ion-strengthened glass",
                "main_camera_mp": "12 MP, f/2.2",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 1715, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "None", "weight_grams": 143, "os_at_launch": "iOS 9",
                "variants": [
                    {"variant_name": "iPhone 6s 64GB", "ram_gb": 2, "storage_gb": 64, "official_msrp_new": 12499000, "aliases": "ip 6s 64, iphone 6s 64gb"}
                ]
            },
            {
                "name": "iPhone 5s", "series": "Touch ID Pioneer", "release_year": 2013,
                "chipset": "Apple A7 (28nm 64-bit)", "cpu_architecture": "Dual-core 1.3GHz Cyclone",
                "gpu": "PowerVR G6430", "antutu_benchmark_score": 140000,
                "display_type": "IPS LCD", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "640 x 1136 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "8 MP, f/2.2",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "1.2 MP, f/2.4", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 1560, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 112, "os_at_launch": "iOS 7",
                "variants": [
                    {"variant_name": "iPhone 5s 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 10499000, "aliases": "ip 5s 16, iphone 5s 16gb"}
                ]
            },
            {
                "name": "iPhone 4", "series": "Retina Pioneer", "release_year": 2010,
                "chipset": "Apple A4 (45nm)", "cpu_architecture": "1.0 GHz Cortex-A8",
                "gpu": "PowerVR SGX535", "antutu_benchmark_score": 45000,
                "display_type": "IPS LCD Retina Display", "screen_size_inch": 3.5,
                "refresh_rate_hz": 60, "resolution": "640 x 960 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "5 MP, f/2.8, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "VGA (0.3 MP)", "video_recording_max": "720p@30fps",
                "battery_capacity_mah": 1420, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 137, "os_at_launch": "iOS 4",
                "variants": [
                    {"variant_name": "iPhone 4 16GB", "ram_gb": 1, "storage_gb": 16, "official_msrp_new": 6999000, "aliases": "ip 4 16, iphone 4 16gb"}
                ]
            }
        ]
    },

    # ==================== 2. SAMSUNG (2010 - 2026) ====================
    {
        "brand": {"name": "Samsung", "country_origin": "South Korea", "tier_category": "Flagship & Multi-Tier"},
        "models": [
            {
                "name": "Galaxy S24 Ultra", "series": "S-Series Flagship", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.39GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 1980000,
                "display_type": "Dynamic LTPO AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1440 x 3120 pixels (QHD+)", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Armor",
                "main_camera_mp": "200 MP (wide, OIS) + 50 MP (5x periscope OIS) + 10 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "5x & 10x Optical Quality",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@120fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 232, "os_at_launch": "Android 14, One UI 6.1 (Galaxy AI)",
                "variants": [
                    {"variant_name": "Galaxy S24 Ultra 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 21999000, "aliases": "s24 ultra 256, samsung s24 ultra 256gb, s24u 256"},
                    {"variant_name": "Galaxy S24 Ultra 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 23999000, "aliases": "s24 ultra 512, samsung s24 ultra 512gb, s24u 512"}
                ]
            },
            {
                "name": "Galaxy Z Fold 6", "series": "Z-Fold", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.39GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 1940000,
                "display_type": "Foldable Dynamic LTPO AMOLED 2X, 120Hz", "screen_size_inch": 7.6,
                "refresh_rate_hz": 120, "resolution": "1856 x 2160 pixels", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "10 MP cover + 4 MP under-display", "video_recording_max": "8K@30fps",
                "battery_capacity_mah": 4400, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP48", "weight_grams": 239, "os_at_launch": "Android 14, One UI 6.1.1",
                "variants": [
                    {"variant_name": "Galaxy Z Fold 6 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 26499000, "aliases": "fold 6 256, z fold 6 256, samsung fold 6"},
                    {"variant_name": "Galaxy Z Fold 6 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 28499000, "aliases": "fold 6 512, z fold 6 512"}
                ]
            },
            {
                "name": "Galaxy A55 5G", "series": "A-Series Midrange", "release_year": 2024,
                "chipset": "Exynos 1480 (4nm)", "cpu_architecture": "Octa-core 2.75GHz",
                "gpu": "Xclipse 530 (AMD RDNA2)", "antutu_benchmark_score": 720000,
                "display_type": "Super AMOLED, 120Hz", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels (FHD+)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus+",
                "main_camera_mp": "50 MP (wide, OIS) + 12 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 213, "os_at_launch": "Android 14, One UI 6.1",
                "variants": [
                    {"variant_name": "Galaxy A55 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "a55 256, samsung a55 5g 256gb"},
                    {"variant_name": "Galaxy A55 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 6899000, "aliases": "a55 12/256, samsung a55 12gb"}
                ]
            },
            {
                "name": "Galaxy S23 Ultra", "series": "S-Series Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.36GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1520000,
                "display_type": "Dynamic AMOLED 2X, 120Hz", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1440 x 3088 pixels", "peak_brightness_nits": 1750,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "200 MP (wide, OIS) + 10 MP (10x periscope) + 10 MP (3x) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "10x Periscope",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 234, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy S23 Ultra 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 19999000, "aliases": "s23 ultra 256, samsung s23 ultra 256gb"},
                    {"variant_name": "Galaxy S23 Ultra 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 21999000, "aliases": "s23 ultra 512, samsung s23 ultra 512gb"}
                ]
            },
            {
                "name": "Galaxy S22 Ultra", "series": "S-Series Flagship", "release_year": 2022,
                "chipset": "Snapdragon 8 Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1150000,
                "display_type": "Dynamic AMOLED 2X, 120Hz", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1440 x 3088 pixels", "peak_brightness_nits": 1750,
                "screen_protection": "Corning Gorilla Glass Victus+",
                "main_camera_mp": "108 MP (wide, OIS) + 10 MP (10x) + 10 MP (3x) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "10x Periscope",
                "selfie_camera_mp": "40 MP, f/2.2", "video_recording_max": "8K@24fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 228, "os_at_launch": "Android 12",
                "variants": [
                    {"variant_name": "Galaxy S22 Ultra 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 18999000, "aliases": "s22 ultra 256, s22u 256"}
                ]
            },
            {
                "name": "Galaxy S20 Ultra", "series": "S-Series Flagship", "release_year": 2020,
                "chipset": "Exynos 990 (7nm+)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G77 MP11", "antutu_benchmark_score": 680000,
                "display_type": "Dynamic AMOLED 2X, 120Hz", "screen_size_inch": 6.9,
                "refresh_rate_hz": 120, "resolution": "1440 x 3200 pixels", "peak_brightness_nits": 1400,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "108 MP (wide, OIS) + 48 MP (4x periscope, 100x Space Zoom) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "4x Periscope",
                "selfie_camera_mp": "40 MP, f/2.2", "video_recording_max": "8K@24fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G / 5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 222, "os_at_launch": "Android 10",
                "variants": [
                    {"variant_name": "Galaxy S20 Ultra 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 18499000, "aliases": "s20 ultra 128, s20u 128"}
                ]
            },
            {
                "name": "Galaxy Note 20 Ultra", "series": "Note Flagship", "release_year": 2020,
                "chipset": "Exynos 990 (7nm+)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G77 MP11", "antutu_benchmark_score": 710000,
                "display_type": "Dynamic AMOLED 2X, 120Hz, S-Pen 9ms", "screen_size_inch": 6.9,
                "refresh_rate_hz": 120, "resolution": "1440 x 3088 pixels", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "108 MP (wide, OIS) + 12 MP (5x periscope OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "8K@24fps",
                "battery_capacity_mah": 4500, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G / 4G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 208, "os_at_launch": "Android 10",
                "variants": [
                    {"variant_name": "Galaxy Note 20 Ultra 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 17999000, "aliases": "note 20 ultra 256, note20u"}
                ]
            },
            {
                "name": "Galaxy Note 10+", "series": "Note Flagship", "release_year": 2019,
                "chipset": "Exynos 9825 (7nm)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G76 MP12", "antutu_benchmark_score": 530000,
                "display_type": "Dynamic AMOLED, HDR10+", "screen_size_inch": 6.8,
                "refresh_rate_hz": 60, "resolution": "1440 x 3040 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (2x telephoto OIS) + 16 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "10 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4300, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 196, "os_at_launch": "Android 9",
                "variants": [
                    {"variant_name": "Galaxy Note 10+ 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 16499000, "aliases": "note 10 plus 256, note 10+ 256"}
                ]
            },
            {
                "name": "Galaxy S10+", "series": "S-Series Flagship", "release_year": 2019,
                "chipset": "Exynos 9820 (8nm)", "cpu_architecture": "Octa-core 2.73GHz",
                "gpu": "Mali-G76 MP12", "antutu_benchmark_score": 490000,
                "display_type": "Dynamic AMOLED, HDR10+", "screen_size_inch": 6.4,
                "refresh_rate_hz": 60, "resolution": "1440 x 3040 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass 6",
                "main_camera_mp": "12 MP (wide) + 12 MP (2x telephoto) + 16 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "10 MP + 8 MP depth", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4100, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 175, "os_at_launch": "Android 9",
                "variants": [
                    {"variant_name": "Galaxy S10+ 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 13999000, "aliases": "s10 plus 128, s10+ 128gb"}
                ]
            },
            {
                "name": "Galaxy S8", "series": "Infinity Display Pioneer", "release_year": 2017,
                "chipset": "Exynos 8895 (10nm)", "cpu_architecture": "Octa-core 2.3GHz",
                "gpu": "Mali-G71 MP20", "antutu_benchmark_score": 260000,
                "display_type": "Super AMOLED, HDR10", "screen_size_inch": 5.8,
                "refresh_rate_hz": 60, "resolution": "1440 x 2960 pixels", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass 5",
                "main_camera_mp": "12 MP, f/1.7, Dual Pixel PDAF, OIS",
                "camera_setup": "Single", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "8 MP, f/1.7, AF", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 3000, "fast_charging_watt": 15, "has_wireless_charging": True, "wireless_charging_watt": 10,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 155, "os_at_launch": "Android 7.0",
                "variants": [
                    {"variant_name": "Galaxy S8 4GB/64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 10499000, "aliases": "samsung s8 64gb, galaxy s8"}
                ]
            },
            {
                "name": "Galaxy S4", "series": "Classic Flagship", "release_year": 2013,
                "chipset": "Exynos 5410 Octa (28nm)", "cpu_architecture": "Octa-core 1.6GHz",
                "gpu": "PowerVR SGX544MP3", "antutu_benchmark_score": 90000,
                "display_type": "Super AMOLED", "screen_size_inch": 5.0,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 400,
                "screen_protection": "Corning Gorilla Glass 3",
                "main_camera_mp": "13 MP, f/2.2, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "2 MP, f/2.4", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 2600, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G / 4G", "has_nfc": True, "ip_rating": "None", "weight_grams": 130, "os_at_launch": "Android 4.2.2 Jelly Bean",
                "variants": [
                    {"variant_name": "Galaxy S4 16GB", "ram_gb": 2, "storage_gb": 16, "official_msrp_new": 7499000, "aliases": "samsung s4 16gb, galaxy s4 i9500"}
                ]
            },
            {
                "name": "Galaxy S (I9000)", "series": "First Generation Flagship", "release_year": 2010,
                "chipset": "Hummingbird (45nm)", "cpu_architecture": "1.0 GHz Cortex-A8",
                "gpu": "PowerVR SGX540", "antutu_benchmark_score": 25000,
                "display_type": "Super AMOLED", "screen_size_inch": 4.0,
                "refresh_rate_hz": 60, "resolution": "480 x 800 pixels", "peak_brightness_nits": 300,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "5 MP, AF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "VGA (0.3 MP)", "video_recording_max": "720p@30fps",
                "battery_capacity_mah": 1500, "fast_charging_watt": 5, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "3G HSPA", "has_nfc": False, "ip_rating": "None", "weight_grams": 119, "os_at_launch": "Android 2.1 Eclair",
                "variants": [
                    {"variant_name": "Galaxy S 8GB", "ram_gb": 1, "storage_gb": 8, "official_msrp_new": 5999000, "aliases": "samsung galaxy s1, i9000"}
                ]
            }
        ]
    },

    # ==================== 3. XIAOMI / POCO / REDMI (2013 - 2026) ====================
    {
        "brand": {"name": "Xiaomi", "country_origin": "China", "tier_category": "Value-for-Money & Flagship"},
        "models": [
            {
                "name": "Xiaomi 14", "series": "Leica Flagship", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.3GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 1960000,
                "display_type": "LTPO OLED, 68B colors, 120Hz, Dolby Vision", "screen_size_inch": 6.36,
                "refresh_rate_hz": 120, "resolution": "1200 x 2670 pixels (1.5K)", "peak_brightness_nits": 3000,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "Leica 50 MP (wide, OIS) + 50 MP (3.2x telephoto OIS) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3.2x Optical",
                "selfie_camera_mp": "32 MP, f/2.0", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4610, "fast_charging_watt": 90, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 193, "os_at_launch": "Android 14, HyperOS",
                "variants": [
                    {"variant_name": "Xiaomi 14 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 11999000, "aliases": "mi 14 256, xiaomi 14 256gb, mi14"},
                    {"variant_name": "Xiaomi 14 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 12999000, "aliases": "mi 14 512, xiaomi 14 512gb"}
                ]
            },
            {
                "name": "Poco F6", "series": "Poco Performance", "release_year": 2024,
                "chipset": "Snapdragon 8s Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 735", "antutu_benchmark_score": 1500000,
                "display_type": "AMOLED, 68B colors, 120Hz, Dolby Vision", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1220 x 2712 pixels (1.5K)", "peak_brightness_nits": 2400,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (wide, Sony IMX882, OIS) + 8 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 90, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP64", "weight_grams": 179, "os_at_launch": "Android 14, HyperOS",
                "variants": [
                    {"variant_name": "Poco F6 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4899000, "aliases": "pocof6 256, poco f6 8/256"},
                    {"variant_name": "Poco F6 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 5699000, "aliases": "pocof6 512, poco f6 12/512"}
                ]
            },
            {
                "name": "Redmi Note 13 Pro+ 5G", "series": "Redmi Note", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7200 Ultra (4nm)", "cpu_architecture": "Octa-core 2.8GHz",
                "gpu": "Mali-G610 MC4", "antutu_benchmark_score": 750000,
                "display_type": "Curved AMOLED, 120Hz", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1220 x 2712 pixels", "peak_brightness_nits": 1800,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "200 MP (wide, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 204, "os_at_launch": "Android 13, MIUI 14",
                "variants": [
                    {"variant_name": "Redmi Note 13 Pro+ 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 5999000, "aliases": "note 13 pro plus 512, redmi note 13 pro+"}
                ]
            },
            {
                "name": "Pocophone F1", "series": "Flagship Killer Pioneer", "release_year": 2018,
                "chipset": "Snapdragon 845 (10nm)", "cpu_architecture": "Octa-core 2.8GHz",
                "gpu": "Adreno 630", "antutu_benchmark_score": 390000,
                "display_type": "IPS LCD", "screen_size_inch": 6.18,
                "refresh_rate_hz": 60, "resolution": "1080 x 2246 pixels", "peak_brightness_nits": 500,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "12 MP (wide) + 5 MP (depth)",
                "camera_setup": "Dual", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "20 MP, f/2.0", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4000, "fast_charging_watt": 18, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 182, "os_at_launch": "Android 8.1 Oreo",
                "variants": [
                    {"variant_name": "Pocophone F1 6GB/64GB", "ram_gb": 6, "storage_gb": 64, "official_msrp_new": 4499000, "aliases": "poco f1 64, pocophone f1"}
                ]
            },
            {
                "name": "Redmi Note 3", "series": "Budget Pioneer", "release_year": 2016,
                "chipset": "Snapdragon 650 (28nm)", "cpu_architecture": "Hexa-core 1.8GHz",
                "gpu": "Adreno 510", "antutu_benchmark_score": 110000,
                "display_type": "IPS LCD", "screen_size_inch": 5.5,
                "refresh_rate_hz": 60, "resolution": "1080 x 1920 pixels", "peak_brightness_nits": 450,
                "screen_protection": "Standard Glass",
                "main_camera_mp": "16 MP, f/2.0, PDAF",
                "camera_setup": "Single", "has_ois": False, "optical_zoom_level": "None",
                "selfie_camera_mp": "5 MP, f/2.0", "video_recording_max": "1080p@30fps",
                "battery_capacity_mah": 4050, "fast_charging_watt": 10, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "4G LTE", "has_nfc": False, "ip_rating": "None", "weight_grams": 164, "os_at_launch": "Android 5.1.1 Lollipop",
                "variants": [
                    {"variant_name": "Redmi Note 3 3GB/32GB", "ram_gb": 3, "storage_gb": 32, "official_msrp_new": 2599000, "aliases": "redmi note 3 pro, kenzo"}
                ]
            }
        ]
    },

    # ==================== 4. VIVO / IQOO (2015 - 2026) ====================
    {
        "brand": {"name": "Vivo", "country_origin": "China", "tier_category": "Optics & Lifestyle Flagship"},
        "models": [
            {
                "name": "Vivo X100 Pro", "series": "X-Series ZEISS", "release_year": 2024,
                "chipset": "MediaTek Dimensity 9300 (4nm)", "cpu_architecture": "Octa-core 3.25GHz",
                "gpu": "Immortalis-G720 MC12", "antutu_benchmark_score": 2100000,
                "display_type": "LTPO AMOLED, 120Hz", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels", "peak_brightness_nits": 3000,
                "screen_protection": "Armor Glass",
                "main_camera_mp": "ZEISS 50 MP (1-inch, OIS) + 50 MP (4.3x periscope APO OIS) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "4.3x Periscope",
                "selfie_camera_mp": "32 MP, f/2.0", "video_recording_max": "8K, 4K@60fps",
                "battery_capacity_mah": 5400, "fast_charging_watt": 100, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 225, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "Vivo X100 Pro 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 16999000, "aliases": "x100 pro 512, vivo x100 pro"}
                ]
            },
            {
                "name": "iQOO 12", "series": "iQOO Gaming", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.3GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 2050000,
                "display_type": "LTPO AMOLED, 144Hz", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1260 x 2800 pixels", "peak_brightness_nits": 3000,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "50 MP (wide, OIS) + 64 MP (3x periscope OIS) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Periscope",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP64", "weight_grams": 203, "os_at_launch": "Android 14",
                "variants": [
                    {"variant_name": "iQOO 12 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 10999000, "aliases": "iqoo12 512, iqoo 12"}
                ]
            }
        ]
    },

    # ==================== 5. OPPO (2013 - 2026) ====================
    {
        "brand": {"name": "Oppo", "country_origin": "China", "tier_category": "Portrait & Design Flagship"},
        "models": [
            {
                "name": "Oppo Find N3 Fold", "series": "Find Foldable", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1560000,
                "display_type": "Foldable LTPO3 OLED, 120Hz, Dolby Vision", "screen_size_inch": 7.82,
                "refresh_rate_hz": 120, "resolution": "2268 x 2440 pixels", "peak_brightness_nits": 2800,
                "screen_protection": "Ultra Thin Glass",
                "main_camera_mp": "Hasselblad 48 MP (wide, OIS) + 64 MP (3x periscope OIS) + 48 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Periscope",
                "selfie_camera_mp": "20 MP cover + 32 MP internal", "video_recording_max": "4K@60fps Dolby Vision",
                "battery_capacity_mah": 4805, "fast_charging_watt": 67, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IPX4", "weight_grams": 239, "os_at_launch": "Android 13, ColorOS 13.2",
                "variants": [
                    {"variant_name": "Oppo Find N3 Fold 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 29999000, "aliases": "find n3 fold 512, oppo find n3"}
                ]
            },
            {
                "name": "Oppo Reno 12 Pro 5G", "series": "Reno Series", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7300 Energy (4nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-G615 MC2", "antutu_benchmark_score": 710000,
                "display_type": "Quad-Curved AMOLED, 120Hz", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 50 MP (2x telephoto) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "50 MP, f/2.0, AF", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP65", "weight_grams": 180, "os_at_launch": "Android 14, ColorOS 14.1",
                "variants": [
                    {"variant_name": "Oppo Reno 12 Pro 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 8999000, "aliases": "reno 12 pro 512, oppo reno 12 pro"}
                ]
            }
        ]
    },

    # ==================== 6. REALME (2018 - 2026) ====================
    {
        "brand": {"name": "Realme", "country_origin": "China", "tier_category": "Performance & Youth"},
        "models": [
            {
                "name": "Realme GT 6", "series": "GT Flagship Killer", "release_year": 2024,
                "chipset": "Snapdragon 8s Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 735", "antutu_benchmark_score": 1580000,
                "display_type": "LTPO AMOLED, 120Hz, Dolby Vision", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1264 x 2780 pixels (1.5K)", "peak_brightness_nits": 6000,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (Sony LYT-808, OIS) + 50 MP (2x telephoto) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5500, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP65", "weight_grams": 199, "os_at_launch": "Android 14, Realme UI 5.0",
                "variants": [
                    {"variant_name": "Realme GT 6 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 7499000, "aliases": "gt 6 256, realme gt 6"}
                ]
            }
        ]
    },

    # ==================== 7. INFINIX & TECNO (2015 - 2026) ====================
    {
        "brand": {"name": "Infinix", "country_origin": "China", "tier_category": "Value Gaming"},
        "models": [
            {
                "name": "Infinix GT 20 Pro", "series": "GT Gaming", "release_year": 2024,
                "chipset": "MediaTek Dimensity 8200 Ultimate (4nm)", "cpu_architecture": "Octa-core 3.1GHz",
                "gpu": "Mali-G610 MC6", "antutu_benchmark_score": 930000,
                "display_type": "AMOLED, 144Hz", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1080 x 2436 pixels", "peak_brightness_nits": 1300,
                "screen_protection": "Standard Glass",
                "main_camera_mp": "108 MP (wide, OIS) + 2 MP (macro) + 2 MP (depth)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 194, "os_at_launch": "Android 14, XOS 14",
                "variants": [
                    {"variant_name": "Infinix GT 20 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 4399000, "aliases": "gt 20 pro 256, infinix gt 20 pro"}
                ]
            }
        ]
    },

    # ==================== 8. GOOGLE PIXEL (2016 - 2026) ====================
    {
        "brand": {"name": "Google", "country_origin": "United States", "tier_category": "Pure Android & AI"},
        "models": [
            {
                "name": "Pixel 8 Pro", "series": "Pixel Pro", "release_year": 2023,
                "chipset": "Google Tensor G3 (4nm)", "cpu_architecture": "Nona-core 3.0GHz",
                "gpu": "Immortalis-G715s MC10", "antutu_benchmark_score": 1150000,
                "display_type": "LTPO OLED, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1344 x 2992 pixels", "peak_brightness_nits": 2400,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (5x telephoto OIS) + 48 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "10.5 MP, f/2.2", "video_recording_max": "4K@60fps 10-bit HDR",
                "battery_capacity_mah": 5050, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 213, "os_at_launch": "Android 14",
                "variants": [
                    {"variant_name": "Pixel 8 Pro 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 16500000, "aliases": "pixel 8 pro 128, google pixel 8 pro 128gb"},
                    {"variant_name": "Pixel 8 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 18500000, "aliases": "pixel 8 pro 256, google pixel 8 pro 256gb"}
                ]
            }
        ]
    },

    # ==================== 9. ASUS ROG & ZENFONE (2015 - 2026) ====================
    {
        "brand": {"name": "Asus", "country_origin": "Taiwan", "tier_category": "Gaming & Compact Flagship"},
        "models": [
            {
                "name": "ROG Phone 8 Pro", "series": "ROG Gaming", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.3GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 2150000,
                "display_type": "LTPO AMOLED, 165Hz", "screen_size_inch": 6.78,
                "refresh_rate_hz": 165, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 2500,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (Gimbal OIS) + 32 MP (3x telephoto OIS) + 13 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 5500, "fast_charging_watt": 65, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 225, "os_at_launch": "Android 14, ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone 8 Pro 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 14999000, "aliases": "rog 8 pro 512, rog phone 8 pro"},
                    {"variant_name": "ROG Phone 8 Pro Edition 24GB/1TB", "ram_gb": 24, "storage_gb": 1024, "official_msrp_new": 19999000, "aliases": "rog 8 pro 1tb, rog 8 pro 24gb"}
                ]
            },
            {
                "name": "Zenfone 10", "series": "Compact Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 (4nm)", "cpu_architecture": "Octa-core 3.2GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1540000,
                "display_type": "Super AMOLED, 144Hz", "screen_size_inch": 5.92,
                "refresh_rate_hz": 144, "resolution": "1080 x 2400 pixels", "peak_brightness_nits": 1100,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "50 MP (Gimbal OIS) + 13 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 4300, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 172, "os_at_launch": "Android 13, ZenUI",
                "variants": [
                    {"variant_name": "Zenfone 10 8GB/128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 8999000, "aliases": "zenfone 10 128, asus zenfone 10"}
                ]
            }
        ]
    },

    # ==================== 10. SONY XPERIA (2013 - 2026) ====================
    {
        "brand": {"name": "Sony", "country_origin": "Japan", "tier_category": "Pro Cinema & Audio"},
        "models": [
            {
                "name": "Xperia 1 VI", "series": "Xperia 1 Flagship", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.3GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 1950000,
                "display_type": "LTPO OLED, 120Hz, HDR", "screen_size_inch": 6.5,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels (FHD+)", "peak_brightness_nits": 1500,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "ZEISS 48 MP (wide, OIS) + 12 MP (3.5x-7.1x continuous optical zoom OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "7.1x Continuous Optical",
                "selfie_camera_mp": "12 MP, f/2.0", "video_recording_max": "4K@120fps HDR",
                "battery_capacity_mah": 5000, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 192, "os_at_launch": "Android 14",
                "variants": [
                    {"variant_name": "Xperia 1 VI 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 21999000, "aliases": "sony xperia 1 vi 256, xperia 1 vi"}
                ]
            }
        ]
    },

    # ==================== 11. HUAWEI (2013 - 2026) ====================
    {
        "brand": {"name": "Huawei", "country_origin": "China", "tier_category": "XMAGE Imaging Flagship"},
        "models": [
            {
                "name": "Pura 70 Ultra", "series": "Pura Flagship", "release_year": 2024,
                "chipset": "Kirin 9010 (7nm)", "cpu_architecture": "Octa-core (Taishan V121)",
                "gpu": "Maleoon 910", "antutu_benchmark_score": 980000,
                "display_type": "LTPO OLED, 1B colors, 120Hz, HDR", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1260 x 2844 pixels", "peak_brightness_nits": 2500,
                "screen_protection": "Kunlun Glass (Basalt-tempered)",
                "main_camera_mp": "XMAGE 50 MP (1-inch retractable, sensor-shift OIS) + 50 MP (3.5x periscope macro OIS) + 40 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3.5x Periscope Macro",
                "selfie_camera_mp": "13 MP, f/2.4", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 5200, "fast_charging_watt": 100, "has_wireless_charging": True, "wireless_charging_watt": 80,
                "network_gen": "5G / 4G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 226, "os_at_launch": "HarmonyOS 4.2",
                "variants": [
                    {"variant_name": "Huawei Pura 70 Ultra 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 20999000, "aliases": "pura 70 ultra 512, huawei pura 70"}
                ]
            }
        ]
    },

    # ==================== 12. NOTHING (2022 - 2026) ====================
    {
        "brand": {"name": "Nothing", "country_origin": "United Kingdom", "tier_category": "Design & Glyph Interface"},
        "models": [
            {
                "name": "Nothing Phone (2)", "series": "Glyph Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8+ Gen 1 (4nm)", "cpu_architecture": "Octa-core 3.0GHz",
                "gpu": "Adreno 730", "antutu_benchmark_score": 1280000,
                "display_type": "LTPO OLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels", "peak_brightness_nits": 1600,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "50 MP (Sony IMX890, OIS) + 50 MP (Samsung JN1 ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Sensor",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 4700, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP54", "weight_grams": 201, "os_at_launch": "Android 13, Nothing OS 2.0",
                "variants": [
                    {"variant_name": "Nothing Phone (2) 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 10999000, "aliases": "nothing phone 2 256, nothing 2"}
                ]
            }
        ]
    }
]

def seed_master_catalog():
    """Mengisi database dengan master catalog smartphone komprehensif 2010 - 2026."""
    init_db()
    db = SessionLocal()
    
    brand_count = 0
    model_count = 0
    variant_count = 0

    try:
        for brand_data in MASTER_CATALOG_2010_2026:
            b_info = brand_data["brand"]
            brand = db.query(MasterBrand).filter(MasterBrand.name == b_info["name"]).first()
            if not brand:
                brand = MasterBrand(
                    name=b_info["name"],
                    country_origin=b_info.get("country_origin"),
                    tier_category=b_info.get("tier_category", "Mainstream")
                )
                db.add(brand)
                db.flush()
                brand_count += 1

            for model_info in brand_data["models"]:
                model = db.query(MasterModel).filter(
                    MasterModel.brand_id == brand.id,
                    MasterModel.name == model_info["name"]
                ).first()

                if not model:
                    model = MasterModel(
                        brand_id=brand.id,
                        name=model_info["name"],
                        series=model_info.get("series"),
                        release_year=model_info["release_year"],
                        chipset=model_info.get("chipset"),
                        cpu_architecture=model_info.get("cpu_architecture"),
                        gpu=model_info.get("gpu"),
                        antutu_benchmark_score=model_info.get("antutu_benchmark_score"),
                        display_type=model_info.get("display_type"),
                        screen_size_inch=model_info.get("screen_size_inch"),
                        refresh_rate_hz=model_info.get("refresh_rate_hz", 60),
                        resolution=model_info.get("resolution"),
                        peak_brightness_nits=model_info.get("peak_brightness_nits"),
                        screen_protection=model_info.get("screen_protection"),
                        main_camera_mp=model_info.get("main_camera_mp"),
                        camera_setup=model_info.get("camera_setup", "Triple"),
                        has_ois=model_info.get("has_ois", True),
                        optical_zoom_level=model_info.get("optical_zoom_level"),
                        selfie_camera_mp=model_info.get("selfie_camera_mp"),
                        video_recording_max=model_info.get("video_recording_max"),
                        battery_capacity_mah=model_info.get("battery_capacity_mah"),
                        fast_charging_watt=model_info.get("fast_charging_watt", 25),
                        has_wireless_charging=model_info.get("has_wireless_charging", False),
                        wireless_charging_watt=model_info.get("wireless_charging_watt", 0),
                        network_gen=model_info.get("network_gen", "5G"),
                        has_nfc=model_info.get("has_nfc", True),
                        ip_rating=model_info.get("ip_rating", "IP68"),
                        weight_grams=model_info.get("weight_grams"),
                        os_at_launch=model_info.get("os_at_launch")
                    )
                    db.add(model)
                    db.flush()
                    model_count += 1
                else:
                    # Update data yang sudah ada
                    model.chipset = model_info.get("chipset") or model.chipset
                    model.antutu_benchmark_score = model_info.get("antutu_benchmark_score") or model.antutu_benchmark_score
                    model.release_year = model_info["release_year"]

                for v_info in model_info["variants"]:
                    variant = db.query(MasterVariant).filter(
                        MasterVariant.model_id == model.id,
                        MasterVariant.variant_name == v_info["variant_name"]
                    ).first()

                    if not variant:
                        variant = MasterVariant(
                            model_id=model.id,
                            variant_name=v_info["variant_name"],
                            ram_gb=v_info.get("ram_gb"),
                            storage_gb=v_info["storage_gb"],
                            official_msrp_new=v_info["official_msrp_new"],
                            aliases=v_info.get("aliases")
                        )
                        db.add(variant)
                        variant_count += 1

        db.commit()
        print(f"[SUCCESS] Seeding Berhasil: {brand_count} Brand Baru Ditambahkan, Total Model: {model_count}, Total Varian: {variant_count}")
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Gagal Seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_master_catalog()
