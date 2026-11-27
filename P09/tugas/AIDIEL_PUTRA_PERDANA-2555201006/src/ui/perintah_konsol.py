from __future__ import annotations

from src.format_nilai import format_nilai
from src.model.penyusun_laporan import PenyusunLaporan


class PerintahKonsol:
    """Penerjemah perintah konsol sederhana berbasis structural pattern matching."""

    BANTUAN: str = (
        "Perintah tersedia:\n"
        "  bantuan | ?           -> tampilkan bantuan\n"
        "  rekap <hari>          -> rekap penghasilan seluruh pegawai\n"
        "  tertinggi <hari>      -> pegawai dengan penghasilan tertinggi\n"
        "  terendah <hari>       -> pegawai dengan penghasilan terendah\n"
        "  total <hari>          -> total penghasilan seluruh pegawai"
    )

    def __init__(self, laporan: PenyusunLaporan) -> None:
        self._laporan = laporan

    def jalankan(self, perintah: str) -> str:
        tokens = perintah.strip().lower().split()
        match tokens:
            case []:
                return "Perintah kosong. Ketik 'bantuan'."
            case ["bantuan"] | ["?"]:
                return self.BANTUAN
            case ["rekap", hari] if hari.isdigit() and int(hari) >= 0:
                baris = [
                    f"{ket}: {format_nilai(gaji)}"
                    for ket, gaji in self._laporan.rekap_penghasilan(int(hari))
                ]
                return "\n".join(baris)
            case ["tertinggi", hari] if hari.isdigit() and int(hari) >= 0:
                pegawai = self._laporan.tertinggi(int(hari))
                gaji = pegawai.hitung_penghasilan(int(hari))
                return f"Tertinggi ({hari} hari): {pegawai.keterangan()} -> {format_nilai(gaji)}"
            case ["terendah", hari] if hari.isdigit() and int(hari) >= 0:
                pegawai = self._laporan.terendah(int(hari))
                gaji = pegawai.hitung_penghasilan(int(hari))
                return f"Terendah ({hari} hari): {pegawai.keterangan()} -> {format_nilai(gaji)}"
            case ["total", hari] if hari.isdigit() and int(hari) >= 0:
                total_gaji = self._laporan.total(int(hari))
                return f"Total ({hari} hari): {format_nilai(total_gaji)}"
            case [perintah_asing, *_]:
                return f"Perintah '{perintah_asing}' tidak dikenal atau format tidak valid. Ketik 'bantuan'."
        return "Perintah tidak dikenali. Ketik 'bantuan'."