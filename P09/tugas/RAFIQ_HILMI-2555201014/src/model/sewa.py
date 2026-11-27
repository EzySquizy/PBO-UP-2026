"""Model untuk mengatur transaksi penyewaan."""

from src.model.sewaan import Sewaan
from src.model.status_sewa import StatusSewa


class Sewa:
    """Mengelola alat yang masuk dalam suatu transaksi penyewaan."""

    def __init__(
        self,
        kode: str,
        status: StatusSewa = StatusSewa.DIPESAN,
    ) -> None:
        self._kode = kode
        self._status = status
        self._alat: list[Sewaan] = []

    @property
    def status(self) -> StatusSewa:
        """Mengembalikan status penyewaan."""
        return self._status

    def ubah_status(self, status: StatusSewa) -> None:
        """Mengubah status penyewaan."""
        self._status = status

    def tambah_alat(self, alat: Sewaan) -> None:
        """Menambahkan alat jika status penyewaan masih memungkinkan."""
        if not self._status.boleh_diubah():
            raise ValueError(
                "Penyewaan yang sudah selesai atau batal tidak dapat diubah."
            )

        self._alat.append(alat)
