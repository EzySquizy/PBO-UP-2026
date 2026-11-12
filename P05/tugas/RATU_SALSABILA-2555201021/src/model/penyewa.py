"""Model domain: petani yang menyewa alat dari UPJA."""

from src.model.alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if len(nik) != 16 or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari 16 digit.")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK hanya dapat dibaca."""
        return self._nik

    @property
    def telepon(self) -> str:
        """Mengembalikan nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memvalidasi nomor telepon penyewa."""
        if nilai != "-" and (
            not nilai.isdigit() or len(nilai) < 10 or len(nilai) > 13
        ):
            raise ValueError("Telepon harus 10-13 digit atau '-'.")
        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan baris identitas singkat untuk nota sewa."""
        return f"{self._nama} ({self._nik}) — {self._alamat.singkat()}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi penyewa."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
