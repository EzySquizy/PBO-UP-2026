import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def test_alamat_valid() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    assert alamat.dusun == "Dusun I"
    assert alamat.desa == "Kuok"
    assert alamat.kecamatan == "Kuok"


def test_alamat_lengkap() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    assert alamat.lengkap() == "Dusun Dusun I, Desa Kuok, Kecamatan Kuok"


def test_alamat_singkat() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    assert alamat.singkat() == "Kuok, Kuok"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Dusun I", "", "Kuok")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Dusun I", "Kuok", "")


def test_alamat_frozen() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    with pytest.raises(AttributeError):
        alamat.desa = "Bangkinang"  # type: ignore[misc]


def test_penyewa_valid() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa("Budi Santoso", "1234567890123456", alamat)
    assert penyewa.nama == "Budi Santoso"
    assert penyewa.nik == "1234567890123456"
    assert penyewa.alamat == alamat


def test_nik_bukan_16_digit_ditolak() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("Budi", "12345", alamat)


def test_nik_mengandung_huruf_ditolak() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("Budi", "12345678901234AB", alamat)


def test_nik_read_only() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa("Budi", "1234567890123456", alamat)
    with pytest.raises(AttributeError):
        penyewa.nik = "6543210987654321"  # type: ignore[misc]

def test_telepon_valid() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa(
        "Budi",
        "1234567890123456",
        alamat,
        "081234567890",
    )
    assert penyewa.telepon == "081234567890"


def test_telepon_strip_valid() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa(
        "Budi",
        "1234567890123456",
        alamat,
        "0812-3456-7890",
    )
    assert penyewa.telepon == "0812-3456-7890"


def test_telepon_tidak_valid_ditolak() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa(
            "Budi",
            "1234567890123456",
            alamat,
            "123",
        )


def test_identitas() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa("Budi Santoso", "1234567890123456", alamat)
    assert (
        penyewa.identitas()
        == "Saya Budi Santoso (1234567890123456), dari Kuok, Kuok."
    )
