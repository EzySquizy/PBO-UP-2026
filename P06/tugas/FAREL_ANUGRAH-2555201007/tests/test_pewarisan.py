
"""Pengujian pewarisan alat pertanian P06."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def test_traktor_merupakan_alat_tani() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 15)
    assert isinstance(alat, AlatTani)

def test_pompa_merupakan_alat_tani() -> None:
    alat = PompaAir("PA-01", "Pompa", 75_000, 600)
    assert isinstance(alat, AlatTani)

def test_perontok_merupakan_alat_tani() -> None:
    alat = Perontok("PR-01", "Perontok", 200_000, 900)
    assert isinstance(alat, AlatTani)

def test_traktor_menyimpan_tenaga_kuda() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 15)
    assert alat.tenaga_kuda == 15

def test_pompa_menyimpan_debit() -> None:
    alat = PompaAir("PA-01", "Pompa", 75_000, 600)
    assert alat.debit == 600

def test_perontok_menyimpan_kapasitas() -> None:
    alat = Perontok("PR-01", "Perontok", 200_000, 900)
    assert alat.kapasitas == 900

def test_traktor_biaya_sewa_satu_hari() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 15)
    assert alat.biaya_sewa(1) == 250_000

def test_traktor_biaya_sewa_tiga_hari() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 15)
    assert alat.biaya_sewa(3) == 750_000

def test_pompa_konsumsi_solar() -> None:
    alat = PompaAir("PA-01", "Pompa", 75_000, 600)
    assert alat.konsumsi_solar_harian() == 18

def test_pompa_biaya_sewa_satu_hari() -> None:
    alat = PompaAir("PA-01", "Pompa", 75_000, 600)
    assert alat.biaya_sewa(1) == 201_000

def test_pompa_biaya_sewa_tiga_hari() -> None:
    alat = PompaAir("PA-01", "Pompa", 75_000, 600)
    assert alat.biaya_sewa(3) == 603_000

def test_perontok_biaya_sewa_satu_hari() -> None:
    alat = Perontok("PR-01", "Perontok", 200_000, 900)
    assert alat.biaya_sewa(1) == 400_000

def test_perontok_biaya_sewa_dua_hari() -> None:
    alat = Perontok("PR-01", "Perontok", 200_000, 900)
    assert alat.biaya_sewa(2) == 400_000

def test_perontok_biaya_sewa_tiga_hari() -> None:
    alat = Perontok("PR-01", "Perontok", 200_000, 900)
    assert alat.biaya_sewa(3) == 600_000

def test_csv_traktor() -> None:
    alat = Traktor.dari_baris_csv("TR-01;Traktor;150000;15")
    assert alat.tenaga_kuda == 15
    assert alat.tarif_harian == 150_000

def test_csv_pompa() -> None:
    alat = PompaAir.dari_baris_csv("PA-01;Pompa;75000;600")
    assert alat.debit == 600
    assert alat.tarif_harian == 75_000

def test_csv_perontok() -> None:
    alat = Perontok.dari_baris_csv("PR-01;Perontok;200000;900")
    assert alat.kapasitas == 900
    assert alat.tarif_harian == 200_000

@pytest.mark.parametrize(
    "kelas,baris",
    [
        (Traktor, "TR-01;Traktor;150000"),
        (PompaAir, "PA-01;Pompa;75000"),
        (Perontok, "PR-01;Perontok;200000"),
    ],
)
def test_csv_menolak_jumlah_kolom_salah(
    kelas: type[AlatTani],
    baris: str,
) -> None:
    with pytest.raises(ValueError):
        kelas.dari_baris_csv(baris)

@pytest.mark.parametrize(
    "pembuat",
    [
        lambda: Traktor("TR-01", "Traktor", 150_000, 0),
        lambda: PompaAir("PA-01", "Pompa", 75_000, 0),
        lambda: Perontok("PR-01", "Perontok", 200_000, 0),
    ],
)
def test_konstruktor_menolak_atribut_nol(
    pembuat: object,
) -> None:
    with pytest.raises(ValueError):
        pembuat()  # type: ignore[operator]

def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    pertama = Traktor("TR-01", "Traktor A", 150_000, 15)
    kedua = PompaAir("TR-01", "Pompa B", 75_000, 600)
    assert pertama == kedua

def test_alat_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 15)
    data = {alat: "Tersedia"}
    assert data[alat] == "Tersedia"

def test_repr_menampilkan_nama_kelas() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 15)
    assert repr(alat).startswith("Traktor(")

def test_str_menampilkan_kode_alat() -> None:
    alat = PompaAir("PA-01", "Pompa", 75_000, 600)
    assert "PA-01" in str(alat)
