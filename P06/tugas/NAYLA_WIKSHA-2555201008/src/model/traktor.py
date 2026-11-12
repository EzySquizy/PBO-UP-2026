
from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Mewakili alat tani berupa traktor."""

    ONGKOS_OPERATOR_HARIAN = 100_000
    JUMLAH_KOLOM_CSV = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        tenaga_kuda: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if tenaga_kuda <= 0:
            raise ValueError("Tenaga kuda harus lebih dari nol")

        self._tenaga_kuda = tenaga_kuda

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Traktor:
        """Membuat objek traktor dari baris CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "Baris harus berisi kode, nama, tarif, dan tenaga kuda"
            )

        kode, nama, tarif_teks, tenaga_teks = bagian

        try:
            tarif = int(tarif_teks)
            tenaga_kuda = int(tenaga_teks)
        except ValueError:
            raise ValueError(
                "Tarif dan tenaga kuda harus berupa angka"
            ) from None

        return cls(kode.strip(), nama.strip(), tarif, tenaga_kuda)

    @property
    def tenaga_kuda(self) -> int:
        return self._tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        return biaya_dasar + self.ONGKOS_OPERATOR_HARIAN * jumlah_hari
