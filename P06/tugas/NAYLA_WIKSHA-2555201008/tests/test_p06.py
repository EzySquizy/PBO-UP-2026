
import pytest
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def test_traktor_mewarisi_data_alat_tani() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 12)

    assert alat.kode == "TR-01"
    assert alat.nama == "Traktor Kubota"
    assert alat.tarif_harian == 150_000
    assert alat.tenaga_kuda == 12


def test_traktor_menolak_tenaga_kuda_nol() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, 0)


def test_traktor_menolak_tenaga_kuda_negatif() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, -5)


def test_traktor_menghitung_biaya_sewa() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 12)

    assert alat.biaya_sewa(3) == 750_000


def test_pompa_air_menghitung_konsumsi_solar() -> None:
    alat = PompaAir("PA-01", "Pompa Diesel", 100_000, 500)

    assert alat.konsumsi_solar_harian() == 15


def test_pompa_air_menghitung_biaya_sewa() -> None:
    alat = PompaAir("PA-01", "Pompa Diesel", 100_000, 500)

    assert alat.biaya_sewa(3) == 615_000


def test_perontok_minimum_sewa_dua_hari() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)

    assert alat.hari_ditagih(1) == 2
    assert alat.biaya_sewa(1) == 400_000


def test_perontok_sewa_tiga_hari() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)

    assert alat.biaya_sewa(3) == 600_000


def test_repr_menggunakan_nama_class_turunan() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 12)

    assert repr(alat).startswith("Traktor(")


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    alat1 = Traktor("TR-01", "Traktor Kubota", 150_000, 12)
    alat2 = Traktor("TR-01", "Traktor Yanmar", 200_000, 15)

    assert alat1 == alat2


def test_alat_tani_tidak_sama_dengan_objek_lain() -> None:
    alat = AlatTani("TR-01", "Traktor Kubota", 150_000)

    assert alat != "TR-01"


def test_alat_tani_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat1 = Traktor("TR-01", "Traktor Kubota", 150_000, 12)
    alat2 = PompaAir("TR-01", "Pompa Diesel", 100_000, 500)

    data: dict[AlatTani, str] = {alat1: "tersimpan"}

    assert data[alat2] == "tersimpan"


def test_alat_tani_dapat_digunakan_dalam_set() -> None:
    alat1 = Traktor("TR-01", "Traktor Kubota", 150_000, 12)
    alat2 = PompaAir("TR-01", "Pompa Diesel", 100_000, 500)

    data: set[AlatTani] = {alat1, alat2}

    assert len(data) == 1


def test_str_menampilkan_identitas_alat() -> None:
    alat = AlatTani("TR-01", "Traktor Kubota", 150_000)

    assert "TR-01" in str(alat)
    assert "Traktor Kubota" in str(alat)


def test_traktor_dibuat_dari_baris_csv() -> None:
    alat = Traktor.dari_baris_csv(
        "TR-02;Traktor John Deere;250000;20"
    )

    assert alat.kode == "TR-02"
    assert alat.nama == "Traktor John Deere"
    assert alat.tarif_harian == 250_000
    assert alat.tenaga_kuda == 20


def test_pompa_air_dibuat_dari_baris_csv() -> None:
    alat = PompaAir.dari_baris_csv(
        "PA-02;Pompa Air;150000;500"
    )

    assert alat.kode == "PA-02"
    assert alat.nama == "Pompa Air"
    assert alat.tarif_harian == 150_000
    assert alat.debit == 500


def test_perontok_dibuat_dari_baris_csv() -> None:
    alat = Perontok.dari_baris_csv(
        "PR-02;Mesin Perontok;200000;900"
    )

    assert alat.kode == "PR-02"
    assert alat.nama == "Mesin Perontok"
    assert alat.tarif_harian == 200_000
    assert alat.kapasitas == 900
