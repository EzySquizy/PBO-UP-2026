
"""Pengujian untuk kelas DaftarHarga."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewaan import Sewaan
from src.model.traktor import Traktor


def contoh_alat() -> list[Sewaan]:
    return [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 600),
        Perontok("PR-01", "Perontok Padi", 200_000, 900),
    ]


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_biaya_semua_menghitung_semua_alat() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.biaya_semua(2) == [
        ("Traktor", 500_000),
        ("Pompa Air", 402_000),
        ("Perontok Padi", 400_000),
    ]


def test_termurah_memilih_alat_dengan_biaya_terendah() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.termurah(1).nama == "Pompa Air"


def test_total_bila_semua_disewa() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.total_bila_semua_disewa(2) == 1_302_000


def test_daftar_harga_menyalin_daftar_asli() -> None:
    alat = contoh_alat()
    daftar = DaftarHarga(alat)

    alat.clear()

    assert daftar.biaya_semua(1) == [
        ("Traktor", 250_000),
        ("Pompa Air", 201_000),
        ("Perontok Padi", 400_000),
    ]


def test_daftar_harga_menerima_objek_non_alat_tani() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 100_000)
    daftar = DaftarHarga([*contoh_alat(), gerobak])

    assert isinstance(gerobak, Sewaan)
    assert not isinstance(gerobak, AlatTani)
    assert ("Gerobak Dorong", 100_000) in daftar.biaya_semua(1)
    assert daftar.total_bila_semua_disewa(1) == 951_000
