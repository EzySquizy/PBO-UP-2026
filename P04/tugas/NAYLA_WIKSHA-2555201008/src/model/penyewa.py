
from typing import Final

from src.model.alamat import Alamat


class Penyewa:
    """Menyimpan identitas dan kontak penyewa."""

    PANJANG_NIK: Final[int] = 16
    PANJANG_TELEPON_MINIMUM: Final[int] = 10

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str,
    ) -> None:
        """Menginisialisasi data penyewa."""
        if (
            len(nik) != self.PANJANG_NIK
            or not nik.isdigit()
        ):
            raise ValueError("NIK harus terdiri dari 16 digit angka")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """Mengembalikan NIK penyewa."""
        return self._nik

    @property
    def nama(self) -> str:
        """Mengembalikan nama penyewa."""
        return self._nama

    @property
    def alamat(self) -> Alamat:
        """Mengembalikan objek alamat penyewa."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Mengembalikan nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Mengubah nomor telepon setelah validasi."""
        if nilai == "-":
            self._telepon = nilai
            return

        nomor = nilai.replace("-", "").replace(" ", "")
        if (
            not nomor.isdigit()
            or len(nomor) < self.PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError("Telepon harus berupa angka minimal 10 digit")

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan ringkasan identitas penyewa."""
        return (
            f"{self._nama} | NIK: {self._nik} | "
            f"{self._alamat.singkat()} | Telepon: {self._telepon}"
        )
