"""Model pegawai kontrak Dinas Pertanian Kabupaten Kampar."""

from src.model.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan batas durasi pembayaran."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok_harian: int,
        durasi_kontrak: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok_harian)

        if durasi_kontrak <= 0:
            raise ValueError("Durasi kontrak harus lebih dari nol")

        self._durasi_kontrak = durasi_kontrak

    @property
    def durasi_kontrak(self) -> int:
        return self._durasi_kontrak

    def hitung_gaji(self, jumlah_hari: int) -> int:
        """Membatasi hari pembayaran sesuai durasi kontrak."""
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        hari_dibayar = min(jumlah_hari, self._durasi_kontrak)
        return super().hitung_gaji(hari_dibayar)