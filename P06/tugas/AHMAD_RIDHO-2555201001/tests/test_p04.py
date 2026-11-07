
import pytest
from src.model.alat_tani import AlatTani


def test_tarif_wajar_dipanggil_tanpa_objek() -> None:
    assert AlatTani.tarif_wajar(150_000) is True
    assert AlatTani.tarif_wajar(6_000_000) is False


def test_pencacah_naik_untuk_setiap_alat_baru() -> None:
    awal = AlatTani.jumlah_terdaftar()

    AlatTani("TR-90", "Traktor Uji", 100_000)
    AlatTani("TR-91", "Traktor Uji", 100_000)

    assert AlatTani.jumlah_terdaftar() == awal + 2


def test_konstruktor_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv("PA-01;Pompa Air;75000")

    assert alat.kode == "PA-01"
    assert alat.nama == "Pompa Air"
    assert alat.tarif_harian == 75_000


def test_baris_csv_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;tujuh puluh lima ribu")


def test_baris_csv_jumlah_kolom_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air")


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"
