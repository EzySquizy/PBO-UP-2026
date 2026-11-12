from src.model.pegawai import Pegawai

class PegawaiTeknis(Pegawai):
    """Pegawai bagian IT/Teknis yang mendapat tunjangan komunikasi bulanan tetap."""
    
    def __init__(self, nip: str, nama: str, honor_harian: int, tunjangan_komunikasi: int) -> None:
        super().__init__(nip, nama, honor_harian)
        if tunjangan_komunikasi < 0:
            raise ValueError(f"Tunjangan tidak boleh negatif, diterima {tunjangan_komunikasi}")
        self._tunjangan_komunikasi = tunjangan_komunikasi

    def hitung_gaji(self, jumlah_hari: int) -> int:
        dasar = super().hitung_gaji(jumlah_hari)
        return dasar + self._tunjangan_komunikasi