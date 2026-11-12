import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_teknis import PegawaiTeknis
from src.model.petugas_retribusi import PetugasRetribusi
from src.model.pegawai_magang import PegawaiMagang

def test_induk_menolak_honor_negatif() -> None:
    with pytest.raises(ValueError):
        Pegawai("P01", "Jijah", -10000)

def test_teknis_menolak_tunjangan_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiTeknis("P02", "Putri", 80000, -50000)

def test_retribusi_menolak_titik_pasar_negatif() -> None:
    with pytest.raises(ValueError):
        PetugasRetribusi("P03", "Ica", 80000, -2)

def test_magang_menolak_maksimum_hari_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiMagang("P04", "Nana", 50000, -5)

def test_induk_hitung_gaji_dasar_normal() -> None:
    p = Pegawai("P01", "Jijah", 100000)
    assert p.hitung_gaji(10) == 1000000

def test_teknis_menambah_tunjangan_komunikasi_di_akhir() -> None:
    p = PegawaiTeknis("P02", "Putri", 100000, 150000)
    # (100.000 * 5 hari) + 150.000
    assert p.hitung_gaji(5) == 650000

def test_retribusi_hitung_insentif_berdasarkan_titik() -> None:
    p = PetugasRetribusi("P03", "Ica", 100000, 3)
    # honor: (100.000 * 5) = 500.000
    # insentif: (3 titik * 15.000 * 5 hari) = 225.000
    assert p.hitung_gaji(5) == 725000

def test_magang_hitung_normal_jika_dibawah_batas() -> None:
    p = PegawaiMagang("P04", "Nana", 50000, 20)
    assert p.hitung_gaji(15) == 750000

def test_magang_memotong_masukan_jika_melebihi_batas() -> None:
    p = PegawaiMagang("P05", "Nayla", 50000, 20)
    # Walau kerja 25 hari, tetap dihitung 20 hari (20 * 50.000)
    assert p.hitung_gaji(25) == 1000000

def test_kesamaan_eq_hanya_dilihat_dari_nip() -> None:
    p1 = Pegawai("P01", "Jijah", 100000)
    p2 = PegawaiTeknis("P01", "Putri", 150000, 500000)
    assert p1 == p2

def test_eq_merespon_benar_jika_dibandingkan_objek_lain() -> None:
    p1 = Pegawai("P01", "Jijah", 100000)
    assert p1 != "P01"

def test_pegawai_berfungsi_sebagai_kunci_dict() -> None:
    p1 = Pegawai("P01", "Jijah", 100000)
    jadwal = {p1: "Shift Pagi"}
    
    # Mencari menggunakan objek baru dengan NIP yang sama
    p_cari = PetugasRetribusi("P01", "Jijah", 100000, 2)
    assert jadwal[p_cari] == "Shift Pagi"