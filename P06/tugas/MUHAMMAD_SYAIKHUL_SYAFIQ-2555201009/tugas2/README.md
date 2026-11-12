# Tugas 2 P06 â€” Hierarki Pegawai Dinas Pertanian Kabupaten Kampar

**Nama:** MUHAMMAD SYAIKHUL SYAFIQ  
**NIM:** 2555201009  
**Instansi:** Dinas Pertanian Kabupaten Kampar

## Deskripsi

Tugas ini menerapkan konsep pewarisan dan polimorfisme dalam Pemrograman Berorientasi Objek (PBO) melalui sistem penggajian pegawai Dinas Pertanian Kabupaten Kampar.

## Struktur Kelas

- `Pegawai`: kelas induk yang menyimpan NIP, nama, dan gaji pokok harian.
- `PegawaiTetap`: menghitung gaji pokok ditambah tunjangan harian.
- `PegawaiHarian`: menghitung gaji berdasarkan upah per jam dan jam kerja.
- `PegawaiKontrak`: menghitung gaji berdasarkan jumlah hari yang dibatasi durasi kontrak.

## Konsep PBO yang Diterapkan

1. **Inheritance:** tiga kelas turunan mewarisi kelas `Pegawai`.
2. **Super:** setiap konstruktor kelas turunan memanggil konstruktor induk.
3. **Polymorphism:** setiap kelas turunan memiliki implementasi `hitung_gaji()` yang berbeda.
4. **Special Methods:** kelas induk menerapkan `__str__`, `__repr__`, `__eq__`, dan `__hash__`.
5. **Encapsulation:** atribut data dikelola melalui atribut privat dan properti.
6. **Validation:** data pegawai dan parameter perhitungan gaji divalidasi.

## Pengujian

Pengujian menggunakan `pytest` untuk memeriksa:

- Perhitungan gaji setiap jenis pegawai.
- Validasi data dan penolakan nilai tidak valid.
- Pemanggilan konstruktor induk.
- Perbandingan objek berdasarkan NIP.
- Penggunaan objek sebagai kunci dictionary.

## Pemeriksaan

Jalankan dari folder `tugas2`:

```powershell
python -m pytest
python -m mypy .\src
python ..\periksa_pbo.py .\src --profil p06