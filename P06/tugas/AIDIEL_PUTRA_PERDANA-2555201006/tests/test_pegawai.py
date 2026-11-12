import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_struktural import PegawaiStruktural
from src.model.pegawai_lapangan import PegawaiLapangan
from src.model.pegawai_penyuluh import PegawaiPenyuluh

def test_pegawai_menolak_gaji_negatif() -> None:
    with pytest.raises(ValueError):
        Pegawai("101", "Aidiel", -50000)

def test_struktural_menolak_tunjangan_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiStruktural("102", "Putra", 100000, -10000)

def test_lapangan_menolak_jarak_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiLapangan("103", "Perdana", 100000, -5)

def test_penyuluh_menolak_minimum_hari_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiPenyuluh("104", "Aidiel Putra Perdana", 100000, -10)

def test_pegawai_induk_hitung_normal() -> None:
    p = Pegawai("101", "Aidiel", 100000)
    assert p.hitung_penghasilan(5) == 500000

def test_struktural_menambah_komponen_tunjangan() -> None:
    p = PegawaiStruktural("102", "putra", 100000, 250000)
    assert p.hitung_penghasilan(5) == 750000

def test_lapangan_menghitung_dari_atribut_sendiri() -> None:
    p = PegawaiLapangan("103", "perdana", 100000, 10)
    assert p.hitung_penghasilan(5) == 600000

def test_penyuluh_mengubah_masukan_kurang_dari_minimum() -> None:
    p = PegawaiPenyuluh("104", "Aidiel Putra Perdana", 100000, 15)
    assert p.hitung_penghasilan(10) == 1500000

def test_penyuluh_mengubah_masukan_lebih_dari_minimum() -> None:
    p = PegawaiPenyuluh("105", "Joko Widodo", 100000, 15)
    assert p.hitung_penghasilan(20) == 2000000

def test_pegawai_eq_berdasarkan_nip() -> None:
    p1 = Pegawai("101", "Aidiel", 100000)
    p2 = PegawaiStruktural("101", "Nama Lain", 120000, 500000)
    assert p1 == p2

def test_pegawai_dibandingkan_dengan_tipe_lain() -> None:
    p1 = Pegawai("101", "Aidiel", 100000)
    assert p1 != "101"

def test_pegawai_sebagai_kunci_dict() -> None:
    p1 = Pegawai("101", "Aidiel", 100000)
    catatan_penugasan = {p1: "Kecamatan Bangkinang"}
    
    p_cari = PegawaiLapangan("101", "Beda Nama", 50000, 10)
    assert catatan_penugasan[p_cari] == "Kecamatan Bangkinang"