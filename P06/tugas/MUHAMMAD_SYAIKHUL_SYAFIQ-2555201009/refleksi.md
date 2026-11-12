
# Refleksi Praktikum P06

Pada praktikum P06, saya mempelajari penerapan pewarisan dan polimorfisme dalam pemrograman berorientasi objek.

Saya membuat kelas induk `AlatTani` dan tiga kelas turunan, yaitu `Traktor`, `PompaAir`, dan `Perontok`. Setiap kelas turunan memiliki atribut dan perhitungan biaya sewa yang berbeda.

Saya juga mempelajari penggunaan `super()` untuk memanggil method kelas induk serta empat method khusus, yaitu `__str__`, `__repr__`, `__eq__`, dan `__hash__`.

Kesulitan yang saya temui adalah mengintegrasikan perhitungan biaya setiap jenis alat ke dalam transaksi sewa tanpa mengubah data tarif yang sudah disimpan. Kesulitan tersebut diselesaikan dengan menyimpan snapshot subtotal ketika transaksi dibuat.

Dari praktikum ini, saya memahami bahwa pewarisan dapat membantu penggunaan kembali kode, sedangkan polimorfisme memungkinkan setiap kelas turunan memiliki perilaku yang berbeda.

Sebagai pemeriksaan akhir, saya menjalankan pemeriksa PBO, mypy, dan pytest. Hasilnya menunjukkan pemeriksaan struktur lolos, tidak ditemukan masalah tipe, dan 102 pengujian berhasil.
