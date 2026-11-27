# PBO-UP-2026 — Kelas A

Praktikum Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai — 2026/2027

## Jadwal dan tenggat

Setiap tugas berjalan **1 minggu** sejak LKM dibagikan.

| Tugas | Mulai | Tenggat (Pull Request sudah dibuat) |
|---|---|---|
| P01 — Lingkungan kerja dan tiga gerbang | Kamis, 24 September 2026 | Rabu, 30 September 2026, pukul 23.59 WIB (sudah lewat) |
| P02 — Kelas `Penyewa` dan `AlatTani` | Kamis, 1 Oktober 2026 | Rabu, 7 Oktober 2026, pukul 23.59 WIB (sudah lewat) |
| P03 — Enkapsulasi: property, setter, objek nilai `Alamat` | Kamis, 15 Oktober 2026 | Rabu, 21 Oktober 2026, pukul 23.59 WIB (sudah lewat) |
| P04 — Milik kelas dan milik objek: konstanta, `classmethod`, `staticmethod` | Kamis, 22 Oktober 2026 | Rabu, 28 Oktober 2026, pukul 23.59 WIB (sudah lewat) |
| P05 — Relasi antar kelas: asosiasi, agregasi, komposisi, diagram kelas | Kamis, 29 Oktober 2026 | Rabu, 4 November 2026, pukul 23.59 WIB (sudah lewat) |
| P06 — Pewarisan: hierarki `AlatTani`, `super()`, `__str__`/`__repr__`/`__eq__`/`__hash__` | Kamis, 5 November 2026 | Rabu, 11 November 2026, pukul 23.59 WIB (sudah lewat) |
| P07 — Polimorfisme: pewarisan, duck typing, `match`, `singledispatch` | Kamis, 12 November 2026 | Rabu, 18 November 2026, pukul 23.59 WIB (sudah lewat) |
| P09 — Abstraksi: `abc.ABC`, `typing.Protocol`, `Enum` | Kamis, 19 November 2026 | Rabu, 25 November 2026, pukul 23.59 WIB (sudah lewat) |
| P10 — Eksepsi: hierarki galat sendiri, `raise ... from`, context manager | Kamis, 26 November 2026 | **Rabu, 2 Desember 2026, pukul 23.59 WIB** |

**P04 berisi Tugas 1 (individu)** yang dinilai terpisah pada nilai akhir — kerjakan sendiri; kemiripan kode
ditelusuri lewat riwayat commit. Rinciannya di `P04/materi/Panduan-Praktikum-P04.pdf` bagian 7: kelas `Kios`
untuk UMKM di Bangkinang (minimal tiga konstanta `Final` termasuk satu persentase, pencacah milik kelas,
konstruktor alternatif dari baris teks, satu `staticmethod`, keluaran f-string yang rata, minimal sepuluh uji
dengan lima penolakan dan uji pencacah berpola selisih). Gerbang memakai profil `p04`; tanda versi `p04-tugas1`.

**P05** dikerjakan per orang di `P05/tugas/NAMA_LENGKAP-NIM/`, rinciannya di `P05/materi/Panduan-Praktikum-P05.pdf`:
kelas `Sewa` dan `BarisSewa` (komposisi, `BarisSewa` menyimpan salinan kode, nama, dan tarif alat), property `baris`
yang mengembalikan tuple, diagram `diagram/kelas-p05.png` yang sesuai dengan kode, minimal 34 fungsi uji termasuk uji
asosiasi dan uji komposisi. Gerbang memakai profil `p05`; tanda versi `p05`. Hapus `tanpa_salinan.py` dan
`komposisi_bocor.py` sebelum commit.

**Proyek kelompok dimulai di P05** (Panduan P05 bagian 7): kelompok tiga sampai empat orang, mitra nyata di Kampar atau
sekitarnya, bukan kasus UPJA atau penyewaan alat pertanian, dan kasus wajib disetujui dosen. Milestone 1 dikumpulkan di
repositori kelompok dengan tanda versi `m1`, tenggatnya pada Pertemuan 6.

**P06** dikerjakan per orang di `P06/tugas/NAMA_LENGKAP-NIM/`, rinciannya di `P06/materi/Panduan-Praktikum-P06.pdf`:
hierarki `AlatTani` dengan turunan `Traktor`, `PompaAir`, dan `Perontok` (setiap turunan memanggil `super().__init__()`
dan memakai pola penimpaan yang berbeda), induk menulis `__str__`, `__repr__`, `__eq__`, dan `__hash__`, ada uji bahwa
objek dapat masuk set dan menjadi kunci dict, minimal 52 fungsi uji. Gerbang memakai profil `p06`; tanda versi `p06`.
Hapus `lupa_super.py` dan `eq_tanpa_hash.py` sebelum commit.

**P06 berisi Tugas 2 (individu)** yang dinilai terpisah (Panduan P06 bagian 8): hierarki `Pegawai` untuk instansi di
Kampar, satu induk dan tiga turunan dengan pola penimpaan berbeda, induk menulis keempat method khusus dengan
perbandingan berdasar atribut identitas, minimal dua belas uji dengan empat penolakan dan satu uji kunci dict. Tambahkan
juga `dari_baris_csv` pada `PompaAir` dan `Perontok`. Tanda versi `p06-tugas2`; tenggat sama dengan P06.

**P07** dikerjakan per orang di `P07/tugas/NAMA_LENGKAP-NIM/`, rinciannya di `P07/materi/Panduan-Praktikum-P07.pdf`:
kelas `DaftarHarga` yang memproses berbagai `AlatTani` tanpa satu pun `isinstance`, `type()`, atau nama kelas turunan,
penerjemah perintah konsol dengan `match` (minimal satu penjaga `if` dan satu `*_`), `format_nilai.py` dengan
`singledispatch` untuk minimal tiga tipe bawaan, uji yang membuat jenis alat baru di dalam badan ujinya sendiri, minimal
73 fungsi uji. Gerbang memakai profil `p07`; tanda versi `p07`. Hapus `rantai_if.py` dan `bebek_rapuh.py` sebelum commit.

**P07 berisi Tugas 3 (individu)** yang dinilai terpisah (Panduan P07 bagian 7): kelas `PenyusunLaporan` untuk hierarki
`Pegawai` dari Tugas 2 (rekap penghasilan, tertinggi, terendah, total; tanpa `isinstance`/`type()`/`match` atas nama
kelasmu), satu uji yang membuat jenis pegawai keempat di dalam badan ujinya sendiri, penerjemah perintah konsol minimal
lima cabang, satu fungsi `singledispatch` untuk tiga tipe bawaan, minimal lima belas uji dengan lima penolakan. Tanda
versi `p07-tugas3`; tenggat sama dengan P07.

**P09** dikerjakan per orang di `P09/tugas/NAMA_LENGKAP-NIM/`, rinciannya di `P09/materi/Panduan-Praktikum-P09.pdf`:
`AlatTani` menjadi kelas abstrak (`abc.ABC`, minimal dua `@abstractmethod`) dan rumus biaya sewa hanya ada di induk
tanpa ditimpa turunan (keenam angka acuan sebelum dan sesudah penataan ulang harus sama), kontrak `Sewaan` berupa
`Protocol` yang dipakai sebagai tipe pada `DaftarHarga` dengan satu kelas bukan turunan yang ikut masuk, dan
`StatusSewa` berupa `Enum` (transaksi selesai menolak penambahan alat). Gerbang memakai profil `p09`; tanda versi `p09`.
Hapus `lupa_abstrak.py` dan `kontrak_kebetulan.py` sebelum commit.

**Penugasan terstruktur P09** (Panduan P09 bagian 7) dikerjakan pada **proyek kelompok** sebagai persiapan Milestone 2
(dikumpulkan pada Pertemuan 11): satu kelas abstrak dengan `@abstractmethod` yang berbeda isinya di tiap turunan, satu
`Protocol` yang dipakai sebagai tipe beserta satu kelas bukan turunan yang memenuhinya, satu atribut teks terbatas yang
diganti `Enum` beserta method-nya, minimal enam uji baru, dan berkas `KEPUTUSAN.md` (alasan ABC atau Protocol). Tanda
versi `p09-tugas`; tenggat sama dengan P09.

**P10** dikerjakan per orang di `P10/tugas/NAMA_LENGKAP-NIM/`, rinciannya di `P10/materi/Panduan-Praktikum-P10.pdf`:
hierarki `SipalaError` (satu induk, dua cabang, sembilan turunan; `DataTidakValid` juga mewarisi `ValueError`,
`AturanUsahaDilanggar` tidak), tidak ada lagi `raise ValueError` di `src/model`, `baca_rupiah` memakai `raise ... from`
dengan `__cause__` teruji, context manager transaksi yang mengembalikan keadaan semula lalu melempar ulang galatnya, dan
uji yang memisahkan kedua cabang saat ditangkap. Gerbang memakai profil `p10`; tanda versi `p10`. Hapus
`menelan_galat.py` dan `urutan_terbalik.py` sebelum commit.

**P10 berisi Tugas 4 (individu)** yang dinilai terpisah (Panduan P10 bagian 7): perkuat kelas `Kios` dari Tugas 1 dengan
hierarki galat dua cabang (minimal satu induk dan lima turunan; cabang data juga mewarisi `ValueError`), minimal satu
`raise ... from`, satu context manager yang mencegah pekerjaan setengah jadi, satu fungsi penerjemah galat menjadi kalimat
untuk pemilik kios (cabang dari khusus ke umum), minimal dua belas uji (enam jenis galat, satu `__cause__`, satu
pembatalan menyeluruh). Tanda versi `p10-tugas4`; tenggat sama dengan P10.

Keterlambatan dihitung dari **waktu Pull Request dibuat** (dicatat GitHub) dan dikurangi
**5 poin per hari**. Commit di fork saja belum dihitung mengumpulkan — buat PR-nya sebelum tenggat.

## Struktur repo

```text
P01/
├── materi/                     dari dosen — JANGAN diubah
│   ├── Panduan-Praktikum-P01.pdf  langkah praktikum dan TUGAS (lihat bagian 6)
│   ├── LKM-P01.pdf             Lembar Kerja Mahasiswa (dicetak/diisi saat praktikum)
│   ├── README.md               langkah praktikum dan tiga gerbang
│   ├── periksa_pbo.py
│   ├── pyproject.toml
│   ├── AI_USAGE.md             contoh pengisian
│   └── salah_prosedural.py
└── tugas/
    └── NAMA_LENGKAP-NIM/       satu folder per mahasiswa
        ├── src/
        ├── tests/
        ├── periksa_pbo.py      salinan dari materi, tidak diubah
        ├── pyproject.toml      salinan dari materi, tidak diubah
        ├── REFLEKSI.md
        ├── LKM-P01.pdf         LKM yang sudah diisi (diunggah dosen)
        └── AI_USAGE.md         WAJIB, termasuk bila tidak memakai AI
P02/
└── ...
P03/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, konstruktor_bocor.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, REFLEKSI.md
P04/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, default_berbagi.py, pencacah_bocor.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, REFLEKSI.md, LKM-P04.pdf
P05/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, tanpa_salinan.py, komposisi_bocor.py, diagram/
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, diagram/kelas-p05.png, periksa_pbo.py, pyproject.toml, AI_USAGE.md, LKM-P05.pdf
P06/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, lupa_super.py, eq_tanpa_hash.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, LKM-P06.pdf (Tugas 2 Pegawai ikut di sini)
P07/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, rantai_if.py, bebek_rapuh.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, LKM-P07.pdf (Tugas 3 ikut di sini)
P09/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, lupa_abstrak.py, kontrak_kebetulan.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, LKM-P09.pdf
P10/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, menelan_galat.py, urutan_terbalik.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, LKM-P10.pdf (Tugas 4 Kios ikut di sini)
```

## Cara mengumpulkan tugas

1. **Fork** repo ini (sekali saja). Sebelum mulai pertemuan baru, klik **Sync fork**
   di halaman fork-mu agar materi terbaru ikut masuk.
2. Buat foldermu di `P0x/tugas/NAMA_LENGKAP-NIM/`.
   - Huruf kapital, kata dipisah garis bawah, tanpa titik.
   - Contoh benar: `P02/tugas/BUDI_SANTOSO-2555201000/`
   - Contoh salah: `budi santoso`, `BUDISANTOSO-2555201000`, `MHD._BUDI-2555201000`
3. Salin `periksa_pbo.py` dan `pyproject.toml` dari `P0x/materi/` ke foldermu **tanpa diubah**.
4. Kerjakan, lalu jalankan tiga gerbang dari dalam foldermu sampai semuanya lolos
   (perintahnya ada di `P0x/materi/README.md`).
5. Isi `REFLEKSI.md` dan `AI_USAGE.md`. Memakai AI tidak otomatis mengurangi nilai;
   **tidak jujur** tentang pemakaiannya yang mengurangi nilai.
6. Commit, push ke fork-mu, lalu buat **Pull Request** ke repo ini dengan judul
   `P0x - NAMA LENGKAP (NIM)`.

### Aturan Pull Request

- Satu PR = satu pertemuan = satu folder milikmu sendiri.
- Jangan mengubah berkas di luar foldermu (materi, folder teman, README ini).
- Setelah PR dibuat, pemeriksaan otomatis berjalan. Lihat hasilnya di bagian bawah PR:
  ✅ berarti lolos, ❌ berarti ada yang harus diperbaiki. Perbaiki di fork-mu lalu push lagi;
  PR yang sama otomatis diperbarui, tidak perlu membuat PR baru.
- PR **tidak di-merge** lewat tombol. Dosen memasukkan tugasmu ke repo ini lalu menutup PR
  dengan komentar "diterima". PR yang ditutup dengan komentar itu artinya tugasmu sudah masuk
  dan dinilai.
