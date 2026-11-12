
from src.model.pegawai import Pegawai


class PegawaiHarian(Pegawai):
    """Mewakili pegawai harian pada instansi."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        gaji_pokok: int,
        hari_kerja: int,
    ) -> None:
        super().__init__(nip, nama, jabatan, gaji_pokok)

        if hari_kerja <= 0:
            raise ValueError("Hari kerja harus lebih dari nol")

        self._hari_kerja = hari_kerja

    @property
    def hari_kerja(self) -> int:
        return self._hari_kerja

    def hitung_penghasilan(self) -> int:
        return self.gaji_pokok * self._hari_kerja
