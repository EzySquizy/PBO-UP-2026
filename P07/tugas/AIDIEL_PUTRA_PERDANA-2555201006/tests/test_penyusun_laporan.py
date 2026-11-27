from __future__ import annotations

import pytest

from src.format_nilai import format_nilai
from src.model.pegawai import Pegawai
from src.model.pegawai_lapangan import PegawaiLapangan
from src.model.pegawai_penyuluh import PegawaiPenyuluh
from src.model.pegawai_struktural import PegawaiStruktural
from src.model.penyusun_laporan import PenyusunLaporan
from src.ui.perintah_konsol import PerintahKonsol


def _buat_tim_standar() -> list[Pegawai]:
    return [
        PegawaiLapangan("P-01", "Budi", gaji_harian=100_000, jarak_km=10),     # 120.000/hari
        PegawaiPenyuluh("P-02", "Sari", gaji_harian=110_000, minimum_hari=5),  # min 5 hari
        PegawaiStruktural("P-03", "Rudi", gaji_harian=120_000, tunjangan_jabatan=300_000),
    ]


def test_penyusun_laporan_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_penyusun_laporan_menolak_hari_negatif() -> None:
    laporan = PenyusunLaporan(_buat_tim_standar())
    with pytest.raises(ValueError):
        laporan.total(-1)


def test_salinan_daftar_tidak_bocor_ke_luar() -> None:
    sumber = _buat_tim_standar()
    laporan = PenyusunLaporan(sumber)
    sumber.clear()
    assert laporan.jumlah_pegawai == 3


def test_rekap_penghasilan_seluruh_pegawai() -> None:
    laporan = PenyusunLaporan(_buat_tim_standar())
    hasil = laporan.rekap_penghasilan(2)
    assert len(hasil) == 3
    assert hasil[0][1] == 240_000
    assert hasil[1][1] == 550_000   # minimum_hari=5 -> 5 * 110.000
    assert hasil[2][1] == 540_000   # 2 * 120.000 + 300.000


def test_total_penghasilan_polimorfik() -> None:
    laporan = PenyusunLaporan(_buat_tim_standar())
    assert laporan.total(2) == 240_000 + 550_000 + 540_000


def test_tertinggi_dan_terendah_berubah_mengikuti_hari() -> None:
    laporan = PenyusunLaporan(_buat_tim_standar())

    # Hari ke-1: Penyuluh (550.000) tertinggi, Lapangan (120.000) terendah
    assert laporan.tertinggi(1)._nip == "P-02"
    assert laporan.terendah(1)._nip == "P-01"

    # Hari ke-10: Struktural (1.500.000) tertinggi, Penyuluh (1.100.000) terendah
    assert laporan.tertinggi(10)._nip == "P-03"
    assert laporan.terendah(10)._nip == "P-02"


def test_jenis_pegawai_keempat_di_badan_uji_tanpa_ubah_penyusun_laporan() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai keempat yang dibuat khusus di dalam fungsi uji."""

        def hitung_penghasilan(self, jumlah_hari: int) -> int:
            return super().hitung_penghasilan(jumlah_hari) + 15_000

    tim = [*_buat_tim_standar(), PegawaiMagang("P-04", "Dina", gaji_harian=80_000)]
    laporan = PenyusunLaporan(tim)

    assert laporan.jumlah_pegawai == 4
    assert laporan.total(1) == 120_000 + 550_000 + 420_000 + 95_000


def test_singledispatch_format_nilai_int_float_list_dan_fallback() -> None:
    assert format_nilai(150_000) == "Rp150.000"
    assert format_nilai(0.825) == "82.5%"
    assert format_nilai([100_000, 0.5]) == "Rp100.000, 50.0%"
    assert format_nilai("kampar") == "kampar"


def test_perintah_konsol_bantuan_dan_rekap() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "Perintah tersedia:" in konsol.jalankan("bantuan")
    assert "Perintah tersedia:" in konsol.jalankan("?")
    assert "Rp240.000" in konsol.jalankan("rekap 2")


def test_perintah_konsol_tertinggi_terendah_dan_total() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "Tertinggi (1 hari)" in konsol.jalankan("tertinggi 1")
    assert "Terendah (1 hari)" in konsol.jalankan("terendah 1")
    assert "Total (2 hari): Rp1.330.000" == konsol.jalankan("total 2")


def test_perintah_asing_1_string_acak() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "tidak dikenal" in konsol.jalankan("ngawur")


def test_perintah_asing_2_input_kosong_atau_spasi() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "Perintah kosong" in konsol.jalankan("   ")


def test_perintah_asing_3_hari_bukan_angka() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "tidak dikenal" in konsol.jalankan("total lima")


def test_perintah_asing_4_hari_negatif() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "tidak dikenal" in konsol.jalankan("rekap -3")


def test_perintah_asing_5_kelebihan_argumen() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "tidak dikenal" in konsol.jalankan("total 2 3")


def test_perintah_asing_6_kurang_argumen() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "tidak dikenal" in konsol.jalankan("tertinggi")


def test_perintah_asing_7_kalimat_panjang_tak_dikenal() -> None:
    konsol = PerintahKonsol(PenyusunLaporan(_buat_tim_standar()))
    assert "tidak dikenal" in konsol.jalankan("hapus semua data pegawai sekarang")