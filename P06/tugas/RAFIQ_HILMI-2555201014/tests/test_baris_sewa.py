"""Pengujian untuk class BarisSewa."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


def buat_alat() -> AlatTani:
    return AlatTani("TR-01", "Traktor", 150_000)


def test_baris_sewa_menyimpan_objek_alat() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)
    assert baris.alat is alat


def test_baris_sewa_menyimpan_kode_alat() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.kode_alat == "TR-01"


def test_baris_sewa_menyimpan_nama_alat() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.nama_alat == "Traktor"


def test_baris_sewa_menyimpan_tarif_saat_sewa() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.tarif_saat_sewa == 150_000


def test_baris_sewa_menyimpan_jumlah_hari() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.jumlah_hari == 3


def test_subtotal_menghitung_biaya_sewa() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.subtotal() == 450_000


def test_tarif_lama_tidak_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000


def test_jumlah_hari_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), -1)


def test_baris_nota_menampilkan_nama_alat() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert "Traktor" in baris.baris_nota()
