"""Model khusus untuk mesin perontok padi."""

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi dengan minimum sewa dua hari."""

    MINIMUM_HARI_SEWA: Final[int] = 2
    JUMLAH_BAGIAN_CSV: Final[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        self._kapasitas = kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat mesin perontok dari satu baris data CSV."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_BAGIAN_CSV:
            raise ValueError(
                f"baris harus berisi 4 bagian, diterima {len(bagian)}"
            )

        kode, nama, tarif, kapasitas = bagian

        if not tarif.strip().isdigit():
            raise ValueError("Tarif harus berupa angka.")

        if not kapasitas.strip().isdigit():
            raise ValueError("Kapasitas harus berupa angka.")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
            int(kapasitas),
        )

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Menghitung hari sewa dengan batas minimum."""
        return max(jumlah_hari, Perontok.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menagih sekurang-kurangnya dua hari."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
