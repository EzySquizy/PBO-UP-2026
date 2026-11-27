
"""Model domain: transaksi penyewaan alat pertanian."""

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Transaksi penyewaan alat oleh seorang penyewa."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

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

    def tambah_alat(
        self,
        alat: AlatTani,
        jumlah_hari: int,
    ) -> None:
        """Menambahkan alat ke dalam transaksi sewa."""

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
