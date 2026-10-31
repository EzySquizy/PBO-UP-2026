
"""Model domain: petani yang menyewa alat dari UPJA."""

from src.model.alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    PANJANG_NIK: int = 16
    MINIMAL_DIGIT_TELEPON: int = 10

    def __init__(
        self, nik: str, nama: str, alamat: Alamat, telepon: str = "-"
    ) -> None:
        if len(nik) != self.PANJANG_NIK or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari 16 digit angka.")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK hanya boleh dibaca dari luar."""
        return self._nik

    @property
    def alamat(self) -> Alamat:
        """Alamat hanya boleh dibaca dari luar."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Mengambil nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memvalidasi nomor telepon sebelum disimpan."""
        if nilai == "-":
            self._telepon = nilai
            return

        nomor = nilai.replace("-", "").replace(" ", "")
        if (
            not nomor.isdigit()
            or len(nomor) < self.MINIMAL_DIGIT_TELEPON
        ):
            raise ValueError(
                "Nomor telepon harus berupa angka dengan minimal 10 digit."
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan baris identitas singkat untuk nota sewa."""
        return f"{self._nama} ({self._nik}) — {self._alamat.singkat()}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi penyewa."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
