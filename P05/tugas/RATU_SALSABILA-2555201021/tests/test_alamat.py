
"""Pengujian objek nilai Alamat."""

import pytest

from src.model.alamat import Alamat


def test_alamat_dapat_dibuat() -> None:
    alamat = Alamat("Kumantan", "Kumantan", "Bangkinang")

    assert alamat.dusun == "Kumantan"
    assert alamat.desa == "Kumantan"
    assert alamat.kecamatan == "Bangkinang"


def test_alamat_lengkap() -> None:
    alamat = Alamat("Kumantan", "Kumantan", "Bangkinang")

    assert alamat.lengkap() == (
        "Dusun Kumantan, Desa Kumantan, Kecamatan Bangkinang"
    )


def test_alamat_singkat() -> None:
    alamat = Alamat("Kumantan", "Kumantan", "Bangkinang")

    assert alamat.singkat() == "Desa Kumantan, Kecamatan Bangkinang"


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = Alamat("Kumantan", "Kumantan", "Bangkinang")

    with pytest.raises(AttributeError):
        alamat.desa = "Desa Baru"  # type: ignore[misc]


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Kumantan", "", "Bangkinang")


def test_desa_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Kumantan", "   ", "Bangkinang")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Kumantan", "Kumantan", "")


def test_kecamatan_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Kumantan", "Kumantan", "   ")
