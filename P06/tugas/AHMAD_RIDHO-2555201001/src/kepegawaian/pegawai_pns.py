"""Model pegawai PNS pada instansi di Kabupaten Kampar."""

from src.kepegawaian.pegawai import Pegawai


class PegawaiPNS(Pegawai):
    """Pegawai PNS yang memperoleh tunjangan jabatan."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan_jabatan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tunjangan_jabatan < 0:
            raise ValueError("tunjangan jabatan tidak boleh negatif")

        self._tunjangan_jabatan = tunjangan_jabatan

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        """Menghitung gaji pokok ditambah tunjangan jabatan."""
        dasar = super().hitung_penghasilan(jumlah_bulan)
        tunjangan = self._tunjangan_jabatan * jumlah_bulan
        return dasar + tunjangan
