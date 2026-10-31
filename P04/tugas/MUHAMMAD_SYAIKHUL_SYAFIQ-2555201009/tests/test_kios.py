
"""Pengujian model Kios."""

import pytest
from src.model.kios import Kios


@pytest.fixture(autouse=True)
def reset_jumlah_produk() -> None:
    Kios._jumlah_produk = 0


def test_kios_menyimpan_data_produk() -> None:
    kios = Kios("P001", "Pupuk Kompos", 10_000, 12_000)
    assert kios.kode == "P001"
    assert kios.nama == "Pupuk Kompos"
    assert kios.harga_modal == 10_000
    assert kios.harga_jual == 12_000


def test_harga_jual_wajar() -> None:
    assert Kios.harga_jual_wajar(10_000, 11_000)


def test_harga_jual_di_bawah_laba_minimum_ditolak() -> None:
    assert not Kios.harga_jual_wajar(10_000, 10_500)


def test_harga_modal_di_bawah_minimum_ditolak() -> None:
    assert not Kios.harga_jual_wajar(500, 1_000)


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Pupuk Kompos", 10_000, 12_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("P001", "  ", 10_000, 12_000)


def test_harga_modal_terlalu_rendah_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("P001", "Bibit Cabai", 500, 1_000)


def test_harga_jual_tidak_cukup_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("P001", "Pupuk Kompos", 10_000, 10_500)


def test_dari_baris_valid() -> None:
    kios = Kios.dari_baris("P001;Pupuk Kompos;10000;12000")
    assert kios.nama == "Pupuk Kompos"
    assert kios.harga_jual == 12_000


def test_dari_baris_kolom_kurang_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("P001;Pupuk Kompos;10000")


def test_dari_baris_kolom_lebih_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("P001;Pupuk Kompos;10000;12000;catatan")


def test_dari_baris_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("P001;Pupuk Kompos;modal;12000")


def test_dari_baris_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("P001; ;10000;12000")


def test_format_rupiah() -> None:
    assert Kios.format_rupiah(12_000) == "Rp12.000"


def test_pencacah_produk_bertambah() -> None:
    sebelum = Kios.jumlah_produk()
    Kios("P001", "Pupuk Kompos", 10_000, 12_000)
    assert Kios.jumlah_produk() - sebelum == 1
