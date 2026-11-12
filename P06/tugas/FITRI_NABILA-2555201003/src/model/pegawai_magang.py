from src.model.pegawai import Pegawai

class PegawaiMagang(Pegawai):
    """Pegawai magang dengan batas maksimum hari yang bisa diklaim dalam sebulan."""

    def __init__(self, nip: str, nama: str, honor_harian: int, maksimum_hari: int) -> None:
        super().__init__(nip, nama, honor_harian)
        if maksimum_hari < 0:
            raise ValueError(f"Maksimum hari tidak boleh negatif, diterima {maksimum_hari}")
        self._maksimum_hari = maksimum_hari

    def hari_dibayar(self, jumlah_hari: int) -> int:
        """Memotong hari berlebih jika melewati batas maksimum."""
        return min(jumlah_hari, self._maksimum_hari)

    def hitung_gaji(self, jumlah_hari: int) -> int:
        return super().hitung_gaji(self.hari_dibayar(jumlah_hari))