
from src.model.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Mewakili pegawai kontrak pada instansi."""

    PERSENTASE_GAJI = 90

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        gaji_pokok: int,
    ) -> None:
        super().__init__(
            nip,
            nama,
            jabatan,
            self._sesuaikan_gaji(gaji_pokok),
        )
        self._persentase_gaji = self.PERSENTASE_GAJI

    @staticmethod
    def _sesuaikan_gaji(gaji_pokok: int) -> int:
        return gaji_pokok * PegawaiKontrak.PERSENTASE_GAJI // 100

    @property
    def persentase_gaji(self) -> int:
        return self._persentase_gaji
