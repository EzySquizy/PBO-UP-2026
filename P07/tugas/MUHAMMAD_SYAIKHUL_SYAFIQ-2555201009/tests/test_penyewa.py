
"""Pengujian untuk kelas Penyewa."""

from dataclasses import FrozenInstanceError

import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


@pytest.fixture
def alamat() -> Alamat:
    return Alamat("Pulau Belimbing", "Kuok", "Kuok")


def test_identitas_penyewa(alamat: Alamat) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat)
    assert penyewa.identitas() == "Budi (1406012509900001) — Kuok, Kuok"


def test_kontak_dengan_nomor(alamat: Alamat) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat, "081234567890")
    assert penyewa.kontak() == "Budi dapat dihubungi di 081234567890"


def test_kontak_tanpa_nomor(alamat: Alamat) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat)
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"


def test_nik_harus_16_digit(alamat: Alamat) -> None:
    with pytest.raises(ValueError):
        Penyewa("123", "Budi", alamat)


def test_nik_harus_berupa_angka(alamat: Alamat) -> None:
    with pytest.raises(ValueError):
        Penyewa("1234567890123ABC", "Budi", alamat)


def test_nik_baca_saja(alamat: Alamat) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat)
    with pytest.raises(AttributeError):
        penyewa.nik = "1406012509900002"  # type: ignore[misc]


def test_alamat_baca_saja(alamat: Alamat) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat)
    assert penyewa.alamat == alamat
    with pytest.raises(AttributeError):
        penyewa.alamat = Alamat("Dusun Baru", "Salo", "Salo")  # type: ignore[misc]


def test_alamat_tidak_dapat_diubah(alamat: Alamat) -> None:
    with pytest.raises(FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]


def test_telepon_tidak_valid_ditolak(alamat: Alamat) -> None:
    with pytest.raises(ValueError):
        Penyewa("1406012509900001", "Budi", alamat, "12AB")


def test_setter_telepon_tidak_mengubah_nilai_jika_ditolak(
    alamat: Alamat,
) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat, "081234567890")
    with pytest.raises(ValueError):
        penyewa.telepon = "123"
    assert penyewa.telepon == "081234567890"


def test_setter_telepon_menerima_nomor_valid(alamat: Alamat) -> None:
    penyewa = Penyewa("1406012509900001", "Budi", alamat)
    penyewa.telepon = "081298765432"
    assert penyewa.telepon == "081298765432"


def test_dua_penyewa_menyimpan_alamat_sendiri() -> None:
    alamat_budi = Alamat("Pulau Belimbing", "Kuok", "Kuok")
    alamat_siti = Alamat("Salo Timur", "Salo", "Salo")
    budi = Penyewa("1406012509900001", "Budi", alamat_budi)
    siti = Penyewa("1406014403950002", "Siti", alamat_siti)
    assert budi.alamat.desa == "Kuok"
    assert siti.alamat.desa == "Salo"
