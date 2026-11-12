from __future__ import annotations

import pytest

from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok


# ==================================================
# PENGUJIAN KELAS TRAKTOR
# ==================================================

def test_traktor_init() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert traktor.kode == "TR-01"
    assert traktor.nama == "Traktor Kubota"
    assert traktor.tarif_harian == 150_000
    assert traktor.tenaga_kuda == 8


def test_traktor_tenaga_kuda_nol() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-02", "Traktor", 150_000, 0)


def test_traktor_tenaga_kuda_negatif() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-03", "Traktor", 150_000, -5)


def test_traktor_biaya_sewa() -> None:
    traktor = Traktor("TR-04", "Traktor", 150_000, 8)
    assert traktor.biaya_sewa(2) == 500_000


def test_traktor_tarif_induk_tidak_valid() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-05", "Traktor", 0, 8)


# ==================================================
# PENGUJIAN KELAS POMPA AIR
# ==================================================

def test_pompa_air_init() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 75_000, 100)
    assert pompa.kode == "PA-01"
    assert pompa.nama == "Pompa Air"
    assert pompa.debit == 100


def test_pompa_air_debit_nol() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-02", "Pompa Air", 75_000, 0)


def test_pompa_air_debit_negatif() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-03", "Pompa Air", 75_000, -10)


def test_pompa_air_konsumsi_solar() -> None:
    pompa = PompaAir("PA-04", "Pompa Air", 75_000, 100)
    assert pompa.konsumsi_solar_harian() == 3


def test_pompa_air_biaya_sewa() -> None:
    pompa = PompaAir("PA-05", "Pompa Air", 75_000, 100)
    assert pompa.biaya_sewa(2) == 192_000


# ==================================================
# PENGUJIAN KELAS PERONTOK
# ==================================================

def test_perontok_init() -> None:
    perontok = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert perontok.kode == "PR-01"
    assert perontok.nama == "Perontok Padi"
    assert perontok.kapasitas == 500


def test_perontok_kapasitas_nol() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-02", "Perontok Padi", 200_000, 0)


def test_perontok_kapasitas_negatif() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-03", "Perontok Padi", 200_000, -100)


def test_perontok_minimum_hari() -> None:
    perontok = Perontok("PR-04", "Perontok Padi", 200_000, 500)
    assert perontok.hari_ditagih(1) == 2
    assert perontok.biaya_sewa(1) == 400_000


def test_perontok_biaya_sewa_normal() -> None:
    perontok = Perontok("PR-05", "Perontok Padi", 200_000, 500)
    assert perontok.biaya_sewa(3) == 600_000


# ==================================================
# PENGUJIAN METODE KHUSUS ALAT TANI
# ==================================================

def test_alat_tani_str() -> None:
    alat = AlatTani("A01", "Cangkul", 50_000)
    assert str(alat) == "[A01] Cangkul"


def test_alat_tani_repr() -> None:
    alat = AlatTani("A02", "Cangkul", 50_000)
    assert "AlatTani" in repr(alat)
    assert "A02" in repr(alat)


def test_alat_tani_eq_kode_sama() -> None:
    alat1 = AlatTani("A03", "Cangkul", 50_000)
    alat2 = AlatTani("A03", "Cangkul Besar", 75_000)
    assert alat1 == alat2


def test_alat_tani_eq_kode_berbeda() -> None:
    alat1 = AlatTani("A04", "Cangkul", 50_000)
    alat2 = AlatTani("A05", "Cangkul", 50_000)
    assert alat1 != alat2


def test_alat_tani_dibandingkan_dengan_objek_lain() -> None:
    alat = AlatTani("A06", "Cangkul", 50_000)
    assert alat != "Cangkul"


def test_alat_tani_hash_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat = AlatTani("A07", "Cangkul", 50_000)
    data = {alat: "Tersedia"}
    assert data[alat] == "Tersedia"


def test_alat_tani_hash_sama_untuk_kode_sama() -> None:
    alat1 = AlatTani("A08", "Cangkul", 50_000)
    alat2 = AlatTani("A08", "Cangkul Baru", 60_000)
    assert hash(alat1) == hash(alat2)
