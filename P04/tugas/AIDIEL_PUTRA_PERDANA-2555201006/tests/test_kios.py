"""Pengujian Tugas 1 Individu: Kelas Kios."""

import pytest
from src.model.kios import Kios

def test_kios_dapat_dibuat_dan_ambil_data() -> None:
    kios = Kios("GUL", "Gula Pasir", 14000)
    assert kios.kode == "GUL"
    assert kios.nama == "Gula Pasir"
    assert kios.modal == 14000

def test_hitung_harga_jual_memakai_persen_laba() -> None:
    kios = Kios("MYK", "Minyak Goreng", 20000)
    # Laba 15% dari 20.000 = 3.000. Jual = 23.000
    assert kios.hitung_harga_jual() == 23000

def test_daftar_tampil_memakai_f_string_rapi() -> None:
    kios = Kios("BRS", "Beras Solok", 15000)
    hasil = kios.daftar_tampil()
    # Memastikan padding string-nya bekerja
    assert "[BRS  ]" in hasil
    assert "Beras Solok    " in hasil

def test_static_method_harga_masuk_akal() -> None:
    assert Kios.harga_masuk_akal(25000) is True
    assert Kios.harga_masuk_akal(-1000) is False
    assert Kios.harga_masuk_akal(2_000_000) is False

def test_class_method_dari_baris_pendataan() -> None:
    baris = "TLR;Telur Ayam;2000"
    kios = Kios.dari_baris_pendataan(baris)
    assert kios.kode == "TLR"
    assert kios.nama == "Telur Ayam"
    assert kios.modal == 2000

def test_pencacah_bertambah_dengan_pola_selisih() -> None:
    awal = Kios.total_produk_terdaftar()
    
    _ = Kios("A01", "Beras A", 10000)
    _ = Kios("A02", "Beras B", 12000)
    
    assert Kios.total_produk_terdaftar() == awal + 2

def test_tolak_kode_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("   ", "Beras", 10000)

def test_tolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("BRS", "   ", 10000)

def test_tolak_modal_nol_atau_minus() -> None:
    with pytest.raises(ValueError):
        Kios("BRS", "Beras", -5000)

def test_tolak_modal_melewati_batas_maksimum() -> None:
    with pytest.raises(ValueError):
        Kios("BRS", "Beras", 2_000_000)

def test_tolak_baris_pendataan_kurang_dari_tiga_bagian() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_pendataan("BRS;Beras Solok")

def test_tolak_baris_pendataan_harga_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_pendataan("BRS;Beras Solok;Lima Belas Ribu")