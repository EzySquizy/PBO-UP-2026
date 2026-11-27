# REFLEKSI P06
## Pewarisan: Satu Induk, Tiga Jenis Alat

### 1. Hal yang Saya Pelajari

Pada praktikum P06, saya mempelajari konsep pewarisan (inheritance) dalam pemrograman berorientasi objek. Pewarisan memungkinkan sebuah kelas turunan menggunakan atribut dan metode dari kelas induk sehingga kode menjadi lebih terstruktur dan dapat digunakan kembali.

Saya menerapkan kelas induk AlatTani dengan tiga kelas turunan, yaitu Traktor, PompaAir, dan Perontok. Saya juga membuat hierarki Pegawai yang terdiri dari kelas Pegawai, PegawaiTetap, PegawaiHarian, dan PegawaiKontrak.

### 2. Penggunaan super()

Saya memahami bahwa super() digunakan untuk memanggil konstruktor atau metode dari kelas induk. Setiap kelas turunan perlu memanggil super().__init__() agar atribut yang dimiliki kelas induk dapat diinisialisasi dengan benar.

### 3. Perbedaan Override

Saya mempelajari tiga pola penimpaan metode:
- Menambahkan komponen penghasilan atau biaya dari hasil perhitungan kelas induk.
- Menghitung nilai berdasarkan atribut khusus milik kelas turunan.
- Mengubah nilai masukan sebelum memanggil metode kelas induk.

Ketiga pola tersebut diterapkan pada perhitungan biaya sewa alat pertanian dan penghasilan pegawai.

### 4. Kesulitan yang Dihadapi

Kesulitan yang saya hadapi adalah memastikan setiap kelas turunan memanggil konstruktor kelas induk dengan benar, membedakan pola override, dan memastikan perhitungan biaya serta penghasilan menghasilkan nilai yang sesuai.

Saya juga menemukan masalah encoding BOM pada file pegawai.py. Masalah tersebut berhasil diperbaiki dengan mengubah file menjadi UTF-8 tanpa BOM.

### 5. Pengujian dan Hasil

Saya menggunakan Ruff untuk memeriksa kualitas kode, mypy untuk pemeriksaan tipe, pytest untuk menjalankan pengujian, dan periksa_pbo.py untuk memeriksa disiplin pemrograman berorientasi objek.

Hasil pengujian terakhir:
- Ruff: All checks passed.
- Mypy: Success, no issues found in 23 source files.
- Pytest: 131 passed.
- Pemeriksa P06: LOLOS.

### 6. Kesimpulan

Melalui praktikum ini, saya memahami bahwa pewarisan bukan hanya tentang membuat kelas turunan, tetapi juga tentang menggunakan kembali perilaku kelas induk dan menyesuaikannya sesuai kebutuhan. Saya juga memahami pentingnya pemanggilan super(), method overriding, validasi data, serta pengujian untuk memastikan program berjalan dengan benar.
