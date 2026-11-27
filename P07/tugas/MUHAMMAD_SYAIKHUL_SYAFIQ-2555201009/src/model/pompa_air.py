
"""Model domain: pompa air pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Alat pertanian berupa pompa air."""

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
            raise ValueError("debit harus lebih dari nol")

        self._debit = debit

    @property
    def debit(self) -> int:
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        """Menghitung kebutuhan solar per hari."""
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung tarif pompa beserta biaya solar."""
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        biaya_solar = (
            self.konsumsi_solar_harian()
            * self.HARGA_SOLAR_PER_LITER
            * jumlah_hari
        )
        return biaya_dasar + biaya_solar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat pompa dari kode;nama;tarif;debit."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError("baris pompa harus berisi 4 bagian")

        kode, nama, tarif, debit = bagian

        try:
            return cls(
                kode.strip(),
                nama.strip(),
                int(tarif.strip()),
                int(debit.strip()),
            )
        except ValueError as kesalahan:
            raise ValueError("data pompa tidak valid") from kesalahan
