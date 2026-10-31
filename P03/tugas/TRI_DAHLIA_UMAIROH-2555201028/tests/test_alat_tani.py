import pytest

from src.model.alat_tani import AlatTani


def test_alat_tani_valid() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    assert alat.kode == "AT01"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 100000


def test_kode_read_only() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    with pytest.raises(AttributeError):
        alat.kode = "AT02"  # type: ignore[misc]


def test_nama_read_only() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    with pytest.raises(AttributeError):
        alat.nama = "Mesin"  # type: ignore[misc]


def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT01", "Traktor", 0)


def test_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT01", "Traktor", -1000)


def test_tarif_terlalu_besar_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT01", "Traktor", 5_000_001)


def test_tarif_bisa_diubah_valid() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000


def test_tarif_baru_nol_ditolak() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 0
