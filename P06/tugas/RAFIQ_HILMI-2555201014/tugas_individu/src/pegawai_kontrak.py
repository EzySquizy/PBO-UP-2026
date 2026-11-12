"""Model pegawai kontrak."""

from src.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan minimal satu bulan penggajian."""

    MINIMUM_BULAN: int = 1

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        lama_kontrak: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if lama_kontrak <= 0:
            raise ValueError("Lama kontrak harus lebih dari nol.")

        self._lama_kontrak = lama_kontrak

    def hitung_penghasilan(self, jumlah_periode: int) -> int:
        """Menghitung penghasilan sesuai lama kontrak."""
        bulan_dibayar = min(
            max(jumlah_periode, self.MINIMUM_BULAN),
            self._lama_kontrak,
        )
        return super().hitung_penghasilan(bulan_dibayar)
