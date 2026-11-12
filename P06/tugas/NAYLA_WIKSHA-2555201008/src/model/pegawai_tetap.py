
from src.model.pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Mewakili pegawai tetap pada instansi."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        gaji_pokok: int,
        tunjangan: int,
    ) -> None:
        super().__init__(nip, nama, jabatan, gaji_pokok)

        if tunjangan < 0:
            raise ValueError("Tunjangan tidak boleh negatif")

        self._tunjangan = tunjangan

    @property
    def tunjangan(self) -> int:
        return self._tunjangan

    def hitung_penghasilan(self) -> int:
        dasar = super().hitung_penghasilan()
        return dasar + self._tunjangan
