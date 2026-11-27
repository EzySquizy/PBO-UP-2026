
"""Penerjemah perintah konsol untuk laporan penghasilan pegawai."""

from src.format_nilai import sebagai_teks
from src.penyusun_laporan import PenyusunLaporan


class PerintahLaporan:
    """Menerjemahkan perintah pengguna menjadi laporan penghasilan."""

    BANTUAN = (
        "Perintah yang tersedia:\n"
        "rekap <periode>\n"
        "tertinggi <periode>\n"
        "terendah <periode>\n"
        "total <periode>\n"
        "bantuan"
    )

    def __init__(self, laporan: PenyusunLaporan) -> None:
        self._laporan = laporan

    def jalankan(self, perintah: str) -> str:
        """Menjalankan perintah berdasarkan teks yang diberikan."""
        match perintah.strip().lower().split():
            case []:
                hasil = "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                hasil = self.BANTUAN

            case ["rekap", periode] if periode.isdigit() and int(periode) > 0:
                rekap = self._laporan.rekap_penghasilan(int(periode))
                baris = [
                    f"{nama}: {sebagai_teks(penghasilan)}"
                    for nama, penghasilan in rekap
                ]
                hasil = "\n".join(baris)

            case ["tertinggi", periode] if (
                periode.isdigit() and int(periode) > 0
            ):
                pegawai = self._laporan.penghasilan_tertinggi(int(periode))
                penghasilan = pegawai.hitung_penghasilan(int(periode))
                hasil = (
                    f"Penghasilan tertinggi: {pegawai.nama} "
                    f"({sebagai_teks(penghasilan)})"
                )

            case ["terendah", periode] if (
                periode.isdigit() and int(periode) > 0
            ):
                pegawai = self._laporan.penghasilan_terendah(int(periode))
                penghasilan = pegawai.hitung_penghasilan(int(periode))
                hasil = (
                    f"Penghasilan terendah: {pegawai.nama} "
                    f"({sebagai_teks(penghasilan)})"
                )

            case ["total", periode] if (
                periode.isdigit() and int(periode) > 0
            ):
                total = self._laporan.total_penghasilan(int(periode))
                hasil = f"Total penghasilan: {sebagai_teks(total)}"

            case [nama_perintah, *_]:
                hasil = (
                    f"Perintah '{nama_perintah}' tidak dikenal. "
                    "Ketik 'bantuan'."
                )

        return hasil
