
"""Pengujian untuk kelas BarisSewa."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


def test_baris_sewa_menyimpan_objek_alat() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.alat is alat


def test_baris_sewa_menyimpan_jumlah_hari() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.jumlah_hari == 3


def test_baris_sewa_menyimpan_kode_alat() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.kode_alat == "AT001"


def test_baris_sewa_menyimpan_nama_alat() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.nama_alat == "Traktor"


def test_baris_sewa_menyimpan_tarif_saat_sewa() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.tarif_saat_sewa == 150_000


def test_subtotal_dihitung_dari_tarif_dan_hari() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    assert baris.subtotal() == 450_000


def test_jumlah_hari_nol_ditolak() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, -2)


def test_subtotal_tidak_berubah_setelah_tarif_alat_berubah() -> None:
    alat = AlatTani("AT001", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.subtotal() == 450_000
    assert baris.tarif_saat_sewa == 150_000
