# Refleksi Praktikum P09

Pada praktikum P09, saya mempelajari penggunaan kelas abstrak (`ABC`), `Protocol`, dan `Enum` dalam pemrograman berorientasi objek.

Kelas abstrak membantu menetapkan aturan yang wajib diterapkan oleh kelas turunannya. Dengan demikian, setiap jenis alat tani harus menyediakan perilaku yang telah ditentukan oleh kelas induk.

Saya juga mempelajari `Protocol` sebagai kontrak struktural. Sebuah kelas dapat memenuhi kontrak `Sewaan` tanpa harus mewarisi kelas tertentu, selama memiliki atribut dan metode yang dibutuhkan.

Selain itu, `Enum` membantu membatasi status penyewaan agar hanya menggunakan nilai yang telah ditentukan. Status tersebut juga digunakan untuk mengatur apakah transaksi masih boleh diubah.

Tantangan dalam praktikum ini adalah memahami perbedaan antara pewarisan dan kontrak struktural serta memastikan perubahan struktur kode tidak mengubah hasil perhitungan biaya sewa.

Setelah menyelesaikan praktikum, seluruh pengujian berhasil dijalankan dengan hasil 102 tes lulus. Pemeriksaan MyPy dan pemeriksa disiplin PBO juga berhasil tanpa pelanggaran.