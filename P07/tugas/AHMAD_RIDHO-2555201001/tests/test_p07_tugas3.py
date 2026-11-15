
"""Pengujian tugas individu 3 P07."""

import pytest
from src.kepegawaian.format_data import format_data
from src.kepegawaian.pegawai import Pegawai
from src.kepegawaian.pegawai_harian import PegawaiHarian
from src.kepegawaian.pegawai_kontrak import PegawaiKontrak
from src.kepegawaian.pegawai_pns import PegawaiPNS
from src.kepegawaian.penyusun_laporan import PenyusunLaporan
from src.ui.perintah_pegawai import PenerjemahPegawai


@pytest.fixture
def daftar_pegawai() -> list[Pegawai]:
    """Menyediakan beberapa jenis pegawai untuk pengujian."""
    return [
        Pegawai("001", "Andi", 3_000_000),
        PegawaiPNS("002", "Budi", 3_000_000, 500_000),
        PegawaiHarian("003", "Cici", 1_000_000, 150_000, 20),
        PegawaiKontrak("004", "Dedi", 2_000_000, 3),
    ]


def test_rekap_penghasilan(daftar_pegawai: list[Pegawai]) -> None:
    laporan = PenyusunLaporan(daftar_pegawai)

    assert laporan.rekap_penghasilan(2) == [
        ("Andi (001)", 6_000_000),
        ("Budi (002)", 7_000_000),
        ("Cici (003)", 6_000_000),
        ("Dedi (004)", 6_000_000),
    ]


def test_penghasilan_tertinggi(daftar_pegawai: list[Pegawai]) -> None:
    laporan = PenyusunLaporan(daftar_pegawai)

    assert laporan.penghasilan_tertinggi(2) == daftar_pegawai[1]


def test_penghasilan_terendah(daftar_pegawai: list[Pegawai]) -> None:
    laporan = PenyusunLaporan(daftar_pegawai)

    assert laporan.penghasilan_terendah(2) == daftar_pegawai[0]


def test_total_penghasilan(daftar_pegawai: list[Pegawai]) -> None:
    laporan = PenyusunLaporan(daftar_pegawai)

    assert laporan.total_penghasilan(2) == 25_000_000


def test_daftar_pegawai_kosong_ditolak() -> None:
    with pytest.raises(ValueError, match="daftar pegawai"):
        PenyusunLaporan([])

def test_polimorfisme_jenis_pegawai_baru() -> None:
    class PegawaiMagang(Pegawai):
        """Pegawai magang dengan penghasilan khusus."""

        def hitung_penghasilan(self, jumlah_bulan: int) -> int:
            if jumlah_bulan <= 0:
                raise ValueError("jumlah bulan harus lebih dari nol")
            return 500_000 * jumlah_bulan

    pegawai = [
        Pegawai("001", "Andi", 3_000_000),
        PegawaiMagang("005", "Eko", 500_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.total_penghasilan(2) == 7_000_000

def test_perintah_bantuan(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("bantuan")

    assert "daftar" in hasil
    assert "tertinggi" in hasil
    assert "terendah" in hasil
    assert "total" in hasil

def test_perintah_tertinggi(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("tertinggi 2")

    assert hasil == "Penghasilan tertinggi: Budi (002)"

def test_perintah_terendah(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("terendah 2")

    assert hasil == "Penghasilan terendah: Andi (001)"

def test_perintah_total(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("total 2")

    assert hasil == "Total penghasilan: Rp25.000.000"

def test_perintah_kosong_ditolak(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("")

    assert hasil == "Perintah tidak boleh kosong."

def test_perintah_tidak_dikenal(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("hapus")

    assert hasil == "Perintah 'hapus' tidak dikenali."

def test_perintah_keluar_tidak_dikenal(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("keluar")

    assert hasil == "Perintah 'keluar' tidak dikenali."

def test_perintah_cetak_tidak_dikenal(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("cetak")

    assert hasil == "Perintah 'cetak' tidak dikenali."

def test_perintah_daftar_tanpa_bulan_ditolak(
    daftar_pegawai: list[Pegawai],
) -> None:
    penerjemah = PenerjemahPegawai(daftar_pegawai)

    hasil = penerjemah.terjemahkan("daftar")

    assert hasil == "Perintah 'daftar' tidak dikenali."

def test_format_data_integer() -> None:
    assert format_data(100) == "Bilangan bulat: 100"


def test_format_data_float() -> None:
    assert format_data(10.5) == "Bilangan desimal: 10.5"


def test_format_data_string() -> None:
    assert format_data("Ridho") == "Teks: Ridho"
