from typing import Final
from src.model.alat_tani import AlatTani
class Traktor(AlatTani):
    """Traktor roda dua. Wajib dioperasikan petugas UPJA."""

    ONGKOS_OPERATOR_HARIAN: Final[int] = 100_000

    def __init__(self, kode: str, nama: str, tarif_harian: int, tenaga_kuda: int) -> None:
        super().__init__(kode, nama, tarif_harian) # ← WAJIB, dan duluan
        if tenaga_kuda <= 0:
            raise ValueError(
                f"tenaga kuda harus lebih dari nol, diterima {tenaga_kuda}")
        self._tenaga_kuda = tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Biaya dasar ditambah ongkos operator untuk setiap hari sewa."""
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + Traktor.ONGKOS_OPERATOR_HARIAN * jumlah_hari

    def __str__(self) -> str:
        return self.keterangan()
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(kode={self._kode!r}, nama={self._nama!r}, tarif_harian={self._tarif_harian!r})"

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode
    
    def __hash__(self) -> int:
        return hash(self._kode)