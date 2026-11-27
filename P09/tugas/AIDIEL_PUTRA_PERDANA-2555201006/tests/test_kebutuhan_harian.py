import pytest
from src.model.kebutuhan_harian import KebutuhanHarian


def test_kebutuhan_harian_subtotal_dan_zona_rak() -> None:
    sabun = KebutuhanHarian("KH-01", "Sabun Mandi Cair", 20_000, 10, zona_rak="Rak B")
    assert sabun.hitung_subtotal(3) == 60_000
    assert "Rak B" in sabun.aturan_penyimpanan()


def test_kebutuhan_harian_menolak_zona_kosong() -> None:
    with pytest.raises(ValueError):
        KebutuhanHarian("KH-02", "Deterjen", 15_000, 8, zona_rak="")