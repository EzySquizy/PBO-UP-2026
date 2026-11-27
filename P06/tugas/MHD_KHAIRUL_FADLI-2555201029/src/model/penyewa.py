
"""Model domain: petani yang menyewa alat dari UPJA."""

from typing import Final

from src.model.alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    PANJANG_NIK: Final[int] = 16
    PANJANG_TELEPON_MINIMUM: Final[int] = 10
    TELEPON_KOSONG: Final[str] = "-"

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = TELEPON_KOSONG,
    ) -> None:
        if (
            len(nik) != self.PANJANG_NIK
            or not nik.isdigit()
        ):
            raise ValueError(
                f"NIK harus {self.PANJANG_NIK} digit angka, "
                f"diterima '{nik}'"
            )

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK penyewa. Tidak dapat diubah setelah dibuat."""
        return self._nik

    @property
    def alamat(self) -> Alamat:
        """Alamat penyewa."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        bersih = nilai.replace("-", "").replace(" ", "")

        if bersih in ("", "-"):
            self._telepon = self.TELEPON_KOSONG
            return

        if (
            not bersih.isdigit()
            or len(bersih) < self.PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError(
                f"nomor telepon tidak sah, diterima '{nilai}'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas lengkap penyewa."""
        return f"{self._nama} ({self._nik}) — {self._alamat.singkat()}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi penyewa."""
        if self._telepon == self.TELEPON_KOSONG:
            return f"{self._nama} belum mencantumkan nomor telepon"

        return f"{self._nama} dapat dihubungi di {self._telepon}"
