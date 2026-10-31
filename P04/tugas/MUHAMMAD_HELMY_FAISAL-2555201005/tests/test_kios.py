"""Pengujian Unit untuk Kelas Kios (Tugas 1 Individu)."""

import pytest
from src.model.kios import Kios

def test_inisialisasi_kios_dan_akses_property() -> None:
    barang = Kios("BRS-01", "Beras Kampar 10kg", 130000)
    assert barang.kode == "BRS-01"
    assert barang.nama == "Beras Kampar 10kg"
    assert barang.harga_pokok == 130000


def test_hitung_harga_jual_dengan_margin_persen() -> None:
    # Modal 50.000, margin 20% = 10.000 -> Harga Jual = 60.000
    barang = Kios("MYK-01", "Minyak Kita", 50000)
    assert barang.hitung_harga_jual() == 60000


def test_format_baris_tabel_fstring_alignment() -> None:
    barang = Kios("GLA-01", "Gula Aren Lokal", 18000)
    hasil = barang.format_baris_tabel()
    assert "[GLA-01]" in hasil
    assert "Gula Aren Lokal" in hasil


def test_static_method_cek_harga_valid() -> None:
    assert Kios.cek_harga_valid(50000) is True
    assert Kios.cek_harga_valid(0) is False
    assert Kios.cek_harga_valid(-10000) is False
    assert Kios.cek_harga_valid(3_000_000) is False


def test_classmethod_dari_teks_pembatas_berhasil() -> None:
    baris = "TLR-01|Telur Ayam Kampung|25000"
    barang = Kios.dari_teks_pembatas(baris)
    assert barang.kode == "TLR-01"
    assert barang.nama == "Telur Ayam Kampung"
    assert barang.harga_pokok == 25000


def test_pencacah_produk_bertambah_dengan_pola_selisih() -> None:
    awal = Kios.jumlah_terdaftar()

    _ = Kios("X-01", "Produk Uji A", 15000)
    _ = Kios("X-02", "Produk Uji B", 25000)

    assert Kios.jumlah_terdaftar() == awal + 2

def test_tolak_kode_spasi_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("   ", "Beras Pulut", 20000)


def test_tolak_nama_spasi_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("BRS-02", "   ", 20000)


def test_tolak_harga_pokok_nol_atau_minus() -> None:
    with pytest.raises(ValueError):
        Kios("BRS-03", "Beras Anak Daro", 0)


def test_tolak_harga_pokok_melebihi_maksimum() -> None:
    with pytest.raises(ValueError):
        Kios("BRS-04", "Beras Premium", 3_000_000)


def test_tolak_format_teks_pembatas_kurang_bagian() -> None:
    with pytest.raises(ValueError):
        Kios.dari_teks_pembatas("BRS-05|Beras Solok")


def test_tolak_format_teks_pembatas_harga_bukan_digit() -> None:
    with pytest.raises(ValueError):
        Kios.dari_teks_pembatas("BRS-06|Beras Solok|Seratus Ribu")