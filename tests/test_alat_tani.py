
from src.model.alat_tani import AlatTani


def test_biaya_sewa():
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(2) == 300000


def test_keterangan():
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"


def test_biaya_sewa_pompa():
    alat = AlatTani("AL-02", "Pompa Air", 50000)
    assert alat.biaya_sewa(3) == 150000
