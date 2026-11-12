from typing import Final
from src.model.pegawai import Pegawai

class PetugasRetribusi(Pegawai):
    """Petugas lapangan pemungut retribusi yang dibayar per titik pasar yang dijaga."""
    
    INSENTIF_PER_TITIK: Final[int] = 15_000

    def __init__(self, nip: str, nama: str, honor_harian: int, titik_pasar: int) -> None:
        super().__init__(nip, nama, honor_harian)
        if titik_pasar < 0:
            raise ValueError(f"Titik pasar tidak boleh negatif, diterima {titik_pasar}")
        self._titik_pasar = titik_pasar
        
    def insentif_harian(self) -> int:
        return self._titik_pasar * PetugasRetribusi.INSENTIF_PER_TITIK

    def hitung_gaji(self, jumlah_hari: int) -> int:
        dasar = super().hitung_gaji(jumlah_hari)
        tambahan = self.insentif_harian() * jumlah_hari
        return dasar + tambahan