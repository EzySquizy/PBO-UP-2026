"""Tes untuk model Alamat pada P03."""

from dataclasses import FrozenInstanceError

import pytest
from src.model.alamat import Alamat


def test_alamat_lengkap() -> None:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    assert alamat.lengkap() == "Dusun Pongkai, Desa Kuok, Kec. Kuok"


def test_alamat_singkat() -> None:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    assert alamat.singkat() == "Kuok, Kuok"


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    with pytest.raises(FrozenInstanceError):
        alamat.desa = "Bangkinang"  # type: ignore[misc]


def test_desa_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Pongkai", " ", "Kuok")


def test_kecamatan_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Pongkai", "Kuok", " ")
