"""Pengujian untuk kelas Penyewa."""

import dataclasses
import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def test_identitas_penyewa_normal() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    petani = Penyewa("1406012509901111", "Joko Widodo", alamat, "081122223333")
    assert petani.identitas() == "Joko Widodo (1406012509901111) — Kuok, Kuok"


def test_kontak_default_parameter() -> None:
    alamat = Alamat("Tanjung", "Salo", "Salo")
    petani = Penyewa("1406012509902222", "Maimunah", alamat)
    assert petani.kontak() == "Maimunah belum mencantumkan nomor telepon"


def test_nik_kurang_digit_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", alamat)


def test_nik_bukan_angka_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("140601250990ABCD", "Budi", alamat)


def test_telepon_pendek_ditolak() -> None:
    """Menguji bahwa nomor telepon kurang dari 10 digit ditolak oleh setter."""
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("1406012509901111", "Joko", alamat, "0812345")


def test_telepon_tidak_sah_ditolak_via_setter() -> None:
    """Menguji penolakan format telepon yang berisi huruf lewat setter."""
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    petani = Penyewa("1406012509901111", "Joko", alamat, "081234567890")
    with pytest.raises(ValueError):
        petani.telepon = "abc"


def test_alamat_tidak_dapat_diubah() -> None:
    a = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        a.desa = "Salo"  # type: ignore[misc]