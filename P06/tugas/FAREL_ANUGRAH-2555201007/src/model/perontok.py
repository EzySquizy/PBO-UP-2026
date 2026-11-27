
"""Model alat pertanian jenis perontok."""

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok dengan minimum biaya sewa dua hari."""

    JUMLAH_KOLOM_CSV: Final[int] = 4
    MINIMUM_HARI_SEWA: Final[int] = 2

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        """Menginisialisasi objek mesin perontok."""
        super().__init__(kode, nama, tarif_harian)

        if kapasitas <= 0:
            raise ValueError("kapasitas harus lebih dari nol")

        self._kapasitas = kapasitas

    @property
    def kapasitas(self) -> int:
        """Mengembalikan kapasitas perontok dalam kg per jam."""
        return self._kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat objek Perontok dari data CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "baris CSV Perontok harus berisi "
                "kode;nama;tarif;kapasitas"
            )

        kode, nama, tarif, kapasitas = (
            item.strip() for item in bagian
        )

        try:
            nilai_tarif = int(tarif)
            nilai_kapasitas = int(kapasitas)
        except ValueError as exc:
            raise ValueError(
                "tarif dan kapasitas harus berupa angka bulat"
            ) from exc

        return cls(
            kode,
            nama,
            nilai_tarif,
            nilai_kapasitas,
        )

    @classmethod
    def hari_ditagih(cls, jumlah_hari: int) -> int:
        """Menentukan jumlah hari minimum yang harus dibayar."""
        return max(jumlah_hari, cls.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya dengan minimum tagihan dua hari."""
        hari = self.hari_ditagih(jumlah_hari)
        return super().biaya_sewa(hari)
