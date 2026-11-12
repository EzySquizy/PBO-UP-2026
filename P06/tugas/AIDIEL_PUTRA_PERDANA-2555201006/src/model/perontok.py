from typing import Final

from src.model.alat_tani import AlatTani

class Perontok(AlatTani):
    """Mesin perontok padi. Biaya angkutnya besar, jadi ada minimum sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2

    def __init__(self, kode: str, nama: str, tarif_harian: int, kapasitas: int) -> None:
        super().__init__(kode, nama, tarif_harian)
        self._kapasitas: int = kapasitas

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Hari yang benar-benar ditagih, memperhitungkan batas minimum."""
        return max(jumlah_hari, Perontok.MINIMUM_HARI_SEWA)
    
    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menagih sekurang-kurangnya dua hari, meski disewa lebih singkat."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))

    def __str__(self) -> str:
        """Untuk dibaca manusia: dipakai print() dan f-string."""
        return self.keterangan()
    
    def __repr__(self) -> str:
        """Untuk dibaca pemrogram: dipakai saat menampilkan isi koleksi."""
        return (f"{type(self).__name__}(kode={self._kode!r}, "
        f"nama={self._nama!r}, tarif_harian={self._tarif_harian!r})")

    def __eq__(self, lain: object) -> bool:
        """Dua alat dianggap sama bila kodenya sama, karena kode itu identitas."""
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode
    
    def __hash__(self) -> int:
        """Wajib ditulis bersama __eq__ agar alat tetap dapat dimasukkan set."""
        return hash(self._kode)
