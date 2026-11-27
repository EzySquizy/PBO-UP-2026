
from typing import Final
from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air bermesin. Penyewa dikenakan biaya solar sesuai debitnya."""
    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3

    def __init__(self, kode: str, nama: str, tarif_harian: int, debit: int) -> None:
        super().__init__(kode, nama, tarif_harian)
        if debit <= 0:
            raise ValueError(f"debit harus lebih dari nol, diterima {debit}")
        self._debit = debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "PompaAir":
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError(
                "Baris harus berisi kode, nama, tarif harian, dan debit."
            )

        kode, nama, tarif_teks, debit_teks = bagian

        try:
            tarif = int(tarif_teks.strip())
            debit = int(debit_teks.strip())
        except ValueError as exc:
            raise ValueError(
                "Tarif harian dan debit harus berupa angka."
            ) from exc

        return cls(kode.strip(), nama.strip(), tarif, debit)

    def konsumsi_solar_harian(self) -> int:
        """Perkiraan pemakaian solar dalam liter untuk satu hari."""
        return (self._debit * PompaAir.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        dasar = super().biaya_sewa(jumlah_hari)
        solar = (
            self.konsumsi_solar_harian()
            * PompaAir.HARGA_SOLAR_PER_LITER
            * jumlah_hari
        )
        return dasar + solar
