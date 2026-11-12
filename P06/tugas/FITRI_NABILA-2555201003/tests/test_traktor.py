import pytest
from src.model.traktor import Traktor


def test_validasi_induk_tetap_berlaku_pada_traktor() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Roda Dua", -5_000, 8)


def test_traktor_biaya_sewa_dengan_operator() -> None:
    tr = Traktor("TR-01", "Traktor Roda Dua Kubota", 150_000, 8)
    assert tr.biaya_sewa(1) == 250_000
    assert tr.biaya_sewa(3) == 750_000


def test_traktor_dapat_menjadi_kunci_dict() -> None:
    tr = Traktor("TR-01", "Traktor", 150_000, 8)
    catatan = {tr: "sedang disewa"}
    assert catatan[Traktor("TR-01", "Lain", 160_000, 9)] == "sedang disewa"


def test_traktor_dapat_dimasukkan_ke_set() -> None:
    t1 = Traktor("TR-01", "Traktor A", 150_000, 8)
    t2 = Traktor("TR-01", "Traktor B", 160_000, 9)
    s = {t1}
    s.add(t2)
    assert len(s) == 1


def test_traktor_dibandingkan_dengan_bukan_alat() -> None:
    assert (Traktor("TR-01", "Traktor", 150_000, 8) == "TR-01") is False


def test_traktor_str_dan_repr() -> None:
    tr = Traktor("TR-01", "Traktor Roda Dua Kubota", 150_000, 8)
    assert str(tr) == tr.keterangan()
    assert "Traktor" in repr(tr)
    assert "TR-01" in repr(tr)

def test_traktor_tarif_maksimum() -> None:
    """Menguji bahwa Traktor menolak tarif yang melebihi batas maksimum UPJA."""
    with pytest.raises(ValueError):
        Traktor("TR-02", "Traktor Mahal", 6_000_000, 8)


def test_traktor_denda_keterlambatan() -> None:
    """Menguji perhitungan denda keterlambatan sewa Traktor."""
    tr = Traktor("TR-01", "Traktor", 150_000, 8)
    assert tr.denda_keterlambatan(2) == 30_000