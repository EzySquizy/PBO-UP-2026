"""Pengujian penyusun laporan penghasilan pegawai."""

import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_lapangan import PegawaiLapangan
from src.model.pegawai_penyuluh import PegawaiPenyuluh
from src.model.pegawai_struktural import PegawaiStruktural
from src.model.penyusun_laporan import PenyusunLaporan


def test_penyusun_laporan_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_rekap_penghasilan_semua_pegawai() -> None:
    pegawai = [
        Pegawai("198001", "Budi", 3_000_000),
        PegawaiLapangan("198002", "Andi", 3_000_000, 50_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.rekap_penghasilan(20) == [
        ("Budi", 2_000_000),
        ("Andi", 3_000_000),
    ]


def test_penghasilan_tertinggi() -> None:
    pegawai = [
        Pegawai("198001", "Budi", 3_000_000),
        PegawaiLapangan("198002", "Andi", 3_000_000, 50_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.penghasilan_tertinggi(20).nama == "Andi"


def test_penghasilan_terendah() -> None:
    pegawai = [
        Pegawai("198001", "Budi", 3_000_000),
        PegawaiLapangan("198002", "Andi", 3_000_000, 50_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.penghasilan_terendah(20).nama == "Budi"


def test_total_penghasilan() -> None:
    pegawai = [
        Pegawai("198001", "Budi", 3_000_000),
        PegawaiLapangan("198002", "Andi", 3_000_000, 50_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.total_penghasilan(20) == 5_000_000


def test_mendukung_semua_jenis_pegawai() -> None:
    pegawai = [
        Pegawai("198001", "Budi", 3_000_000),
        PegawaiLapangan("198002", "Andi", 3_000_000, 50_000),
        PegawaiPenyuluh("198003", "Siti", 3_000_000, 2),
        PegawaiStruktural("198004", "Rudi", 3_000_000, "III"),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.total_penghasilan(20) == 9_500_000


def test_mendukung_jenis_pegawai_baru_tanpa_perubahan_kelas() -> None:
    class PegawaiKontrak(Pegawai):
        def hitung_penghasilan(self, hari_kerja: int) -> int:
            return super().hitung_penghasilan(hari_kerja) + 100_000

    pegawai = PegawaiKontrak("198005", "Dewi", 3_000_000)
    laporan = PenyusunLaporan([pegawai])

    assert laporan.rekap_penghasilan(20) == [("Dewi", 2_100_000)]
    assert laporan.penghasilan_tertinggi(20) == pegawai
    assert laporan.penghasilan_terendah(20) == pegawai
    assert laporan.total_penghasilan(20) == 2_100_000


def test_meneruskan_validasi_hari_kerja() -> None:
    laporan = PenyusunLaporan([
        Pegawai("198001", "Budi", 3_000_000),
    ])

    with pytest.raises(ValueError):
        laporan.total_penghasilan(32)
