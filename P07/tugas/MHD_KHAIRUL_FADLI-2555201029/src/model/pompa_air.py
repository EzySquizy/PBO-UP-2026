
"""Model alat tani jenis pompa air."""

from typing import Final

from .alat_tani import AlatTani


class PompaAir(AlatTani):
    """Alat tani pompa air dengan biaya bahan bakar solar."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3
    JUMLAH_KOLOM_POMPA_CSV: Final[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if debit <= 0:
            raise ValueError("debit pompa harus lebih dari nol")

        self._debit = debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat objek PompaAir dari baris CSV."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_POMPA_CSV:
            raise ValueError(
                "baris CSV pompa harus berisi kode, nama, tarif, dan debit"
            )

        kode, nama, tarif, debit = bagian

        if not tarif.strip().isdigit():
            raise ValueError("tarif harus berupa angka")

        if not debit.strip().isdigit():
            raise ValueError("debit harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(tarif),
            int(debit),
        )

    @property
    def debit(self) -> int:
        """Mengembalikan debit pompa air."""
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        """Menghitung kebutuhan solar harian berdasarkan debit."""
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa ditambah biaya solar."""
        biaya_solar = (
            self.konsumsi_solar_harian()
            * self.HARGA_SOLAR_PER_LITER
            * jumlah_hari
        )
        return super().biaya_sewa(jumlah_hari) + biaya_solar
