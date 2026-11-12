"""Model domain: transaksi penyewaan alat tani."""

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Mengelola penyewaan alat tani oleh seorang penyewa."""

    BATAS_ALAT_PER_SEWA = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        """Membuat transaksi dengan penyewa yang sudah tersedia."""
        if not nomor.strip():
            raise ValueError("Nomor sewa tidak boleh kosong.")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def nomor(self) -> str:
        """Mengembalikan nomor transaksi."""
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        """Mengembalikan penyewa transaksi."""
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        """Mengembalikan baris sewa sebagai tuple."""
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        """Menambahkan alat ke transaksi."""
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("Jumlah alat dalam sewa sudah mencapai batas.")

        if any(item.kode_alat == alat.kode for item in self._baris):
            raise ValueError("Alat yang sama tidak boleh ditambahkan dua kali.")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        """Menghitung total biaya berdasarkan tarif historis."""
        return sum(item.subtotal() for item in self._baris)

    def nota(self) -> str:
        """Menghasilkan nota transaksi penyewaan."""
        rincian = "\n".join(item.baris_nota() for item in self._baris)
        total = AlatTani.format_rupiah(self.total())
        return (
            f"Nomor sewa: {self._nomor}\n"
            f"Penyewa: {self._penyewa.identitas()}\n"
            f"{rincian}\n"
            f"Total: {total}"
        )
