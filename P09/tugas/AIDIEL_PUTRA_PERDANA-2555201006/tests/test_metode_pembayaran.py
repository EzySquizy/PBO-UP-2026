import pytest
from src.model.metode_pembayaran import MetodePembayaran


def test_metode_pembayaran_tidak_dikenal_ditolak() -> None:
    with pytest.raises(ValueError):
        MetodePembayaran("bon_hutang")


def test_metode_pembayaran_aturan_kembalian() -> None:
    assert MetodePembayaran.CASH.perlu_kembalian() is True
    assert MetodePembayaran.TRANSFER.perlu_kembalian() is False
    assert MetodePembayaran.QRIS.perlu_kembalian() is False