"""Pengujian untuk kelas Penyewa dan Alamat."""

import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi Santoso", alamat, "081234567890")
    assert penyewa.identitas() == "Budi Santoso (1406012509900001) — Kuok, Kuok"


def test_kontak_dengan_telepon() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi", alamat, "081234567890")
    assert penyewa.kontak() == "Budi dapat dihubungi di 081234567890"


def test_kontak_tanpa_telepon() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa("1406012509900001", "Budi", alamat)
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"


def test_nik_kurang_dari_16_digit_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", alamat)


def test_nik_bukan_angka_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("140601250990000A", "Budi", alamat)


def test_telepon_tidak_valid_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("1406012509900001", "Budi", alamat, "0812")


def test_desa_alamat_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "", "Kuok")
