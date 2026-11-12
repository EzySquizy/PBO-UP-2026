from src.model.pegawai import Pegawai

class PegawaiPenyuluh(Pegawai):
    """Penyuluh desa. Memiliki batas minimum hari yang diakui tiap bulan."""

    def __init__(self, nip: str, nama: str, gaji_harian: int, minimum_hari: int) -> None:
        super().__init__(nip, nama, gaji_harian)
        if minimum_hari < 0:
            raise ValueError(f"minimum hari tidak boleh negatif, diterima {minimum_hari}")
        self._minimum_hari = minimum_hari

    def hari_diakui(self, jumlah_hari: int) -> int:
        """Menjamin minimum hari kerja terpenuhi."""
        return max(jumlah_hari, self._minimum_hari)

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        return super().hitung_penghasilan(self.hari_diakui(jumlah_hari))