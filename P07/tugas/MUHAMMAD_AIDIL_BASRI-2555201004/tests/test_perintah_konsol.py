
"""Pengujian interpreter perintah konsol."""

from src.model import DaftarHarga, Perontok, PompaAir, Traktor
from src.ui.perintah_konsol import BANTUAN, PerintahKonsol


def buat_konsol() -> PerintahKonsol:
    daftar = DaftarHarga([
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 600),
        Perontok("PR-01", "Perontok Padi", 200_000, 900),
    ])
    return PerintahKonsol(daftar)


def test_perintah_kosong() -> None:
    assert buat_konsol().jalankan("") == (
        "Perintah kosong. Ketik 'bantuan'."
    )


def test_perintah_bantuan() -> None:
    assert buat_konsol().jalankan("bantuan") == BANTUAN


def test_perintah_tanda_tanya() -> None:
    assert buat_konsol().jalankan("?") == BANTUAN


def test_perintah_daftar() -> None:
    hasil = buat_konsol().jalankan("daftar 3")
    assert "Traktor Kubota" in hasil
    assert "Rp750.000" in hasil


def test_perintah_harga() -> None:
    hasil = buat_konsol().jalankan("harga TR-01 3")
    assert hasil == "Traktor Kubota, 3 hari: Rp750.000"


def test_perintah_harga_kode_tidak_ditemukan() -> None:
    hasil = buat_konsol().jalankan("harga XX-99 1")
    assert hasil == "Alat berkode XX-99 tidak ada dalam daftar."


def test_perintah_termurah() -> None:
    hasil = buat_konsol().jalankan("termurah 3")
    assert hasil == "Termurah untuk 3 hari: Perontok Padi"


def test_perintah_tidak_dikenal() -> None:
    hasil = buat_konsol().jalankan("ngawur")
    assert hasil == "Perintah 'ngawur' tidak dikenal. Ketik 'bantuan'."


def test_format_perintah_tidak_valid() -> None:
    hasil = buat_konsol().jalankan("daftar satu dua")
    assert hasil == "Perintah 'daftar' tidak dikenal. Ketik 'bantuan'."

def test_perintah_total() -> None:
    hasil = buat_konsol().jalankan("total 3")
    assert hasil == "Total biaya untuk 3 hari: Rp1.953.000"


def test_perintah_total_hari_nol_ditolak() -> None:
    hasil = buat_konsol().jalankan("total 0")
    assert hasil == "Perintah 'total' tidak dikenal. Ketik 'bantuan'."

