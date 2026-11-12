
"""Pengujian untuk kelas Penyewa."""

import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_penyewa(telepon: str = "0812-3456-7890") -> Penyewa:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat,
        telepon,
    )


def test_penyewa_menyimpan_data() -> None:
    penyewa = buat_penyewa()

    assert penyewa.nik == "1406012509900001"
    assert penyewa._nama == "Budi Santoso"
    assert penyewa.alamat.desa == "Kuok"
    assert penyewa.telepon == "0812-3456-7890"


def test_penyewa_identitas() -> None:
    penyewa = buat_penyewa()

    assert penyewa.identitas() == (
        "Budi Santoso (1406012509900001) — Kuok, Kuok"
    )


def test_penyewa_kontak() -> None:
    penyewa = buat_penyewa()

    assert penyewa.kontak() == (
        "Budi Santoso dapat dihubungi di 0812-3456-7890"
    )


def test_penyewa_tanpa_telepon() -> None:
    penyewa = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        Alamat("Dusun Salo", "Salo", "Salo"),
    )

    assert penyewa.kontak() == (
        "Siti Aminah belum mencantumkan nomor telepon"
    )


def test_nik_bukan_16_digit_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", Alamat("Dusun A", "Kuok", "Kuok"))


def test_nik_mengandung_huruf_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa(
            "140601250990000A",
            "Budi",
            Alamat("Dusun A", "Kuok", "Kuok"),
        )


def test_nik_tidak_bisa_diubah() -> None:
    penyewa = buat_penyewa()

    with pytest.raises(AttributeError):
        penyewa.nik = "1406014403950002"  # type: ignore[misc]


def test_alamat_tidak_bisa_diubah() -> None:
    penyewa = buat_penyewa()

    with pytest.raises(AttributeError):
        penyewa.alamat = Alamat("Dusun B", "Salo", "Salo")  # type: ignore[misc]


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        buat_penyewa("12345")


def test_telepon_mengandung_huruf_ditolak() -> None:
    with pytest.raises(ValueError):
        buat_penyewa("0812ABCDEF")


def test_telepon_boleh_memakai_tanda_hubung() -> None:
    penyewa = buat_penyewa("0812-3456-7890")

    assert penyewa.telepon == "0812-3456-7890"


def test_telepon_bisa_diubah_ke_nomor_valid() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "081234567890"

    assert penyewa.telepon == "081234567890"


def test_telepon_bisa_diubah_ke_tanda_strip() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "-"

    assert penyewa.telepon == "-"
