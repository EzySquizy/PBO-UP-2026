# Refleksi Pertemuan 4: Milik Kelas vs Milik Objek

## Poin Utama & Pengalaman Praktikum
1. **Pencacah Bocor (`self` vs Nama Kelas):**
   Sering keliru nulis `self._jumlah_terdaftar += 1` yang bikin nilainya gak nambah. Harusnya dipanggil lewat nama kelas (`AlatTani._jumlah_terdaftar += 1`) biar terhitung untuk semua objek.

2. **List Kosong di Parameter (`[]`):**
   Menggunakan list `[]` sebagai nilai bawaan parameter itu berbahaya karena list-nya bakal dipakai bersama oleh seluruh objek. Solusinya set default-nya ke `None`, lalu inisialisasi list di dalam fungsi.

3. **Batasan Linter (Ruff):**
   Ruff cuma bisa mengecek kesalahan format/sintaksis dan pola rawan (kayak list kosong), tapi gak bisa mendeteksi salah logika (kayak pemanggilan `self` pada pencacah). Jadi tetep wajib bikin pengujian manual pakai Pytest.

4. **Testing Pencacah di Pytest:**
   Gak boleh mematok angka pasti (`assert ... == 2`) karena urutan tes di Pytest itu acak. Wajib pakai pola selisih: ambil nilai `awal`, jalankan pembuat objek, baru cek `assert ... == awal + n`.

## Kesimpulan
Gunakan `self` hanya untuk data pribadi milik instansi objek. Untuk data bersama, aturan umum, atau fungsi utilitas, manfaatkan atribut kelas, `@classmethod`, atau `@staticmethod`.