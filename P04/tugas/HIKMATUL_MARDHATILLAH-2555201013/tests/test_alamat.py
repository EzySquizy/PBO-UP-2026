
"""Pengujian untuk kelas Alamat."""

import pytest

from src.model.alamat import Alamat


def test_alamat_lengkap() -> None:
    alamat = Alamat("Dusun Pulau Jambu", "Kuok", "Kuok")
    assert alamat.lengkap() == "Dusun Dusun Pulau Jambu, Desa Kuok, Kec. Kuok"


def test_alamat_singkat() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    assert alamat.singkat() == "Kuok, Kuok"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Dusun I", "", "Kuok")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Dusun I", "Kuok", "")


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    with pytest.raises(AttributeError):
        setattr(alamat, "desa", "Salo")