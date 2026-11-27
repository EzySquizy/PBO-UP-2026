"""Model pegawai harian."""

from src.pegawai import Pegawai


class PegawaiHarian(Pegawai):
    """Pegawai yang penghasilannya berdasarkan jumlah hari kerja."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        upah_harian: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if upah_harian <= 0:
            raise ValueError("Upah harian harus lebih dari nol.")

        self._upah_harian = upah_harian

    def hitung_penghasilan(self, jumlah_periode: int) -> int:
        """Menghitung penghasilan dari upah harian."""
        if jumlah_periode <= 0:
            raise ValueError("Jumlah hari kerja harus lebih dari nol.")

        return self._upah_harian * jumlah_periode
