
"""Pengujian untuk kelas Kios."""

import pytest

from src.model.kios import Kios


def test_produk_valid() -> None:
    produk = Kios("BR-01", "Beras", 10000, 11000, 5)
    assert produk.ringkasan() == "Beras: harga jual Rp11.000, stok 5"


def test_margin_minimum_diterima() -> None:
    assert Kios.harga_wajar(10000, 11000)


def test_margin_kurang_ditolak() -> None:
    assert not Kios.harga_wajar(10000, 10999)


def test_harga_modal_nol_ditolak() -> None:
    assert not Kios.harga_wajar(0, 1000)


def test_harga_jual_nol_ditolak() -> None:
    assert not Kios.harga_wajar(1000, 0)


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios(" ", "Beras", 10000, 11000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", " ", 10000, 11000)


def test_harga_modal_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", "Beras", 0, 11000)


def test_stok_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", "Beras", 10000, 11000, -1)


def test_baris_pendataan_valid() -> None:
    produk = Kios.dari_baris("BR-02;Beras;10000;11000;8")
    assert produk.ringkasan() == "Beras: harga jual Rp11.000, stok 8"


def test_baris_pendataan_tidak_lengkap_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR-03;Gula;15000")


def test_baris_pendataan_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR-04;Gula;modal;17000;5")


def test_pencacah_bertambah_satu() -> None:
    sebelum = Kios.jumlah_terdaftar()
    Kios("BR-05", "Minyak Goreng", 15000, 16500, 4)
    sesudah = Kios.jumlah_terdaftar()

    assert sesudah - sebelum == 1


def test_format_daftar() -> None:
    produk = Kios("BR-06", "Beras", 10000, 11000, 5)
    hasil = produk.format_daftar()

    assert "BR-06" in hasil
    assert "Beras" in hasil
    assert "Rp" in hasil
    assert "Stok" in hasil
