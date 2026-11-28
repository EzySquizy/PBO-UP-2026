import pytest
from src.model.errors import (
    FormatBarisTidakValid,
    HargaBukanAngka,
    HargaJualDiAtasMaksimum,
    HargaJualDiBawahMinimum,
    HargaJualTidakWajar,
    KodeProdukTidakValid,
    ModalTidakValid,
    NamaProdukTidakValid,
)
from src.model.kios import Kios
from src.model.pesan import terjemahkan_eksepsi
from src.model.produk import Produk
from src.model.transaksi import transaksi_kios


def test_produk_beras_dapat_dibuat() -> None:
    produk = Produk("BR001", "Beras")

    assert produk.kode == "BR001"
    assert produk.nama == "Beras"


def test_produk_gula_dapat_dibuat() -> None:
    produk = Produk("GL001", "Gula")

    assert produk.kode == "GL001"
    assert produk.nama == "Gula"


def test_produk_minyak_dapat_dibuat() -> None:
    produk = Produk("MY001", "Minyak")

    assert produk.kode == "MY001"
    assert produk.nama == "Minyak"


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(KodeProdukTidakValid):
        Produk("", "Beras")


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(NamaProdukTidakValid):
        Produk("BR001", "")


def test_modal_nol_ditolak() -> None:
    with pytest.raises(ModalTidakValid):
        Kios("BR001", "Beras", 0, 15_000)


def test_modal_negatif_ditolak() -> None:
    with pytest.raises(ModalTidakValid):
        Kios("BR001", "Beras", -1_000, 15_000)


def test_harga_jual_di_bawah_modal_ditolak() -> None:
    with pytest.raises(HargaJualTidakWajar):
        Kios("BR001", "Beras", 10_000, 10_500)


def test_harga_jual_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(HargaJualDiBawahMinimum):
        Kios("BR001", "Beras", 500, 900)


def test_harga_jual_di_atas_batas_ditolak() -> None:
    with pytest.raises(HargaJualDiAtasMaksimum):
        Kios("BR001", "Beras", 1_000_000, 10_000_001)


def test_baris_dengan_kolom_kurang_ditolak() -> None:
    with pytest.raises(FormatBarisTidakValid):
        Kios.dari_baris("BR001;Beras;14000")


def test_baris_dengan_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(HargaBukanAngka):
        Kios.dari_baris("BR001;Beras;abc;16000")


def test_kesalahan_harga_menyimpan_penyebab() -> None:
    with pytest.raises(HargaBukanAngka) as info:
        Kios.dari_baris("BR001;Beras;abc;16000")

    assert isinstance(info.value.__cause__, ValueError)


def test_konstruktor_dari_baris() -> None:
    kios = Kios.dari_baris("BR001;Beras;14000;16000")

    assert "BR001" in kios.informasi()
    assert "Beras" in kios.informasi()


def test_pencacah_produk_bertambah_satu() -> None:
    jumlah_awal = Kios.jumlah_produk()

    Kios("BR001", "Beras", 14_000, 16_000)

    assert Kios.jumlah_produk() == jumlah_awal + 1


def test_staticmethod_menolak_harga_tidak_wajar() -> None:
    assert not Kios.harga_jual_wajar(10_000, 10_500)


def test_staticmethod_menerima_harga_wajar() -> None:
    assert Kios.harga_jual_wajar(10_000, 12_000)


def test_transaksi_berhasil_menyimpan_produk() -> None:
    jumlah_awal = Kios.jumlah_produk()

    with transaksi_kios() as daftar:
        daftar.append(Kios("BR001", "Beras", 14_000, 16_000))

    assert len(daftar) == 1
    assert Kios.jumlah_produk() == jumlah_awal + 1


def test_transaksi_gagal_melakukan_rollback() -> None:
    jumlah_awal = Kios.jumlah_produk()

    with pytest.raises(ModalTidakValid), transaksi_kios() as daftar:
        daftar.append(Kios("BR003", "Beras", 14_000, 16_000))
        Kios("BR004", "Gula", 0, 18_000)

    assert daftar == []
    assert Kios.jumlah_produk() == jumlah_awal


def test_penerjemah_kesalahan_kode() -> None:
    pesan = terjemahkan_eksepsi(KodeProdukTidakValid())

    assert pesan == "Pendaftaran gagal: kode produk belum diisi."


def test_penerjemah_kesalahan_umum() -> None:
    pesan = terjemahkan_eksepsi(Exception("Kesalahan umum"))

    assert pesan == "Terjadi kesalahan yang tidak dapat diproses."
