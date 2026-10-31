
"""Pengujian untuk kelas Kios."""

import pytest

from src.model.kios import Kios


def test_membuat_produk_valid() -> None:
    produk = Kios("BR-01", "Beras", 10_000, 11_000)
    assert produk.kode == "BR-01"
    assert produk.nama == "Beras"


def test_harga_beli_dan_jual() -> None:
    produk = Kios("GL-01", "Gula", 15_000, 17_000)
    assert produk.harga_beli == 15_000
    assert produk.harga_jual == 17_000


def test_margin_minimum_diterima() -> None:
    assert Kios.harga_jual_wajar(10_000, 11_000) is True


def test_harga_jual_di_bawah_margin_ditolak() -> None:
    assert Kios.harga_jual_wajar(10_000, 10_999) is False


def test_harga_beli_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-02", "Beras", 0, 11_000)


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("   ", "Beras", 10_000, 11_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-03", "   ", 10_000, 11_000)


def test_harga_jual_tidak_wajar_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-04", "Beras", 10_000, 10_500)


def test_harga_jual_melebihi_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-05", "Beras", 10_000, 100_000_001)


def test_baris_csv_valid() -> None:
    produk = Kios.dari_baris_csv("BR-06;Beras;10000;11000")
    assert produk.kode == "BR-06"
    assert produk.harga_jual == 11_000


def test_baris_csv_bagian_tidak_lengkap_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR-07;Beras;10000")


def test_baris_csv_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR-08;Beras;sepuluh ribu;11000")


def test_pencacah_bertambah_sesuai_selisih() -> None:
    awal = Kios.jumlah_terdaftar()
    Kios("BR-09", "Beras", 10_000, 11_000)
    Kios("GL-02", "Gula", 15_000, 17_000)
    assert Kios.jumlah_terdaftar() == awal + 2


def test_format_keterangan() -> None:
    produk = Kios("MG-01", "Minyak Goreng", 15_000, 17_000)
    hasil = produk.keterangan()
    assert "MG-01" in hasil
    assert "Minyak Goreng" in hasil
    assert "Rp17.000" in hasil
