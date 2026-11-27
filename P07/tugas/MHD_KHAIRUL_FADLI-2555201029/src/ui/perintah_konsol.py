
"""Penerjemah perintah konsol menggunakan match-case."""

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga


def _cari_alat(kode: str, daftar: DaftarHarga) -> AlatTani | None:
    """Mencari alat berdasarkan kode."""
    return next(
        (alat for alat in daftar._alat if alat.kode == kode),
        None,
    )


def proses_perintah(
    perintah: str,
    daftar: DaftarHarga,
) -> str:
    """Memproses perintah pengguna menggunakan match-case."""
    bagian = perintah.strip().split()

    match bagian:
        case []:
            hasil = "Perintah tidak boleh kosong."

        case ["bantuan"] | ["?"]:
            hasil = (
                "Perintah tersedia: bantuan, daftar <hari>, "
                "harga <kode> <hari>, termurah <hari>."
            )

        case ["daftar", hari] if hari.isdigit():
            biaya = daftar.biaya_semua(int(hari))
            hasil = "\n".join(
                AlatTani.format_rupiah(nilai)
                for nilai in biaya
            )

        case ["harga", kode, hari] if hari.isdigit():
            alat = _cari_alat(kode, daftar)
            hasil = (
                AlatTani.format_rupiah(alat.biaya_sewa(int(hari)))
                if alat is not None
                else f"Alat dengan kode {kode} tidak ditemukan."
            )

        case ["termurah", hari] if hari.isdigit():
            alat = daftar.termurah(int(hari))
            hasil = f"Alat termurah: {alat.nama}"

        case [perintah_pertama, *_]:
            hasil = f"Perintah tidak dikenal: {perintah_pertama}"

        case _:
            hasil = "Format perintah tidak valid."

    return hasil
