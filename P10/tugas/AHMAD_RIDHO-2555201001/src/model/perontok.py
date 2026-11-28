
"""Model mesin perontok padi sebagai jenis alat tani."""

from typing import ClassVar

from src.model.alat_tani import AlatTani
from src.model.galat import BarisPendataanRusak, DataTidakValid


class Perontok(AlatTani):
    """Mesin perontok padi dengan minimum sewa dua hari."""

    MINIMUM_HARI_SEWA: ClassVar[int] = 2
    JUMLAH_KOLOM_PERONTOK_CSV: ClassVar[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if kapasitas <= 0:
            raise DataTidakValid(
                f"kapasitas harus lebih dari nol, diterima {kapasitas}"
            )

        self._kapasitas = kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat mesin perontok dari satu baris CSV."""
        bagian = baris.strip().split(AlatTani.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_PERONTOK_CSV:
            raise BarisPendataanRusak(
                f"baris perontok harus berisi "
                f"{cls.JUMLAH_KOLOM_PERONTOK_CSV} bagian, "
                f"diterima {len(bagian)}"
            )

        kode, nama, tarif, kapasitas = bagian

        if not tarif.strip().isdigit() or not kapasitas.strip().isdigit():
            raise DataTidakValid("tarif dan kapasitas harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
            int(kapasitas),
        )

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Menentukan minimum masa sewa dua hari."""
        return max(
            super().hari_ditagih(jumlah_hari),
            self.MINIMUM_HARI_SEWA,
        )

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Perontok tidak memiliki biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Menjelaskan syarat penggunaan mesin perontok."""
        return "Digunakan sesuai kapasitas mesin."
