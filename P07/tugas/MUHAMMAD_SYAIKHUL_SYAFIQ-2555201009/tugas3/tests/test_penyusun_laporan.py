
"""Pengujian PenyusunLaporan."""

import pytest

from src.model.pegawai import Pegawai
from src.model.pegawai_tetap import PegawaiTetap
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.penyusun_laporan import PenyusunLaporan


@pytest.fixture
def daftar_pegawai() -> list[Pegawai]:
    return [
        Pegawai("P001", "Andi", 100_000),
        PegawaiTetap("P002", "Budi", 100_000, 50_000),
        PegawaiHarian("P003", "Citra", 100_000, 25_000, 8),
        PegawaiKontrak("P004", "Dedi", 100_000, 20),
    ]


@pytest.fixture
def laporan() -> PenyusunLaporan:
    return PenyusunLaporan()


def test_rekap_penghasilan(
    laporan: PenyusunLaporan,
    daftar_pegawai: list[Pegawai],
) -> None:
    hasil = laporan.rekap_penghasilan(daftar_pegawai, 2)
    assert len(hasil) == 4
    assert hasil[0] == ("Andi", 200_000)


def test_rekap_memuat_semua_nama(
    laporan: PenyusunLaporan,
    daftar_pegawai: list[Pegawai],
) -> None:
    hasil = laporan.rekap_penghasilan(daftar_pegawai, 1)
    assert [item[0] for item in hasil] == [
        "Andi", "Budi", "Citra", "Dedi"
    ]


def test_penghasilan_tertinggi(
    laporan: PenyusunLaporan,
    daftar_pegawai: list[Pegawai],
) -> None:
    hasil = laporan.penghasilan_tertinggi(daftar_pegawai, 2)
    assert hasil.nama == "Citra"


def test_penghasilan_terendah(
    laporan: PenyusunLaporan,
    daftar_pegawai: list[Pegawai],
) -> None:
    hasil = laporan.penghasilan_terendah(daftar_pegawai, 2)
    assert hasil.nama == "Andi"


def test_total_penghasilan(
    laporan: PenyusunLaporan,
    daftar_pegawai: list[Pegawai],
) -> None:
    hasil = laporan.total_penghasilan(daftar_pegawai, 2)
    assert hasil == 1_100_000


def test_rekap_daftar_kosong(laporan: PenyusunLaporan) -> None:
    assert laporan.rekap_penghasilan([], 2) == []


def test_total_daftar_kosong(laporan: PenyusunLaporan) -> None:
    assert laporan.total_penghasilan([], 2) == 0


def test_tertinggi_daftar_kosong(laporan: PenyusunLaporan) -> None:
    with pytest.raises(ValueError):
        laporan.penghasilan_tertinggi([], 2)


def test_terendah_daftar_kosong(laporan: PenyusunLaporan) -> None:
    with pytest.raises(ValueError):
        laporan.penghasilan_terendah([], 2)


def test_menerima_jenis_pegawai_baru(laporan: PenyusunLaporan) -> None:
    class PegawaiMagang(Pegawai):
        def hitung_gaji(self, jumlah_hari: int) -> int:
            if jumlah_hari <= 0:
                raise ValueError("Jumlah hari harus lebih dari nol")
            return 50_000 * jumlah_hari

    pegawai_baru = PegawaiMagang("P005", "Eka", 100_000)

    hasil = laporan.rekap_penghasilan([pegawai_baru], 2)

    assert hasil == [("Eka", 100_000)]
    assert laporan.total_penghasilan([pegawai_baru], 2) == 100_000
