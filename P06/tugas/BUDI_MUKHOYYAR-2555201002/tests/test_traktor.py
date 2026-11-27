"""Pengujian untuk kelas Traktor."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor


def test_traktor_merupakan_turunan_alat_tani() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 24)
    assert isinstance(traktor, AlatTani)


def test_biaya_sewa_satu_hari_ditambah_operator() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 24)
    assert traktor.biaya_sewa(1) == 250_000


def test_biaya_sewa_tiga_hari_ditambah_operator() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 24)
    assert traktor.biaya_sewa(3) == 750_000


def test_tenaga_kuda_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, 0)


def test_tenaga_kuda_minus_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, -10)