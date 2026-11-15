
"""Penerjemah perintah konsol untuk laporan pegawai."""

from src.kepegawaian.pegawai import Pegawai
from src.kepegawaian.penyusun_laporan import PenyusunLaporan


class PenerjemahPegawai:
    """Menerjemahkan perintah laporan penghasilan pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        self._laporan = PenyusunLaporan(pegawai)

    def terjemahkan(self, perintah: str) -> str:
        """Menerjemahkan perintah pengguna menjadi laporan."""
        bagian = perintah.strip().lower().split()

        match bagian:
            case []:
                hasil = "Perintah tidak boleh kosong."
            case ["bantuan"]:
                hasil = (
                    "Perintah tersedia: bantuan, daftar <bulan>, "
                    "tertinggi <bulan>, terendah <bulan>, total <bulan>."
                )
            case ["daftar", bulan] if bulan.isdigit() and int(bulan) > 0:
                data = self._laporan.rekap_penghasilan(int(bulan))
                hasil = "\n".join(
                    f"{nama}: Rp{penghasilan:,}".replace(",", ".")
                    for nama, penghasilan in data
                )
            case ["tertinggi", bulan] if bulan.isdigit() and int(bulan) > 0:
                pegawai = self._laporan.penghasilan_tertinggi(int(bulan))
                hasil = f"Penghasilan tertinggi: {pegawai}"
            case ["terendah", bulan] if bulan.isdigit() and int(bulan) > 0:
                pegawai = self._laporan.penghasilan_terendah(int(bulan))
                hasil = f"Penghasilan terendah: {pegawai}"
            case ["total", bulan] if bulan.isdigit() and int(bulan) > 0:
                total = self._laporan.total_penghasilan(int(bulan))
                hasil = f"Total penghasilan: Rp{total:,}".replace(",", ".")
            case [perintah_pertama, *_]:
                hasil = f"Perintah '{perintah_pertama}' tidak dikenali."

        return hasil
