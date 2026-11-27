
"""Pengujian untuk class DaftarHarga."""

import pytest
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewaan import Sewaan
from src.model.traktor import Traktor


@pytest.fixture
def daftar() -> DaftarHarga:
    alat: list[Sewaan] = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 45),
        PompaAir("PA-01", "Pompa Air Honda", 80_000, 100),
        Perontok("PR-01", "Perontok Padi", 100_000, 10),
        GerobakDorong("GD-01", "Gerobak Dorong", 150_000),
    ]
    return DaftarHarga(alat)


def test_membuat_daftar_harga(daftar: DaftarHarga) -> None:
    assert daftar.jumlah_alat == 4


def test_daftar_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_biaya_semua_satu_hari(daftar: DaftarHarga) -> None:
    hasil = daftar.biaya_semua(1)
    assert hasil == [
        ("Traktor Kubota", 250_000),
        ("Pompa Air Honda", 101_000),
        ("Perontok Padi", 200_000),
        ("Gerobak Dorong", 150_000),
    ]


def test_biaya_semua_tiga_hari(daftar: DaftarHarga) -> None:
    hasil = daftar.biaya_semua(3)
    assert hasil == [
        ("Traktor Kubota", 750_000),
        ("Pompa Air Honda", 303_000),
        ("Perontok Padi", 300_000),
        ("Gerobak Dorong", 450_000),
    ]


def test_mencari_alat_berdasarkan_kode(daftar: DaftarHarga) -> None:
    alat = daftar.cari("TR-01")
    assert alat is not None
    assert alat.nama == "Traktor Kubota"


def test_mencari_kode_yang_tidak_ada(daftar: DaftarHarga) -> None:
    assert daftar.cari("XX-99") is None


def test_alat_termurah_satu_hari(daftar: DaftarHarga) -> None:
    assert daftar.termurah(1).nama == "Pompa Air Honda"


def test_alat_termurah_tiga_hari(daftar: DaftarHarga) -> None:
    assert daftar.termurah(3).nama == "Perontok Padi"


def test_total_bila_semua_disewa_satu_hari(
    daftar: DaftarHarga,
) -> None:
    assert daftar.total_bila_semua_disewa(1) == 701_000


def test_total_bila_semua_disewa_tiga_hari(
    daftar: DaftarHarga,
) -> None:
    assert daftar.total_bila_semua_disewa(3) == 1_803_000


def test_tabel_satu_hari(daftar: DaftarHarga) -> None:
    hasil = daftar.tabel(1)
    assert "Daftar harga sewa untuk 1 hari:" in hasil
    assert "Traktor Kubota: Rp250.000" in hasil
    assert "Pompa Air Honda: Rp101.000" in hasil


def test_tabel_tiga_hari(daftar: DaftarHarga) -> None:
    hasil = daftar.tabel(3)
    assert "Perontok Padi: Rp300.000" in hasil
    assert "Gerobak Dorong: Rp450.000" in hasil


def test_daftar_menyimpan_salinnya() -> None:
    alat: list[Sewaan] = [GerobakDorong("GD-01", "Alat", 50_000)]
    daftar = DaftarHarga(alat)
    alat.append(GerobakDorong("GD-02", "Alat Kedua", 75_000))
    assert daftar.jumlah_alat == 1


def test_daftar_menggunakan_polimorfisme() -> None:
    alat: list[Sewaan] = [
        Traktor("TR-02", "Traktor", 100_000, 40),
        Perontok("PR-02", "Perontok", 80_000, 10),
    ]
    daftar = DaftarHarga(alat)
    assert daftar.biaya_semua(1) == [
        ("Traktor", 200_000),
        ("Perontok", 160_000),
    ]
