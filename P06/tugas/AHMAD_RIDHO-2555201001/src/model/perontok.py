"""Model mesin perontok padi sebagai jenis alat tani."""

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi dengan minimum sewa dua hari."""

    MINIMUM_HARI_SEWA: Final[int] = 2
    JUMLAH_KOLOM_PERONTOK_CSV: Final[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if kapasitas <= 0:
            raise ValueError(
                f"kapasitas harus lebih dari nol, diterima {kapasitas}"
            )

        self._kapasitas = kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat mesin perontok dari satu baris CSV."""
        bagian = baris.strip().split(AlatTani.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_PERONTOK_CSV:
            raise ValueError(
                f"baris perontok harus berisi "
                f"{cls.JUMLAH_KOLOM_PERONTOK_CSV} bagian, "
                f"diterima {len(bagian)}"
            )

        kode, nama, tarif, kapasitas = bagian

        if not tarif.strip().isdigit() or not kapasitas.strip().isdigit():
            raise ValueError("tarif dan kapasitas harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
            int(kapasitas),
        )

    @classmethod
    def hari_ditagih(cls, jumlah_hari: int) -> int:
        return max(jumlah_hari, cls.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
