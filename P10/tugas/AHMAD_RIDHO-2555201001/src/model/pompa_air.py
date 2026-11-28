
"""Model pompa air sebagai jenis alat tani."""

from typing import ClassVar

from src.model.alat_tani import AlatTani
from src.model.galat import BarisPendataanRusak, DataTidakValid


class PompaAir(AlatTani):
    """Pompa air bermesin dengan biaya solar sesuai debitnya."""

    HARGA_SOLAR_PER_LITER: ClassVar[int] = 7_000
    LITER_PER_SERATUS_DEBIT: ClassVar[int] = 3
    JUMLAH_KOLOM_POMPA_CSV: ClassVar[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if debit <= 0:
            raise DataTidakValid(
                f"debit harus lebih dari nol, diterima {debit}"
            )

        self._debit = debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat pompa air dari satu baris CSV."""
        bagian = baris.strip().split(AlatTani.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_POMPA_CSV:
            raise BarisPendataanRusak(
                f"baris pompa air harus berisi "
                f"{cls.JUMLAH_KOLOM_POMPA_CSV} bagian, "
                f"diterima {len(bagian)}"
            )

        kode, nama, tarif, debit = bagian

        if not tarif.strip().isdigit() or not debit.strip().isdigit():
            raise DataTidakValid("tarif dan debit harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
            int(debit),
        )

    def konsumsi_solar_harian(self) -> int:
        """Menghitung perkiraan pemakaian solar per hari."""
        return (self._debit * PompaAir.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung biaya solar selama masa sewa."""
        solar_per_hari = (
            self.konsumsi_solar_harian()
            * PompaAir.HARGA_SOLAR_PER_LITER
        )
        return solar_per_hari * jumlah_hari

    def syarat_pemakaian(self) -> str:
        """Menjelaskan syarat penggunaan pompa air."""
        return "Membutuhkan bahan bakar solar selama pengoperasian."
