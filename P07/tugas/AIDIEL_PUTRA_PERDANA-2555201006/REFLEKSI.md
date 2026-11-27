## Refleksi

Pada praktikum ini saya mempelajari cara mengganti rantai percabangan `if-isinstance` yang kaku dengan polimorfisme menggunakan `DaftarHarga` sehingga penambahan jenis alat baru seperti `Penggiling` bisa langsung dihitung tanpa mengubah kode yang sudah berjalan, sekaligus mempraktikkan *pattern matching* pada `PerintahKonsol` dan pemformatan berbasis tipe lewat `functools.singledispatch`.

Kendala yang saya temui saat pengerjaan adalah melengkapi struktur kelas `PerintahKonsol` yang di panduan hanya berupa potongan method, menyesuaikan pemanggilan method `DaftarHarga` agar tidak memicu eror atribut maupun `Missing return statement` saat dicek dengan `mypy`, serta menambahkan *docstring* yang sempat terlewat pada kelas tersebut sehingga gagal lolos pemeriksaan `periksa_pbo.py`.