
"""Penerjemah perintah konsol untuk laporan pegawai."""

from src.model.pegawai import Pegawai
from src.model.penyusun_laporan import PenyusunLaporan


class PerintahLaporan:
    """Menangani perintah laporan melalui pola match-case."""

    BANTUAN = (
        "Perintah tersedia:\n"
        "rekap HARI\n"
        "tertinggi HARI\n"
        "terendah HARI\n"
        "total HARI\n"
        "bantuan atau ?"
    )

    def __init__(
        self,
        daftar_pegawai: list[Pegawai],
        penyusun: PenyusunLaporan,
    ) -> None:
        self._daftar_pegawai = daftar_pegawai
        self._penyusun = penyusun

    def jalankan(self, perintah: str) -> str:
        """Menerjemahkan dan menjalankan perintah pengguna."""
        match perintah.strip().lower().split():
            case []:
                return "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                return self.BANTUAN

            case ["rekap", hari] if hari.isdigit():
                hasil = self._penyusun.rekap_penghasilan(
                    self._daftar_pegawai, int(hari)
                )
                return "\n".join(
                    f"{nama}: Rp{penghasilan:,}".replace(",", ".")
                    for nama, penghasilan in hasil
                )

            case ["tertinggi", hari] if hari.isdigit():
                pegawai = self._penyusun.penghasilan_tertinggi(
                    self._daftar_pegawai, int(hari)
                )
                penghasilan = pegawai.hitung_gaji(int(hari))
                return (
                    f"Penghasilan tertinggi: {pegawai.nama} "
                    f"(Rp{penghasilan:,})".replace(",", ".")
                )

            case ["terendah", hari] if hari.isdigit():
                pegawai = self._penyusun.penghasilan_terendah(
                    self._daftar_pegawai, int(hari)
                )
                penghasilan = pegawai.hitung_gaji(int(hari))
                return (
                    f"Penghasilan terendah: {pegawai.nama} "
                    f"(Rp{penghasilan:,})".replace(",", ".")
                )

            case ["total", hari] if hari.isdigit():
                total = self._penyusun.total_penghasilan(
                    self._daftar_pegawai, int(hari)
                )
                return f"Total penghasilan: Rp{total:,}".replace(",", ".")

            case [perintah_pertama, *_]:
                return (
                    f"Perintah '{perintah_pertama}' tidak dikenal. "
                    "Ketik 'bantuan'."
                )

        return "Perintah tidak valid."
