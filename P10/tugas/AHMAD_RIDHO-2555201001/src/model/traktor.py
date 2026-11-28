
"""Model traktor sebagai jenis alat tani."""

from typing import ClassVar

from src.model.alat_tani import AlatTani
from src.model.galat import DataTidakValid


class Traktor(AlatTani):
    """Traktor roda dua yang wajib dioperasikan petugas UPJA."""

    ONGKOS_OPERATOR_HARIAN: ClassVar[int] = 100_000

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        tenaga_kuda: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if tenaga_kuda <= 0:
            raise DataTidakValid(
                f"tenaga kuda harus lebih dari nol, diterima {tenaga_kuda}"
            )

        self._tenaga_kuda = tenaga_kuda

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung ongkos operator traktor."""
        return Traktor.ONGKOS_OPERATOR_HARIAN * jumlah_hari

    def syarat_pemakaian(self) -> str:
        """Menjelaskan syarat penggunaan traktor."""
        return "Wajib dioperasikan oleh petugas UPJA."
