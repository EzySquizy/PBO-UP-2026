
"""Pengujian untuk kelas AlatTani."""

import pytest
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua Kubota - Rp150.000/hari"


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("PA-01", "Pompa Air 3 Inci", 75000)
    assert alat.biaya_sewa(1) == 75000


def test_kode_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.kode == "TR-01"
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.nama == "Traktor"
    with pytest.raises(AttributeError):
        alat.nama = "Pompa"  # type: ignore[misc]


def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_minus_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_di_atas_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)


def test_setter_tarif_tidak_mengubah_nilai_jika_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000


def test_setter_tarif_menerima_nilai_valid() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000

def test_tarif_wajar_batas_minimum() -> None:
    assert AlatTani.tarif_wajar(10_000) is True


def test_tarif_wajar_batas_maksimum() -> None:
    assert AlatTani.tarif_wajar(5_000_000) is True


def test_tarif_wajar_di_bawah_minimum() -> None:
    assert AlatTani.tarif_wajar(9_999) is False


def test_tarif_wajar_di_atas_maksimum() -> None:
    assert AlatTani.tarif_wajar(5_000_001) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_format_rupiah_nol() -> None:
    assert AlatTani.format_rupiah(0) == "Rp0"


def test_dari_baris_csv_valid() -> None:
    alat = AlatTani.dari_baris_csv("PA-01;Pompa Air;75000")
    assert alat.kode == "PA-01"
    assert alat.nama == "Pompa Air"
    assert alat.tarif_harian == 75_000


def test_dari_baris_csv_kolom_kurang() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air")


def test_dari_baris_csv_kolom_lebih() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;75000;catatan")


def test_dari_baris_csv_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;mahal")


def test_dari_baris_csv_tarif_di_luar_batas() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;5000")


def test_denda_keterlambatan_dua_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    assert alat.denda_keterlambatan(2) == 30_000


def test_denda_tanpa_keterlambatan() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    assert alat.denda_keterlambatan(0) == 0


def test_denda_hari_negatif_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)


def test_jumlah_terdaftar_bertambah_satu() -> None:
    sebelum = AlatTani.jumlah_terdaftar()
    AlatTani("UJI-01", "Alat Uji", 100_000)
    assert AlatTani.jumlah_terdaftar() == sebelum + 1
