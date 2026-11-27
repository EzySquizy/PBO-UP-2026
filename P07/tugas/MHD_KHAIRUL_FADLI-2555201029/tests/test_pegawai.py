
"""Pengujian hierarki Pegawai untuk Tugas 2 P06."""

import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_lapangan import PegawaiLapangan
from src.model.pegawai_penyuluh import PegawaiPenyuluh
from src.model.pegawai_struktural import PegawaiStruktural


def test_pegawai_dapat_dibuat() -> None:
    pegawai = Pegawai("198001", "Budi", 3_000_000)

    assert pegawai.nip == "198001"
    assert pegawai.nama == "Budi"
    assert pegawai.gaji_pokok == 3_000_000


def test_penghasilan_pegawai_dasar() -> None:
    pegawai = Pegawai("198001", "Budi", 3_000_000)

    assert pegawai.hitung_penghasilan(20) == 2_000_000


def test_pegawai_lapangan_menambah_transport() -> None:
    pegawai = PegawaiLapangan("198002", "Andi", 3_000_000, 50_000)

    assert pegawai.hitung_penghasilan(20) == 3_000_000


def test_pegawai_penyuluh_menghitung_honor_kegiatan() -> None:
    pegawai = PegawaiPenyuluh("198003", "Siti", 3_000_000, 2)

    assert pegawai.hitung_penghasilan(20) == 2_300_000


def test_pegawai_struktural_menambah_hari_kerja() -> None:
    pegawai = PegawaiStruktural("198004", "Rudi", 3_000_000, "III")

    assert pegawai.hitung_penghasilan(29) == 3_100_000


def test_pegawai_struktural_memiliki_tingkat_jabatan() -> None:
    pegawai = PegawaiStruktural("198004", "Rudi", 3_000_000, "III")

    assert pegawai.tingkat_jabatan == "III"


def test_str_pegawai() -> None:
    pegawai = Pegawai("198001", "Budi", 3_000_000)

    assert str(pegawai) == "Budi (198001)"


def test_repr_pegawai() -> None:
    pegawai = Pegawai("198001", "Budi", 3_000_000)

    assert repr(pegawai) == (
        "Pegawai(nip='198001', nama='Budi', gaji_pokok=3000000)"
    )


def test_dua_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pegawai1 = Pegawai("198001", "Budi", 3_000_000)
    pegawai2 = Pegawai("198001", "Budi Santoso", 3_500_000)

    assert pegawai1 == pegawai2


def test_pegawai_dengan_nip_berbeda_tidak_sama() -> None:
    pegawai1 = Pegawai("198001", "Budi", 3_000_000)
    pegawai2 = Pegawai("198002", "Andi", 3_000_000)

    assert pegawai1 != pegawai2


def test_pegawai_dapat_digunakan_sebagai_kunci_dict() -> None:
    pegawai = Pegawai("198001", "Budi", 3_000_000)
    data_pegawai = {pegawai: "Pegawai tetap"}

    assert data_pegawai[pegawai] == "Pegawai tetap"


def test_pegawai_dapat_dimasukkan_ke_set() -> None:
    pegawai1 = Pegawai("198001", "Budi", 3_000_000)
    pegawai2 = Pegawai("198001", "Budi Santoso", 3_500_000)

    data_pegawai = {pegawai1, pegawai2}

    assert len(data_pegawai) == 1


def test_pegawai_menolak_nip_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Budi", 3_000_000)


def test_pegawai_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("198001", "", 3_000_000)


def test_pegawai_menolak_gaji_nol() -> None:
    with pytest.raises(ValueError):
        Pegawai("198001", "Budi", 0)


def test_pegawai_lapangan_menolak_transport_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiLapangan("198002", "Andi", 3_000_000, -50_000)


def test_pegawai_penyuluh_menolak_kegiatan_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiPenyuluh("198003", "Siti", 3_000_000, -1)


def test_pegawai_struktural_menolak_jabatan_kosong() -> None:
    with pytest.raises(ValueError):
        PegawaiStruktural("198004", "Rudi", 3_000_000, "")


def test_pegawai_menolak_hari_kerja_di_luar_batas() -> None:
    pegawai = Pegawai("198001", "Budi", 3_000_000)

    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(32)
