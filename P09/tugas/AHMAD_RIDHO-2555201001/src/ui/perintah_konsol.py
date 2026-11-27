
"""Penerjemah perintah konsol untuk daftar harga alat tani."""

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga


class PenerjemahPerintah:
    """Menerjemahkan perintah pengguna menggunakan match-case."""

    def __init__(self, alat: list[AlatTani]) -> None:
        self._alat = list(alat)
        self._daftar = DaftarHarga(self._alat)

    def _harga(self, kode: str, hari: int) -> str:
        alat = next(
            (item for item in self._alat if item.kode.lower() == kode),
            None,
        )

        if alat is None:
            return f"Alat dengan kode {kode} tidak ditemukan."

        biaya = alat.biaya_sewa(hari)
        return f"{alat.nama}: {AlatTani.format_rupiah(biaya)}"

    def terjemahkan(self, perintah: str) -> str:
        bagian = perintah.strip().lower().split()

        match bagian:
            case []:
                hasil = "Perintah tidak boleh kosong."

            case ["bantuan"] | ["?"]:
                hasil = (
                    "Perintah tersedia: bantuan, daftar <hari>, "
                    "harga <kode> <hari>, termurah <hari>."
                )

            case ["daftar", hari] if hari.isdigit():
                data = self._daftar.biaya_semua(int(hari))
                hasil = "\n".join(
                    f"{nama}: {AlatTani.format_rupiah(biaya)}"
                    for nama, biaya in data
                )

            case ["harga", kode, hari] if hari.isdigit():
                hasil = self._harga(kode, int(hari))

            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                biaya = alat.biaya_sewa(int(hari))
                hasil = (
                    f"{alat.nama}: "
                    f"{AlatTani.format_rupiah(biaya)}"
                )

            case [perintah_pertama, *_]:
                hasil = f"Perintah '{perintah_pertama}' tidak dikenali."

        return hasil
