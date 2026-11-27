
"""Model domain: pompa air sebagai alat pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air yang membutuhkan bahan bakar solar."""

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
            raise ValueError("debit harus lebih dari 0")

        self._debit = debit

    @property
    def debit(self) -> int:
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        return (self._debit * self.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        dasar = super().biaya_sewa(jumlah_hari)
        biaya_solar = (
            self.konsumsi_solar_harian()
            * self.HARGA_SOLAR_PER_LITER
            * jumlah_hari
        )
        return dasar + biaya_solar

    def keterangan(self) -> str:
        return (
            f"{super().keterangan()} · "
            f"{self._debit} L/mnt · "
            f"±{self.konsumsi_solar_harian()} L solar/hari"
        )
