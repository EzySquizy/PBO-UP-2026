
"""Pengujian penerjemah perintah laporan."""

import pytest

from src.model.pegawai import Pegawai
from src.model.penyusun_laporan import PenyusunLaporan
from src.ui.perintah_laporan import PerintahLaporan


@pytest.fixture
def perintah() -> PerintahLaporan:
    daftar: list[Pegawai] = [
        Pegawai("P001", "Andi", 100_000),
        Pegawai("P002", "Budi", 150_000),
    ]
    return PerintahLaporan(daftar, PenyusunLaporan())


def test_perintah_bantuan(perintah: PerintahLaporan) -> None:
    assert "Perintah tersedia" in perintah.jalankan("bantuan")


def test_perintah_tanda_tanya(perintah: PerintahLaporan) -> None:
    assert "Perintah tersedia" in perintah.jalankan("?")


def test_perintah_kosong(perintah: PerintahLaporan) -> None:
    assert "Perintah kosong" in perintah.jalankan("")


def test_perintah_rekap(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("rekap 2")
    assert "Andi" in hasil
    assert "Budi" in hasil


def test_perintah_tertinggi(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("tertinggi 2")
    assert "Budi" in hasil


def test_perintah_terendah(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("terendah 2")
    assert "Andi" in hasil


def test_perintah_total(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("total 2")
    assert "Total penghasilan" in hasil


def test_perintah_asing_cetak(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("cetak 2")


def test_perintah_asing_hapus(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("hapus 2")


def test_perintah_asing_simpan(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("simpan 2")


def test_perintah_asing_keluar(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("keluar")


def test_perintah_asing_edit(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("edit data")


def test_rekap_hari_bukan_angka(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("rekap abc")


def test_rekap_parameter_kurang(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("rekap")


def test_rekap_parameter_lebih(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("rekap 2 3")
