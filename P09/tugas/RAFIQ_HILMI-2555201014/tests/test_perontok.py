
"""Pengujian untuk class Perontok."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok


def test_membuat_perontok() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.kode == "PR-01"
    assert alat.nama == "Perontok Padi"
    assert alat.tarif_harian == 100_000


def test_hari_ditagih_satu_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.hari_ditagih(1) == 2


def test_hari_ditagih_dua_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.hari_ditagih(2) == 2


def test_hari_ditagih_tiga_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.hari_ditagih(3) == 3


def test_biaya_sewa_satu_hari_dihitung_dua_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.biaya_sewa(1) == 200_000


def test_biaya_sewa_dua_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.biaya_sewa(2) == 200_000


def test_biaya_sewa_tiga_hari() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert alat.biaya_sewa(3) == 300_000


def test_perontok_merupakan_alat_tani() -> None:
    alat = Perontok("PR-01", "Perontok Padi", 100_000, 10)
    assert isinstance(alat, AlatTani)


def test_csv_perontok() -> None:
    alat = Perontok.dari_baris_csv("PR-01;Perontok Padi;100000;10")
    assert alat.kode == "PR-01"
    assert alat.nama == "Perontok Padi"
    assert alat.tarif_harian == 100_000


def test_csv_perontok_jumlah_bagian_salah() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-01;Perontok Padi;100000")


def test_csv_perontok_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-01;Perontok Padi;mahal;10")


def test_csv_perontok_kapasitas_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-01;Perontok Padi;100000;besar")
