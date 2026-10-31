import pytest
from src.model.kios import Kios


def test_produk_beras_dapat_dibuat() -> None:
    produk = Kios("BR001", "Beras", 14_000, 16_000)
    assert produk._produk.nama == "Beras"


def test_produk_gula_dapat_dibuat() -> None:
    produk = Kios("GL001", "Gula pasir", 16_000, 18_000)
    assert produk._produk.nama == "Gula pasir"


def test_produk_minyak_dapat_dibuat() -> None:
    produk = Kios("MG001", "Minyak goreng", 17_000, 19_000)
    assert produk._produk.nama == "Minyak goreng"


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 14_000, 16_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR001", "", 14_000, 16_000)


def test_modal_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR001", "Beras", 0, 16_000)


def test_modal_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR001", "Beras", -1_000, 16_000)


def test_harga_jual_di_bawah_modal_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR001", "Beras", 14_000, 14_000)


def test_harga_jual_di_atas_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR001", "Beras", 14_000, 11_000_000)


def test_baris_dengan_kolom_kurang_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR001;Beras;14000")


def test_baris_dengan_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR001;Beras;modal;16000")


def test_konstruktor_dari_baris() -> None:
    produk = Kios.dari_baris("BR001;Beras;14000;16000")
    assert produk._produk.kode == "BR001"
    assert produk._produk.nama == "Beras"


def test_pencacah_produk_bertambah_satu() -> None:
    sebelum = Kios.jumlah_produk()

    Kios("TB001", "Tepung beras", 10_000, 12_000)

    sesudah = Kios.jumlah_produk()
    assert sesudah - sebelum == 1


def test_staticmethod_menolak_harga_tidak_wajar() -> None:
    assert not Kios.harga_jual_wajar(14_000, 14_000)


def test_staticmethod_menerima_harga_wajar() -> None:
    assert Kios.harga_jual_wajar(14_000, 16_000)
