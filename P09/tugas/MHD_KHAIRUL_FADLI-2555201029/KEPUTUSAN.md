# Keputusan Desain P09

## 1. Penggunaan Abstract Base Class (ABC)

`AlatTani` menggunakan `abc.ABC` sebagai kelas abstrak karena seluruh alat tani wajib memiliki kontrak perilaku yang sama.

Metode abstrak:
- `biaya_tambahan(jumlah_hari)`
- `syarat_pemakaian()`

Kelas turunan seperti `Traktor`, `PompaAir`, dan `Perontok` wajib mengimplementasikan kedua metode tersebut. Dengan demikian, objek `AlatTani` tidak dapat dibuat secara langsung.

## 2. Penggunaan Protocol

`Sewaan` menggunakan `typing.Protocol` untuk mendefinisikan kontrak struktural.

Objek yang memiliki atribut dan metode sesuai kontrak dapat digunakan sebagai `Sewaan`, tanpa harus mewarisi kelas tertentu.

`GerobakDorong` menjadi contoh penerapan karena memenuhi kontrak `Sewaan`, tetapi tidak mewarisi `AlatTani`.

`DaftarHarga` menerima kumpulan objek bertipe `Sewaan`, sehingga dapat menangani alat tani maupun objek lain yang memenuhi kontrak tersebut.

## 3. Perbedaan ABC dan Protocol

ABC menggunakan pewarisan nominal. Kelas harus menjadi turunan dari kelas abstrak untuk memenuhi hubungan pewarisan tersebut.

Protocol menggunakan kesesuaian struktural. Kelas tidak perlu mewarisi Protocol selama menyediakan atribut dan metode yang dipersyaratkan.

ABC digunakan untuk hierarki alat tani, sedangkan Protocol digunakan untuk menyatukan berbagai objek yang dapat disewakan.

## 4. Penggunaan Enum

`StatusSewa` menggunakan `enum.Enum` untuk membatasi status transaksi pada nilai yang telah ditentukan:
- DIPESAN
- BERJALAN
- SELESAI
- BATAL

Penggunaan Enum mencegah status berupa teks sembarang. Nilai yang tidak dikenal akan menghasilkan `ValueError`.

Perubahan status transaksi dilakukan melalui `ubah_status()`. Penambahan alat tidak diperbolehkan jika transaksi sudah selesai atau dibatalkan.

## 5. Keputusan Pengujian

Pengujian dilakukan untuk memastikan:
- Kelas abstrak tidak dapat dibuat secara langsung.
- Kelas konkret mengimplementasikan metode abstrak.
- GerobakDorong memenuhi Protocol Sewaan tanpa mewarisi AlatTani.
- Perhitungan biaya sewa tetap sesuai ketentuan.
- Status transaksi hanya menerima anggota Enum yang valid.
- Transaksi yang sudah selesai atau dibatalkan tidak dapat ditambah alat.

