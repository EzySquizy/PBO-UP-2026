from enum import Enum


class MetodePembayaran(Enum):
    """Tiga metode pembayaran yang diterima kasir SRC Datuk."""

    CASH = "cash"
    TRANSFER = "transfer"
    QRIS = "qris"

    def perlu_kembalian(self) -> bool:
        """Hanya pembayaran tunai (cash) yang menghitung uang kembalian."""
        return self == MetodePembayaran.CASH