
# Keputusan Desain P09

**1. Pemilihan Abstract Class (ABC)**

Saya menggunakan Abstract Base Class (ABC) pada kelas `AlatTani` karena beberapa jenis alat pertanian memiliki atribut dan fungsi dasar yang sama, seperti kode alat, nama alat, tarif sewa, dan perhitungan biaya sewa. Namun, setiap jenis alat memiliki aturan biaya tambahan dan syarat pemakaian yang berbeda. Oleh karena itu, `AlatTani` dibuat sebagai kelas abstrak dengan metode `biaya_tambahan()` dan `syarat_pemakaian()` yang wajib diterapkan oleh setiap kelas turunannya.

**2. Pemilihan Protocol**

Saya menggunakan `Protocol` pada `Sewaan` agar objek yang memiliki struktur dan fungsi sesuai kontrak dapat digunakan tanpa harus mewarisi kelas yang sama. Contohnya adalah `GerobakDorong`, yang dapat digunakan oleh `DaftarHarga` meskipun tidak mewarisi `AlatTani`. Dengan cara ini, program menjadi lebih fleksibel karena cukup memenuhi struktur metode dan atribut yang ditentukan oleh Protocol.

**3. Pemilihan Enum**

Saya menggunakan `Enum` pada `StatusSewa` untuk membatasi status penyewaan agar hanya menggunakan nilai yang sudah ditentukan, yaitu `DIPESAN`, `BERJALAN`, `SELESAI`, dan `BATAL`. Penggunaan Enum membuat status lebih konsisten dibandingkan menggunakan teks biasa, serta mencegah penggunaan status yang tidak dikenal. Selain itu, metode `boleh_diubah()` digunakan untuk menentukan apakah data penyewaan masih boleh diubah berdasarkan statusnya.
