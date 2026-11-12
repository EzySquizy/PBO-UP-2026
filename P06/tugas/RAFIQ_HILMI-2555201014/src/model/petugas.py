"""Model domain: petugas yang melayani penyewaan alat UPJA."""

from typing import Final

from src.model.nomor_pegawai import NomorPegawai

PANJANG_TELEPON_MINIMUM: Final[int] = 10


class Petugas:
    """Identitas seorang petugas yang melayani penyewaan alat UPJA."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        self._nomor_pegawai = NomorPegawai(id_petugas)
        self._nama = nama
        self._jabatan = jabatan
        self._telepon = "-"
        self.telepon = telepon

    # Property baca-saja agar nomor identitas tidak diganti sembarangan.
    @property
    def id_petugas(self) -> str:
        """Mengambil nomor identitas petugas."""
        return self._nomor_pegawai.nilai

    # Property baca-saja agar nama hanya dapat dibaca dari luar.
    @property
    def nama(self) -> str:
        """Mengambil nama petugas."""
        return self._nama

    # Property baca-saja agar jabatan tidak diubah tanpa aturan.
    @property
    def jabatan(self) -> str:
        """Mengambil jabatan petugas."""
        return self._jabatan

    # Property dengan setter agar nomor telepon dapat diperbarui secara tervalidasi.
    @property
    def telepon(self) -> str:
        """Mengambil nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memastikan nomor telepon valid sebelum disimpan."""
        if nilai == "-":
            self._telepon = nilai
            return

        nomor = nilai.replace("-", "").replace(" ", "")
        if (
            not nomor.isdigit()
            or len(nomor) < PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError(
                "Nomor telepon harus berupa angka dengan minimal 10 digit."
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan baris identitas singkat petugas."""
        return f"{self._nama} ({self.id_petugas}) — {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
