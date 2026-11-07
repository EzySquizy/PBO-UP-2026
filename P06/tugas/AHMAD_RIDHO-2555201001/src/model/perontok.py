"""Model mesin perontok padi sebagai jenis alat tani."""

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi dengan minimum sewa dua hari."""

    MINIMUM_HARI_SEWA: Final[int] = 2

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
    def hari_ditagih(cls, jumlah_hari: int) -> int:
        return max(jumlah_hari, cls.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
