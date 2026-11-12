from typing import Final
from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air bermesin. Penyewa dikenakan biaya solar sesuai debitnya."""
    
    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3

    def __init__(self, kode: str, nama: str, tarif_harian: int, debit: int) -> None:
        super().__init__(kode, nama, tarif_harian)
        if debit <= 0:
            raise ValueError(f"Debit harus lebih dari nol, diterima {debit}")
        self._debit: int = debit

    def konsumsi_solar_harian(self) -> int:
        """Perkiraan pemakaian solar dalam liter untuk satu hari."""
        return (self._debit * PompaAir.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        dasar = super().biaya_sewa(jumlah_hari)
        solar = self.konsumsi_solar_harian() * PompaAir.HARGA_SOLAR_PER_LITER
        return dasar + solar * jumlah_hari

    def __str__(self) -> str:
        """Untuk dibaca manusia: dipakai print() dan f-string."""
        return self.keterangan()

    def __repr__(self) -> str:
        """Untuk dibaca pemrogram: dipakai saat menampilkan isi koleksi."""
        return (f"{type(self).__name__}(kode={self._kode!r}, "
                f"nama={self._nama!r}, tarif_harian={self._tarif_harian!r})")

    def __eq__(self, lain: object) -> bool:
        """Dua alat dianggap sama bila kodenya sama."""
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode

    def __hash__(self) -> int:
        """Wajib ditulis bersama __eq__ agar alat dapat dimasukkan set/dict."""
        return hash(self._kode)