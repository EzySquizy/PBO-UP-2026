
"""Status transaksi penyewaan."""

from enum import Enum


class StatusSewa(Enum):
    """Mewakili status suatu transaksi penyewaan."""

    DIPESAN = "dipesan"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    BATAL = "batal"

    def boleh_diubah(self) -> bool:
        """Memeriksa apakah status transaksi masih boleh diubah."""
        return self in (
            StatusSewa.DIPESAN,
            StatusSewa.BERJALAN,
        )
