
import pytest
from src.model.kios import Kios

HARGA_BERAS = 100_000
STOK_BERAS = 10
HARGA_JUAL_BERAS = 110_000
HARGA_MINYAK = 25_000
STOK_MINYAK = 8


def test_data_barang_valid() -> None:
    barang = Kios("Beras", HARGA_BERAS, STOK_BERAS)

    assert barang.nama_barang == "Beras"
    assert barang.harga_modal == HARGA_BERAS
    assert barang.stok == STOK_BERAS


def test_nama_barang_dihilangkan_spasinya() -> None:
    barang = Kios("  Gula  ", 20_000, 5)

    assert barang.nama_barang == "Gula"


def test_harga_jual_dengan_margin() -> None:
    barang = Kios("Beras", HARGA_BERAS, STOK_BERAS)

    assert barang.harga_jual() == HARGA_JUAL_BERAS


def test_membuat_barang_dari_baris_teks() -> None:
    barang = Kios.dari_baris_teks("Minyak Goreng;25000;8")

    assert barang.nama_barang == "Minyak Goreng"
    assert barang.harga_modal == HARGA_MINYAK
    assert barang.stok == STOK_MINYAK


def test_harga_minimum_valid() -> None:
    assert Kios.harga_wajar(Kios.BATAS_HARGA_MINIMUM)


def test_harga_maksimum_valid() -> None:
    assert Kios.harga_wajar(Kios.BATAS_HARGA_MAKSIMUM)


def test_pencacah_naik_satu() -> None:
    sebelum = Kios.jumlah_produk()
    Kios("Minyak Goreng", HARGA_MINYAK, STOK_MINYAK)
    sesudah = Kios.jumlah_produk()

    assert sesudah - sebelum == 1


def test_harga_di_bawah_minimum_ditolak() -> None:
    assert not Kios.harga_wajar(Kios.BATAS_HARGA_MINIMUM - 1)


def test_harga_di_atas_maksimum_ditolak() -> None:
    assert not Kios.harga_wajar(Kios.BATAS_HARGA_MAKSIMUM + 1)


def test_harga_boolean_ditolak() -> None:
    assert not Kios.harga_wajar(True)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", HARGA_BERAS, STOK_BERAS)


def test_harga_modal_tidak_wajar_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("Gula", 500, STOK_BERAS)


def test_stok_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("Beras", HARGA_BERAS, -1)


def test_format_baris_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_teks("Beras;100000")


def test_harga_teks_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_teks("Beras;mahal;10")


def test_stok_teks_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_teks("Beras;100000;banyak")


def test_baris_bukan_teks_ditolak() -> None:
    with pytest.raises(TypeError):
        Kios.dari_baris_teks(None)  # type: ignore[arg-type]
