"""Pengujian pewarisan class alat tani."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def test_traktor_mewarisi_alat_tani() -> None:
    traktor = Traktor("TR-01", "Traktor", 150_000, 8)

    assert isinstance(traktor, AlatTani)


def test_pompa_air_mewarisi_alat_tani() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 75_000, 600)

    assert isinstance(pompa, AlatTani)


def test_perontok_mewarisi_alat_tani() -> None:
    perontok = Perontok("PR-01", "Perontok", 200_000, 900)

    assert isinstance(perontok, AlatTani)


def test_biaya_sewa_traktor_termasuk_operator() -> None:
    traktor = Traktor("TR-01", "Traktor", 150_000, 8)

    assert traktor.biaya_sewa(3) == 750_000


def test_biaya_sewa_pompa_air_termasuk_solar() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 75_000, 600)

    assert pompa.biaya_sewa(3) == 603_000


def test_perontok_menagih_minimum_dua_hari() -> None:
    perontok = Perontok("PR-01", "Perontok", 200_000, 900)

    assert perontok.biaya_sewa(1) == 400_000
    assert perontok.biaya_sewa(3) == 600_000

def test_str_menampilkan_keterangan_alat() -> None:
    traktor = Traktor("TR-01", "Traktor", 150_000, 8)

    assert str(traktor) == traktor.keterangan()


def test_repr_menampilkan_nama_class() -> None:
    traktor = Traktor("TR-01", "Traktor", 150_000, 8)

    assert repr(traktor).startswith("Traktor(")


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    alat1 = Traktor("TR-01", "Traktor", 150_000, 8)
    alat2 = Traktor("TR-01", "Traktor Lain", 160_000, 9)

    assert alat1 == alat2


def test_dua_alat_dengan_kode_berbeda_dianggap_berbeda() -> None:
    alat1 = Traktor("TR-01", "Traktor", 150_000, 8)
    alat2 = Traktor("TR-02", "Traktor", 150_000, 8)

    assert alat1 != alat2


def test_alat_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat1 = Traktor("TR-01", "Traktor", 150_000, 8)
    alat2 = Traktor("TR-01", "Traktor Lain", 160_000, 9)

    catatan = {alat1: "sedang disewa"}

    assert catatan[alat2] == "sedang disewa"


def test_alat_dibandingkan_dengan_bukan_alat() -> None:
    traktor = Traktor("TR-01", "Traktor", 150_000, 8)

    assert traktor != "TR-01"


def test_pompa_air_dibuat_dari_baris_csv() -> None:
    pompa = PompaAir.dari_baris_csv("PA-02;Pompa Sawah;125000;200")

    assert pompa.kode == "PA-02"
    assert pompa.nama == "Pompa Sawah"
    assert pompa.tarif_harian == 125_000
    assert pompa.konsumsi_solar_harian() == 6


def test_perontok_dibuat_dari_baris_csv() -> None:
    perontok = Perontok.dari_baris_csv("PR-02;Perontok Padi;150000;500")

    assert perontok.kode == "PR-02"
    assert perontok.nama == "Perontok Padi"
    assert perontok.tarif_harian == 150_000
    assert perontok.biaya_sewa(1) == 300_000


def test_pompa_air_menolak_jumlah_bagian_csv_salah() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-02;Pompa Sawah;125000")


def test_pompa_air_menolak_tarif_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-02;Pompa Sawah;abc;200")


def test_pompa_air_menolak_debit_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-02;Pompa Sawah;125000;abc")


def test_perontok_menolak_jumlah_bagian_csv_salah() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-02;Perontok Padi;150000")


def test_perontok_menolak_tarif_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-02;Perontok Padi;abc;500")


def test_perontok_menolak_kapasitas_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-02;Perontok Padi;150000;abc")
