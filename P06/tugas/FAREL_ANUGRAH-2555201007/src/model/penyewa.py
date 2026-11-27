"""Model domain penyewa alat pertanian."""

from typing import Final

from src.model.alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    PANJANG_NIK: Final[int] = 16
    PANJANG_MINIMUM_TELEPON: Final[int] = 10

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if len(nik) != self.PANJANG_NIK or not nik.isdigit():
            raise ValueError(
                f"NIK harus 16 digit angka, diterima '{nik}'"
            )

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK hanya dapat dibaca karena merupakan identitas tetap."""
        return self._nik

    @property
    def nama(self) -> str:
        """Nama penyewa."""
        return self._nama

    @property
    def alamat(self) -> Alamat:
        """Alamat berupa objek nilai yang tidak dapat diubah."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Nomor telepon boleh berubah, tetapi harus valid."""
        bersih = nilai.replace("-", "").replace(" ", "")

        if nilai == "-":
            self._telepon = "-"
            return

        if not bersih.isdigit() or len(bersih) < self.PANJANG_MINIMUM_TELEPON:
            raise ValueError(
                f"nomor telepon tidak sah, diterima '{nilai}'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        return f"{self._nama} ({self._nik}) — {self._alamat.singkat()}"

    def kontak(self) -> str:
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
