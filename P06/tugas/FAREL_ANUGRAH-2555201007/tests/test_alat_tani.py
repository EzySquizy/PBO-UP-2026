"""Tes untuk model AlatTani pada P03."""

import pytest
from src.model.alat_tani import AlatTani


def test_biaya_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan_rupiah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(0) == 0


def test_setiap_objek_independen() -> None:
    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("PM-01", "Pompa", 75000)
    assert traktor.biaya_sewa(1) == 150000
    assert pompa.biaya_sewa(1) == 75000


def test_properti_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.kode == "TR-01"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 150000


def test_tarif_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000


@pytest.mark.parametrize("tarif", [0, -1, -100])
def test_tarif_tidak_valid(tarif: int) -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", tarif)


def test_tarif_melebihi_batas() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)


def test_kode_harus_diisi() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150000)


def test_kode_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Pompa"  # type: ignore[misc]

# Pengujian tambahan P04: konstanta dan anggota kelas.


def test_konstanta_kelas() -> None:
    assert AlatTani.TARIF_MINIMUM == 10_000
    assert AlatTani.TARIF_MAKSIMUM == 5_000_000
    assert AlatTani.PERSEN_DENDA_HARIAN == 10
    assert AlatTani.PEMISAH_BARIS == ";"


def test_tarif_wajar() -> None:
    assert AlatTani.tarif_wajar(10_000)
    assert AlatTani.tarif_wajar(150_000)
    assert AlatTani.tarif_wajar(5_000_000)
    assert not AlatTani.tarif_wajar(5_000)
    assert not AlatTani.tarif_wajar(5_000_001)


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"
    assert AlatTani.format_rupiah(1_000_000) == "Rp1.000.000"


def test_jumlah_terdaftar_bertambah() -> None:
    sebelum = AlatTani.jumlah_terdaftar()

    AlatTani("TR-01", "Traktor", 150_000)
    AlatTani("PA-01", "Pompa", 75_000)

    sesudah = AlatTani.jumlah_terdaftar()
    assert sesudah == sebelum + 2


def test_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv("TR-02;Traktor Mini;125000")

    assert alat.kode == "TR-02"
    assert alat.nama == "Traktor Mini"
    assert alat.tarif_harian == 125_000


@pytest.mark.parametrize(
    "baris",
    [
        "TR-01;Traktor",
        "TR-01;Traktor;150000;extra",
    ],
)
def test_csv_jumlah_bagian_tidak_valid(baris: str) -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv(baris)


def test_csv_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError, match="tarif harus berupa angka"):
        AlatTani.dari_baris_csv("TR-01;Traktor;mahal")


def test_denda_keterlambatan() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)

    assert alat.denda_keterlambatan(2) == 30_000


def test_denda_nol_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)

    assert alat.denda_keterlambatan(0) == 0


def test_denda_hari_negatif_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)

    with pytest.raises(ValueError, match="tidak boleh negatif"):
        alat.denda_keterlambatan(-1)
