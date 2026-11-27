# pbo-sipala-CONTOH — Pertemuan 6

Kode acuan Pertemuan 6 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Hierarki AlatTani

```
                       AlatTani
        (kode, nama, tarif_harian, validasi,
         __str__  __repr__  __eq__  __hash__)
                          │
        ┌─────────────────┼─────────────────┐
     Traktor          PompaAir          Perontok
   +tenaga_kuda        +debit          +kapasitas
```

## Tiga pola penimpaan yang berbeda

| Turunan | Pola | Kode |
|---|---|---|
| `Traktor` | Menambah komponen | `dasar = super().biaya_sewa(hari)` lalu `+ ONGKOS * hari` |
| `PompaAir` | Menambah dari atribut sendiri | `+ konsumsi_solar_harian() * HARGA * hari` |
| `Perontok` | Mengubah masukan | `return super().biaya_sewa(self.hari_ditagih(hari))` |

Hasilnya:

```
[TR-01] Traktor Roda Dua Kubota — Rp150.000/hari · 8 HP · termasuk operator
    1 hari:   Rp250.000      3 hari:   Rp750.000
[PA-01] Pompa Air 3 Inci — Rp75.000/hari · 600 L/mnt · ±18 L solar/hari
    1 hari:   Rp201.000      3 hari:   Rp603.000
[PR-01] Mesin Perontok Padi — Rp200.000/hari · 900 kg/jam · minimum 2 hari
    1 hari:   Rp400.000      3 hari:   Rp600.000
                ↑ disewa 1 hari, ditagih 2
```

## Tiga gerbang

```
python periksa_pbo.py src --profil p06
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 18 source files
52 passed
```

## Dua kesalahan yang sengaja ditanam

**① `super().__init__()` yang terlupa** — `python lupa_super.py`:

```
Objek berhasil dibuat  : Traktor           ← tidak ada galat
Tenaga kuda terbaca    : 8                 ← atribut sendiri baik-baik saja
Isi objek              : ['_tenaga_kuda']  ← seharusnya EMPAT atribut

keterangan()    : RUNTUH -> 'Traktor' object has no attribute '_kode'
biaya_sewa(3)   : RUNTUH -> 'Traktor' object has no attribute '_tarif_harian'
```

Yang runtuh bukan baris yang salah, melainkan method warisan yang jauh dari sana.

**② `__eq__` tanpa `__hash__`** — `python eq_tanpa_hash.py`:

```
Perbandingan berhasil : True
Nilai __hash__ kelas  : None        ← sengaja dimatikan Python
Dimasukkan ke set     : GAGAL -> unhashable type: 'AlatTani'
Dijadikan kunci dict  : GAGAL -> unhashable type: 'AlatTani'
```

## Dua cara perkakas menangkap kesalahan

```
ruff check lupa_super.py     → ARG002 Unused method argument   (menunjuk GEJALA)
ruff check eq_tanpa_hash.py  → PLW1641 Object does not implement `__hash__`
                                                                (menunjuk PENYAKIT)
```

Ruff tidak memahami pewarisan. Pada kesalahan ① ia hanya melihat tiga parameter
yang tak terpakai — gejalanya, bukan penyakitnya. Perkakas sering menolong dengan
cara seperti itu: menunjuk arah yang benar tanpa tahu apa yang sesungguhnya salah.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
