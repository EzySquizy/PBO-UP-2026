
"""Model domain: traktor pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Alat pertanian berupa traktor."""

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
        return self._tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung tarif traktor beserta ongkos operator."""
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        return biaya_dasar + self.ONGKOS_OPERATOR_HARIAN * jumlah_hari

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Traktor:
        """Membuat traktor dari kode;nama;tarif;tenaga_kuda."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError("baris traktor harus berisi 4 bagian")

        kode, nama, tarif, tenaga_kuda = bagian

        try:
            return cls(
                kode.strip(),
                nama.strip(),
                int(tarif.strip()),
                int(tenaga_kuda.strip()),
            )
        except ValueError as kesalahan:
            raise ValueError("data traktor tidak valid") from kesalahan
