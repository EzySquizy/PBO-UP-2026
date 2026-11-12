from src.model.pegawai import Pegawai

class PegawaiStruktural(Pegawai):
    """Pegawai dengan jabatan struktural. Mendapat tambahan tunjangan tetap per bulan."""
    
    def __init__(self, nip: str, nama: str, gaji_harian: int, tunjangan_jabatan: int) -> None:
        super().__init__(nip, nama, gaji_harian)
        if tunjangan_jabatan < 0:
            raise ValueError(f"tunjangan jabatan tidak boleh negatif, diterima {tunjangan_jabatan}")
        self._tunjangan_jabatan = tunjangan_jabatan

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        dasar = super().hitung_penghasilan(jumlah_hari)
        return dasar + self._tunjangan_jabatan