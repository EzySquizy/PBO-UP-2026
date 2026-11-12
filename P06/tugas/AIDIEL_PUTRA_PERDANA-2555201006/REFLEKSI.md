# Refleksi Pertemuan 6

* **Fungsi `super()`:** Wajib dipanggil pertama kali pada konstruktor turunan. Saat menimpa method, tetap manfaatkan `super()` (menambah hasil atau mengubah parameternya) agar tidak mengulang kode induk.
* **Tampilan Objek:** `__str__` digunakan untuk tampilan rapi bagi pengguna, sedangkan `__repr__` untuk kebutuhan debugging pemrogram.
* **Aturan `__eq__` & `__hash__`:** Harus selalu berpasangan. Jika `__eq__` diubah (misal berdasarkan kesamaan kode/NIP), `__hash__` wajib dibuat ulang agar objek bisa masuk ke `set` atau `dict`.
* **Pewarisan vs Komposisi:** Jangan memaksakan pewarisan. Gunakan hanya jika relasinya "adalah sejenis", bukan "punya".