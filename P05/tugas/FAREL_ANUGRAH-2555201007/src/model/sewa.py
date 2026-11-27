"""Model transaksi penyewaan alat pertanian."""

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Transaksi penyewaan milik seorang penyewa."""

    BATAS_ALAT_PER_SEWA = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        """Mengembalikan baris sewa dalam bentuk tuple."""
        return tuple(self._baris)

    def tambah_alat(
        self, alat: AlatTani, jumlah_hari: int
    ) -> None:
        """Menambahkan alat ke dalam transaksi."""
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError(
                "jumlah alat dalam satu transaksi tidak boleh lebih dari 10"
            )

        for baris in self._baris:
            if baris.kode_alat == alat.kode:
                raise ValueError(
                    f"alat {alat.kode} sudah ada dalam transaksi ini"
                )

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def jumlah_alat(self) -> int:
        """Menghitung jumlah jenis alat dalam transaksi."""
        return len(self._baris)

    def total(self) -> int:
        """Menghitung total biaya penyewaan."""
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        """Membuat nota penyewaan."""
        judul = f"NOTA SEWA {self._nomor}"
        kepada = self._penyewa.identitas()
        garis = "-" * 68
        isi = "\n".join(
            baris.baris_nota() for baris in self._baris
        )
        total = AlatTani.format_rupiah(self.total())

        return (
            f"{judul}\n{kepada}\n{garis}\n{isi}\n{garis}\n"
            f"{'TOTAL':<47}{total:>21}"
        )
