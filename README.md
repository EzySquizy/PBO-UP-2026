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
| P05 — Relasi antar kelas: asosiasi, agregasi, komposisi, diagram kelas | Kamis, 29 Oktober 2026 | **Rabu, 4 November 2026, pukul 23.59 WIB** |

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
