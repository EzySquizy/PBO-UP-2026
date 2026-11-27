from enum import Enum

class StatusSewa(Enum):
    """Empat keadaan yang mungkin dialami sebuah transaksi sewa."""
    DIPESAN = "dipesan"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    BATAL = "batal"

    def boleh_diubah(self) -> bool:
        """Transaksi yang selesai atau batal tidak boleh diubah lagi."""
        return self in (StatusSewa.DIPESAN, StatusSewa.BERJALAN)
