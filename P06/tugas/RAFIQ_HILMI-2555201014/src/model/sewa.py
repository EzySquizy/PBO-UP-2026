
"""Model domain: transaksi penyewaan alat."""

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Transaksi penyewaan alat oleh seorang penyewa."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("Nomor sewa tidak boleh kosong.")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        """Mengembalikan rincian sebagai tuple agar tidak bisa diubah dari luar."""
        return tuple(self._baris)

    def jumlah_alat(self) -> int:
        return len(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        """Menambahkan alat ke transaksi."""
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("Maksimal 10 alat dalam satu transaksi.")

        if any(baris.kode_alat == alat.kode for baris in self._baris):
            raise ValueError("Alat tersebut sudah ada dalam transaksi.")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        """Menghitung total seluruh biaya penyewaan."""
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        """Menghasilkan nota transaksi penyewaan."""
        rincian = "\n".join(baris.baris_nota() for baris in self._baris)

        return (
            f"NOTA PENYEWAAN ALAT\n"
            f"Nomor       : {self._nomor}\n"
            f"Penyewa     : {self._penyewa.identitas()}\n"
            f"{'-' * 70}\n"
            f"{rincian}\n"
            f"{'-' * 70}\n"
            f"TOTAL       : {AlatTani.format_rupiah(self.total())}"
        )
