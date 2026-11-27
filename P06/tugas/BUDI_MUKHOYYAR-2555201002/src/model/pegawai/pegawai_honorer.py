
from src.model.pegawai.pegawai import Pegawai


class PegawaiHonorer(Pegawai):
    """Pegawai honorer Kantor Camat Bangkinang Kota."""

    def __init__(
        self,
        nip: str,
        nama: str,
        tarif_per_jam: int,
        jam_kerja: int,
    ) -> None:
        super().__init__(nip, nama, 0)

        if tarif_per_jam <= 0:
            raise ValueError("Tarif per jam harus lebih dari nol")
        if jam_kerja < 0:
            raise ValueError("Jam kerja tidak boleh negatif")

        self._tarif_per_jam = tarif_per_jam
        self._jam_kerja = jam_kerja

    def hitung_penghasilan(self, penyesuaian: int = 0) -> int:
        """Penghasilan dihitung dari tarif per jam dikali jam kerja."""
        hasil = (self._tarif_per_jam * self._jam_kerja) + penyesuaian

        if hasil < 0:
            raise ValueError("Penghasilan tidak boleh negatif")

        return hasil
