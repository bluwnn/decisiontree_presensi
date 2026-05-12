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

# =========================================================
# MENAMPILKAN DATA MAHASISWA
# =========================================================

def tampilkan_data():

  table = Table(
    title="📋 DATA MAHASISWA",
    show_lines=True,
    header_style="bold cyan"
  )

  # Header kolom
  table.add_column("Nama", style="white", justify="left")
  table.add_column("Kehadiran", justify="center")
  table.add_column("Tugas", justify="center")
  table.add_column("Status", justify="center")
  table.add_column("Keterangan", justify="center")

  # Menampilkan data mahasiswa
  for data in mahasiswa:

    # Menentukan status dan keterangan otomatis
    status, keterangan = klasifikasi_mahasiswa(
        data["kehadiran"],
        data["tugas"]
    )

    # Warna status
    if status == "Aktif":
        status_warna = "[green]Aktif[/green]"
    else:
        status_warna = "[red]Tidak Aktif[/red]"

    # Warna keterangan
    if keterangan == "Mahasiswa Disiplin":
        ket_warna = "[yellow]Mahasiswa Disiplin[/yellow]"
    else:
        ket_warna = "[white]Perlu Peningkatan[/white]"

    # Tambahkan row ke tabel
    table.add_row(
        data["nama"],
        data["kehadiran"],
        data["tugas"],
        status_warna,
        ket_warna
    )

console.print(Table)

# =========================================================
# MENAMBAHKAN DATA MAHASISWA
# =========================================================

def tambah_mahasiswa():

  print(Fore.CYAN + "\n➕ TAMBAH MAHASISWA")
  print(Fore.CYAN + "-" * 35)

  nama = input("Masukkan Nama : ")

  kehadiran = input(
      "Masukkan Kehadiran (Tinggi/Rendah) : "
  )

  tugas = input(
      "Masukkan Tugas (Lengkap/Tidak Lengkap) : "
  )

  # Menambahkan data baru
  mahasiswa.append({
      "nama": nama,
      "kehadiran": kehadiran,
      "tugas": tugas
  })

  # Klasifikasi otomatis
  status, keterangan = klasifikasi_mahasiswa(
      kehadiran,
      tugas
  )

  print(Fore.GREEN + "\n✅ Data mahasiswa berhasil ditambahkan!")

  print(Fore.YELLOW + f"Status     : {status}")
  print(Fore.YELLOW + f"Keterangan : {keterangan}")


# =========================================================
# MENCARI MAHASISWA
# =========================================================

def cari_mahasiswa():

    print(Fore.CYAN + "\n🔍 CARI MAHASISWA")
    print(Fore.CYAN + "-" * 35)

    keyword = input("Masukkan nama mahasiswa : ")

    ditemukan = False

    for data in mahasiswa:

        if keyword.lower() in data["nama"].lower():

            status, keterangan = klasifikasi_mahasiswa(
                data["kehadiran"],
                data["tugas"]
            )

            print(Fore.GREEN + "\n✅ Data ditemukan")
            print("-" * 35)

            print(f"Nama        : {data['nama']}")
            print(f"Kehadiran   : {data['kehadiran']}")
            print(f"Tugas       : {data['tugas']}")
            print(f"Status      : {status}")
            print(f"Keterangan  : {keterangan}")

            ditemukan = True

    if not ditemukan:
        print(Fore.RED + "\n❌ Mahasiswa tidak ditemukan")
# =========================================================
# MENCARI MAHASISWA
# =========================================================

def cari_mahasiswa():

    print(Fore.CYAN + "\n🔍 CARI MAHASISWA")
    print(Fore.CYAN + "-" * 35)

    keyword = input("Masukkan nama mahasiswa : ")

    ditemukan = False

    for data in mahasiswa:

        if keyword.lower() in data["nama"].lower():

            status, keterangan = klasifikasi_mahasiswa(
                data["kehadiran"],
                data["tugas"]
            )

            print(Fore.GREEN + "\n✅ Data ditemukan")
            print("-" * 35)

            print(f"Nama        : {data['nama']}")
            print(f"Kehadiran   : {data['kehadiran']}")
            print(f"Tugas       : {data['tugas']}")
            print(f"Status      : {status}")
            print(f"Keterangan  : {keterangan}")

            ditemukan = True

    if not ditemukan:
        print(Fore.RED + "\n❌ Mahasiswa tidak ditemukan")  