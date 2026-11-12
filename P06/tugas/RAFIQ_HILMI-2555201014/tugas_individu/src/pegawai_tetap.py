"""Model pegawai tetap."""

from src.pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Pegawai tetap yang memperoleh tunjangan bulanan."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tunjangan < 0:
            raise ValueError("Tunjangan tidak boleh minus.")

        self._tunjangan = tunjangan

    def hitung_penghasilan(self, jumlah_periode: int) -> int:
        """Menghitung gaji pokok ditambah tunjangan."""
        dasar = super().hitung_penghasilan(jumlah_periode)
        return dasar + (self._tunjangan * jumlah_periode)
