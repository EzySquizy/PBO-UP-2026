
from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mewakili alat tani berupa mesin perontok."""

    MINIMUM_HARI_SEWA = 2
    JUMLAH_KOLOM_CSV = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari nol")

        self._kapasitas = kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat objek mesin perontok dari baris CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "Baris harus berisi kode, nama, tarif, dan kapasitas"
            )

        kode, nama, tarif_teks, kapasitas_teks = bagian

        try:
            tarif = int(tarif_teks)
            kapasitas = int(kapasitas_teks)
        except ValueError:
            raise ValueError(
                "Tarif dan kapasitas harus berupa angka"
            ) from None

        return cls(kode.strip(), nama.strip(), tarif, kapasitas)

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    def hari_ditagih(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        return max(jumlah_hari, self.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        hari = self.hari_ditagih(jumlah_hari)
        return super().biaya_sewa(hari)
