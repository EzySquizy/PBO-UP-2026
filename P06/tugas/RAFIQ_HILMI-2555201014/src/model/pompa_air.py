"""Model khusus untuk pompa air."""

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air bermesin dengan biaya solar sesuai debitnya."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3
    JUMLAH_BAGIAN_CSV: Final[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        self._debit = debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat pompa air dari satu baris data CSV."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_BAGIAN_CSV:
            raise ValueError(
                f"baris harus berisi 4 bagian, diterima {len(bagian)}"
            )

        kode, nama, tarif, debit = bagian

        if not tarif.strip().isdigit():
            raise ValueError("Tarif harus berupa angka.")

        if not debit.strip().isdigit():
            raise ValueError("Debit harus berupa angka.")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
            int(debit),
        )

    def konsumsi_solar_harian(self) -> int:
        """Menghitung perkiraan pemakaian solar per hari."""
        return (self._debit * PompaAir.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa ditambah biaya solar."""
        dasar = super().biaya_sewa(jumlah_hari)
        solar = (
            self.konsumsi_solar_harian()
            * PompaAir.HARGA_SOLAR_PER_LITER
        )
        return dasar + solar * jumlah_hari
