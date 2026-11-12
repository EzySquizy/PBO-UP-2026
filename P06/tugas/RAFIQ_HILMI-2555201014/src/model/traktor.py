"""Model khusus untuk alat traktor."""

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Traktor yang membutuhkan biaya operator."""

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
            raise ValueError(
                f"tenaga kuda harus lebih dari nol, diterima {tenaga_kuda}"
            )

        self._tenaga_kuda = tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa ditambah ongkos operator."""
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + Traktor.ONGKOS_OPERATOR_HARIAN * jumlah_hari
