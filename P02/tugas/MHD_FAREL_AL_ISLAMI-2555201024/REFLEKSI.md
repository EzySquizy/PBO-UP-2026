# Refleksi Praktikum P02: Kelas Pertama SIPALA (Penyewa dan Alat Tani)

Pada praktikum Pertemuan 2 (P02), saya mempelajari dasar-dasar perancangan kelas dan enkapsulasi awal dalam Pemrograman Berorientasi Objek (PBO) menggunakan Python:

1. **Memilah Entitas dan Perilaku:** Belajar memecah deskripsi kasus nyata (UPJA) ke dalam kelas-kelas domain terpisah (`Penyewa` dan `AlatTani`) di dalam folder `src/model/`[cite: 9, 11, 13].
2. **Konstruktor dan Peran `self`:** Menggunakan method khusus `__init__` untuk inisialisasi atribut dengan anotasi tipe data yang lengkap, serta memahami bagaimana argumen `self` membawa data objek masing-masing[cite: 9, 11, 13].
3. **Parameter Berdefault:** Menerapkan nilai default pada parameter konstruktor (seperti nomor telepon `-`) untuk data opsional yang tidak wajib diisi oleh setiap entitas[cite: 9, 11, 12].
4. **Kemandirian Objek:** Membuktikan melalui pengujian (`pytest`) bahwa beberapa objek yang dibuat dari cetak biru (kelas) yang sama masing-masing menyimpan data dan kondisinya secara terpisah[cite: 9, 15].
5. **Bahaya Akses Atribut Langsung:** Menyadari kelemahan enkapsulasi Python di mana atribut bergaris bawah tunggal (`_tarif_harian`) masih dapat diubah secara bebas dari luar tanpa peringatan sistem, yang melandasi kebutuhan penggunaan `@property` pada pertemuan berikutnya[cite: 9, 15].