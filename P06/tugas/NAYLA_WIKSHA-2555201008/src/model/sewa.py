
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Mewakili transaksi penyewaan alat tani."""

    BATAS_ALAT_PER_SEWA = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        """Menginisialisasi transaksi penyewaan."""
        if not nomor.strip():
            raise ValueError("Nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        """Mengembalikan baris sewa dalam bentuk tuple."""
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        """Menambahkan alat ke transaksi penyewaan."""
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("Maksimal 10 alat dalam satu transaksi")

        if any(baris.kode_alat == alat.kode for baris in self._baris):
            raise ValueError("Alat yang sama tidak boleh ditambahkan dua kali")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        """Menghitung total seluruh baris penyewaan."""
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        """Menghasilkan nota transaksi penyewaan."""
        garis = "-" * 68
        rincian = "\n".join(baris.baris_nota() for baris in self._baris)

        return (
            f"NOTA SEWA {self._nomor}\n"
            f"{self._penyewa.identitas()}\n"
            f"{garis}\n"
            f"{rincian}\n"
            f"{garis}\n"
            f"TOTAL: {AlatTani.format_rupiah(self.total())}"
        )
