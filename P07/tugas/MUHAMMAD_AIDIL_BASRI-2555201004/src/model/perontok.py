
"""Model domain: mesin perontok padi."""

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok dengan ketentuan minimum dua hari sewa."""

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
            raise ValueError("kapasitas harus lebih dari 0")

        self._kapasitas = kapasitas

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    def hari_ditagih(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari 0")
        return max(jumlah_hari, self.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))

    def keterangan(self) -> str:
        return (
            f"{super().keterangan()} · "
            f"{self._kapasitas} kg/jam · minimum 2 hari"
        )
