"""Pengujian untuk kelas PompaAir."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.pompa_air import PompaAir


def test_pompa_merupakan_turunan_alat_tani() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 100_000, 100)
    assert isinstance(pompa, AlatTani)


def test_konsumsi_solar_harian() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 100_000, 100)
    assert pompa.konsumsi_solar_harian() == 3


def test_biaya_sewa_satu_hari_ditambah_solar() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 100_000, 100)
    assert pompa.biaya_sewa(1) == 121_000


def test_biaya_sewa_dua_hari_ditambah_solar() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 100_000, 100)
    assert pompa.biaya_sewa(2) == 242_000


def test_debit_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-01", "Pompa Air", 100_000, 0)


def test_debit_minus_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-01", "Pompa Air", 100_000, -10)
        