
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
            raise ValueError("NIK harus terdiri dari 16 digit")
        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    # Property baca-saja agar NIK yang sudah divalidasi tidak dapat diubah.
    @property
    def nik(self) -> str:
        return self._nik

    # Property baca-saja agar alamat menggunakan objek nilai Alamat.
    @property
    def alamat(self) -> Alamat:
        return self._alamat

    # Property baca-saja untuk menjaga nama setelah objek dibuat.
    @property
    def nama(self) -> str:
        return self._nama

    # Setter digunakan karena nomor telepon boleh berubah setelah divalidasi.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._telepon = nilai
            return

        bersih = nilai.replace("-", "").replace(" ", "")
        if not bersih.isdigit() or len(bersih) < 10:
            raise ValueError(
                "telepon harus berupa angka dengan minimal 10 digit"
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
