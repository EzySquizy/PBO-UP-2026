
"""Model domain: traktor sebagai alat pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Alat pertanian berupa traktor yang memerlukan operator."""

    ONGKOS_OPERATOR_HARIAN: Final[int] = 100_000

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        tenaga_kuda: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if tenaga_kuda <= 0:
            raise ValueError("tenaga kuda harus lebih dari 0")

        self._tenaga_kuda = tenaga_kuda

    @property
    def tenaga_kuda(self) -> int:
        return self._tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + self.ONGKOS_OPERATOR_HARIAN * jumlah_hari

    def keterangan(self) -> str:
        return (
            f"{super().keterangan()} · "
            f"{self._tenaga_kuda} HP · termasuk operator"
        )
