
from src.model.pegawai.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak Kantor Camat Bangkinang Kota."""

    PERSEN_PENYESUAIAN = 10

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_kontrak: int,
        transportasi: int,
    ) -> None:
        super().__init__(nip, nama, gaji_kontrak)

        if transportasi < 0:
            raise ValueError("Transportasi tidak boleh negatif")

        self._transportasi = transportasi

    def hitung_penghasilan(self, penyesuaian: int = 0) -> int:
        """Menambahkan penyesuaian 10 persen sebelum memanggil kelas induk."""
        penyesuaian_kontrak = (
            penyesuaian
            + (self._gaji_pokok * self.PERSEN_PENYESUAIAN // 100)
            + self._transportasi
        )

        return super().hitung_penghasilan(penyesuaian_kontrak)
