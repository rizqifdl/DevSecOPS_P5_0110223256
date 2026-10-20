# SecureTask Manager

SecureTask Manager adalah aplikasi CLI sederhana berbasis Python untuk mencatat tugas, melihat daftar tugas, dan menandai tugas sebagai selesai. Data disimpan secara lokal dalam file JSON (`tasks.json`).

## Teknologi yang digunakan

- Python 3.12
- `unittest` untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk otomatisasi pipeline CI/CD

## Struktur utama

- `app.py`: titik masuk aplikasi
- `cli.py`: antarmuka terminal
- `task_manager.py`: logika pengelolaan tugas
- `validators.py`: validasi judul tugas
- `storage.py`: penyimpanan dan pembacaan JSON
- `tests/`: unit test
- `.github/workflows/devsecops.yml`: pipeline GitHub Actions

## Cara menjalankan aplikasi

Pastikan Python 3.12 atau versi kompatibel sudah terpasang.

```bash
git clone https://github.com/USERNAME/devsecops-p5-NIM.git
cd devsecops-p5-NIM
python app.py
```

Pilih menu `1` untuk melihat tugas, `2` untuk menambah tugas, `3` untuk menyelesaikan tugas, atau `4` untuk keluar. Ganti URL clone di atas dengan URL repository milik Anda.

## Menjalankan pengujian lokal

```bash
python -m unittest discover -s tests -v
```

## Overview pipeline CI/CD

Workflow berada di `.github/workflows/devsecops.yml` dan berjalan ketika ada `push` ke branch `main` atau `pull_request` yang menargetkan branch `main`. Semua job menggunakan runner `ubuntu-latest`.

1. **build**: checkout repository, menyiapkan Python, menginstal dependencies, melakukan kompilasi pemeriksaan sintaks, lalu menjalankan unit test.
2. **sast-scan**: berjalan setelah job `build` berhasil melalui `needs: build`. Job ini menjalankan Bandit untuk memindai pola kode Python yang berpotensi tidak aman.

Jika unit test gagal, job SAST tidak akan berjalan karena bergantung pada job `build`. Hasil tiap job dapat dilihat pada tab **Actions** di GitHub.

## Pengembangan

Proyek ini dibuat sebagai implementasi tugas DevSecOps
dengan GitHub Actions, unit testing, dan SAST menggunakan Bandit.