
# Refleksi Praktikum P09

Pada praktikum P09, saya mempelajari konsep abstraksi dalam pemrograman berorientasi objek. Saya memahami bahwa kelas abstrak dapat digunakan untuk menetapkan aturan yang harus diterapkan oleh kelas turunannya. Dengan menggunakan `ABC` dan `@abstractmethod`, kelas `AlatTani` dapat menentukan metode yang wajib dimiliki oleh setiap jenis alat pertanian.

Saya juga mempelajari `Protocol` sebagai cara menentukan kontrak berdasarkan perilaku suatu objek tanpa mengharuskannya mewarisi kelas tertentu. Penerapan ini membuat `DaftarHarga` lebih fleksibel karena dapat menerima objek lain selama memiliki atribut dan metode yang sesuai dengan kontrak `Sewaan`.

Selain itu, saya mempelajari `Enum` untuk mengelola status transaksi penyewaan. Dengan `StatusSewa`, pilihan status menjadi lebih teratur dan tidak bergantung pada penulisan teks secara bebas.

Kendala yang saya temui adalah menyesuaikan pengujian setelah kelas `AlatTani` diubah menjadi kelas abstrak serta memperbaiki kesalahan pemeriksaan tipe data menggunakan mypy. Setelah melakukan perbaikan dan pengujian kembali, saya memahami bahwa abstraksi membantu membuat program lebih terstruktur, fleksibel, dan mudah dikembangkan.

Dari praktikum ini, saya belajar bahwa penggunaan ABC, Protocol, dan Enum memiliki tujuan yang berbeda, tetapi dapat digunakan bersama untuk menghasilkan program yang lebih baik.
