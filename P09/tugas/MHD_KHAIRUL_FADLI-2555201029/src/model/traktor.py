
"""Model alat tani jenis traktor."""

from typing import Final

from .alat_tani import AlatTani


class Traktor(AlatTani):
    """Alat tani traktor dengan biaya operator harian."""

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
            raise ValueError("tenaga kuda harus lebih dari nol")

        self._tenaga_kuda = tenaga_kuda

    @property
    def tenaga_kuda(self) -> int:
        """Mengembalikan tenaga mesin traktor."""
        return self._tenaga_kuda

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung biaya operator berdasarkan lama sewa."""
        return self.ONGKOS_OPERATOR_HARIAN * jumlah_hari

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan traktor."""
        return "Harus didampingi operator."
