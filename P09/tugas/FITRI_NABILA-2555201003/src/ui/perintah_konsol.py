
"""Menerjemahkan perintah pengurus melalui konsol."""

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga


class PerintahKonsol:
    """Menerjemahkan perintah konsol untuk daftar harga alat."""

    BANTUAN = (
        "Daftar perintah:\n"
        "bantuan atau ?          : menampilkan bantuan\n"
        "daftar [hari]           : menampilkan seluruh harga sewa\n"
        "harga [kode] [hari]     : menampilkan harga satu alat\n"
        "termurah [hari]         : menampilkan alat termurah"
    )

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def jalankan(self, perintah: str) -> str:
        """Menjalankan perintah berdasarkan pola teks."""
        hasil = "Perintah tidak dikenal. Ketik 'bantuan'."

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

    def _harga_satu_alat(self, kode: str, jumlah_hari: int) -> str:
        """Mencari dan menampilkan harga sewa satu alat."""
        hasil = self._daftar.harga_satu_alat(kode, jumlah_hari)

        if hasil is None:
            return f"Alat berkode {kode} tidak ada dalam daftar."

        nama, biaya = hasil
        return (
            f"{nama}, {jumlah_hari} hari: "
            f"{AlatTani.format_rupiah(biaya)}"
        )
