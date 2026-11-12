
"""Pengujian enkapsulasi untuk kelas AlatTani."""

import pytest

from src.model.alat_tani import AlatTani


def test_data_alat_dapat_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.kode == "TR-01"
    assert alat.nama == "Traktor"


def test_biaya_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan() -> None:
    alat = AlatTani("PA-01", "Pompa Air", 75000)
    assert "[PA-01] Pompa Air" in alat.keterangan()


def test_tarif_bisa_diubah_dengan_nilai_valid() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000


@pytest.mark.parametrize("tarif", [0, -1, 5000001, -100])
def test_tarif_tidak_valid_ditolak(tarif: int) -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", tarif)


def test_kode_hanya_bisa_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_hanya_bisa_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Traktor Baru"  # type: ignore[misc]


def test_tarif_tidak_valid_saat_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 0
