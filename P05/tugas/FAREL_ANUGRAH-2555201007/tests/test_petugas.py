"""Tes untuk model Petugas pada P03."""

import pytest
from src.model.kontak_petugas import KontakPetugas
from src.model.petugas import Petugas


def buat_petugas() -> Petugas:
    kontak = KontakPetugas(
        "petugas@upja.id",
        "Kantor UPJA Kuok",
    )
    return Petugas(
        "198501152010011001",
        "Ahmad Fauzi",
        "Pengelola UPJA",
        kontak,
        "081234567890",
    )


def test_identitas_petugas() -> None:
    petugas = buat_petugas()
    assert petugas.identitas() == (
        "Ahmad Fauzi (198501152010011001) - Pengelola UPJA"
    )


def test_informasi_kontak_petugas() -> None:
    petugas = buat_petugas()
    assert petugas.informasi_kontak() == (
        "Telepon: 081234567890, Email: petugas@upja.id"
    )


def test_nip_tidak_valid() -> None:
    kontak = KontakPetugas("petugas@upja.id", "Kantor UPJA Kuok")
    with pytest.raises(ValueError):
        Petugas("123", "Ahmad", "Pengelola", kontak, "081234567890")


def test_nama_tidak_boleh_kosong() -> None:
    kontak = KontakPetugas("petugas@upja.id", "Kantor UPJA Kuok")
    with pytest.raises(ValueError):
        Petugas(
            "198501152010011001",
            "",
            "Pengelola",
            kontak,
            "081234567890",
        )


def test_jabatan_tidak_boleh_kosong() -> None:
    kontak = KontakPetugas("petugas@upja.id", "Kantor UPJA Kuok")
    with pytest.raises(ValueError):
        Petugas(
            "198501152010011001",
            "Ahmad",
            "",
            kontak,
            "081234567890",
        )


def test_telepon_tidak_valid() -> None:
    petugas = buat_petugas()
    with pytest.raises(ValueError):
        petugas.telepon = "123"


def test_telepon_bisa_diubah() -> None:
    petugas = buat_petugas()
    petugas.telepon = "081298765432"
    assert petugas.telepon == "081298765432"


def test_kontak_bersifat_beku() -> None:
    petugas = buat_petugas()
    with pytest.raises(AttributeError):
        petugas.kontak.email = "baru@upja.id"  # type: ignore[misc]


def test_email_kontak_tidak_valid() -> None:
    with pytest.raises(ValueError):
        KontakPetugas("email-salah", "Kantor UPJA Kuok")
