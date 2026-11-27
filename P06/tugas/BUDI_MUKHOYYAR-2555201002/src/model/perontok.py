
from typing import Final
from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi. Biaya angkutnya besar, jadi ada minimum sewa."""
    MINIMUM_HARI_SEWA: Final[int] = 2

    def __init__(self, kode: str, nama: str, tarif_harian: int, kapasitas: int) -> None:
        super().__init__(kode, nama, tarif_harian)
        if kapasitas <= 0:
            raise ValueError(f"kapasitas harus lebih dari nol, diterima {kapasitas}")
        self._kapasitas = kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Perontok":
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError(
                "Baris harus berisi kode, nama, tarif harian, dan kapasitas."
            )

        kode, nama, tarif_teks, kapasitas_teks = bagian

        try:
            tarif = int(tarif_teks.strip())
            kapasitas = int(kapasitas_teks.strip())
        except ValueError as exc:
            raise ValueError(
                "Tarif harian dan kapasitas harus berupa angka."
            ) from exc

        return cls(kode.strip(), nama.strip(), tarif, kapasitas)

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Hari yang benar-benar ditagih, memperhitungkan batas minimum."""
        return max(jumlah_hari, Perontok.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menagih sekurang-kurangnya dua hari, meski disewa lebih singkat."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
