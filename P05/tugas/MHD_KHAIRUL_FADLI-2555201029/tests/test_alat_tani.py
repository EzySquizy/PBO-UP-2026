
"""Pengujian untuk kelas AlatTani."""

import dataclasses

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150_000)
    assert alat.biaya_sewa(3) == 450_000


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150_000)
    assert alat.biaya_sewa(1) == 150_000


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150_000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua — Rp150.000/hari"


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150_000)
    b = AlatTani("PA-01", "Pompa", 75_000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5_000)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5_000
    assert alat.tarif_harian == 150_000


def test_kode_tidak_punya_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore[misc]


def test_alamat_tidak_dapat_diubah() -> None:
    a = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        a.desa = "Salo"  # type: ignore[misc]


def test_tarif_minimum() -> None:
    assert AlatTani.TARIF_MINIMUM == 10_000


def test_tarif_maksimum() -> None:
    assert AlatTani.TARIF_MAKSIMUM == 5_000_000


def test_tarif_wajar_diterima() -> None:
    assert AlatTani.tarif_wajar(150_000) is True


def test_tarif_di_bawah_minimum_ditolak() -> None:
    assert AlatTani.tarif_wajar(5_000) is False


def test_tarif_di_atas_maksimum_ditolak() -> None:
    assert AlatTani.tarif_wajar(6_000_000) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_jumlah_terdaftar_bertambah() -> None:
    sebelum = AlatTani.jumlah_terdaftar()
    AlatTani("TR-10", "Traktor", 150_000)
    assert AlatTani.jumlah_terdaftar() == sebelum + 1


def test_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv("TR-20;Traktor;200000")
    assert alat.kode == "TR-20"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 200_000


def test_csv_dengan_format_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-20;Traktor")


def test_csv_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-20;Traktor;mahal")


def test_denda_tiga_hari() -> None:
    alat = AlatTani("TR-30", "Traktor", 150_000)
    assert alat.denda_keterlambatan(3) == 45_000


def test_denda_nol_hari() -> None:
    alat = AlatTani("TR-31", "Traktor", 150_000)
    assert alat.denda_keterlambatan(0) == 0


def test_denda_hari_negatif_ditolak() -> None:
    alat = AlatTani("TR-32", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)
