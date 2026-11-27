"""Pengujian tugas individu P06."""

import pytest
from src.kepegawaian.pegawai import Pegawai
from src.kepegawaian.pegawai_harian import PegawaiHarian
from src.kepegawaian.pegawai_kontrak import PegawaiKontrak
from src.kepegawaian.pegawai_pns import PegawaiPNS
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir


def test_penghasilan_pegawai() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert pegawai.hitung_penghasilan(2) == 6_000_000


def test_str_pegawai() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert str(pegawai) == "Andi (001)"


def test_repr_pegawai() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert repr(pegawai) == (
        "Pegawai(nip='001', nama='Andi', gaji_pokok=3000000)"
    )


def test_pegawai_sama_berdasarkan_nip() -> None:
    pertama = Pegawai("001", "Andi", 3_000_000)
    kedua = Pegawai("001", "Budi", 4_000_000)
    assert pertama == kedua


def test_pegawai_berbeda_nip() -> None:
    pertama = Pegawai("001", "Andi", 3_000_000)
    kedua = Pegawai("002", "Andi", 3_000_000)
    assert pertama != kedua


def test_pegawai_dapat_menjadi_kunci_dictionary() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    data = {pegawai: "Pegawai tetap"}
    assert data[pegawai] == "Pegawai tetap"


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Andi", 3_000_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "", 3_000_000)


def test_gaji_pokok_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "Andi", 0)


def test_penghasilan_pegawai_pns() -> None:
    pegawai = PegawaiPNS("001", "Andi", 3_000_000, 500_000)
    assert pegawai.hitung_penghasilan(2) == 7_000_000


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiPNS("001", "Andi", 3_000_000, -100_000)


def test_penghasilan_pegawai_harian() -> None:
    pegawai = PegawaiHarian(
        "002", "Budi", 3_000_000, 100_000, 22
    )
    assert pegawai.hitung_penghasilan(2) == 4_400_000


def test_tarif_harian_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("002", "Budi", 3_000_000, 0, 22)


def test_hari_kerja_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("002", "Budi", 3_000_000, 100_000, 0)


def test_bulan_pegawai_harian_tidak_valid_ditolak() -> None:
    pegawai = PegawaiHarian(
        "002", "Budi", 3_000_000, 100_000, 22
    )
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(0)


def test_penghasilan_pegawai_kontrak() -> None:
    pegawai = PegawaiKontrak("003", "Citra", 2_000_000, 3)
    assert pegawai.hitung_penghasilan(2) == 6_000_000


def test_minimum_bulan_kontrak_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiKontrak("003", "Citra", 2_000_000, 0)


def test_bulan_pegawai_kontrak_tidak_valid_ditolak() -> None:
    pegawai = PegawaiKontrak("003", "Citra", 2_000_000, 3)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(0)


def test_parser_csv_pompa_air() -> None:
    baris = AlatTani.PEMISAH_BARIS.join(
        ["P001", "Pompa Air", "10000", "100"]
    )
    pompa = PompaAir.dari_baris_csv(baris)
    assert isinstance(pompa, PompaAir)
    assert pompa._debit == 100


def test_parser_pompa_air_jumlah_kolom_salah() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("P001,Pompa Air,10000")


def test_parser_pompa_air_angka_tidak_valid() -> None:
    baris = AlatTani.PEMISAH_BARIS.join(
        ["P001", "Pompa Air", "abc", "100"]
    )
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv(baris)


def test_parser_csv_perontok() -> None:
    baris = AlatTani.PEMISAH_BARIS.join(
        ["R001", "Mesin Perontok", "15000", "50"]
    )
    perontok = Perontok.dari_baris_csv(baris)
    assert isinstance(perontok, Perontok)
    assert perontok._kapasitas == 50


def test_parser_perontok_jumlah_kolom_salah() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("R001,Mesin Perontok,15000")


def test_parser_perontok_angka_tidak_valid() -> None:
    baris = AlatTani.PEMISAH_BARIS.join(
        ["R001", "Mesin Perontok", "abc", "50"]
    )
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv(baris)
