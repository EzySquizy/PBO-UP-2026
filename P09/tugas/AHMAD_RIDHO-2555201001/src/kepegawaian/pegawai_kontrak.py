"""Model pegawai kontrak pada instansi di Kabupaten Kampar."""

from typing import Final

from src.kepegawaian.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan ketentuan minimum masa pembayaran."""

    MINIMUM_BULAN_KONTRAK: Final[int] = 3

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        minimum_bulan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if minimum_bulan <= 0:
            raise ValueError("minimum bulan harus lebih dari nol")

        self._minimum_bulan = minimum_bulan

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        """Mengubah jumlah bulan sebelum menghitung penghasilan."""
        if jumlah_bulan <= 0:
            raise ValueError("jumlah bulan harus lebih dari nol")

        bulan_dibayar = max(jumlah_bulan, self._minimum_bulan)
        return super().hitung_penghasilan(bulan_dibayar)
