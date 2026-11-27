
"""Enum untuk status transaksi penyewaan."""

from enum import Enum


class StatusSewa(Enum):
    """Status yang tersedia dalam transaksi penyewaan."""

    DIPESAN = "dipesan"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    BATAL = "batal"

    def boleh_diubah(self) -> bool:
        """Menentukan apakah transaksi masih boleh ditambah alat."""
        return self in (StatusSewa.DIPESAN, StatusSewa.BERJALAN)
