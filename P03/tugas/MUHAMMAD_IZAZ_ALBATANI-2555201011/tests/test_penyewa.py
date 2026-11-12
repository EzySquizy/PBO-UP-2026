
"""Pengujian untuk kelas Penyewa."""

import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Suka Maju", "Kuok", "Kuok")
    return Penyewa("1234567890123456", "Budi Santoso", alamat)


def test_identitas_penyewa() -> None:
    penyewa = buat_penyewa()
    assert penyewa.identitas() == (
        "Budi Santoso (1234567890123456) — Kuok, Kuok"
    )


def test_kontak_penyewa_dengan_telepon() -> None:
    alamat = Alamat("Suka Maju", "Kuok", "Kuok")
    penyewa = Penyewa(
        "1234567890123456", "Budi Santoso", alamat, "081234567890"
    )
    assert penyewa.kontak() == (
        "Budi Santoso dapat dihubungi di 081234567890"
    )


def test_kontak_penyewa_tanpa_telepon() -> None:
    penyewa = buat_penyewa()
    assert penyewa.kontak() == (
        "Budi Santoso belum mencantumkan nomor telepon"
    )


def test_nik_harus_16_digit() -> None:
    alamat = Alamat("Suka Maju", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", alamat)


def test_nik_tidak_boleh_huruf() -> None:
    alamat = Alamat("Suka Maju", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("123456789012345A", "Budi", alamat)


def test_nik_tidak_bisa_diubah() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(AttributeError):
        penyewa.nik = "9876543210987654"  # type: ignore[misc]


def test_alamat_tidak_bisa_diganti() -> None:
    penyewa = buat_penyewa()
    alamat_baru = Alamat("Melati", "Salo", "Salo")
    with pytest.raises(AttributeError):
        penyewa.alamat = alamat_baru  # type: ignore[misc]


def test_telepon_bisa_diubah() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "081234567890"
    assert penyewa.telepon == "081234567890"


def test_telepon_boleh_strip_dan_spasi() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "0812-3456-7890"
    assert penyewa.telepon == "0812-3456-7890"


def test_telepon_tidak_boleh_kurang_dari_10_digit() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(ValueError):
        penyewa.telepon = "0812345"


def test_telepon_tidak_boleh_huruf() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(ValueError):
        penyewa.telepon = "08123ABCDE"
