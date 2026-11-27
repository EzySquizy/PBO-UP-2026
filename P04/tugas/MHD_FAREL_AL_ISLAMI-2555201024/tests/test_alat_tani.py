
"""Pengujian untuk kelas AlatTani dan Alamat."""

import dataclasses

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani

# Pengujian lama


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert "TR-01" in alat.keterangan()
    assert "Traktor" in alat.keterangan()


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("PA-01", "Pompa Air", 75000)
    assert alat.biaya_sewa(0) == 0


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000


def test_kode_tidak_punya_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore


# Pengujian fitur P04: konstanta dan staticmethod


def test_konstanta_tarif_alat() -> None:
    assert AlatTani.TARIF_MINIMUM == 10000
    assert AlatTani.TARIF_MAKSIMUM == 5000000
    assert AlatTani.PERSEN_DENDA_HARIAN == 10


def test_tarif_wajar_menerima_batas_minimum() -> None:
    assert AlatTani.tarif_wajar(10000) is True


def test_tarif_wajar_menerima_batas_maksimum() -> None:
    assert AlatTani.tarif_wajar(5000000) is True


def test_tarif_wajar_menolak_tarif_di_bawah_minimum() -> None:
    assert AlatTani.tarif_wajar(5000) is False


def test_tarif_wajar_menolak_tarif_di_atas_maksimum() -> None:
    assert AlatTani.tarif_wajar(6000000) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150000) == "Rp150.000"


# Pengujian fitur P04: classmethod dan penghitung objek


def test_jumlah_terdaftar_bertambah_satu() -> None:
    sebelum = AlatTani.jumlah_terdaftar()
    AlatTani("TR-99", "Traktor Uji", 150000)
    sesudah = AlatTani.jumlah_terdaftar()

    assert sesudah == sebelum + 1


def test_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv(
        "PA-01;Pompa Air Honda;75000"
    )

    assert alat.kode == "PA-01"
    assert alat.nama == "Pompa Air Honda"
    assert alat.tarif_harian == 75000


def test_dari_baris_csv_menolak_kolom_tidak_lengkap() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air")


def test_dari_baris_csv_menolak_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;mahal")


def test_dari_baris_csv_menolak_tarif_di_bawah_minimum() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;5000")


# Pengujian fitur P04: denda keterlambatan


def test_denda_keterlambatan_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    assert alat.denda_keterlambatan(3) == 45000


def test_denda_keterlambatan_nol_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    assert alat.denda_keterlambatan(0) == 0


def test_denda_keterlambatan_menolak_hari_negatif() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)
