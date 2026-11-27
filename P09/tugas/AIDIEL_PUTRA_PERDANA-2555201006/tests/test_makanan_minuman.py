import pytest
from src.model.makanan_minuman import MakananMinuman


def test_makanan_minuman_subtotal_dan_penyimpanan() -> None:
    biskuit = MakananMinuman("MM-01", "Biskuit Kaleng", 25_000, 15, "2027-05-10")
    assert biskuit.hitung_subtotal(2) == 50_000
    assert "2027-05-10" in biskuit.aturan_penyimpanan()


def test_makanan_minuman_menolak_kedaluwarsa_kosong() -> None:
    with pytest.raises(ValueError):
        MakananMinuman("MM-02", "Teh Botol", 5_000, 20, "   ")