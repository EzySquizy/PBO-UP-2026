
"""Pengujian untuk kelas Alamat."""

from dataclasses import FrozenInstanceError

import pytest
from src.model.alamat import Alamat


def test_alamat_menyimpan_data() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")

    assert alamat.dusun == "Pulau Jambu"
    assert alamat.desa == "Kuok"
    assert alamat.kecamatan == "Kuok"


def test_alamat_lengkap() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")

    assert alamat.lengkap() == (
        "Dusun Pulau Jambu, Desa Kuok, Kec. Kuok"
    )


def test_alamat_singkat() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")

    assert alamat.singkat() == "Kuok, Kuok"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "", "Kuok")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "Kuok", "")


def test_desa_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "   ", "Kuok")


def test_kecamatan_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "Kuok", "   ")


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")

    with pytest.raises(FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]
