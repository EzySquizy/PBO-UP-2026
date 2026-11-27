import pytest
from src.model.sembako import Sembako


def test_sembako_harga_satuan_dan_potongan_grosir() -> None:
    beras = Sembako("SB-01", "Beras Anak Daro 1kg", 16_000, 50, minimal_grosir=5, potongan_per_unit=500)
    assert beras.hitung_subtotal(3) == 48_000
    assert beras.hitung_subtotal(5) == 77_500


def test_sembako_aturan_penyimpanan_dan_validasi() -> None:
    beras = Sembako("SB-01", "Beras Anak Daro 1kg", 16_000, 50)
    assert "palet kayu" in beras.aturan_penyimpanan()

    with pytest.raises(ValueError):
        Sembako("SB-02", "Minyak Goreng", 18_000, 10, minimal_grosir=0)