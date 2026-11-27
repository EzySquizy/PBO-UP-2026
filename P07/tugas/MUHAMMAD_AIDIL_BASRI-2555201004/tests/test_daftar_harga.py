
"""Pengujian polimorfisme pada DaftarHarga."""

import pytest
from src.model import AlatTani, DaftarHarga, Perontok, PompaAir, Traktor


@pytest.fixture
def daftar_harga() -> DaftarHarga:
    """Menyediakan daftar tiga jenis alat pertanian."""
    alat = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 600),
        Perontok("PR-01", "Perontok Padi", 200_000, 900),
    ]
    return DaftarHarga(alat)


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError, match="daftar harga"):
        DaftarHarga([])


def test_jumlah_alat(daftar_harga: DaftarHarga) -> None:
    assert daftar_harga.jumlah_alat == 3


def test_biaya_semua_tiga_hari(daftar_harga: DaftarHarga) -> None:
    assert daftar_harga.biaya_semua(3) == [
        ("Traktor Kubota", 750_000),
        ("Pompa Air", 603_000),
        ("Perontok Padi", 600_000),
    ]


def test_termurah_satu_hari(daftar_harga: DaftarHarga) -> None:
    assert daftar_harga.termurah(1).kode == "PA-01"


def test_termurah_tiga_hari(daftar_harga: DaftarHarga) -> None:
    assert daftar_harga.termurah(3).kode == "PR-01"


def test_total_bila_semua_disewa(daftar_harga: DaftarHarga) -> None:
    assert daftar_harga.total_bila_semua_disewa(3) == 1_953_000


def test_tabel_memuat_nama_dan_biaya(daftar_harga: DaftarHarga) -> None:
    hasil = daftar_harga.tabel(3)

    assert "Traktor Kubota" in hasil
    assert "Rp750.000" in hasil
    assert "Rp603.000" in hasil
    assert "Rp600.000" in hasil


def test_daftar_harga_menerima_subkelas_baru() -> None:
    class Penggiling(AlatTani):
        """Jenis alat baru dengan ongkos angkut tambahan."""

        ONGKOS_ANGKUT = 50_000

        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + self.ONGKOS_ANGKUT

    daftar = DaftarHarga([
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        Penggiling("PG-01", "Penggiling Gabah", 120_000),
    ])

    assert daftar.biaya_semua(3) == [
        ("Traktor Kubota", 750_000),
        ("Penggiling Gabah", 410_000),
    ]
