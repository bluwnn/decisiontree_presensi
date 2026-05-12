# 🎓 Sistem Presensi Mahasiswa dengan Decision Tree Sederhana

Mini aplikasi terminal modern menggunakan Python untuk mensimulasikan konsep klasifikasi sederhana menggunakan IF-ELSE sebagai Decision Tree.

---

# 📌 Deskripsi Program

Program ini dibuat untuk menentukan status mahasiswa berdasarkan:

- tingkat kehadiran
- status tugas

Program menggunakan:

- IF-ELSE
- list of dictionaries
- terminal interaktif
- tabel modern menggunakan library Rich

---

# ✨ Fitur Program

✅ Menampilkan seluruh data mahasiswa  
✅ Menambahkan mahasiswa baru  
✅ Mencari mahasiswa berdasarkan nama  
✅ Statistik mahasiswa  
✅ Tampilan terminal modern dan berwarna  
✅ Decision Tree sederhana menggunakan IF-ELSE  
✅ Looping menu interaktif

---

# 🧠 Konsep Decision Tree

Program menggunakan IF-ELSE sebagai simulasi sederhana konsep Decision Tree.

Aturan klasifikasi:

## Status Mahasiswa

- Jika Kehadiran = Tinggi
  → Status = Aktif

- Jika Kehadiran = Rendah
  → Status = Tidak Aktif

## Keterangan Mahasiswa

- Jika Kehadiran = Tinggi DAN Tugas = Lengkap
  → Mahasiswa Disiplin

- Selain itu
  → Perlu Peningkatan

---

# 📦 Library yang Digunakan

## 1. colorama

Digunakan untuk memberikan warna pada terminal.

## 2. rich

Digunakan untuk:

- membuat tabel modern
- mempercantik tampilan terminal
- membuat output lebih rapi

---

# ▶️ Cara Install

## Install library

```bash
pip install colorama rich
```

---

# ▶️ Cara Menjalankan Program

```bash
python sistem_presensi.py
```

---

# 📂 Struktur Folder

```text
sistem-presensi-decision-tree/
├── sistem_presensi.py
├── README.md
```

---

# 📋 Struktur Data

Program menggunakan struktur data:

```python
list of dictionaries
```

Contoh:

```python
{
    "nama": "Andi",
    "kehadiran": "Tinggi",
    "tugas": "Lengkap"
}
```

---

# 💻 Contoh Tampilan Terminal

```text
=======================================================================
🎓 SISTEM PRESENSI MAHASISWA - DECISION TREE 🎓
=======================================================================

📌 MENU PROGRAM
-----------------------------------
1. 📋 Lihat Data Mahasiswa
2. ➕ Tambah Mahasiswa
3. 🔍 Cari Mahasiswa
4. 📊 Statistik Mahasiswa
5. ❌ Keluar
```

---

# 🎯 Tujuan Pembelajaran

Program ini dibuat untuk mempelajari:

- dasar IF-ELSE
- konsep Decision Tree sederhana
- penggunaan function
- penggunaan looping
- penggunaan list dan dictionary
- pembuatan terminal interaktif Python

---

# 🎮 Demo Singkat Program

<video controls src="demo_singkat.mp4" title="Title"></video>
