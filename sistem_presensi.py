# =========================================================
# 🎓 SISTEM PRESENSI MAHASISWA
# Decision Tree Sederhana Menggunakan IF-ELSE
# =========================================================

# =========================================================
# IMPORT LIBRARY
# =========================================================

from colorama import Fore, init
from rich.console import Console
from rich.table import Table

# Inisialisasi colorama
init(autoreset=True)

# Console rich
console = Console()

# =========================================================
# DATA AWAL MAHASISWA
# Menggunakan List of Dictionaries
# =========================================================

mahasiswa = [
    {
        "nama": "Andi",
        "kehadiran": "Tinggi",
        "tugas": "Lengkap"
    },
    {
        "nama": "Budi",
        "kehadiran": "Rendah",
        "tugas": "Tidak Lengkap"
    },
    {
        "nama": "Citra",
        "kehadiran": "Tinggi",
        "tugas": "Tidak Lengkap"
    },
    {
        "nama": "Deni",
        "kehadiran": "Rendah",
        "tugas": "Lengkap"
    },
    {
        "nama": "Rina",
        "kehadiran": "Tinggi",
        "tugas": "Lengkap"
    }
]