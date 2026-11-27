"""Tes untuk model Penyewa pada P03."""

import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    return Penyewa(
        "1234567890123456",
        "Budi",
        alamat,
        "08123456789",
    )


def test_identitas_penyewa() -> None:
    penyewa = buat_penyewa()
    assert penyewa.identitas() == (
        "Budi (1234567890123456) — Kuok, Kuok"
    )


def test_kontak_penyewa() -> None:
    penyewa = buat_penyewa()
    assert penyewa.kontak() == (
        "Budi dapat dihubungi di 08123456789"
    )


def test_telepon_default() -> None:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    penyewa = Penyewa("1234567890123456", "Budi", alamat)
    assert penyewa.telepon == "-"
    assert penyewa.kontak() == (
        "Budi belum mencantumkan nomor telepon"
    )


def test_nik_tidak_valid() -> None:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("123", "Budi", alamat)


def test_telepon_tidak_valid() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(ValueError):
        penyewa.telepon = "123"


def test_telepon_bisa_diubah() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "081298765432"
    assert penyewa.telepon == "081298765432"
