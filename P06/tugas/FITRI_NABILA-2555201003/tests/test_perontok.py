import pytest
from src.model.perontok import Perontok


def test_validasi_induk_tetap_berlaku_pada_perontok() -> None:
    """Menguji validasi tarif dari kelas induk pada kelas Perontok."""
    with pytest.raises(ValueError):
        Perontok("PR-01", "Mesin Perontok", -10_000, 900)


def test_perontok_menagih_minimum_dua_hari() -> None:
    """Menguji bahwa Perontok menagih minimum sewa 2 hari (pola mengubah masukan)."""
    r = Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900)
    assert r.biaya_sewa(1) == r.biaya_sewa(2)
    assert r.biaya_sewa(1) == 400_000
    assert r.biaya_sewa(3) == 600_000


def test_perontok_dapat_menjadi_kunci_dict() -> None:
    """Menguji bahwa objek Perontok dapat dijadikan kunci dictionary."""
    pr = Perontok("PR-01", "Mesin Perontok", 200_000, 900)
    catatan = {pr: "dalam perawatan"}
    assert catatan[Perontok("PR-01", "Perontok Lain", 220_000, 1000)] == "dalam perawatan"


def test_perontok_str_dan_repr() -> None:
    """Menguji format __str__ dan __repr__ pada Perontok."""
    pr = Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900)
    assert str(pr) == pr.keterangan()
    assert "Perontok" in repr(pr)
    assert "PR-01" in repr(pr)


def test_perontok_denda_negatif_ditolak() -> None:
    """Menguji bahwa denda keterlambatan dengan hari minus melempar ValueError."""
    pr = Perontok("PR-01", "Perontok", 200_000, 900)
    with pytest.raises(ValueError):
        pr.denda_keterlambatan(-1)


def test_perontok_properti_dasar() -> None:
    """Menguji properti kode dan nama pada Perontok."""
    pr = Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900)
    assert pr.kode == "PR-01"
    assert pr.nama == "Mesin Perontok Padi"
    assert pr.tarif_harian == 200_000