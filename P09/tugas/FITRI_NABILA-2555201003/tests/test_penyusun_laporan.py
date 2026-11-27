
"""Pengujian untuk kelas PenyusunLaporan."""

import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_magang import PegawaiMagang
from src.model.pegawai_teknis import PegawaiTeknis
from src.model.penyusun_laporan import PenyusunLaporan
from src.model.petugas_retribusi import PetugasRetribusi


def contoh_pegawai() -> list[Pegawai]:
    return [
        PegawaiTeknis("P01", "Putri", 100_000, 150_000),
        PegawaiMagang("P02", "Nana", 50_000, 20),
        PetugasRetribusi("P03", "Ica", 100_000, 3),
    ]


def test_laporan_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_rekap_penghasilan_semua_pegawai() -> None:
    laporan = PenyusunLaporan(contoh_pegawai())
    hasil = laporan.rekap_penghasilan(5)

    assert len(hasil) == 3
    assert hasil[0][1] == 650_000
    assert hasil[1][1] == 250_000
    assert hasil[2][1] == 725_000


def test_penghasilan_tertinggi() -> None:
    laporan = PenyusunLaporan(contoh_pegawai())

    assert laporan.tertinggi(5) == PetugasRetribusi(
        "P03", "Ica", 100_000, 3
    )


def test_penghasilan_terendah() -> None:
    laporan = PenyusunLaporan(contoh_pegawai())

    assert laporan.terendah(5) == PegawaiMagang(
        "P02", "Nana", 50_000, 20
    )


def test_total_penghasilan_semua_pegawai() -> None:
    laporan = PenyusunLaporan(contoh_pegawai())

    assert laporan.total(5) == 1_625_000


def test_laporan_menggunakan_salinan_daftar() -> None:
    daftar = contoh_pegawai()
    laporan = PenyusunLaporan(daftar)

    daftar.clear()

    assert len(laporan.rekap_penghasilan(5)) == 3


def test_pegawai_jenis_baru_tetap_dapat_diproses() -> None:
    class PegawaiLepas(Pegawai):
        """Jenis pegawai baru untuk menguji polimorfisme."""

        def hitung_gaji(self, jumlah_hari: int) -> int:
            return super().hitung_gaji(jumlah_hari) + 25_000

    daftar = [
        *contoh_pegawai(),
        PegawaiLepas("P04", "Budi", 100_000),
    ]
    laporan = PenyusunLaporan(daftar)

    assert len(laporan.rekap_penghasilan(1)) == 4
    assert laporan.total(1) == 570_000
    assert laporan.tertinggi(1) == PegawaiTeknis(
        "P01", "Putri", 100_000, 150_000
    )
