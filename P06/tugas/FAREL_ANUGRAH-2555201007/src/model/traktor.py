
"""Model alat pertanian jenis traktor."""

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Traktor dengan tambahan biaya operator harian."""

    JUMLAH_KOLOM_CSV: Final[int] = 4
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
        """Mengembalikan tenaga mesin dalam satuan HP."""
        return self._tenaga_kuda

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Traktor:
        """Membuat objek Traktor dari CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "baris CSV Traktor harus berisi "
                "kode;nama;tarif;tenaga_kuda"
            )

        kode, nama, tarif, tenaga_kuda = (
            item.strip() for item in bagian
        )

        try:
            nilai_tarif = int(tarif)
            nilai_tenaga_kuda = int(tenaga_kuda)
        except ValueError as exc:
            raise ValueError(
                "tarif dan tenaga kuda harus berupa angka bulat"
            ) from exc

        return cls(kode, nama, nilai_tarif, nilai_tenaga_kuda)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa termasuk operator."""
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + self.ONGKOS_OPERATOR_HARIAN * jumlah_hari
