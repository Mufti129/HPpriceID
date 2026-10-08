"""
Master Catalog Seeder untuk Smartphone (HP) Indonesia.
Menyediakan katalog lengkap merk, model, spesifikasi teknis hardware, dan varian memori/storage.
"""
from models.database import SessionLocal, init_db
from models.catalog import MasterBrand, MasterModel, MasterVariant

CATALOG_DATA = [
    # ==================== APPLE ====================
    {
        "brand": {"name": "Apple", "country_origin": "United States", "tier_category": "Flagship-Dominant"},
        "models": [
            {
                "name": "iPhone 16 Pro Max", "series": "Pro Max", "release_year": 2024,
                "chipset": "Apple A18 Pro (3nm)", "cpu_architecture": "6-core CPU (2 performance + 4 efficiency)",
                "gpu": "Apple GPU (6-core graphics)", "antutu_benchmark_score": 1950000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.9,
                "refresh_rate_hz": 120, "resolution": "1320 x 2868 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Latest-generation Ceramic Shield",
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
                "name": "iPhone 15 Pro Max", "series": "Pro Max", "release_year": 2023,
                "chipset": "Apple A17 Pro (3nm)", "cpu_architecture": "6-core CPU (2 performance + 4 efficiency)",
                "gpu": "Apple GPU (6-core graphics)", "antutu_benchmark_score": 1580000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1290 x 2796 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide, sensor-shift OIS) + 12 MP (5x periscope telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "12 MP, f/1.9, PDAF, OIS", "video_recording_max": "4K@60fps ProRes HDR",
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
                "selfie_camera_mp": "12 MP, f/1.9, PDAF", "video_recording_max": "4K@60fps ProRes",
                "battery_capacity_mah": 3274, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 187, "os_at_launch": "iOS 17",
                "variants": [
                    {"variant_name": "iPhone 15 Pro 128GB", "ram_gb": 8, "storage_gb": 128, "official_msrp_new": 20999000, "aliases": "15 pro 128, ip 15 pro 128, iphone 15 pro 128gb"},
                    {"variant_name": "iPhone 15 Pro 256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 23999000, "aliases": "15 pro 256, ip 15 pro 256, iphone 15 pro 256gb"},
                    {"variant_name": "iPhone 15 Pro 512GB", "ram_gb": 8, "storage_gb": 512, "official_msrp_new": 27999000, "aliases": "15 pro 512, ip 15 pro 512, iphone 15 pro 512gb"}
                ]
            },
            {
                "name": "iPhone 15", "series": "Standard", "release_year": 2023,
                "chipset": "Apple A16 Bionic (4nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1380000,
                "display_type": "Super Retina XDR OLED (Dynamic Island)", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "1179 x 2556 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide, sensor-shift OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "2x Sensor Crop",
                "selfie_camera_mp": "12 MP, f/1.9", "video_recording_max": "4K@60fps Dolby Vision",
                "battery_capacity_mah": 3349, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 171, "os_at_launch": "iOS 17",
                "variants": [
                    {"variant_name": "iPhone 15 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 16499000, "aliases": "ip 15 128, iphone 15 128gb, ip15 128"},
                    {"variant_name": "iPhone 15 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 19499000, "aliases": "ip 15 256, iphone 15 256gb, ip15 256"}
                ]
            },
            {
                "name": "iPhone 14 Pro Max", "series": "Pro Max", "release_year": 2022,
                "chipset": "Apple A16 Bionic (4nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1420000,
                "display_type": "LTPO Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1290 x 2796 pixels", "peak_brightness_nits": 2000,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "48 MP (wide) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/1.9, PDAF", "video_recording_max": "4K@60fps ProRes",
                "battery_capacity_mah": 4323, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 240, "os_at_launch": "iOS 16",
                "variants": [
                    {"variant_name": "iPhone 14 Pro Max 128GB", "ram_gb": 6, "storage_gb": 128, "official_msrp_new": 21999000, "aliases": "14 pmax 128, ip 14 pro max 128, iphone 14 pro max 128gb"},
                    {"variant_name": "iPhone 14 Pro Max 256GB", "ram_gb": 6, "storage_gb": 256, "official_msrp_new": 24999000, "aliases": "14 pmax 256, ip 14 pro max 256, iphone 14 pro max 256gb"}
                ]
            },
            {
                "name": "iPhone 13 Pro", "series": "Pro", "release_year": 2021,
                "chipset": "Apple A15 Bionic (5nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (5-core)", "antutu_benchmark_score": 1250000,
                "display_type": "Super Retina XDR OLED, 120Hz ProMotion", "screen_size_inch": 6.1,
                "refresh_rate_hz": 120, "resolution": "1170 x 2532 pixels", "peak_brightness_nits": 1200,
                "screen_protection": "Ceramic Shield",
                "main_camera_mp": "12 MP (wide, sensor-shift) + 12 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps Cinematic",
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
                "main_camera_mp": "12 MP (wide, sensor-shift) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps Dolby Vision",
                "battery_capacity_mah": 3240, "fast_charging_watt": 20, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 174, "os_at_launch": "iOS 15",
                "variants": [
                    {"variant_name": "iPhone 13 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 14999000, "aliases": "ip 13 128, iphone 13 128gb, ip13 128"},
                    {"variant_name": "iPhone 13 256GB", "ram_gb": 4, "storage_gb": 256, "official_msrp_new": 17499000, "aliases": "ip 13 256, iphone 13 256gb, ip13 256"}
                ]
            },
            {
                "name": "iPhone 11", "series": "Standard", "release_year": 2019,
                "chipset": "Apple A13 Bionic (7nm)", "cpu_architecture": "6-core CPU",
                "gpu": "Apple GPU (4-core)", "antutu_benchmark_score": 820000,
                "display_type": "Liquid Retina IPS LCD", "screen_size_inch": 6.1,
                "refresh_rate_hz": 60, "resolution": "828 x 1792 pixels", "peak_brightness_nits": 625,
                "screen_protection": "Scratch-resistant glass",
                "main_camera_mp": "12 MP (wide, OIS) + 12 MP (ultrawide)",
                "camera_setup": "Dual", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "4K@60fps",
                "battery_capacity_mah": 3110, "fast_charging_watt": 18, "has_wireless_charging": True, "wireless_charging_watt": 7.5,
                "network_gen": "4G LTE", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 194, "os_at_launch": "iOS 13",
                "variants": [
                    {"variant_name": "iPhone 11 64GB", "ram_gb": 4, "storage_gb": 64, "official_msrp_new": 12999000, "aliases": "ip 11 64, iphone 11 64gb, ip11 64"},
                    {"variant_name": "iPhone 11 128GB", "ram_gb": 4, "storage_gb": 128, "official_msrp_new": 14199000, "aliases": "ip 11 128, iphone 11 128gb, ip11 128"}
                ]
            }
        ]
    },

    # ==================== SAMSUNG ====================
    {
        "brand": {"name": "Samsung", "country_origin": "South Korea", "tier_category": "Flagship & Multi-Tier"},
        "models": [
            {
                "name": "Galaxy S24 Ultra", "series": "S-Series Flagship", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 for Galaxy (4nm)", "cpu_architecture": "Octa-core (1x3.39GHz + 5x3.1GHz + 2x2.2GHz)",
                "gpu": "Adreno 750 (1 GHz)", "antutu_benchmark_score": 1980000,
                "display_type": "Dynamic LTPO AMOLED 2X, 120Hz, HDR10+", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1440 x 3120 pixels (QHD+)", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Armor (Anti-Reflective)",
                "main_camera_mp": "200 MP (wide, OIS) + 50 MP (5x periscope OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "5x & 10x Optical Quality",
                "selfie_camera_mp": "12 MP, f/2.2, Dual Pixel PDAF", "video_recording_max": "8K@30fps, 4K@120fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 232, "os_at_launch": "Android 14, One UI 6.1 (Galaxy AI)",
                "variants": [
                    {"variant_name": "Galaxy S24 Ultra 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 21999000, "aliases": "s24 ultra 256, samsung s24 ultra 256gb, s24u 256"},
                    {"variant_name": "Galaxy S24 Ultra 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 23999000, "aliases": "s24 ultra 512, samsung s24 ultra 512gb, s24u 512"}
                ]
            },
            {
                "name": "Galaxy S23 Ultra", "series": "S-Series Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 2 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.36GHz",
                "gpu": "Adreno 740", "antutu_benchmark_score": 1520000,
                "display_type": "Dynamic AMOLED 2X, 120Hz", "screen_size_inch": 6.8,
                "refresh_rate_hz": 120, "resolution": "1440 x 3088 pixels (QHD+)", "peak_brightness_nits": 1750,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "200 MP (wide, OIS) + 10 MP (10x periscope OIS) + 10 MP (3x telephoto) + 12 MP (ultrawide)",
                "camera_setup": "Quad", "has_ois": True, "optical_zoom_level": "10x Periscope",
                "selfie_camera_mp": "12 MP, f/2.2", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 45, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 234, "os_at_launch": "Android 13, One UI 5.1",
                "variants": [
                    {"variant_name": "Galaxy S23 Ultra 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 19999000, "aliases": "s23 ultra 256, samsung s23 ultra 256gb, s23u 256"},
                    {"variant_name": "Galaxy S23 Ultra 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 21999000, "aliases": "s23 ultra 512, samsung s23 ultra 512gb, s23u 512"}
                ]
            },
            {
                "name": "Galaxy A55 5G", "series": "A-Series Midrange", "release_year": 2024,
                "chipset": "Exynos 1480 (4nm)", "cpu_architecture": "Octa-core (4x2.75GHz + 4x2.0GHz)",
                "gpu": "Xclipse 530 (AMD RDNA2)", "antutu_benchmark_score": 720000,
                "display_type": "Super AMOLED, 120Hz, HDR10+", "screen_size_inch": 6.6,
                "refresh_rate_hz": 120, "resolution": "1080 x 2340 pixels (FHD+)", "peak_brightness_nits": 1000,
                "screen_protection": "Corning Gorilla Glass Victus+",
                "main_camera_mp": "50 MP (wide, OIS) + 12 MP (ultrawide) + 5 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "32 MP, f/2.2", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 25, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP67", "weight_grams": 213, "os_at_launch": "Android 14, One UI 6.1",
                "variants": [
                    {"variant_name": "Galaxy A55 5G 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 5999000, "aliases": "a55 256, samsung a55 5g 256gb, galaxy a55"},
                    {"variant_name": "Galaxy A55 5G 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 6899000, "aliases": "a55 12/256, samsung a55 12gb"}
                ]
            },
            {
                "name": "Galaxy Z Fold 6", "series": "Z-Fold", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 for Galaxy (4nm)", "cpu_architecture": "Octa-core 3.39GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 1940000,
                "display_type": "Foldable Dynamic LTPO AMOLED 2X, 120Hz", "screen_size_inch": 7.6,
                "refresh_rate_hz": 120, "resolution": "1856 x 2160 pixels", "peak_brightness_nits": 2600,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 10 MP (3x telephoto OIS) + 12 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "10 MP cover + 4 MP under-display", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 4400, "fast_charging_watt": 25, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP48", "weight_grams": 239, "os_at_launch": "Android 14, One UI 6.1.1",
                "variants": [
                    {"variant_name": "Galaxy Z Fold 6 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 26499000, "aliases": "fold 6 256, z fold 6 256, samsung fold 6"},
                    {"variant_name": "Galaxy Z Fold 6 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 28499000, "aliases": "fold 6 512, z fold 6 512"}
                ]
            }
        ]
    },

    # ==================== XIAOMI / POCO ====================
    {
        "brand": {"name": "Xiaomi", "country_origin": "China", "tier_category": "Value-for-Money & Flagship"},
        "models": [
            {
                "name": "Xiaomi 14", "series": "Xiaomi Flagship", "release_year": 2024,
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
                    {"variant_name": "Poco F6 8GB/256GB", "ram_gb": 8, "storage_gb": 256, "official_msrp_new": 4899000, "aliases": "pocof6 256, poco f6 8/256, f6 256"},
                    {"variant_name": "Poco F6 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 5699000, "aliases": "pocof6 512, poco f6 12/512, f6 512"}
                ]
            },
            {
                "name": "Redmi Note 13 Pro+ 5G", "series": "Redmi Note", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7200 Ultra (4nm)", "cpu_architecture": "Octa-core 2.8GHz",
                "gpu": "Mali-G610 MC4", "antutu_benchmark_score": 750000,
                "display_type": "Curved AMOLED, 68B colors, 120Hz, Dolby Vision", "screen_size_inch": 6.67,
                "refresh_rate_hz": 120, "resolution": "1220 x 2712 pixels (1.5K)", "peak_brightness_nits": 1800,
                "screen_protection": "Corning Gorilla Glass Victus",
                "main_camera_mp": "200 MP (wide, Samsung ISOCELL HP3, OIS) + 8 MP (ultrawide) + 2 MP (macro)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "None",
                "selfie_camera_mp": "16 MP, f/2.4", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 204, "os_at_launch": "Android 13, MIUI 14",
                "variants": [
                    {"variant_name": "Redmi Note 13 Pro+ 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 5999000, "aliases": "note 13 pro plus 512, redmi note 13 pro+ 5g"}
                ]
            }
        ]
    },

    # ==================== VIVO / IQOO ====================
    {
        "brand": {"name": "Vivo", "country_origin": "China", "tier_category": "Camera & Flagship"},
        "models": [
            {
                "name": "Vivo X100 Pro", "series": "X-Series Flagship", "release_year": 2024,
                "chipset": "MediaTek Dimensity 9300 (4nm)", "cpu_architecture": "Octa-core (4x3.25GHz + 4x2.0GHz)",
                "gpu": "Immortalis-G720 MC12", "antutu_benchmark_score": 2100000,
                "display_type": "LTPO AMOLED, 1B colors, 120Hz", "screen_size_inch": 6.78,
                "refresh_rate_hz": 120, "resolution": "1260 x 2800 pixels", "peak_brightness_nits": 3000,
                "screen_protection": "Armor Glass",
                "main_camera_mp": "ZEISS 50 MP (1-inch sensor, OIS) + 50 MP (4.3x periscope APO OIS) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "4.3x Periscope",
                "selfie_camera_mp": "32 MP, f/2.0", "video_recording_max": "8K, 4K@60fps 10-bit Log",
                "battery_capacity_mah": 5400, "fast_charging_watt": 100, "has_wireless_charging": True, "wireless_charging_watt": 50,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 225, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "Vivo X100 Pro 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 16999000, "aliases": "x100 pro 512, vivo x100 pro 16/512, x100pro"}
                ]
            },
            {
                "name": "iQOO 12", "series": "iQOO Gaming Flagship", "release_year": 2023,
                "chipset": "Snapdragon 8 Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.3GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 2050000,
                "display_type": "LTPO AMOLED, 1B colors, 144Hz, HDR10+", "screen_size_inch": 6.78,
                "refresh_rate_hz": 144, "resolution": "1260 x 2800 pixels (1.5K)", "peak_brightness_nits": 3000,
                "screen_protection": "Corning Gorilla Glass",
                "main_camera_mp": "50 MP (wide, 1/1.3, OIS) + 64 MP (3x periscope OIS) + 50 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Periscope",
                "selfie_camera_mp": "16 MP, f/2.5", "video_recording_max": "8K@30fps, 4K@60fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 120, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP64", "weight_grams": 203, "os_at_launch": "Android 14, Funtouch 14",
                "variants": [
                    {"variant_name": "iQOO 12 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 10999000, "aliases": "iqoo12 512, iqoo 12 16/512, iqoo 12 bmw"}
                ]
            }
        ]
    },

    # ==================== OPPO & REALME ====================
    {
        "brand": {"name": "Oppo", "country_origin": "China", "tier_category": "Camera & Lifestyle"},
        "models": [
            {
                "name": "Oppo Reno 12 Pro 5G", "series": "Reno Series", "release_year": 2024,
                "chipset": "MediaTek Dimensity 7300 Energy (4nm)", "cpu_architecture": "Octa-core 2.5GHz",
                "gpu": "Mali-G615 MC2", "antutu_benchmark_score": 710000,
                "display_type": "Quad-Curved AMOLED, 1B colors, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1080 x 2412 pixels (FHD+)", "peak_brightness_nits": 1200,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, Sony LYT-600, OIS) + 50 MP (2x telephoto) + 8 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "2x Optical",
                "selfie_camera_mp": "50 MP, f/2.0, AF", "video_recording_max": "4K@30fps",
                "battery_capacity_mah": 5000, "fast_charging_watt": 80, "has_wireless_charging": False, "wireless_charging_watt": 0,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP65", "weight_grams": 180, "os_at_launch": "Android 14, ColorOS 14.1",
                "variants": [
                    {"variant_name": "Oppo Reno 12 Pro 5G 12GB/512GB", "ram_gb": 12, "storage_gb": 512, "official_msrp_new": 8999000, "aliases": "reno 12 pro 512, oppo reno 12 pro 5g"}
                ]
            }
        ]
    },

    # ==================== GOOGLE PIXEL ====================
    {
        "brand": {"name": "Google", "country_origin": "United States", "tier_category": "AI & Pure Android"},
        "models": [
            {
                "name": "Pixel 8 Pro", "series": "Pixel Pro", "release_year": 2023,
                "chipset": "Google Tensor G3 (4nm)", "cpu_architecture": "Nona-core (1x3.0GHz + 4x2.45GHz + 4x2.15GHz)",
                "gpu": "Immortalis-G715s MC10", "antutu_benchmark_score": 1150000,
                "display_type": "LTPO OLED, 120Hz, HDR10+", "screen_size_inch": 6.7,
                "refresh_rate_hz": 120, "resolution": "1344 x 2992 pixels (QHD+)", "peak_brightness_nits": 2400,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (wide, OIS) + 48 MP (5x periscope telephoto OIS) + 48 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "5x Periscope",
                "selfie_camera_mp": "10.5 MP, f/2.2, PDAF", "video_recording_max": "4K@60fps 10-bit HDR",
                "battery_capacity_mah": 5050, "fast_charging_watt": 30, "has_wireless_charging": True, "wireless_charging_watt": 23,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 213, "os_at_launch": "Android 14 (7 Years OS Updates)",
                "variants": [
                    {"variant_name": "Pixel 8 Pro 12GB/128GB", "ram_gb": 12, "storage_gb": 128, "official_msrp_new": 16500000, "aliases": "pixel 8 pro 128, google pixel 8 pro 128gb"},
                    {"variant_name": "Pixel 8 Pro 12GB/256GB", "ram_gb": 12, "storage_gb": 256, "official_msrp_new": 18500000, "aliases": "pixel 8 pro 256, google pixel 8 pro 256gb"}
                ]
            }
        ]
    },

    # ==================== ASUS ROG ====================
    {
        "brand": {"name": "Asus", "country_origin": "Taiwan", "tier_category": "Gaming Flagship"},
        "models": [
            {
                "name": "ROG Phone 8 Pro", "series": "ROG Gaming", "release_year": 2024,
                "chipset": "Snapdragon 8 Gen 3 (4nm)", "cpu_architecture": "Octa-core 3.3GHz",
                "gpu": "Adreno 750", "antutu_benchmark_score": 2150000,
                "display_type": "LTPO AMOLED, 1B colors, 165Hz, HDR10", "screen_size_inch": 6.78,
                "refresh_rate_hz": 165, "resolution": "1080 x 2400 pixels (FHD+)", "peak_brightness_nits": 2500,
                "screen_protection": "Corning Gorilla Glass Victus 2",
                "main_camera_mp": "50 MP (Gimbal OIS) + 32 MP (3x telephoto OIS) + 13 MP (ultrawide)",
                "camera_setup": "Triple", "has_ois": True, "optical_zoom_level": "3x Optical",
                "selfie_camera_mp": "32 MP, f/2.5", "video_recording_max": "8K@24fps, 4K@60fps",
                "battery_capacity_mah": 5500, "fast_charging_watt": 65, "has_wireless_charging": True, "wireless_charging_watt": 15,
                "network_gen": "5G", "has_nfc": True, "ip_rating": "IP68", "weight_grams": 225, "os_at_launch": "Android 14, ROG UI",
                "variants": [
                    {"variant_name": "ROG Phone 8 Pro 16GB/512GB", "ram_gb": 16, "storage_gb": 512, "official_msrp_new": 14999000, "aliases": "rog 8 pro 512, rog phone 8 pro 16/512, asus rog 8"},
                    {"variant_name": "ROG Phone 8 Pro Edition 24GB/1TB", "ram_gb": 24, "storage_gb": 1024, "official_msrp_new": 19999000, "aliases": "rog 8 pro 1tb, rog 8 pro 24gb"}
                ]
            }
        ]
    }
]

def seed_master_catalog():
    """Mengisi database dengan master catalog smartphone komprehensif."""
    init_db()
    db = SessionLocal()
    
    brand_count = 0
    model_count = 0
    variant_count = 0

    try:
        for brand_data in CATALOG_DATA:
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
        print(f"[SUCCESS] Seeding Berhasil: {brand_count} Brand, {model_count} Model, {variant_count} Varian HP.")
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Gagal Seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_master_catalog()
