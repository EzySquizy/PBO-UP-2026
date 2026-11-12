"""Model domain: penyewa alat UPJA."""

from typing import Final

from src.model.alamat import Alamat

PANJANG_NIK: Final[int] = 16
PANJANG_TELEPON_MINIMUM: Final[int] = 10


class Penyewa:
    """Menyimpan identitas dan informasi penyewa."""

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if len(nik) != PANJANG_NIK or not nik.isdigit():
            raise ValueError(
                f"NIK harus 16 digit angka, diterima '{nik}'"
            )

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    # NIK bersifat tetap sebagai identitas resmi penyewa.
    @property
    def nik(self) -> str:
        return self._nik

    # Nama penyewa hanya boleh dibaca melalui objek.
    @property
    def nama(self) -> str:
        return self._nama

    # Alamat dijaga agar tidak diganti langsung setelah objek dibuat.
    @property
    def alamat(self) -> Alamat:
        return self._alamat

    # Telepon boleh diperbarui selama memenuhi format yang sah.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._telepon = nilai
            return

        bersih = nilai.replace("-", "").replace(" ", "")

        if (
            not bersih.isdigit()
            or len(bersih) < PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError(
                f"nomor telepon tidak sah, diterima '{nilai}'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas lengkap penyewa."""
        return (
            f"{self._nama} ({self._nik}) — "
            f"{self._alamat.singkat()}"
        )

    def kontak(self) -> str:
        """Mengembalikan informasi kontak penyewa."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"

        return f"{self._nama} dapat dihubungi di {self._telepon}"
