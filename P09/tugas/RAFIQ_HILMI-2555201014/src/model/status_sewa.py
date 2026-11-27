"""Status penyewaan alat tani."""

from enum import Enum


class StatusSewa(Enum):
    """Pilihan status dalam proses penyewaan."""

    DIPESAN = "dipesan"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    BATAL = "batal"

    def boleh_diubah(self) -> bool:
        """Memeriksa apakah penyewaan masih boleh diubah."""
        return self in (StatusSewa.DIPESAN, StatusSewa.BERJALAN)
