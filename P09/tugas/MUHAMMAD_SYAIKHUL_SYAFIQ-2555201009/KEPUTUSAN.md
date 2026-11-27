# Keputusan Desain P09

## Penggunaan ABC

Saya menggunakan ABC pada kelas AlatTani karena semua jenis alat pertanian harus memiliki perilaku tertentu, yaitu biaya_tambahan dan syarat_pemakaian. ABC cocok digunakan karena Traktor, PompaAir, dan Perontok merupakan turunan AlatTani serta memiliki data dan perilaku umum yang sama, seperti kode, nama, tarif, validasi, dan perhitungan biaya_sewa. Dengan menggunakan @abstractmethod, setiap kelas turunan diwajibkan menyediakan implementasi metode tersebut.

## Penggunaan Protocol

Saya menggunakan Protocol Sewaan pada DaftarHarga karena daftar harga tidak seharusnya bergantung pada pewarisan kelas AlatTani. DaftarHarga hanya membutuhkan objek yang memiliki atribut kode, nama, dan metode biaya_sewa. Protocol memungkinkan objek lain, seperti GerobakDorong, memenuhi kontrak tersebut tanpa harus menjadi turunan AlatTani. Dengan demikian, ABC digunakan ketika hubungan pewarisan memang diperlukan, sedangkan Protocol digunakan ketika program hanya membutuhkan kesesuaian perilaku suatu objek.