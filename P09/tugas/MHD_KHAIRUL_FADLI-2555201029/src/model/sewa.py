
"""Model domain: transaksi penyewaan alat pertanian."""

from enum import Enum

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class StatusSewa(Enum):
    """Status yang mungkin dimiliki transaksi penyewaan."""

    DIPESAN = "dipesan"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    BATAL = "batal"

    def boleh_diubah(self) -> bool:
        """Memeriksa apakah transaksi masih boleh diubah."""
        return self in (
            StatusSewa.DIPESAN,
            StatusSewa.BERJALAN,
        )


class Sewa:
    """Transaksi penyewaan alat oleh seorang penyewa."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []
        self._status = StatusSewa.DIPESAN

    @property
    def nomor(self) -> str:
        """Nomor transaksi sewa."""
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        """Penyewa yang melakukan transaksi."""
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        """Daftar baris sewa dalam bentuk tuple."""
        return tuple(self._baris)

    @property
    def status(self) -> StatusSewa:
        """Status transaksi penyewaan."""
        return self._status

    def ubah_status(self, status: StatusSewa) -> None:
        """Mengubah status transaksi penyewaan."""
        if not isinstance(status, StatusSewa):
            raise TypeError("status sewa tidak valid")

        if not self._status.boleh_diubah():
            raise ValueError(
                f"status {self._status.value} tidak dapat diubah"
            )

        self._status = status

    def tambah_alat(
        self,
        alat: AlatTani,
        jumlah_hari: int,
    ) -> None:
        """Menambahkan alat ke dalam transaksi sewa."""

        if not self._status.boleh_diubah():
            raise ValueError(
                "alat tidak dapat ditambahkan pada status "
                f"{self._status.value}"
            )

        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError(
                "jumlah alat dalam satu transaksi tidak boleh "
                f"lebih dari {self.BATAS_ALAT_PER_SEWA}"
            )

        for baris in self._baris:
            if baris.kode_alat == alat.kode:
                raise ValueError(
                    f"alat dengan kode {alat.kode} sudah ditambahkan"
                )

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        """Menghitung total biaya seluruh alat yang disewa."""
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        """Membuat nota transaksi penyewaan."""
        hasil = [
            f"NOTA PENYEWAAN: {self._nomor}",
            f"Penyewa: {self._penyewa.identitas()}",
            f"Status: {self._status.value}",
            "-" * 60,
        ]

        for baris in self._baris:
            subtotal = AlatTani.format_rupiah(baris.subtotal())
            tarif = AlatTani.format_rupiah(baris.tarif_saat_sewa)

            hasil.append(
                f"{baris.kode_alat} - {baris.nama_alat} | "
                f"{baris.jumlah_hari} hari x {tarif} = {subtotal}"
            )

        hasil.extend([
            "-" * 60,
            f"TOTAL: {AlatTani.format_rupiah(self.total())}",
        ])

        return "\n".join(hasil)
