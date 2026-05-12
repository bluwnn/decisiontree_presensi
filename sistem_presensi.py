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

# =========================================================
# FUNGSI DECISION TREE SEDERHANA MENGGUNAKAN IF-ELSE
# =========================================================

def klasifikasi_mahasiswa(kehadiran, tugas):
    """
    Menentukan status dan keterangan mahasiswa
    menggunakan IF-ELSE sebagai simulasi Decision Tree
    """

    # Menentukan status
    if kehadiran.lower() == "tinggi":
        status = "Aktif"
    else:
        status = "Tidak Aktif"

    # Menentukan keterangan
    if kehadiran.lower() == "tinggi" and tugas.lower() == "lengkap":
        keterangan = "Mahasiswa Disiplin"
    else:
        keterangan = "Perlu Peningkatan"

    return status, keterangan


# =========================================================
# HEADER PROGRAM
# =========================================================

def tampilkan_header():

    print(Fore.CYAN + "=" * 72)
    print(Fore.CYAN + "🎓 SISTEM PRESENSI MAHASISWA 🎓".center(72))
    print(Fore.CYAN + "=" * 72)


# =========================================================
# MENU PROGRAM
# =========================================================

def tampilkan_menu():

    print(Fore.CYAN + "\n📌 MENU PROGRAM")
    print(Fore.CYAN + "-" * 35)

    print("1. 📋 Lihat Data Mahasiswa")
    print("2. ➕ Tambah Mahasiswa")
    print("3. 🔍 Cari Mahasiswa")
    print("4. 📊 Statistik Mahasiswa")
    print("5. ⬅️ Keluar")