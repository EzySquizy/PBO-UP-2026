"""Pengujian untuk kelas BarisSewa."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


def test_baris_sewa_menyimpan_data_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    baris = BarisSewa(alat, 3)

    assert baris.alat is alat
    assert baris.kode_alat == "TR-01"
    assert baris.nama_alat == "Traktor"
    assert baris.jumlah_hari == 3


def test_subtotal_menggunakan_tarif_saat_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    baris = BarisSewa(alat, 3)

    assert baris.subtotal() == 450000


def test_tarif_historis_tidak_berubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175000

    assert baris.tarif_saat_sewa == 150000
    assert baris.subtotal() == 450000
    assert alat.tarif_harian == 175000


@pytest.mark.parametrize("jumlah_hari", [0, -1, -5])
def test_jumlah_hari_tidak_valid_ditolak(jumlah_hari: int) -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(ValueError):
        BarisSewa(alat, jumlah_hari)


def test_baris_nota_menggunakan_data_historis() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175000
    nota = baris.baris_nota()

    assert "TR-01" in nota
    assert "Traktor" in nota
    assert "Rp150.000" in nota
    assert "Rp450.000" in nota
