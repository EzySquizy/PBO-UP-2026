
"""Mendefinisikan status transaksi penyewaan."""

from enum import Enum


class StatusSewa(Enum):
    """Pilihan status yang berlaku untuk transaksi sewa."""

    DIBUAT = "dibuat"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    DIBATALKAN = "dibatalkan"

    def keterangan(self) -> str:
        """Mengembalikan keterangan status dalam bahasa Indonesia."""
        keterangan_status = {
            StatusSewa.DIBUAT: "Transaksi telah dibuat.",
            StatusSewa.BERJALAN: "Penyewaan sedang berjalan.",
            StatusSewa.SELESAI: "Penyewaan telah selesai.",
            StatusSewa.DIBATALKAN: "Penyewaan telah dibatalkan.",
        }
        return keterangan_status[self]
