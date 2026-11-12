
import pytest

from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok


def test_traktor_menghitung_ongkos_operator() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)

    assert alat.biaya_sewa(1) == 250000
    assert alat.biaya_sewa(3) == 750000


def test_traktor_menyimpan_tenaga_kuda() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)

    assert alat.tenaga_kuda == 8


def test_traktor_tenaga_kuda_harus_positif() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150000, 0)


def test_pompa_menghitung_konsumsi_solar() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75000, 600)

    assert alat.konsumsi_solar_harian() == 18


def test_pompa_menghitung_biaya_sewa() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75000, 600)

    assert alat.biaya_sewa(3) == 603000


def test_pompa_debit_harus_positif() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-01", "Pompa Air", 75000, 0)


def test_perontok_minimum_dua_hari() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200000, 900)

    assert alat.hari_ditagih(1) == 2
    assert alat.biaya_sewa(1) == 400000


def test_perontok_tiga_hari() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200000, 900)

    assert alat.biaya_sewa(3) == 600000


def test_perontok_kapasitas_harus_positif() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-01", "Mesin Perontok", 200000, 0)


def test_semua_alat_merupakan_turunan_alat_tani() -> None:
    assert issubclass(Traktor, AlatTani)
    assert issubclass(PompaAir, AlatTani)
    assert issubclass(Perontok, AlatTani)


def test_dunder_eq_membandingkan_kode() -> None:
    pertama = Traktor("TR-01", "Traktor A", 150000, 8)
    kedua = PompaAir("TR-01", "Pompa B", 75000, 600)

    assert pertama == kedua


def test_dunder_hash_konsisten_dengan_eq() -> None:
    pertama = Traktor("TR-01", "Traktor A", 150000, 8)
    kedua = PompaAir("TR-01", "Pompa B", 75000, 600)

    assert pertama == kedua
    assert hash(pertama) == hash(kedua)


def test_alat_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)
    data = {alat: "Tersedia"}

    assert data[alat] == "Tersedia"


def test_eq_dengan_objek_lain() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)

    assert alat != "TR-01"


def test_str_menggunakan_keterangan() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)

    assert str(alat) == alat.keterangan()


def test_repr_menampilkan_nama_kelas() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)

    assert repr(alat).startswith("Traktor(")
    assert "tenaga_kuda=8" in repr(alat)


def test_snapshot_biaya_traktor_tidak_berubah() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150000, 8)
    from src.model.baris_sewa import BarisSewa

    baris = BarisSewa(alat, 2)
    alat.tarif_harian = 200000

    assert baris.tarif_saat_sewa == 150000
    assert baris.subtotal() == 500000
