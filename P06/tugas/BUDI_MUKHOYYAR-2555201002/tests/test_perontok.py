"""Pengujian untuk kelas Perontok."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok


def test_perontok_merupakan_turunan_alat_tani() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert isinstance(alat, AlatTani)


def test_sewa_satu_hari_ditagih_dua_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert alat.biaya_sewa(1) == 400_000


def test_sewa_dua_hari_ditagih_dua_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert alat.biaya_sewa(2) == 400_000


def test_sewa_tiga_hari_ditagih_tiga_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert alat.biaya_sewa(3) == 600_000


def test_hari_ditagih_memenuhi_minimum() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert alat.hari_ditagih(1) == 2


def test_kapasitas_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-01", "Perontok Padi", 200_000, 0)


def test_kapasitas_minus_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-01", "Perontok Padi", 200_000, -100)