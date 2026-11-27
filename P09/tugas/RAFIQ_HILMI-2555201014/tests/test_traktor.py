
"""Pengujian untuk class Traktor."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor


def test_membuat_traktor() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    assert traktor.kode == "TR-01"
    assert traktor.nama == "Traktor Kubota"
    assert traktor.tarif_harian == 150_000


def test_biaya_sewa_traktor_satu_hari() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    assert traktor.biaya_sewa(1) == 250_000


def test_biaya_sewa_traktor_tiga_hari() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    assert traktor.biaya_sewa(3) == 750_000


def test_biaya_sewa_traktor_nol_hari() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    with pytest.raises(ValueError):
        traktor.biaya_sewa(0)


def test_traktor_menolak_tenaga_kuda_nol() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, 0)


def test_traktor_menolak_tenaga_kuda_minus() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, -10)


def test_traktor_memiliki_ongkos_operator() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    assert traktor.biaya_sewa(2) == (
        150_000 * 2 + Traktor.ONGKOS_OPERATOR_HARIAN * 2
    )


def test_traktor_tetap_mewarisi_format_keterangan() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    assert traktor.keterangan() == (
        "[TR-01] Traktor Kubota — Rp150.000/hari"
    )


def test_traktor_merupakan_alat_tani() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 45)
    assert isinstance(traktor, AlatTani)
