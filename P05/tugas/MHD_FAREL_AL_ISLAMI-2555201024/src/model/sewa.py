"""Model domain: transaksi penyewaan alat pertanian."""

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Transaksi sewa yang memiliki beberapa baris rincian."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")

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
        """Mengembalikan rincian sebagai tuple agar tidak dapat diubah."""
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        """Menambahkan alat ke transaksi dengan komposisi BarisSewa."""
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("jumlah alat dalam satu sewa sudah mencapai batas")

        for baris in self._baris:
            if baris.kode_alat == alat.kode:
                raise ValueError(f"alat {alat.kode} sudah ditambahkan")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        """Menghitung total seluruh rincian sewa."""
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        """Menyusun nota transaksi penyewaan."""
        garis = "-" * 68
        rincian = "\n".join(baris.baris_nota() for baris in self._baris)

        return (
            f"NOTA SEWA {self._nomor}\n"
            f"Penyewa: {self._penyewa.identitas()}\n"
            f"{garis}\n"
            f"{rincian}\n"
            f"{garis}\n"
            f"TOTAL: {AlatTani.format_rupiah(self.total())}"
        )
