
"""Penerjemah perintah konsol menggunakan match."""

from src.model.daftar_harga import DaftarHarga
from src.model.alat_tani import AlatTani


class PerintahKonsol:
    """Menerjemahkan perintah pengguna untuk daftar harga."""

    BANTUAN = (
        "Perintah tersedia:\n"
        "daftar HARI\n"
        "harga KODE HARI\n"
        "termurah HARI\n"
        "bantuan atau ?"
    )

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def jalankan(self, perintah: str) -> str:
        """Menerjemahkan perintah menggunakan match."""
        match perintah.strip().lower().split():
            case []:
                return "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                return self.BANTUAN

            case ["daftar", hari] if hari.isdigit():
                return self._daftar.tabel(int(hari))

            case ["harga", kode, hari] if hari.isdigit():
                return self._harga_satu_alat(kode.upper(), int(hari))

            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                return f"Termurah untuk {hari} hari: {alat.nama}"

            case [perintah_pertama, *_]:
                return (
                    f"Perintah '{perintah_pertama}' tidak dikenal. "
                    "Ketik 'bantuan'."
                )

        return "Perintah tidak valid."

    def _harga_satu_alat(self, kode: str, jumlah_hari: int) -> str:
        """Menampilkan biaya sewa satu alat berdasarkan kode."""
        try:
            nama, biaya = self._daftar.biaya_berdasarkan_kode(
                kode,
                jumlah_hari,
            )
            return (
                f"{nama}, {jumlah_hari} hari: "
                f"{AlatTani.format_rupiah(biaya)}"
            )
        except ValueError:
            return f"Alat berkode {kode} tidak ada dalam daftar."
