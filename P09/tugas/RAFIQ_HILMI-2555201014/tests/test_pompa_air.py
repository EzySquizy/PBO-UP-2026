
"""Pengujian untuk class PompaAir."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.pompa_air import PompaAir


def test_membuat_pompa_air() -> None:
    pompa = PompaAir("PA-01", "Pompa Air Honda", 75_000, 100)
    assert pompa.kode == "PA-01"
    assert pompa.nama == "Pompa Air Honda"
    assert pompa.tarif_harian == 75_000


def test_konsumsi_solar_harian() -> None:
    pompa = PompaAir("PA-01", "Pompa Air Honda", 75_000, 100)
    assert pompa.konsumsi_solar_harian() == 3


def test_biaya_sewa_satu_hari() -> None:
    pompa = PompaAir("PA-01", "Pompa Air Honda", 75_000, 100)
    assert pompa.biaya_sewa(1) == 96_000


def test_biaya_sewa_tiga_hari() -> None:
    pompa = PompaAir("PA-01", "Pompa Air Honda", 75_000, 100)
    assert pompa.biaya_sewa(3) == 288_000


def test_biaya_sewa_nol_hari() -> None:
    pompa = PompaAir("PA-01", "Pompa Air Honda", 75_000, 100)
    with pytest.raises(ValueError):
        pompa.biaya_sewa(0)


def test_pompa_air_merupakan_alat_tani() -> None:
    pompa = PompaAir("PA-01", "Pompa Air Honda", 75_000, 100)
    assert isinstance(pompa, AlatTani)


def test_csv_pompa_air() -> None:
    pompa = PompaAir.dari_baris_csv("PA-01;Pompa Honda;75000;100")
    assert pompa.kode == "PA-01"
    assert pompa.nama == "Pompa Honda"
    assert pompa.tarif_harian == 75_000
    assert pompa.konsumsi_solar_harian() == 3


def test_csv_pompa_air_jumlah_bagian_salah() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-01;Pompa Honda;75000")


def test_csv_pompa_air_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-01;Pompa Honda;mahal;100")


def test_csv_pompa_air_debit_bukan_angka() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-01;Pompa Honda;75000;besar")
