"""Pengujian untuk kelas Penyewa dan Alamat."""

import dataclasses
import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def test_penyewa_identitas() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi Santoso", alamat, "0812-3456-7890")
    assert penyewa.identitas() == "Budi Santoso (1406012509900001) — Kuok, Kuok"


def test_penyewa_kontak_ada_telepon() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi Santoso", alamat, "0812-3456-7890")
    assert penyewa.kontak() == "Budi Santoso dapat dihubungi di 0812-3456-7890"


def test_penyewa_kontak_tanpa_telepon() -> None:
    alamat = Alamat("Pulau Jambu", "Salo", "Salo")
    penyewa = Penyewa("1406014403950002", "Siti Aminah", alamat)
    assert penyewa.kontak() == "Siti Aminah belum mencantumkan nomor telepon"


def test_nik_kurang_dari_16_digit_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi Santoso", alamat)


def test_nik_mengandung_huruf_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("140601250990000A", "Budi Santoso", alamat)


def test_nik_tidak_punya_setter() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi Santoso", alamat)
    with pytest.raises(AttributeError):
        penyewa.nik = "1406012509900002"  # type: ignore[misc]


def test_telepon_tidak_sah_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi Santoso", alamat)
    with pytest.raises(ValueError):
        penyewa.telepon = "123"


def test_alamat_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "  ", "Kuok")


def test_alamat_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "Kuok", "  ")


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]