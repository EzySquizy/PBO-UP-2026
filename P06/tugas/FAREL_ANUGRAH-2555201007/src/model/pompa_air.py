
"""Model alat pertanian jenis pompa air."""

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air dengan tambahan biaya konsumsi solar."""

    JUMLAH_KOLOM_CSV: Final[int] = 4
    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        """Menginisialisasi objek pompa air."""
        super().__init__(kode, nama, tarif_harian)

        if debit <= 0:
            raise ValueError("debit harus lebih dari nol")

        self._debit = debit

    @property
    def debit(self) -> int:
        """Mengembalikan debit pompa dalam liter per menit."""
        return self._debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat objek PompaAir dari data CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "baris CSV PompaAir harus berisi "
                "kode;nama;tarif;debit"
            )

        kode, nama, tarif, debit = (
            item.strip() for item in bagian
        )

        try:
            nilai_tarif = int(tarif)
            nilai_debit = int(debit)
        except ValueError as exc:
            raise ValueError(
                "tarif dan debit harus berupa angka bulat"
            ) from exc

        return cls(kode, nama, nilai_tarif, nilai_debit)

    def konsumsi_solar_harian(self) -> int:
        """Menghitung konsumsi solar harian berdasarkan debit."""
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa termasuk biaya solar."""
        dasar = super().biaya_sewa(jumlah_hari)

        biaya_solar = (
            self.konsumsi_solar_harian()
            * self.HARGA_SOLAR_PER_LITER
            * jumlah_hari
        )

        return dasar + biaya_solar
