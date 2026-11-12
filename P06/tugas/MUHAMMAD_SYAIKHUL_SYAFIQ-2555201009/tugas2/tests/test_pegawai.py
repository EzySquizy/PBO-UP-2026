"""Pengujian hierarki pegawai Dinas Pertanian Kabupaten Kampar."""

import pytest

from src.model.pegawai import Pegawai
from src.model.pegawai_tetap import PegawaiTetap
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak


def test_pegawai_menghitung_gaji_pokok() -> None:
    pegawai = Pegawai("19800101", "Andi", 100_000)
    assert pegawai.hitung_gaji(22) == 2_200_000


def test_pegawai_tetap_menambahkan_tunjangan() -> None:
    pegawai = PegawaiTetap("19800102", "Budi", 150_000, 50_000)
    assert pegawai.hitung_gaji(22) == 4_400_000


def test_pegawai_harian_menghitung_upah_jam() -> None:
    pegawai = PegawaiHarian(
        "19800103", "Citra", 100_000, 20_000, 8
    )
    assert pegawai.hitung_gaji(5) == 800_000


def test_pegawai_kontrak_membatasi_hari() -> None:
    pegawai = PegawaiKontrak("19800104", "Dedi", 100_000, 10)
    assert pegawai.hitung_gaji(15) == 1_000_000


def test_pegawai_kontrak_menerima_hari_di_bawah_batas() -> None:
    pegawai = PegawaiKontrak("19800105", "Eka", 100_000, 10)
    assert pegawai.hitung_gaji(5) == 500_000


def test_semua_pegawai_merupakan_turunan_pegawai() -> None:
    daftar = [
        PegawaiTetap("19800106", "Fani", 100_000, 20_000),
        PegawaiHarian("19800107", "Gani", 100_000, 15_000, 8),
        PegawaiKontrak("19800108", "Hani", 100_000, 30),
    ]

    assert all(isinstance(item, Pegawai) for item in daftar)


def test_identitas_pegawai() -> None:
    pegawai = Pegawai("19800109", "Indra", 100_000)
    assert pegawai.nip == "19800109"
    assert pegawai.nama == "Indra"


def test_str_pegawai() -> None:
    pegawai = Pegawai("19800110", "Joko", 100_000)
    assert str(pegawai) == "Joko (19800110)"


def test_repr_pegawai() -> None:
    pegawai = Pegawai("19800111", "Kiki", 100_000)
    assert repr(pegawai) == (
        "Pegawai(nip='19800111', nama='Kiki', "
        "gaji_pokok_harian=100000)"
    )


def test_dua_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pertama = Pegawai("19800112", "Lina", 100_000)
    kedua = Pegawai("19800112", "Mira", 200_000)
    assert pertama == kedua


def test_pegawai_dengan_nip_berbeda_tidak_sama() -> None:
    pertama = Pegawai("19800113", "Nina", 100_000)
    kedua = Pegawai("19800114", "Oki", 100_000)
    assert pertama != kedua


def test_pegawai_dapat_digunakan_sebagai_kunci_dictionary() -> None:
    pegawai = Pegawai("19800115", "Putra", 100_000)
    data = {pegawai: "Dinas Pertanian"}
    assert data[pegawai] == "Dinas Pertanian"


def test_pegawai_dapat_dibandingkan_dengan_non_pegawai() -> None:
    pegawai = Pegawai("19800116", "Rina", 100_000)
    assert pegawai != "bukan pegawai"


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Sari", 100_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("19800117", "", 100_000)


def test_gaji_pokok_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("19800118", "Tono", 0)


def test_jumlah_hari_nol_ditolak() -> None:
    pegawai = Pegawai("19800119", "Udin", 100_000)
    with pytest.raises(ValueError):
        pegawai.hitung_gaji(0)


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("19800120", "Vina", 100_000, -1)


def test_upah_per_jam_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("19800121", "Wati", 100_000, 0, 8)


def test_durasi_kontrak_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiKontrak("19800122", "Yudi", 100_000, 0)