"""Model domain: transaksi penyewaan alat pertanian."""

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Satu transaksi milik seorang penyewa dan berisi 1 sampai 10 baris."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")
        self._nomor = nomor.strip()
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
        """Mengembalikan snapshot tuple, bukan daftar internal."""
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("jumlah alat dalam satu sewa maksimal 10")
        for item in self._baris:
            if item.kode_alat == alat.kode:
                raise ValueError("alat tersebut sudah ada dalam transaksi")
        self._baris.append(BarisSewa(alat, jumlah_hari))

    def jumlah_alat(self) -> int:
        return len(self._baris)

    def total(self) -> int:
        return sum(item.subtotal() for item in self._baris)

    def nota(self) -> str:
        """Menyusun nota lengkap berdasarkan salinan data setiap baris."""
        judul = f"NOTA SEWA {self._nomor}"
        alamat = self._penyewa.alamat
        kepada = (
            f"{self._penyewa.identitas()} — "
            f"{alamat.kelurahan}, {alamat.kota}"
        )
        garis = "-" * 68
        isi = "\n".join(item.baris_nota() for item in self._baris)
        total = AlatTani.format_rupiah(self.total())
        return (
            f"{judul}\n{kepada}\n{garis}\n{isi}\n{garis}\n"
            f"{'TOTAL':<47}{total:>21}"
        )
