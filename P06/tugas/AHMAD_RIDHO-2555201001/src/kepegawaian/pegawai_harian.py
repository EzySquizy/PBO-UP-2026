"""Model pegawai harian pada instansi di Kabupaten Kampar."""

from src.kepegawaian.pegawai import Pegawai


class PegawaiHarian(Pegawai):
    """Pegawai yang penghasilannya dihitung berdasarkan tarif harian."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tarif_harian: int,
        hari_kerja_per_bulan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tarif_harian <= 0:
            raise ValueError("tarif harian harus lebih dari nol")
        if hari_kerja_per_bulan <= 0:
            raise ValueError("hari kerja harus lebih dari nol")

        self._tarif_harian = tarif_harian
        self._hari_kerja_per_bulan = hari_kerja_per_bulan

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        """Menghitung penghasilan dari tarif dan hari kerja."""
        if jumlah_bulan <= 0:
            raise ValueError("jumlah bulan harus lebih dari nol")

        return (
            self._tarif_harian
            * self._hari_kerja_per_bulan
            * jumlah_bulan
        )
