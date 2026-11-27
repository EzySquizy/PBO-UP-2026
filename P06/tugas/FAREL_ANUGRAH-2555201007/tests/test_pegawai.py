"""Pengujian hierarki pegawai."""

import pytest
from src.model.pegawai import (
    Pegawai,
    PegawaiHarian,
    PegawaiKontrak,
    PegawaiTetap,
)


def test_pegawai_tetap_merupakan_turunan_pegawai() -> None:
    pegawai = PegawaiTetap("P001", "Andi", 2_200_000, 220_000)
    assert isinstance(pegawai, Pegawai)

def test_pegawai_harian_merupakan_turunan_pegawai() -> None:
    pegawai = PegawaiHarian("P002", "Budi", 25_000, 160)
    assert isinstance(pegawai, Pegawai)

def test_pegawai_kontrak_merupakan_turunan_pegawai() -> None:
    pegawai = PegawaiKontrak("P003", "Citra", 2_200_000)
    assert isinstance(pegawai, Pegawai)

def test_pegawai_menyimpan_identitas() -> None:
    pegawai = Pegawai("P001", "Andi", 2_200_000)
    assert pegawai.nip == "P001"
    assert pegawai.nama == "Andi"
    assert pegawai.gaji_pokok == 2_200_000

def test_penghasilan_pegawai_induk() -> None:
    pegawai = Pegawai("P001", "Andi", 2_200_000)
    assert pegawai.hitung_penghasilan() == 2_200_000

def test_pegawai_tetap_memiliki_tunjangan() -> None:
    pegawai = PegawaiTetap("P001", "Andi", 2_200_000, 220_000)
    assert pegawai.tunjangan_jabatan == 220_000

def test_penghasilan_pegawai_tetap() -> None:
    pegawai = PegawaiTetap("P001", "Andi", 2_200_000, 220_000)
    assert pegawai.hitung_penghasilan() == 2_420_000

def test_penghasilan_pegawai_tetap_setengah_bulan() -> None:
    pegawai = PegawaiTetap("P001", "Andi", 2_200_000, 220_000)
    assert pegawai.hitung_penghasilan(11) == 1_210_000

def test_pegawai_harian_memiliki_tarif_dan_jam() -> None:
    pegawai = PegawaiHarian("P002", "Budi", 25_000, 160)
    assert pegawai.tarif_per_jam == 25_000
    assert pegawai.jam_kerja_bulanan == 160

def test_penghasilan_pegawai_harian() -> None:
    pegawai = PegawaiHarian("P002", "Budi", 25_000, 160)
    assert pegawai.hitung_penghasilan() == 4_000_000

def test_penghasilan_pegawai_harian_setengah_bulan() -> None:
    pegawai = PegawaiHarian("P002", "Budi", 25_000, 160)
    assert pegawai.hitung_penghasilan(11) == 2_000_000

def test_penghasilan_pegawai_kontrak() -> None:
    pegawai = PegawaiKontrak("P003", "Citra", 2_200_000)
    assert pegawai.hitung_penghasilan() == 2_200_000

def test_pegawai_kontrak_membatasi_hari_kerja() -> None:
    pegawai = PegawaiKontrak("P003", "Citra", 2_200_000)
    assert pegawai.hitung_penghasilan(30) == 2_200_000

def test_penghasilan_kontrak_setengah_bulan() -> None:
    pegawai = PegawaiKontrak("P003", "Citra", 2_200_000)
    assert pegawai.hitung_penghasilan(11) == 1_100_000

def test_penghasilan_nol_hari() -> None:
    pegawai = Pegawai("P001", "Andi", 2_200_000)
    assert pegawai.hitung_penghasilan(0) == 0

def test_str_pegawai() -> None:
    pegawai = Pegawai("P001", "Andi", 2_200_000)
    assert str(pegawai) == "[P001] Andi"

def test_repr_pegawai_tetap() -> None:
    pegawai = PegawaiTetap("P001", "Andi", 2_200_000, 220_000)
    assert "PegawaiTetap" in repr(pegawai)

def test_dua_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pertama = Pegawai("P001", "Andi", 2_200_000)
    kedua = Pegawai("P001", "Budi", 3_000_000)
    assert pertama == kedua

def test_pegawai_berbeda_nip_tidak_sama() -> None:
    pertama = Pegawai("P001", "Andi", 2_200_000)
    kedua = Pegawai("P002", "Andi", 2_200_000)
    assert pertama != kedua

def test_pegawai_dapat_digunakan_sebagai_kunci_dict() -> None:
    pegawai = Pegawai("P001", "Andi", 2_200_000)
    data = {pegawai: "Bagian Administrasi"}
    assert data[pegawai] == "Bagian Administrasi"

def test_pegawai_lintas_subkelas_dengan_nip_sama() -> None:
    tetap = PegawaiTetap("P001", "Andi", 2_200_000, 220_000)
    kontrak = PegawaiKontrak("P001", "Budi", 2_000_000)
    assert tetap == kontrak

def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Andi", 2_200_000)

def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("P001", "", 2_200_000)

def test_gaji_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("P001", "Andi", -100)

def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("P001", "Andi", 2_200_000, -100)

def test_tarif_per_jam_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("P002", "Budi", 0, 160)

def test_jam_kerja_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("P002", "Budi", 25_000, 0)

def test_hari_kerja_melebihi_batas_pegawai_induk_ditolak() -> None:
    pegawai = Pegawai("P001", "Andi", 2_200_000)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(23)

def test_hari_kerja_negatif_pegawai_harian_ditolak() -> None:
    pegawai = PegawaiHarian("P002", "Budi", 25_000, 160)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(-1)
