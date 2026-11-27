
"""Model alat tani jenis perontok."""

from __future__ import annotations

from typing import Final

from .alat_tani import AlatTani


class Perontok(AlatTani):
    """Alat perontok dengan minimum dua hari sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2
    JUMLAH_KOLOM_PERONTOK_CSV: Final[int] = 3

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat objek Perontok dari baris CSV."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_PERONTOK_CSV:
            raise ValueError(
                "baris CSV perontok harus berisi kode, nama, dan tarif"
            )

        kode, nama, tarif = bagian

        if not tarif.strip().isdigit():
            raise ValueError("tarif harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
        )

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Memastikan durasi sewa minimal dua hari."""
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari sewa harus lebih dari nol")
        return max(jumlah_hari, self.MINIMUM_HARI_SEWA)

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Perontok tidak memiliki biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan perontok."""
        return "Minimal penyewaan dua hari."

