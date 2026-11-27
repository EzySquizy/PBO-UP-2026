
"""Pengujian untuk kelas PenyusunLaporan."""

import pytest
from src.pegawai import Pegawai
from src.pegawai_harian import PegawaiHarian
from src.pegawai_kontrak import PegawaiKontrak
from src.pegawai_tetap import PegawaiTetap
from src.penyusun_laporan import PenyusunLaporan


@pytest.fixture
def daftar_pegawai() -> list[Pegawai]:
    """Menyediakan beberapa jenis pegawai untuk pengujian."""
    return [
        Pegawai("P001", "Budi", 3_000_000),
        PegawaiTetap("P002", "Siti", 4_000_000, 500_000),
        PegawaiHarian("P003", "Andi", 2_000_000, 150_000),
        PegawaiKontrak("P004", "Rina", 3_500_000, 6),
    ]


@pytest.fixture
def laporan(daftar_pegawai: list[Pegawai]) -> PenyusunLaporan:
    """Menyediakan objek laporan."""
    return PenyusunLaporan(daftar_pegawai)


def test_laporan_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_rekap_penghasilan_satu_periode(
    laporan: PenyusunLaporan,
) -> None:
    assert laporan.rekap_penghasilan(1) == [
        ("Budi", 3_000_000),
        ("Siti", 4_500_000),
        ("Andi", 150_000),
        ("Rina", 3_500_000),
    ]


def test_rekap_penghasilan_dua_periode(
    laporan: PenyusunLaporan,
) -> None:
    assert laporan.rekap_penghasilan(2) == [
        ("Budi", 6_000_000),
        ("Siti", 9_000_000),
        ("Andi", 300_000),
        ("Rina", 7_000_000),
    ]


def test_penghasilan_tertinggi(laporan: PenyusunLaporan) -> None:
    assert laporan.penghasilan_tertinggi(1).nama == "Siti"


def test_penghasilan_terendah(laporan: PenyusunLaporan) -> None:
    assert laporan.penghasilan_terendah(1).nama == "Andi"


def test_total_penghasilan_satu_periode(
    laporan: PenyusunLaporan,
) -> None:
    assert laporan.total_penghasilan(1) == 11_150_000


def test_total_penghasilan_dua_periode(
    laporan: PenyusunLaporan,
) -> None:
    assert laporan.total_penghasilan(2) == 22_300_000


def test_rekap_penghasilan_mendukung_pegawai_keempat() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai tambahan yang dibuat khusus dalam pengujian."""

        def hitung_penghasilan(self, jumlah_periode: int) -> int:
            return super().hitung_penghasilan(jumlah_periode) + 250_000

    pegawai = [
        Pegawai("P001", "Budi", 3_000_000),
        PegawaiMagang("P005", "Dewi", 2_000_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.rekap_penghasilan(1) == [
        ("Budi", 3_000_000),
        ("Dewi", 2_250_000),
    ]


def test_penghasilan_tertinggi_mendukung_pegawai_keempat() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai tambahan untuk menguji polymorphism."""

        def hitung_penghasilan(self, jumlah_periode: int) -> int:
            return super().hitung_penghasilan(jumlah_periode) + 500_000

    pegawai = [
        Pegawai("P001", "Budi", 3_000_000),
        PegawaiMagang("P005", "Dewi", 2_000_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.penghasilan_tertinggi(1).nama == "Budi"


def test_penghasilan_terendah_mendukung_pegawai_keempat() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai tambahan untuk menguji polymorphism."""

        def hitung_penghasilan(self, jumlah_periode: int) -> int:
            return super().hitung_penghasilan(jumlah_periode) + 100_000

    pegawai = [
        Pegawai("P001", "Budi", 3_000_000),
        PegawaiMagang("P005", "Dewi", 2_000_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.penghasilan_terendah(1).nama == "Dewi"


def test_total_penghasilan_mendukung_pegawai_keempat() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai tambahan untuk menguji polymorphism."""

        def hitung_penghasilan(self, jumlah_periode: int) -> int:
            return super().hitung_penghasilan(jumlah_periode) + 250_000

    pegawai = [
        Pegawai("P001", "Budi", 3_000_000),
        PegawaiMagang("P005", "Dewi", 2_000_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.total_penghasilan(1) == 5_250_000


def test_rekap_penghasilan_mempertahankan_daftar_asli(
    daftar_pegawai: list[Pegawai],
) -> None:
    laporan = PenyusunLaporan(daftar_pegawai)
    daftar_pegawai.clear()

    assert laporan.total_penghasilan(1) == 11_150_000


def test_rekap_penghasilan_tiga_periode(
    laporan: PenyusunLaporan,
) -> None:
    assert laporan.total_penghasilan(3) == 33_450_000
