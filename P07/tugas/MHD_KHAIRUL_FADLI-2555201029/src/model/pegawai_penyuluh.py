
"""Model pegawai penyuluh."""

from typing import Final

from .pegawai import Pegawai


class PegawaiPenyuluh(Pegawai):
    """Pegawai penyuluh dengan honor berdasarkan jumlah kegiatan."""

    HONOR_PER_KEGIATAN: Final[int] = 150_000

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        jumlah_kegiatan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if jumlah_kegiatan < 0:
            raise ValueError("jumlah kegiatan tidak boleh negatif")

        self._jumlah_kegiatan = jumlah_kegiatan

    @property
    def jumlah_kegiatan(self) -> int:
        """Mengembalikan jumlah kegiatan penyuluhan."""
        return self._jumlah_kegiatan

    def hitung_penghasilan(self, hari_kerja: int) -> int:
        """Menghitung penghasilan dari gaji dan honor kegiatan."""
        penghasilan_pokok = super().hitung_penghasilan(hari_kerja)
        honor = self._jumlah_kegiatan * self.HONOR_PER_KEGIATAN

        return penghasilan_pokok + honor
