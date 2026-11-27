
"""Pengujian untuk penerjemah perintah konsol."""

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.ui.perintah_konsol import PerintahKonsol


def contoh_konsol() -> PerintahKonsol:
    daftar = DaftarHarga([
        AlatTani("TR-01", "Traktor", 150_000),
        AlatTani("PA-01", "Pompa Air", 75_000),
    ])
    return PerintahKonsol(daftar)


def test_perintah_bantuan() -> None:
    hasil = contoh_konsol().jalankan("bantuan")
    assert "Daftar perintah" in hasil


def test_perintah_tanda_tanya() -> None:
    hasil = contoh_konsol().jalankan("?")
    assert "Daftar perintah" in hasil


def test_perintah_daftar_dengan_hari_valid() -> None:
    hasil = contoh_konsol().jalankan("daftar 2")
    assert "Traktor" in hasil
    assert "Pompa Air" in hasil


def test_perintah_harga_dengan_kode_valid() -> None:
    hasil = contoh_konsol().jalankan("harga TR-01 2")
    assert "Traktor" in hasil
    assert "2 hari" in hasil


def test_perintah_harga_kode_tidak_ditemukan() -> None:
    hasil = contoh_konsol().jalankan("harga XX-99 2")
    assert "tidak ada dalam daftar" in hasil


def test_perintah_termurah() -> None:
    hasil = contoh_konsol().jalankan("termurah 2")
    assert "Pompa Air" in hasil


def test_perintah_kosong() -> None:
    hasil = contoh_konsol().jalankan("")
    assert "Perintah kosong" in hasil


def test_perintah_tidak_dikenal_satu_kata() -> None:
    hasil = contoh_konsol().jalankan("cetak")
    assert "tidak dikenal" in hasil


def test_perintah_tidak_dikenal_dengan_argumen() -> None:
    hasil = contoh_konsol().jalankan("hapus TR-01")
    assert "tidak dikenal" in hasil


def test_perintah_daftar_menolak_hari_huruf() -> None:
    hasil = contoh_konsol().jalankan("daftar besok")
    assert "tidak dikenal" in hasil


def test_perintah_harga_menolak_hari_huruf() -> None:
    hasil = contoh_konsol().jalankan("harga TR-01 besok")
    assert "tidak dikenal" in hasil


def test_perintah_termurah_menolak_hari_huruf() -> None:
    hasil = contoh_konsol().jalankan("termurah besok")
    assert "tidak dikenal" in hasil


def test_perintah_daftar_menolak_argumen_berlebih() -> None:
    hasil = contoh_konsol().jalankan("daftar 2 tambahan")
    assert "tidak dikenal" in hasil
