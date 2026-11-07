"""Model pompa air sebagai jenis alat tani."""

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air bermesin dengan biaya solar sesuai debitnya."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if debit <= 0:
            raise ValueError(
                f"debit harus lebih dari nol, diterima {debit}"
            )

        self._debit = debit

    def konsumsi_solar_harian(self) -> int:
        """Menghitung perkiraan pemakaian solar per hari."""
        return (self._debit * PompaAir.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        dasar = super().biaya_sewa(jumlah_hari)
        solar = (
            self.konsumsi_solar_harian()
            * PompaAir.HARGA_SOLAR_PER_LITER
        )
        return dasar + solar * jumlah_hari
