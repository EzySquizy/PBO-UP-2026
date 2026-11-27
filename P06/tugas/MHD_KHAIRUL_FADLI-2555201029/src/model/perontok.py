
"""Model alat tani jenis perontok."""

from typing import Final

from .alat_tani import AlatTani


class Perontok(AlatTani):
    """Alat perontok dengan minimum dua hari sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2

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

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
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

    @classmethod
    def hari_ditagih(cls, jumlah_hari: int) -> int:
        """Minimal durasi sewa yang ditagihkan adalah dua hari."""
        return max(jumlah_hari, cls.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya berdasarkan minimum hari sewa."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
