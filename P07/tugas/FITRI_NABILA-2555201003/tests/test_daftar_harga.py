
"""Pengujian untuk kelas DaftarHarga."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga


def contoh_alat() -> list[AlatTani]:
    return [
        AlatTani("TR-01", "Traktor", 250_000),
        AlatTani("PA-01", "Pompa Air", 100_000),
        AlatTani("PR-01", "Perontok Padi", 150_000),
    ]


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_biaya_semua_menghitung_semua_alat() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.biaya_semua(2) == [
        ("Traktor", 500_000),
        ("Pompa Air", 200_000),
        ("Perontok Padi", 300_000),
    ]


def test_termurah_memilih_alat_dengan_biaya_terendah() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.termurah(1).nama == "Pompa Air"


def test_total_bila_semua_disewa() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.total_bila_semua_disewa(2) == 1_000_000


def test_daftar_harga_menyalin_daftar_asli() -> None:
    alat = contoh_alat()
    daftar = DaftarHarga(alat)

    alat.clear()

    assert daftar.biaya_semua(1) == [
        ("Traktor", 250_000),
        ("Pompa Air", 100_000),
        ("Perontok Padi", 150_000),
    ]


def test_daftar_harga_menerima_alat_turunan_baru() -> None:
    class Penggiling(AlatTani):
        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + 25_000

    daftar = DaftarHarga([
        *contoh_alat(),
        Penggiling("PG-01", "Penggiling", 100_000),
    ])

    assert ("Penggiling", 125_000) in daftar.biaya_semua(1)
    assert daftar.total_bila_semua_disewa(1) == 625_000
