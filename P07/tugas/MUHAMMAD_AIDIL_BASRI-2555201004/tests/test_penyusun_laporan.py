"""Pengujian penyusun laporan penghasilan pegawai."""

import pytest

from src.model.pegawai import (
    Pegawai,
    PegawaiHarian,
    PegawaiProduksi,
    PegawaiTetap,
)
from src.model.penyusun_laporan import PenyusunLaporan


def buat_daftar_pegawai() -> list[Pegawai]:
    return [
        Pegawai("001", "Andi", 100_000),
        PegawaiTetap("002", "Budi", 100_000, 10_000),
        PegawaiProduksi("003", "Citra", 100_000, 2, 5_000),
        PegawaiHarian("004", "Dedi", 100_000, 1),
    ]


def test_rekap_penghasilan_semua_jenis_pegawai() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.rekap_penghasilan(2) == [
        ("Andi", 200_000),
        ("Budi", 220_000),
        ("Citra", 220_000),
        ("Dedi", 100_000),
    ]


def test_penghasilan_tertinggi() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.penghasilan_tertinggi(2) == ("Budi", 220_000)


def test_penghasilan_terendah() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.penghasilan_terendah(2) == ("Dedi", 100_000)


def test_total_penghasilan() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.total_penghasilan(2) == 740_000


def test_daftar_asli_tidak_memengaruhi_laporan() -> None:
    pegawai = buat_daftar_pegawai()
    laporan = PenyusunLaporan(pegawai)
    pegawai.clear()
    assert len(laporan.rekap_penghasilan(2)) == 4


def test_pegawai_jenis_keempat_tanpa_mengubah_penyusun() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai baru yang dibuat khusus dalam pengujian."""

        def hitung_penghasilan(self, jumlah_hari: int) -> int:
            return super().hitung_penghasilan(jumlah_hari) + 25_000

    magang = PegawaiMagang("005", "Eka", 100_000)
    laporan = PenyusunLaporan([magang])
    assert laporan.rekap_penghasilan(2) == [("Eka", 225_000)]


def test_satu_pegawai_sebagai_penghasilan_tertinggi() -> None:
    laporan = PenyusunLaporan([Pegawai("006", "Fani", 80_000)])
    assert laporan.penghasilan_tertinggi(2) == ("Fani", 160_000)


def test_satu_pegawai_sebagai_penghasilan_terendah() -> None:
    laporan = PenyusunLaporan([Pegawai("007", "Gita", 80_000)])
    assert laporan.penghasilan_terendah(2) == ("Gita", 160_000)


def test_daftar_pegawai_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Andi", 100_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "   ", 100_000)


def test_upah_harian_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "Andi", 0)


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("002", "Budi", 100_000, -1)


def test_unit_produksi_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiProduksi("003", "Citra", 100_000, 0, 5_000)


def test_upah_per_unit_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiProduksi("003", "Citra", 100_000, 2, 0)


def test_hari_tidak_hadir_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("004", "Dedi", 100_000, -1)


def test_jumlah_hari_nol_ditolak() -> None:
    laporan = PenyusunLaporan([Pegawai("001", "Andi", 100_000)])
    with pytest.raises(ValueError):
        laporan.rekap_penghasilan(0)


def test_jumlah_hari_negatif_ditolak() -> None:
    laporan = PenyusunLaporan([Pegawai("001", "Andi", 100_000)])
    with pytest.raises(ValueError):
        laporan.total_penghasilan(-1)


