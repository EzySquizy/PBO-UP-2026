"""Pengujian untuk kelas BarisSewa."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


def test_baris_sewa_menyimpan_data_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.alat is alat
    assert baris.kode_alat == "TR-01"
    assert baris.nama_alat == "Traktor"
    assert baris.jumlah_hari == 3


def test_subtotal_dihitung_dari_tarif_dan_hari() -> None:
    alat = AlatTani("TR-02", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.subtotal() == 450_000


def test_tarif_tetap_sesuai_saat_transaksi() -> None:
    alat = AlatTani("TR-03", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000


def test_nama_dan_kode_tetap_sebagai_snapshot() -> None:
    alat = AlatTani("TR-04", "Traktor", 150_000)
    baris = BarisSewa(alat, 2)

    alat._nama = "Traktor Baru"
    alat._kode = "TR-99"

    assert baris.nama_alat == "Traktor"
    assert baris.kode_alat == "TR-04"


def test_jumlah_hari_nol_ditolak() -> None:
    alat = AlatTani("TR-05", "Traktor", 150_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    alat = AlatTani("TR-06", "Traktor", 150_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, -1)


def test_baris_nota_memuat_rincian_sewa() -> None:
    alat = AlatTani("TR-07", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    nota = baris.baris_nota()

    assert "Traktor" in nota
    assert "TR-07" in nota
    assert "450.000" in nota
