
"""Pengujian untuk kelas Kios."""

import pytest
from src.model.kios import Kios


def test_membuat_produk_kios() -> None:
    produk = Kios("PR-01", "Beras Lokal", 15000, 18000, 50)

    assert produk.kode == "PR-01"
    assert produk.nama == "Beras Lokal"
    assert produk.harga_modal == 15000
    assert produk.harga_jual == 18000
    assert produk.stok == 50


def test_keterangan_produk() -> None:
    produk = Kios("PR-01", "Beras Lokal", 15000, 18000, 50)

    hasil = produk.keterangan()

    assert "PR-01" in hasil
    assert "Beras Lokal" in hasil
    assert "Rp18.000" in hasil


def test_harga_jual_wajar() -> None:
    assert Kios.harga_jual_wajar(15000, 16500) is True


def test_harga_jual_di_bawah_keuntungan_minimum() -> None:
    assert Kios.harga_jual_wajar(15000, 16000) is False


def test_jumlah_produk_bertambah_satu() -> None:
    sebelum = Kios.jumlah_produk()
    Kios("PR-02", "Jagung", 10000, 12000, 20)

    assert Kios.jumlah_produk() == sebelum + 1


def test_membuat_produk_dari_baris_teks() -> None:
    produk = Kios.dari_baris_teks(
        "PR-03;Cabai Merah;20000;25000;30"
    )

    assert produk.kode == "PR-03"
    assert produk.nama == "Cabai Merah"
    assert produk.harga_modal == 20000
    assert produk.harga_jual == 25000
    assert produk.stok == 30


# Pengujian penolakan


def test_kode_produk_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 15000, 18000, 50)


def test_nama_produk_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("PR-01", "", 15000, 18000, 50)


def test_harga_modal_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("PR-01", "Beras", 0, 18000, 50)


def test_harga_jual_tidak_mencapai_keuntungan_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("PR-01", "Beras", 15000, 16000, 50)


def test_stok_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("PR-01", "Beras", 15000, 18000, -1)


def test_baris_teks_kolom_tidak_lengkap_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_teks("PR-01;Beras;15000")


def test_baris_teks_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_teks(
            "PR-01;Beras;modal;18000;50"
        )
