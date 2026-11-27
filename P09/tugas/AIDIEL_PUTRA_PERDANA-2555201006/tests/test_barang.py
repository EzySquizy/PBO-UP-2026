import pytest
from src.model.barang import Barang
from src.model.sembako import Sembako


def test_barang_abstrak_tidak_dapat_diinstansiasi() -> None:
    with pytest.raises(TypeError):
        Barang("BR-00", "Barang Umum", 10_000, 5)  # type: ignore[abstract]


def test_manajemen_stok_dan_validasi_induk() -> None:
    barang = Sembako("SB-01", "Gula Pasir 1kg", 17_000, 10)
    barang.kurangi_stok(3)
    assert barang.stok == 7

    barang.tambah_stok(5)
    assert barang.stok == 12

    with pytest.raises(ValueError):
        barang.kurangi_stok(20)