"""Model domain: penyewa alat UPJA."""

from src.model.alamat import Alamat


class Penyewa:
    """Data penyewa alat pertanian."""

    def __init__(
        self,
        nama: str,
        nik: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        self._nama = nama

        if len(nik) != 16 or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari tepat 16 digit.")
        self._nik = nik

        self._alamat = alamat
        self.telepon = telepon

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nik(self) -> str:
        return self._nik

    @property
    def alamat(self) -> Alamat:
        return self._alamat

    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai != "-":
            bersih = nilai.replace("-", "").replace(" ", "")
            if not bersih.isdigit() or len(bersih) < 10:
                raise ValueError("Telepon harus '-' atau minimal 10 digit.")
        self._telepon = nilai

    def identitas(self) -> str:
        return (
            f"Saya {self._nama} "
            f"({self._nik}), "
            f"dari {self._alamat.singkat()}."
        )
