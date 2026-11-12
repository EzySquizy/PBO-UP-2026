
"""Model pegawai tetap Dinas Pertanian Kabupaten Kampar."""

from src.model.pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Pegawai tetap dengan tambahan tunjangan harian."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok_harian: int,
        tunjangan_harian: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok_harian)

        if tunjangan_harian < 0:
            raise ValueError("Tunjangan tidak boleh negatif")

        self._tunjangan_harian = tunjangan_harian

    @property
    def tunjangan_harian(self) -> int:
        return self._tunjangan_harian

    def hitung_gaji(self, jumlah_hari: int) -> int:
        """Menghitung gaji pokok ditambah tunjangan harian."""
        gaji_pokok = super().hitung_gaji(jumlah_hari)
        return gaji_pokok + (self._tunjangan_harian * jumlah_hari)
