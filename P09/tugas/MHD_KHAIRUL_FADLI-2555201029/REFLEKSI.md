# Refleksi Praktikum P09

## 1. Hal yang Dipelajari

Pada praktikum P09, saya mempelajari penerapan abstraksi dalam pemrograman berorientasi objek menggunakan Python, khususnya Abstract Base Class (ABC), Protocol, dan Enum.

Saya memahami bahwa ABC digunakan untuk membuat kelas abstrak yang tidak dapat dibuat objeknya secara langsung. Kelas turunannya harus mengimplementasikan metode abstrak yang telah ditentukan.

Saya juga mempelajari Protocol sebagai kontrak struktural. Sebuah kelas dapat memenuhi Protocol tanpa harus mewarisi kelas tersebut, selama memiliki atribut dan metode yang sesuai.

Selain itu, saya memahami penggunaan Enum untuk membatasi pilihan status transaksi agar lebih konsisten dan menghindari kesalahan penulisan.

## 2. Kesulitan yang Dihadapi

Kesulitan utama selama praktikum adalah memahami perbedaan antara ABC dan Protocol.

Keduanya sama-sama digunakan untuk mendefinisikan kontrak, tetapi memiliki cara kerja yang berbeda. ABC menggunakan pewarisan, sedangkan Protocol memeriksa kesesuaian struktur objek.

Saya juga mengalami beberapa kesalahan ketika menyesuaikan kelas lama dengan metode abstrak dan tipe Protocol.

## 3. Solusi yang Dilakukan

Untuk mengatasi kesulitan tersebut, saya melakukan beberapa langkah:

1. Mempelajari kembali konsep ABC, Protocol, dan Enum.
2. Memeriksa implementasi metode abstrak pada setiap kelas turunan.
3. Memastikan GerobakDorong memenuhi kontrak Sewaan tanpa mewarisi AlatTani.
4. Menggunakan Enum untuk mengatur status transaksi penyewaan.
5. Memperbaiki pengujian yang terdampak perubahan struktur kelas.
6. Menjalankan pytest, mypy, ruff, dan pemeriksa PBO untuk memastikan program berjalan dengan baik.

## 4. Hasil Pembelajaran

Dari praktikum ini, saya memahami bahwa abstraksi membantu membuat program lebih terstruktur dan mudah dikembangkan.

Saya juga memahami bahwa ABC cocok digunakan untuk kelas-kelas yang memiliki hubungan pewarisan, sedangkan Protocol cocok digunakan ketika beberapa kelas berbeda perlu memenuhi kontrak yang sama.

Penggunaan Enum membantu menjaga konsistensi nilai status transaksi dan mencegah penggunaan status yang tidak dikenal.

## 5. Kesimpulan

Praktikum P09 memberikan pemahaman mengenai pentingnya pemilihan kontrak dalam pemrograman berorientasi objek.

ABC, Protocol, dan Enum memiliki fungsi yang berbeda, tetapi dapat digunakan bersama untuk menghasilkan program yang lebih terstruktur, fleksibel, dan mudah diuji.

Melalui praktikum ini, saya belajar untuk lebih memperhatikan rancangan kelas dan kontrak sebelum mengimplementasikan fitur program.
