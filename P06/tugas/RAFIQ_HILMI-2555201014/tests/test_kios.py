"""Pengujian untuk model Kios."""

import pytest
from src.model.kios import Kios


def test_data_produk_valid() -> None:
    produk = Kios("P01", "Beras", 10, 10000, 11000)
    assert produk.kode == "P01"
    assert produk.nama == "Beras"
    assert produk.stok == 10


def test_keuntungan_per_produk() -> None:
    produk = Kios("P02", "Gula", 10, 12000, 13200)
    assert produk.keuntungan_per_produk() == 1200


def test_tambah_stok() -> None:
    produk = Kios("P03", "Minyak", 5, 10000, 11000)
    produk.tambah_stok(3)
    assert produk.stok == 8


def test_kurangi_stok() -> None:
    produk = Kios("P04", "Beras", 10, 10000, 11000)
    produk.kurangi_stok(4)
    assert produk.stok == 6


def test_buat_dari_baris() -> None:
    produk = Kios.dari_baris("P05;Gula;10;10000;11000")
    assert produk.nama == "Gula"
    assert produk.harga_jual == 11000


def test_harga_jual_wajar() -> None:
    assert Kios.harga_jual_wajar(10000, 11000)


def test_harga_jual_tidak_wajar() -> None:
    assert not Kios.harga_jual_wajar(10000, 10500)


def test_jumlah_produk_terdaftar_bertambah() -> None:
    awal = Kios.jumlah_terdaftar()
    Kios("P06", "Pupuk", 5, 10000, 11000)
    assert Kios.jumlah_terdaftar() == awal + 1


def test_format_daftar() -> None:
    produk = Kios("P07", "Beras", 10, 10000, 11000)
    hasil = produk.format_daftar()
    assert "Beras" in hasil
    assert "P07" in hasil
    assert "Rp" in hasil


def test_tolak_kode_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 10, 10000, 11000)


def test_tolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("P08", "   ", 10, 10000, 11000)


def test_tolak_stok_negatif() -> None:
    with pytest.raises(ValueError):
        Kios("P09", "Beras", -1, 10000, 11000)


def test_tolak_harga_modal_nol() -> None:
    with pytest.raises(ValueError):
        Kios("P10", "Beras", 10, 0, 11000)


def test_tolak_harga_jual_di_bawah_margin() -> None:
    with pytest.raises(ValueError):
        Kios("P11", "Beras", 10, 10000, 10500)


def test_tolak_baris_tidak_lengkap() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("P12;Beras;10;10000")


def test_tolak_baris_dengan_angka_tidak_valid() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("P13;Beras;abc;10000;11000")


def test_tolak_penambahan_stok_nol() -> None:
    produk = Kios("P14", "Beras", 10, 10000, 11000)
    with pytest.raises(ValueError):
        produk.tambah_stok(0)


def test_tolak_pengurangan_stok_melebihi_stok() -> None:
    produk = Kios("P15", "Beras", 5, 10000, 11000)
    with pytest.raises(ValueError):
        produk.kurangi_stok(6)
