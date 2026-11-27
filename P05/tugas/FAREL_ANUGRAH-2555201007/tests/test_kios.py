"""Pengujian kelas Kios."""

import pytest
from src.model.kios import Kios


def test_membuat_produk_valid() -> None:
    produk = Kios("BR001", "Beras", 10_000, 12_000, 20)

    assert produk.kode == "BR001"
    assert produk.nama == "Beras"
    assert produk.harga_modal == 10_000
    assert produk.harga_jual == 12_000
    assert produk.stok == 20


def test_menolak_kode_kosong() -> None:
    with pytest.raises(ValueError, match="kode produk"):
        Kios("", "Beras", 10_000, 12_000, 20)


def test_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError, match="nama produk"):
        Kios("BR001", " ", 10_000, 12_000, 20)


def test_menolak_harga_modal_tidak_wajar() -> None:
    with pytest.raises(ValueError, match="harga modal"):
        Kios("BR001", "Beras", 500, 1_000, 20)


def test_menolak_harga_jual_di_bawah_margin() -> None:
    with pytest.raises(ValueError, match="margin"):
        Kios("BR001", "Beras", 10_000, 11_000, 20)


def test_menolak_stok_negatif() -> None:
    with pytest.raises(ValueError, match="stok"):
        Kios("BR001", "Beras", 10_000, 12_000, -1)


def test_harga_jual_wajar() -> None:
    assert Kios.harga_jual_wajar(10_000, 11_500)


def test_harga_jual_tidak_wajar() -> None:
    assert not Kios.harga_jual_wajar(10_000, 11_000)


def test_constructor_dari_baris() -> None:
    produk = Kios.dari_baris("G001;Gula Pasir;15_000;18_000;30")

    assert produk.kode == "G001"
    assert produk.nama == "Gula Pasir"
    assert produk.harga_modal == 15_000
    assert produk.harga_jual == 18_000
    assert produk.stok == 30


def test_menolak_format_baris_tidak_valid() -> None:
    with pytest.raises(ValueError, match="5 bagian"):
        Kios.dari_baris("G001;Gula Pasir;15000")


def test_menolak_data_angka_tidak_valid() -> None:
    with pytest.raises(ValueError, match="angka bulat"):
        Kios.dari_baris("G001;Gula Pasir;abc;18000;30")


def test_menambah_stok() -> None:
    produk = Kios("BR002", "Beras Premium", 20_000, 24_000, 10)

    produk.tambah_stok(5)

    assert produk.stok == 15


def test_menolak_penambahan_stok_nol() -> None:
    produk = Kios("BR003", "Beras Medium", 10_000, 12_000, 10)

    with pytest.raises(ValueError, match="positif"):
        produk.tambah_stok(0)


def test_mengurangi_stok() -> None:
    produk = Kios("MG001", "Minyak Goreng", 15_000, 18_000, 20)

    produk.kurangi_stok(5)

    assert produk.stok == 15


def test_menolak_pengurangan_stok_melebihi_persediaan() -> None:
    produk = Kios("MG002", "Minyak Goreng", 15_000, 18_000, 5)

    with pytest.raises(ValueError, match="tidak mencukupi"):
        produk.kurangi_stok(10)


def test_penghitung_produk_bertambah() -> None:
    sebelum = Kios.jumlah_produk()

    Kios("BR004", "Beras Lokal", 10_000, 12_000, 10)

    assert Kios.jumlah_produk() == sebelum + 1


def test_format_inventaris() -> None:
    produk = Kios("BR005", "Beras", 10_000, 12_000, 20)

    hasil = produk.format_inventaris()

    assert "BR005" in hasil
    assert "Beras" in hasil
    assert "20" in hasil
    assert "12,000" in hasil


def test_keterangan_produk() -> None:
    produk = Kios("MG003", "Minyak Goreng", 15_000, 18_000, 10)

    assert "Minyak Goreng" in produk.keterangan()
    assert "18,000" in produk.keterangan()
