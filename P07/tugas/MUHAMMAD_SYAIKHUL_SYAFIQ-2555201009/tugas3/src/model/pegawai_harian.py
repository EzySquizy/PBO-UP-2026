"""Model pegawai harian Dinas Pertanian Kabupaten Kampar."""

from src.model.pegawai import Pegawai


class PegawaiHarian(Pegawai):
    """Pegawai harian dengan perhitungan berdasarkan upah per jam."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok_harian: int,
        upah_per_jam: int,
        jam_per_hari: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok_harian)

        if upah_per_jam <= 0:
            raise ValueError("Upah per jam harus lebih dari nol")
        if jam_per_hari <= 0:
            raise ValueError("Jam kerja harus lebih dari nol")

        self._upah_per_jam = upah_per_jam
        self._jam_per_hari = jam_per_hari

    @property
    def upah_per_jam(self) -> int:
        return self._upah_per_jam

    @property
    def jam_per_hari(self) -> int:
        return self._jam_per_hari

    def hitung_gaji(self, jumlah_hari: int) -> int:
        """Menghitung gaji dari upah per jam dan jam kerja."""
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        return (
            self._upah_per_jam
            * self._jam_per_hari
            * jumlah_hari
        )