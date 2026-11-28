# AI_USAGE.md

## Informasi AI

- **Nama AI:** ChatGPT
- **Pengembang:** OpenAI
- **Model:** GPT-6

## Bentuk Penggunaan AI

AI digunakan sebagai alat bantu dalam pengerjaan praktikum P10. Penggunaan AI meliputi:

1. **Memahami Materi**
   - Membantu memahami konsep hierarki eksepsi.
   - Menjelaskan perbedaan `DataTidakValid` dan `AturanUsahaDilanggar`.
   - Membantu memahami penggunaan context manager.

2. **Pemeriksaan dan Perbaikan Kode**
   - Membantu memeriksa penerapan hierarki kelas eksepsi.
   - Membantu menentukan penggunaan eksepsi khusus.
   - Membantu memeriksa penggunaan `raise ... from ...`.
   - Membantu memeriksa mekanisme rollback pada transaksi.

3. **Pengujian Program**
   - Membantu menyusun pengujian pemisahan cabang eksepsi.
   - Membantu menambahkan pengujian batas maksimal 10 jenis alat.
   - Membantu menguji pembatalan transaksi ketika terjadi kesalahan.
   - Membantu menganalisis hasil pengujian.

## Verifikasi Hasil

Kode diperiksa menggunakan beberapa perintah berikut:

- `python -m pytest`
- `python periksa_pbo.py src --profil p10`
- `python -m mypy`
- `python -m src.main`

Hasil pemeriksaan terakhir:

- **Pytest:** 126 passed.
- **Pemeriksa PBO:** LOLOS.
- **Mypy:** Tidak ditemukan masalah pada 38 berkas sumber.
- **Program utama:** Berhasil dijalankan.

## Tanggung Jawab Penggunaan AI

AI digunakan sebagai alat bantu untuk memahami materi dan menyelesaikan kendala selama praktikum. Setiap perubahan kode diperiksa dan dijalankan kembali untuk memastikan program berjalan sesuai kebutuhan praktikum.