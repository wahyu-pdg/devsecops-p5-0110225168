# Inventory Management System

Aplikasi berbasis Python untuk mengelola stok barang melalui Command Line Interface (CLI).

## Fitur

- Menambahkan data barang.
- Menampilkan daftar barang.
- Memperbarui stok barang.
- Menghapus data barang.
- Menampilkan barang dengan stok rendah.
- Menyimpan data barang dalam file JSON.

## Teknologi yang Digunakan

- Python
- Pytest untuk pengujian aplikasi.
- Bandit untuk Static Application Security Testing (SAST).
- GitHub Actions untuk menjalankan pipeline otomatis.

## Struktur Proyek

```text
devsecops-p5-0110225168/
├── inventory/
├── tests/
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── devsecops.yml
```

## Cara Menjalankan Aplikasi

1. Pastikan Python sudah terinstal.
2. Clone repository ini dan masuk ke folder proyek.
3. Instal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:

   ```bash
   python main.py
   ```

   Untuk menggunakan fitur tertentu, jalankan perintah sesuai fitur yang tersedia, misalnya:

   ```bash
   python main.py list
   ```

## Pengujian

Jalankan pengujian menggunakan perintah:

```bash
pytest -v
```

## Pipeline DevSecOps

Proyek ini menggunakan GitHub Actions untuk mengotomatisasi proses pengujian dan pemeriksaan keamanan kode.

Pipeline mencakup:

1. **Build dan Testing:** Memasang dependensi dan menjalankan pengujian menggunakan Pytest.
2. **Security Scanning:** Memindai kode sumber menggunakan Bandit.
3. **Quality Gate:** Memeriksa temuan keamanan berdasarkan tingkat severity dan confidence yang ditentukan dalam konfigurasi Bandit.
4. **Security Report:** Menghasilkan laporan pemindaian dalam format JSON jika proses pemindaian berhasil menghasilkan laporan.

Pipeline berjalan ketika terdapat push ke branch `main` atau pull request yang menargetkan branch `main`.

## Tujuan Proyek

Proyek ini dibuat sebagai implementasi praktikum DevSecOps untuk mempelajari otomatisasi pengujian, pemindaian keamanan kode, dan integrasi keamanan ke dalam alur pengembangan perangkat lunak.