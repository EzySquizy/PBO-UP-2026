
"""Pengujian untuk penerjemah perintah laporan."""

import pytest
from src.pegawai import Pegawai
from src.pegawai_harian import PegawaiHarian
from src.pegawai_kontrak import PegawaiKontrak
from src.pegawai_tetap import PegawaiTetap
from src.penyusun_laporan import PenyusunLaporan
from src.perintah_laporan import PerintahLaporan


@pytest.fixture
def perintah() -> PerintahLaporan:
    """Menyediakan penerjemah perintah dengan data pegawai."""
    pegawai = [
        Pegawai("P001", "Budi", 3_000_000),
        PegawaiTetap("P002", "Siti", 4_000_000, 500_000),
        PegawaiHarian("P003", "Andi", 2_000_000, 150_000),
        PegawaiKontrak("P004", "Rina", 3_500_000, 6),
    ]
    laporan = PenyusunLaporan(pegawai)
    return PerintahLaporan(laporan)


def test_perintah_kosong(perintah: PerintahLaporan) -> None:
    assert perintah.jalankan("") == (
        "Perintah kosong. Ketik 'bantuan'."
    )


def test_perintah_bantuan(perintah: PerintahLaporan) -> None:
    assert perintah.jalankan("bantuan") == PerintahLaporan.BANTUAN


def test_perintah_tanda_tanya(perintah: PerintahLaporan) -> None:
    assert perintah.jalankan("?") == PerintahLaporan.BANTUAN


def test_perintah_rekap(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("rekap 1")

    assert "Budi: Rp3.000.000" in hasil
    assert "Siti: Rp4.500.000" in hasil
    assert "Andi: Rp150.000" in hasil
    assert "Rina: Rp3.500.000" in hasil


def test_perintah_tertinggi(perintah: PerintahLaporan) -> None:
    assert perintah.jalankan("tertinggi 1") == (
        "Penghasilan tertinggi: Siti (Rp4.500.000)"
    )


def test_perintah_terendah(perintah: PerintahLaporan) -> None:
    assert perintah.jalankan("terendah 1") == (
        "Penghasilan terendah: Andi (Rp150.000)"
    )


def test_perintah_total(perintah: PerintahLaporan) -> None:
    assert perintah.jalankan("total 1") == (
        "Total penghasilan: Rp11.150.000"
    )


def test_perintah_tidak_dikenal(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("cetak 1")

    assert "tidak dikenal" in hasil


def test_perintah_tidak_dikenal_lain(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("hapus")

    assert "tidak dikenal" in hasil


def test_perintah_tidak_dikenal_dengan_argumen(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("cari Budi")

    assert "tidak dikenal" in hasil


def test_perintah_rekap_tanpa_periode(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("rekap")

    assert "tidak dikenal" in hasil


def test_perintah_rekap_periode_nol(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("rekap 0")

    assert "tidak dikenal" in hasil


def test_perintah_rekap_periode_huruf(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("rekap abc")

    assert "tidak dikenal" in hasil


def test_perintah_total_periode_negatif(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("total -1")

    assert "tidak dikenal" in hasil


def test_perintah_tertinggi_tanpa_periode(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("tertinggi")

    assert "tidak dikenal" in hasil


def test_perintah_dengan_argumen_berlebih(
    perintah: PerintahLaporan,
) -> None:
    hasil = perintah.jalankan("total 1 tambahan")

    assert "tidak dikenal" in hasil
