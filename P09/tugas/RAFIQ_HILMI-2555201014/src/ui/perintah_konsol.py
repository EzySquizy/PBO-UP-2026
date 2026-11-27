
"""Penerjemah perintah konsol untuk daftar harga alat tani."""

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga


class PerintahKonsol:
    """Menerjemahkan perintah pengguna menjadi informasi harga."""

    BANTUAN = (
        "Perintah yang tersedia:\n"
        "daftar <hari>\n"
        "harga <kode> <hari>\n"
        "termurah <hari>\n"
        "bantuan"
    )

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def _harga_satu_alat(self, kode: str, jumlah_hari: int) -> str:
        alat = self._daftar.cari(kode)

        if alat is None:
            return f"Alat berkode {kode} tidak ada dalam daftar."

        biaya = alat.biaya_sewa(jumlah_hari)
        return (
            f"{alat.nama}, {jumlah_hari} hari: "
            f"{AlatTani.format_rupiah(biaya)}"
        )

    def jalankan(self, perintah: str) -> str:
        """Menerjemahkan perintah berdasarkan bentuk teksnya."""
        match perintah.strip().lower().split():
            case []:
                hasil = "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                hasil = PerintahKonsol.BANTUAN

            case ["daftar", hari] if hari.isdigit():
                hasil = self._daftar.tabel(int(hari))

            case ["harga", kode, hari] if hari.isdigit():
                hasil = self._harga_satu_alat(kode.upper(), int(hari))

            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                hasil = f"Termurah untuk {hari} hari: {alat.nama}"

            case [perintah_pertama, *_]:
                hasil = (
                    f"Perintah '{perintah_pertama}' tidak dikenal. "
                    "Ketik 'bantuan'."
                )

        return hasil
