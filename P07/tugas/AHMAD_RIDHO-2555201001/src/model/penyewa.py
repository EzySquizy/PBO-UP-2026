"""Model penyewa alat pertanian."""

from src.model.alamat import Alamat


class Penyewa:
    """Mewakili penyewa alat pertanian."""

    PANJANG_NIK: int = 16
    MIN_DIGIT_TELEPON: int = 10

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if len(nik) != self.PANJANG_NIK or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari 16 digit")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK bersifat tetap setelah penyewa dibuat."""
        return self._nik

    @property
    def nama(self) -> str:
        """Nama penyewa."""
        return self._nama

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
        nomor = nilai.replace("-", "").replace(" ", "")

        if nilai != "-" and (
            not nomor.isdigit()
            or len(nomor) < self.MIN_DIGIT_TELEPON
        ):
            raise ValueError(
                "telepon harus berupa angka minimal 10 digit atau '-'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        return f"{self._nama} ({self._nik}) — {self._alamat.singkat()}"

    def kontak(self) -> str:
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"

        return f"{self._nama} dapat dihubungi di {self._telepon}"
