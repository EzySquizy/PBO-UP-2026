
"""Pengujian pewarisan dan overriding alat pertanian P06."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def test_traktor_menghitung_biaya_operator() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 8)

    assert alat.biaya_sewa(1) == 250_000
    assert alat.biaya_sewa(3) == 750_000


def test_traktor_menolak_tenaga_kuda_nol() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-02", "Traktor", 150_000, 0)


def test_pompa_air_menghitung_konsumsi_solar() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)

    assert alat.konsumsi_solar_harian() == 18


def test_pompa_air_menghitung_biaya_sewa() -> None:
    alat = PompaAir("PA-02", "Pompa Air", 75_000, 600)

    assert alat.biaya_sewa(1) == 201_000
    assert alat.biaya_sewa(3) == 603_000


def test_pompa_air_menolak_debit_nol() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-03", "Pompa Air", 75_000, 0)


def test_perontok_menerapkan_minimum_hari() -> None:
    alat = Perontok("PR-01", "Perontok", 200_000, 900)

    assert alat.hari_ditagih(1) == 2
    assert alat.hari_ditagih(3) == 3
    assert alat.biaya_sewa(1) == 400_000
    assert alat.biaya_sewa(3) == 600_000


def test_perontok_menolak_kapasitas_nol() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-02", "Perontok", 200_000, 0)


def test_perontok_menolak_jumlah_hari_nol() -> None:
    alat = Perontok("PR-03", "Perontok", 200_000, 900)

    with pytest.raises(ValueError):
        alat.biaya_sewa(0)


def test_subclass_mewarisi_alat_tani() -> None:
    traktor = Traktor("TR-04", "Traktor", 150_000, 8)
    pompa = PompaAir("PA-04", "Pompa", 75_000, 600)
    perontok = Perontok("PR-04", "Perontok", 200_000, 900)

    assert isinstance(traktor, AlatTani)
    assert isinstance(pompa, AlatTani)
    assert isinstance(perontok, AlatTani)


def test_str_menghasilkan_keterangan_alat() -> None:
    alat = Traktor("TR-05", "Traktor", 150_000, 8)

    assert str(alat) == alat.keterangan()


def test_repr_memuat_nama_kelas() -> None:
    alat = Traktor("TR-06", "Traktor", 150_000, 8)

    assert repr(alat).startswith("Traktor(")


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    alat1 = Traktor("TR-07", "Traktor A", 150_000, 8)
    alat2 = PompaAir("TR-07", "Pompa B", 75_000, 600)

    assert alat1 == alat2
    assert hash(alat1) == hash(alat2)


def test_alat_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat = Traktor("TR-08", "Traktor", 150_000, 8)
    data = {alat: "tersedia"}

    assert data[alat] == "tersedia"


def test_baris_sewa_menyimpan_biaya_traktor() -> None:
    alat = Traktor("TR-09", "Traktor", 150_000, 8)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 200_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 750_000


def test_baris_sewa_menyimpan_biaya_pompa() -> None:
    alat = PompaAir("PA-09", "Pompa", 75_000, 600)
    baris = BarisSewa(alat, 3)

    assert baris.subtotal() == 603_000


def test_baris_sewa_menyimpan_biaya_perontok() -> None:
    alat = Perontok("PR-09", "Perontok", 200_000, 900)
    baris = BarisSewa(alat, 1)

    assert baris.subtotal() == 400_000

def test_alat_dapat_dimasukkan_ke_set() -> None:
    alat1 = Traktor("TR-10", "Traktor A", 150_000, 8)
    alat2 = Traktor("TR-10", "Traktor B", 160_000, 9)

    kumpulan = {alat1, alat2}

    assert len(kumpulan) == 1
