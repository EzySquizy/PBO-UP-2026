import dataclasses

import pytest

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def test_alat_tani_dibuat_dengan_tarif_valid() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.tarif_harian == 150000


def test_kode_alat_bersifat_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore[misc]


def test_nama_alat_bersifat_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Traktor Baru"  # type: ignore[misc]


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_nol_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_diatas_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5000001)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000


def test_biaya_sewa_dihitung_benar() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_alamat_dapat_dibuat() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    assert alamat.singkat() == "Kuok, Kuok"


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "", "Kuok")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "Kuok", "")


def test_nik_penyewa_valid() -> None:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    penyewa = Penyewa("1401011234567890", "Budi", alamat)
    assert penyewa.nik == "1401011234567890"


def test_nik_tidak_16_digit_ditolak() -> None:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", alamat)


def test_telepon_tidak_valid_ditolak() -> None:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    penyewa = Penyewa("1401011234567890", "Budi", alamat)
    with pytest.raises(ValueError):
        penyewa.telepon = "123"