# REFLEKSI PRAKTIKUM P06

**Nama:** MHD KHAIRUL FADLI  
**NIM:** 2555201029  
**Praktikum:** P06 – Pewarisan (Inheritance)

## 1. Hal yang Dipelajari

Pada praktikum P06, saya mempelajari konsep pewarisan (*inheritance*) dalam Pemrograman Berorientasi Objek menggunakan Python. Pewarisan memungkinkan sebuah kelas turunan menggunakan atribut dan metode dari kelas induk sehingga kode menjadi lebih terstruktur dan dapat digunakan kembali.

Saya membuat tiga kelas turunan dari kelas `AlatTani`, yaitu `Traktor`, `PompaAir`, dan `Perontok`. Setiap kelas memiliki karakteristik dan perhitungan biaya sewa masing-masing.

## 2. Kesulitan yang Dihadapi

Kesulitan yang saya hadapi adalah memahami penggunaan `super()` untuk memanggil konstruktor kelas induk serta melakukan *method overriding* pada metode `biaya_sewa()`.

Saya juga perlu memastikan setiap kelas turunan memiliki perhitungan biaya yang sesuai dengan ketentuan praktikum, terutama biaya operator pada Traktor, biaya solar pada PompaAir, dan ketentuan minimum dua hari sewa pada Perontok.

## 3. Cara Mengatasi Kesulitan

Saya mengatasi kesulitan tersebut dengan mempelajari kembali struktur kelas induk dan kelas turunan, memperhatikan penggunaan `super().__init__()`, serta membuat pengujian untuk setiap perilaku kelas.

Saya juga menjalankan pytest, Ruff, MyPy, dan pemeriksa disiplin PBO untuk memastikan program berjalan dengan baik dan memenuhi ketentuan praktikum.

## 4. Hasil yang Diperoleh

Dari praktikum ini, saya berhasil membuat tiga kelas turunan dengan perilaku yang berbeda:

- **Traktor:** memiliki tambahan biaya operator harian.
- **PompaAir:** memiliki tambahan biaya solar berdasarkan debit.
- **Perontok:** menerapkan biaya minimum dua hari meskipun hanya disewa satu hari.

Saya juga berhasil menerapkan metode `__str__()`, `__repr__()`, `__eq__()`, dan `__hash__()` pada kelas `AlatTani`.

Hasil pengujian menunjukkan 80 pengujian berhasil, pemeriksaan Ruff dan MyPy lolos, serta pemeriksa profil P06 menyatakan tidak ada pelanggaran disiplin berorientasi objek.

## 5. Kesimpulan

Praktikum P06 membantu saya memahami penerapan konsep pewarisan dan *method overriding* dalam Python. Saya memahami bahwa kelas turunan dapat menggunakan fitur kelas induk sekaligus menambahkan perilaku khusus sesuai kebutuhannya.

Melalui praktikum ini, saya menjadi lebih memahami cara membuat program yang terstruktur, mengurangi pengulangan kode, dan lebih mudah dikembangkan.