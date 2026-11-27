import pytest
from src.model.pompa_air import PompaAir


def test_validasi_induk_tetap_berlaku_pada_pompa_air() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-01", "Pompa Air", -10_000, 600)


def test_pompa_air_biaya_sewa_dengan_solar() -> None:
    pa = PompaAir("PA-01", "Pompa Air 3 Inci", 75_000, 600)
    assert pa.biaya_sewa(1) == 201_000
    assert pa.biaya_sewa(3) == 603_000


def test_pompa_air_dapat_menjadi_kunci_dict() -> None:
    pa = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    catatan = {pa: "tersedia"}
    assert catatan[PompaAir("PA-01", "Pompa Air Lain", 80_000, 500)] == "tersedia"


def test_pompa_air_str_dan_repr() -> None:
    pa = PompaAir("PA-01", "Pompa Air 3 Inci", 75_000, 600)
    assert str(pa) == pa.keterangan()
    assert "PompaAir" in repr(pa)
    assert "PA-01" in repr(pa)

def test_pompa_air_debit_tidak_boleh_minus() -> None:
    """Menguji bahwa PompaAir menolak debit nol atau minus."""
    with pytest.raises(ValueError):
        PompaAir("PA-02", "Pompa Rusak", 75_000, 0)


def test_pompa_air_format_rupiah() -> None:
    """Menguji helper format rupiah pada PompaAir."""
    pa = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    assert pa.format_rupiah(150_000) == "Rp150.000"