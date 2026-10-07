# Mengapa PBO diperlukan pada Pencatatan Absensi Siswa

## Gambaran Kasus

Absensi merupakan kegiatan yang dilakukan untuk mengetahui kehadiran siswa dalam proses belajar. Setiap hari guru perlu mencatat siapa saja yang hadir, izin, sakit, atau tidak masuk.

Kalau jumlah siswa cukup banyak dan pencatatan dilakukan terus-menerus, data absensi akan semakin banyak. Guru juga akan membutuhkan cara yang lebih mudah untuk melihat kehadiran siswa pada tanggal tertentu.

## Permasalahan

Salah satu kesulitan dalam pencatatan absensi adalah mengelola data yang terus bertambah. Kesalahan memasukkan status kehadiran juga bisa terjadi, misalnya siswa yang sebenarnya hadir justru tercatat tidak hadir.

Selain itu, ketika ingin melihat riwayat kehadiran seorang siswa, pencarian data secara manual dapat membutuhkan waktu karena harus memeriksa catatan sebelumnya.

## Penerapan PBO

Menurut saya, PBO dapat digunakan untuk membuat sistem absensi dengan membagi data berdasarkan objeknya. Misalnya terdapat objek Siswa yang menyimpan nama, NIM, dan kelas. Kemudian terdapat objek Absensi yang menyimpan tanggal dan status kehadiran.

Objek Absensi juga dapat memiliki method untuk mencatat kehadiran siswa. Dengan begitu, proses pencatatan tidak hanya menyimpan data, tetapi juga mempunyai fungsi yang mengatur bagaimana data tersebut digunakan.

Penggunaan objek membuat data setiap siswa dapat dikelola secara terpisah. Jika nantinya sistem membutuhkan fitur seperti melihat riwayat absensi atau menghitung jumlah kehadiran, fitur tersebut juga dapat ditambahkan ke dalam program.

## Kesimpulan

Menurut saya, PBO dapat membantu membuat pencatatan absensi menjadi lebih teratur karena data siswa dan data kehadirannya dapat dikelola menggunakan objek yang berbeda. Cara ini juga membuat program lebih mudah dikembangkan apabila jumlah siswa dan data absensi semakin banyak.