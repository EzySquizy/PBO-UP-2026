
"""Model domain: mesin perontok pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Alat pertanian berupa mesin perontok."""

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
            raise ValueError("kapasitas harus lebih dari nol")

        self._kapasitas = kapasitas

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    def hari_ditagih(self, hari: int) -> int:
        """Menentukan jumlah hari yang harus dibayar."""
        if hari <= 0:
            raise ValueError("jumlah hari harus lebih dari nol")
        return max(hari, self.MINIMUM_HARI_SEWA)

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Perontok tidak memiliki biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan perontok."""
        return "Gunakan sesuai kapasitas mesin."

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat perontok dari kode;nama;tarif;kapasitas."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError("baris perontok harus berisi 4 bagian")

        kode, nama, tarif, kapasitas = bagian

        try:
            return cls(
                kode.strip(),
                nama.strip(),
                int(tarif.strip()),
                int(kapasitas.strip()),
            )
        except ValueError as kesalahan:
            raise ValueError("data perontok tidak valid") from kesalahan
