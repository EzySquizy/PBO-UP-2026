"""Pengujian untuk pewarisan kelas Pegawai."""

import pytest
from src.pegawai import Pegawai
from src.pegawai_harian import PegawaiHarian
from src.pegawai_kontrak import PegawaiKontrak
from src.pegawai_tetap import PegawaiTetap

GAJI_TETAP_DENGAN_TUNJANGAN = 4_500_000
PENGHASILAN_HARIAN = 3_000_000
PENGHASILAN_KONTRAK = 21_000_000
PENGHASILAN_DASAR = 6_000_000


def test_penghasilan_pegawai_tetap() -> None:
    pegawai = PegawaiTetap("001", "Andi", 4_000_000, 500_000)
    assert pegawai.hitung_penghasilan(1) == GAJI_TETAP_DENGAN_TUNJANGAN


def test_penghasilan_pegawai_harian() -> None:
    pegawai = PegawaiHarian("002", "Budi", 3_000_000, 150_000)
    assert pegawai.hitung_penghasilan(20) == PENGHASILAN_HARIAN


def test_penghasilan_pegawai_kontrak() -> None:
    pegawai = PegawaiKontrak("003", "Citra", 3_500_000, 6)
    assert pegawai.hitung_penghasilan(6) == PENGHASILAN_KONTRAK


def test_penghasilan_dasar_pegawai() -> None:
    pegawai = Pegawai("004", "Doni", 3_000_000)
    assert pegawai.hitung_penghasilan(2) == PENGHASILAN_DASAR


def test_str_pegawai() -> None:
    pegawai = Pegawai("005", "Eka", 3_000_000)
    assert str(pegawai) == "005 - Eka"


def test_repr_pegawai() -> None:
    pegawai = Pegawai("006", "Fani", 3_000_000)
    assert "Pegawai(" in repr(pegawai)
    assert "006" in repr(pegawai)


def test_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pertama = Pegawai("007", "Gani", 3_000_000)
    kedua = Pegawai("007", "Hani", 4_000_000)
    assert pertama == kedua


def test_pegawai_dengan_nip_berbeda_tidak_sama() -> None:
    pertama = Pegawai("008", "Iwan", 3_000_000)
    kedua = Pegawai("009", "Joko", 3_000_000)
    assert pertama != kedua


def test_pegawai_dapat_digunakan_sebagai_key_dictionary() -> None:
    pegawai = Pegawai("010", "Kiki", 3_000_000)
    data = {pegawai: "Bagian Administrasi"}
    assert data[pegawai] == "Bagian Administrasi"


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Lina", 3_000_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("011", " ", 3_000_000)


def test_gaji_pokok_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("012", "Mira", 0)


def test_tunjangan_minus_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("013", "Nina", 3_000_000, -100_000)


def test_upah_harian_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("014", "Oki", 3_000_000, 0)


def test_lama_kontrak_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiKontrak("015", "Pia", 3_000_000, 0)


def test_jumlah_periode_nol_ditolak_oleh_pegawai() -> None:
    pegawai = Pegawai("016", "Qori", 3_000_000)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(0)


def test_jumlah_hari_nol_ditolak_oleh_pegawai_harian() -> None:
    pegawai = PegawaiHarian("017", "Rian", 3_000_000, 150_000)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(0)

def test_penghasilan_pegawai_kontrak_tidak_melebihi_lama_kontrak() -> None:
    pegawai = PegawaiKontrak(
        "198004", "Dedi", 3_500_000, 3
    )

    hasil_yang_diharapkan = 10_500_000
    assert pegawai.hitung_penghasilan(5) == hasil_yang_diharapkan
