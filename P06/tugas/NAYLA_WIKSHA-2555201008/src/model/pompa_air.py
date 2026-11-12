
from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Mewakili alat tani berupa pompa air."""

    HARGA_SOLAR_PER_LITER = 7_000
    LITER_PER_SERATUS_DEBIT = 3
    JUMLAH_KOLOM_CSV = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        self._debit = debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat objek pompa air dari baris CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "Baris harus berisi kode, nama, tarif, dan debit"
            )

        kode, nama, tarif_teks, debit_teks = bagian

        try:
            tarif = int(tarif_teks)
            debit = int(debit_teks)
        except ValueError:
            raise ValueError(
                "Tarif dan debit harus berupa angka"
            ) from None

        return cls(kode.strip(), nama.strip(), tarif, debit)

    @property
    def debit(self) -> int:
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        solar_per_hari = self.konsumsi_solar_harian()
        biaya_solar = solar_per_hari * self.HARGA_SOLAR_PER_LITER

        return biaya_dasar + (biaya_solar * jumlah_hari)
