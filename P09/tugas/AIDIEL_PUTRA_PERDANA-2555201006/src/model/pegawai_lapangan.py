from typing import Final
from src.model.pegawai import Pegawai

class PegawaiLapangan(Pegawai):
    """Pegawai lapangan. Mendapat uang bensin harian sesuai jarak area tugas."""
    
    TARIF_BENSIN_PER_KM: Final[int] = 2_000

    def __init__(self, nip: str, nama: str, gaji_harian: int, jarak_km: int) -> None:
        super().__init__(nip, nama, gaji_harian)
        if jarak_km < 0:
            raise ValueError(f"jarak area tugas tidak boleh negatif, diterima {jarak_km}")
        self._jarak_km = jarak_km
        
    def konsumsi_bensin_harian(self) -> int:
        return self._jarak_km * PegawaiLapangan.TARIF_BENSIN_PER_KM

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        dasar = super().hitung_penghasilan(jumlah_hari)
        bensin = self.konsumsi_bensin_harian() * jumlah_hari
        return dasar + bensin