# pbo-sipala-CONTOH — Pertemuan 10

Kode acuan Pertemuan 10 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Hierarki SipalaError

```
SipalaError                                (Exception)
│
├─ DataTidakValid                          (juga ValueError)
│  ├─ TarifTidakValid          tarif di luar rentang wajar
│  ├─ NikTidakValid            NIK bukan 16 digit angka
│  ├─ HariTidakValid           jumlah hari tidak masuk akal
│  ├─ TeleponTidakValid        nomor telepon tidak sah
│  └─ BarisPendataanRusak      baris CSV tidak dapat dibaca
│
└─ AturanUsahaDilanggar                    (BUKAN ValueError)
   ├─ AlatSudahAdaDalamSewa    alat sama dua kali dalam satu transaksi
   ├─ BatasAlatTerlampaui      melebihi sepuluh alat per transaksi
   └─ TransaksiTerkunci        transaksi selesai atau batal diubah
```

| | `DataTidakValid` | `AturanUsahaDilanggar` |
|---|---|---|
| Sebab | Bentuk masukannya salah | Bentuknya benar, aturannya melarang |
| Jawaban ke pengurus | "Silakan ketik ulang" | "Tidak diizinkan, sebabnya …" |
| Juga `ValueError`? | Ya, disengaja | Tidak, dan itu memang benar |

Pewarisan ganda `DataTidakValid(SipalaError, ValueError)` disengaja: kita
mempersempit makna penolakan tanpa mematahkan kode lama yang menangkap
`ValueError`. Cabang aturan usaha sengaja **tidak** diberi perlakuan sama —
karena menangkap pelanggaran aturan sebagai `ValueError` memang keliru sejak awal.

## Tiga gerbang

```
python periksa_pbo.py src --profil p10
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 28 source files
66 passed
```

## Rantai penyebab

```
baca_rupiah("150.000")                  →  150000
baca_rupiah("Rp1.250.000")              →  1250000
baca_rupiah("seratus lima puluh ribu")  →  ditolak: tarif tidak dapat dibaca
                                            sebabnya: ValueError  (di __cause__)
```

## Context manager: transaksi tidak setengah jadi

```
Jumlah alat sebelum: 0
  tambah traktor  ✓
  tambah pompa    ✓
  tambah kembar   ✗ ditolak
Jumlah alat sesudah: 0 — kembali ke keadaan semula
```

Perhatikan kata `raise` sendirian di baris terakhir context manager. Tanpanya,
kita justru sedang **menelan eksepsi** — kesalahan yang ditanam nomor ①.

## Dua kesalahan yang sengaja ditanam

**① Menelan eksepsi** — `python menelan_galat.py`:

```
Baris yang dimasukkan pengurus : 10
Alat yang berhasil terdaftar   : 7

Program tidak melaporkan satu pun kegagalan.
```

Dua perkakas, dua tanggapan yang berbeda:

```
periksa_pbo.py  → PBO-031 eksepsi ditelan tanpa penanganan; tangani atau lempar ulang
ruff check      → SIM105 Use `contextlib.suppress(Exception)` instead of try-except-pass
```

Gerbang kita menyebutnya salah. Ruff menawarkan cara **menelannya yang lebih
ringkas** — karena Ruff adalah perkakas gaya dan menganggap Anda memang
bermaksud menelan. Peringatan perkakas selalu membawa asumsi tentang apa yang
Anda maksudkan.

**② Urutan cabang terbalik** — `python urutan_terbalik.py`:

```
Galat                cara buruk                       cara benar
TarifTidakValid      Terjadi kesalahan pada sistem.   Tarif tidak wajar…
TransaksiTerkunci    Terjadi kesalahan pada sistem.   Transaksi sudah ditutup…
```

Cabang khusus tidak pernah tercapai karena cabang umum menangkapnya lebih dulu.
Tidak ada perkakas yang memperingatkan — baik gerbang maupun Ruff.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
