# Refleksi Tugas 2 P06

Pada Tugas 2 P06, saya membuat hierarki kelas pegawai dengan studi kasus Dinas Pertanian Kabupaten Kampar.

Saya membuat kelas induk `Pegawai` dan tiga kelas turunan, yaitu `PegawaiTetap`, `PegawaiHarian`, dan `PegawaiKontrak`. Ketiga kelas turunan memiliki cara perhitungan gaji yang berbeda sesuai dengan jenis pegawainya.

Melalui tugas ini, saya mempelajari penggunaan pewarisan, polimorfisme, dan `super()` dalam Python. Saya juga menerapkan empat method khusus, yaitu `__str__`, `__repr__`, `__eq__`, dan `__hash__` pada kelas induk.

Kesulitan yang saya temui adalah membedakan pola perhitungan gaji pada setiap kelas turunan. Saya mengatasinya dengan memberikan atribut tambahan dan melakukan override pada method `hitung_gaji()`.

Saya juga membuat pengujian untuk memastikan perhitungan gaji, validasi data, kesamaan objek berdasarkan NIP, dan penggunaan objek sebagai kunci dictionary berjalan dengan benar.

Berdasarkan hasil pemeriksaan sementara, seluruh 20 pengujian berhasil, pemeriksaan mypy tidak menemukan masalah tipe, dan pemeriksa disiplin PBO profil P06 dinyatakan lolos.

Dari tugas ini, saya memahami bahwa pewarisan dapat mengurangi pengulangan kode dan polimorfisme memungkinkan setiap jenis pegawai memiliki perilaku perhitungan gaji yang berbeda.