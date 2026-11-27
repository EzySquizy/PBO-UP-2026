
from src.model.pegawai.pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Pegawai tetap Kantor Camat Bangkinang Kota."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tunjangan < 0:
            raise ValueError("Tunjangan tidak boleh negatif")

        self._tunjangan = tunjangan

    def hitung_penghasilan(self, penyesuaian: int = 0) -> int:
        """Penghasilan terdiri dari gaji pokok, tunjangan, dan penyesuaian."""
        return super().hitung_penghasilan(
            penyesuaian + self._tunjangan
        )
