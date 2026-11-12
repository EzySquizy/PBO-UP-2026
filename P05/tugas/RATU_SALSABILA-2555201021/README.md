# pbo-sipala-CONTOH — Pertemuan 5

Kode acuan Pertemuan 5 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Tiga relasi yang diterapkan

| Relasi | Antara | Wujud dalam kode |
|---|---|---|
| Asosiasi | `Sewa` — `Penyewa` | Objek diterima dari luar lewat konstruktor |
| Agregasi | `BarisSewa` — `AlatTani` | Rujukan disimpan; objeknya dibuat pihak lain |
| Komposisi | `Sewa` — `BarisSewa` | Dibuat di dalam `tambah_alat()`; property mengembalikan `tuple` |

## Salinan data historis

`BarisSewa` menyimpan **rujukan** ke alatnya *dan* **salinan** kode, nama, serta
tarif pada saat penyewaan terjadi. Rujukan untuk penelusuran; salinan untuk
arsip. Keduanya, bukan salah satu.

```
Tarif traktor sekarang : Rp175.000
Tarif pada nota lama   : Rp150.000
Total nota lama        : Rp825.000     ← tidak ikut berubah
```

## Tiga gerbang

```
python periksa_pbo.py src --profil p05
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 14 source files
34 passed

NOTA SEWA SW-2026-001
Budi Santoso (1406012509900001) — Kuok, Kuok
--------------------------------------------------------------------
Traktor Roda Dua Kubota        3 hr ×    Rp150.000 =      Rp450.000
Pompa Air 3 Inci               5 hr ×     Rp75.000 =      Rp375.000
--------------------------------------------------------------------
TOTAL                                                      Rp825.000
```

## Dua kesalahan yang sengaja ditanam

**① Nota yang berubah sendiri** — `python tanpa_salinan.py`:

```
Nota Maret, saat dicetak : Traktor Roda Dua 3 hr x Rp150.000 = Rp450.000
Nota Maret, dibuka lagi  : Traktor Roda Dua 3 hr x Rp175.000 = Rp525.000
```

Petani membayar Rp450.000 pada bulan Maret dan menyimpan notanya. Enam bulan
kemudian arsip UPJA mencatat Rp525.000. Tidak ada galat, tidak ada gerbang yang
menolak, Ruff pun lolos. Hanya sebuah rujukan yang seharusnya berupa salinan.

**② Komposisi yang bocor** — `python komposisi_bocor.py`:

```
Jumlah alat awal   : 2
Setelah disusupi   : 4 ['TR-01', 'PA-01', 'PR-99', 'PR-99']
Setelah dikosongkan: 0
```

Batas sepuluh alat, larangan alat ganda, dan pemeriksaan jumlah hari — ketiganya
hanya berlaku bagi yang lewat pintu depan. Perbaikan satu baris:
`return tuple(self._baris)`.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
