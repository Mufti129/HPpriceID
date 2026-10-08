"""
Kamus Slang & Terminologi Khusus Pasar Jual Beli Smartphone (HP) Bekas & Baru di Indonesia.
Digunakan oleh NLP Normalizer dan Scam Detector untuk ekstraksi metadata spesifikasi pasar sekunder.
"""

WARRANTY_PATTERNS = {
    "resmi_indonesia": [
        r"\bibox\b", r"\bdigimap\b", r"\bgdn\b", r"\bsein\b", r"\btam\b", r"\berajaya\b",
        r"\bresmi\s*indo(?:nesia)?\b", r"\bpa/a\b", r"\bid/a\b", r"\bsa/a\b", r"\bgaransi\s*resmi\b"
    ],
    "ex_inter_pajak": [
        r"\bimei\s*bea\s*cukai\b", r"\blolos\s*beacukai\b", r"\bpajak\s*resmi\b",
        r"\bimei\s*kemenkeu\b", r"\bsinyal\s*permanen\b", r"\ball\s*operator\s*permanen\b"
    ],
    "ex_inter_non_pajak": [
        r"\binter\b", r"\bex\s*inter\b", r"\bll/a\b", r"\bza/a\b", r"\bzp/a\b", r"\bj/a\b",
        r"\bkh/a\b", r"\bch/a\b", r"\bnon\s*pajak\b"
    ],
    "distributor": [
        r"\bgaransi\s*distributor\b", r"\bdistri\b", r"\bbless\b", r"\bplatinum\b"
    ]
}

IMEI_SIGNAL_PATTERNS = {
    "kemenperin_resmi": [
        r"\bimei\s*terdaftar\s*(?:di\s*)?kemenperin\b", r"\bimei\s*kemenperin\b",
        r"\bresmi\s*kemenperin\b", r"\bsinyal\s*aman\s*selamanya\b"
    ],
    "all_operator": [
        r"\ball\s*operat(?:or|er)\b", r"\ball\s*provider\b", r"\bsinyal\s*on\b",
        r"\bsinyal\s*aman\b", r"\bbebas\s*reset\b", r"\bpermanen\s*all\s*op\b"
    ],
    "smartfren_temp": [
        r"\bsmartfren\s*only\b", r"\bsmartfen\s*only\b", r"\bimei\s*3\s*bulan\b",
        r"\btembak\s*sinyal\b", r"\bkartu\s*smartfren\b"
    ],
    "wifi_only": [
        r"\bwifi\s*only\b", r"\bno\s*service\b", r"\bsinyal\s*blokir\b", r"\bimei\s*blokir\b",
        r"\bsinyal\s*(?:mati|hilang|off)\b", r"\bbypass\s*sinyal\b"
    ]
}

BATTERY_PATTERNS = [
    r"\bbh\s*[:\s]?\s*(\d{2,3})\s*%?\b",
    r"\bbattery\s*health\s*[:\s]?\s*(\d{2,3})\s*%?\b",
    r"\bbatre\s*[:\s]?\s*(\d{2,3})\s*%",
    r"\bbh\s*(\d{2,3})\b"
]

COMPLETENESS_PATTERNS = {
    "fullset_original": [
        r"\bfullset\s*ori(?:ginal)?\b", r"\bkomplit\s*ori(?:ginal)?\b", r"\bfullset\s*bawaan\b",
        r"\blengkap\s*nota\b", r"\bfullset\s*dus\s*ori\b", r"\bfull\s*set\b"
    ],
    "fullset_oem": [
        r"\bfullset\s*oem\b", r"\bdus\s*oem\b", r"\bcharger\s*oem\b", r"\bkotak\s*oem\b"
    ],
    "batangan": [
        r"\bbatangan\b", r"\bunit\s*only\b", r"\bhp\s*(?:aja|tok|doang)\b",
        r"\bno\s*box\b", r"\btanpa\s*(?:dus|kotak|box)\b", r"\bbatang\b"
    ]
}

PHYSICAL_GRADE_PATTERNS = {
    "grade_a_plus": [
        r"\blike\s*new\b", r"\bmulus\s*99%?\b", r"\bgrade\s*a\+?\b", r"\bistimewa\b",
        r"\bno\s*minus\s*mulus\b", r"\bbeku\b", r"\bserasa\s*baru\b"
    ],
    "grade_a": [
        r"\bmulus\s*95%?\b", r"\bmulus\s*wajar\b", r"\bno\s*minus\b", r"\bmulus\b",
        r"\bterawat\b", r"\bbaret\s*pemakaian\s*halus\b"
    ],
    "grade_b": [
        r"\bmulus\s*90%?\b", r"\blecet\s*pemakaian\b", r"\blecet\s*wajar\b", r"\bdent\s*tipis\b",
        r"\bkorosi\s*tipis\b", r"\bjamur\s*bodi\s*tipis\b"
    ],
    "grade_c": [
        r"\bdent\s*(?:parah|kasar|banyak)\b", r"\bkorosi\s*parah\b", r"\bjamur\s*bodi\b",
        r"\bbackdoor\s*retak\b", r"\bkaca\s*belakang\s*retak\b", r"\bbodi\s*bengkok\b"
    ]
}

SCREEN_PATTERNS = {
    "normal_original": [
        r"\blayar\s*ori(?:ginal)?\b", r"\blcd\s*ori(?:ginal)?\b", r"\blayar\s*jernih\b",
        r"\blayar\s*mulus\b", r"\bno\s*shadow\b", r"\blcd\s*bawaan\b"
    ],
    "layar_ganti_oem": [
        r"\blcd\s*gantian\b", r"\blayar\s*ganti\b", r"\blcd\s*oem\b", r"\blcd\s*incell\b",
        r"\blcd\s*gx\b", r"\blcd\s*oled\s*oem\b", r"\bpernah\s*ganti\s*lcd\b"
    ],
    "shadow_tipis": [
        r"\bshadow\s*tipis\b", r"\bshadow\s*samar\b", r"\blayar\s*shadow\s*tipis\b"
    ],
    "shadow_tebal": [
        r"\bshadow\s*(?:tebal|pekat|merah|jelas)\b", r"\bshadow\s*banget\b"
    ],
    "green_line": [
        r"\bgreen\s*line\b", r"\blayar\s*garis\b", r"\bgaris\s*hijau\b",
        r"\blayar\s*bergaris\b", r"\bwhite\s*screen\b", r"\btompel\b"
    ],
    "glass_retak": [
        r"\bretak\s*kaca\b", r"\bglass\s*retak\b", r"\blayar\s*retak\s*sentuh\s*normal\b"
    ]
}

BIOMETRICS_PATTERNS = {
    "normal": [
        r"\bface\s*id\s*(?:on|aktif|normal|jalan|hidup)\b",
        r"\btouch\s*id\s*(?:on|aktif|normal|jalan|hidup)\b",
        r"\bfingerprint\s*(?:on|aktif|normal)\b"
    ],
    "broken": [
        r"\bface\s*id\s*(?:off|mati|rusak|gak\s*bisa|hilang)\b",
        r"\btouch\s*id\s*(?:off|mati|rusak|gak\s*bisa)\b",
        r"\bfingerprint\s*(?:off|mati|rusak)\b",
        r"\bno\s*face\s*id\b", r"\bface\s*id\s*down\b"
    ]
}

TRUETONE_PATTERNS = {
    "aktif": [
        r"\btruetone\s*(?:on|aktif|jalan|hidup)\b",
        r"\btrue\s*tone\s*(?:on|aktif|jalan|hidup)\b"
    ],
    "mati": [
        r"\btruetone\s*(?:off|mati|hilang|tidak\s*aktif)\b",
        r"\btrue\s*tone\s*(?:off|mati|hilang)\b"
    ]
}

STORAGE_PATTERNS = [
    r"\b(1024|512|256|128|64|32|16)\s*(?:gb|gigabyte|g)\b",
    r"\b1\s*(?:tb|terabyte)\b",
    r"\bram\s*(\d{1,2})\s*[/,]\s*(\d{2,4})\s*(?:gb)?\b"
]

DP_SCAM_PATTERNS = [
    r"\bdp\b", r"\buang\s*muka\b", r"\bcicilan\b", r"\bangsuran\b",
    r"\bkredit\b", r"\bcredit\b", r"\bleasing\b", r"\bpaylater\b",
    r"\bakulaku\b", r"\bkredivo\b", r"\btanda\s*jadi\b"
]

PRICE_SLANG_PATTERNS = [
    (r"(\d+(?:[\.,]\d+)?)\s*(?:jt|juta)", 1_000_000),
    (r"(\d+(?:[\.,]\d+)?)\s*k\b", 1_000),
    (r"(\d+(?:[\.,]\d+)?)\s*rb\b", 1_000),
]
