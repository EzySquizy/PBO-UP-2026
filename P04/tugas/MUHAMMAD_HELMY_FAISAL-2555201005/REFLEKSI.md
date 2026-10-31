# Refleksi P04 - Anggota Kelas vs Anggota Objek

## Hal Penting yang Dipelajari
1. **Atribut Kelas (`AlatTani._jumlah_terdaftar`):**
   Sempat keliru pakai `self` untuk pencacah. Akibatnya nilai tidak pernah bertambah secara global. Memakai nama kelas terbukti membuat data terhitung terpusat untuk semua instansi.

2. **Default Argument Berbahaya (`[]`):**
   Menetapkan list kosong pada parameter fungsi ternyata membuat objek berbagi referensi memori yang sama. Solusinya selalu gunakan `None` sebagai default, lalu inisialisasi list baru di dalam body fungsi.

3. **Ruff vs Pytest:**
   Linter seperti Ruff hanya menangkap kesalahan pola/sintaksis (seperti mutable default argument), tetapi tidak membaca logika kode. Pengujian logika penuh tetap bergantung pada skenario unit test di Pytest.

4. **Pola Selisih pada Test Counter:**
   Karena Pytest menjalankan fungsi uji secara acak, cara paling valid menguji atribut kelas adalah mencatat nilai awal terlebih dahulu, baru memastikan selisihnya sesuai (`assert total == awal + n`).

## Kesimpulan
Gunakan `self` hanya untuk atribut yang unik per objek. Aturan umum, konstanta, pencacah global, dan fungsi utilitas wajib ditempatkan pada level kelas.