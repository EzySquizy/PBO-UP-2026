"""Pengujian untuk kelas AlatTani."""
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert "TR-01" in alat.keterangan()
    assert "Traktor" in alat.keterangan()


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("PA-01", "Pompa Air", 75000)
    assert alat.biaya_sewa(0) == 0