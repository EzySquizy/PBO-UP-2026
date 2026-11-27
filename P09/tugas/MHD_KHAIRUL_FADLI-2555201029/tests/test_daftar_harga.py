
"""Pengujian polimorfisme pada DaftarHarga."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewaan import Sewaan
from src.model.traktor import Traktor


class AlatUji(AlatTani):
    """Alat konkret khusus untuk pengujian."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Menghitung biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat pemakaian."""
        return "Untuk pengujian."


def buat_daftar() -> DaftarHarga:
    """Membuat daftar harga untuk pengujian."""
    return DaftarHarga(
        [
            Traktor("TR-01", "Traktor", 150_000, 20),
            PompaAir("PA-01", "Pompa Air", 100_000, 100),
            Perontok("PR-01", "Perontok", 200_000),
        ]
    )


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_daftar_harga_menyalin_daftar_alat() -> None:
    alat = [AlatUji("A-01", "Alat", 100_000)]
    daftar = DaftarHarga(alat)

    alat.clear()

    assert daftar.biaya_semua(2) == [200_000]


def test_biaya_semua_menggunakan_polimorfisme() -> None:
    daftar = buat_daftar()

    assert daftar.biaya_semua(3) == [
        750_000,
        363_000,
        600_000,
    ]


def test_total_bila_semua_disewa() -> None:
    daftar = buat_daftar()

    assert daftar.total_bila_semua_disewa(3) == 1_713_000


def test_termurah_mengembalikan_alat_termurah() -> None:
    daftar = buat_daftar()

    assert daftar.termurah(3).kode == "PA-01"


def test_termurah_dapat_berubah_berdasarkan_durasi() -> None:
    daftar = DaftarHarga(
        [
            AlatUji("A-01", "Alat A", 100_000),
            Perontok("PR-01", "Perontok", 200_000),
        ]
    )

    assert daftar.termurah(1).kode == "A-01"
    assert daftar.termurah(3).kode == "A-01"


def test_daftar_harga_menerima_subkelas_baru() -> None:
    class Penggiling(AlatTani):
        """Alat penggiling dengan ongkos angkut."""

        def biaya_tambahan(self, _jumlah_hari: int) -> int:
            return 0

        def syarat_pemakaian(self) -> str:
            return "Untuk pengujian."

        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + 50_000

    penggiling = Penggiling("PG-01", "Penggiling Padi", 120_000)
    daftar = DaftarHarga([penggiling])

    assert daftar.biaya_semua(3) == [410_000]
    assert daftar.total_bila_semua_disewa(3) == 410_000


def test_gerobak_memenuhi_kontrak_sewaan() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)

    assert isinstance(gerobak, Sewaan)


def test_gerobak_bukan_subkelas_alat_tani() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)

    assert not isinstance(gerobak, AlatTani)


def test_daftar_harga_menerima_gerobak_dorong() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)
    daftar = DaftarHarga([gerobak])

    assert daftar.biaya_semua(3) == [150_000]
    assert daftar.termurah(3).kode == "GD-01"

