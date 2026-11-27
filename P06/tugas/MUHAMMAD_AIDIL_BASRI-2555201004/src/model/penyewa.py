"""Model domain: data penyewa alat pertanian."""

from src.model.alamat import Alamat


class Penyewa:
    """Menyimpan identitas dan alamat seorang penyewa."""

    def __init__(self, nik: str, nama: str, alamat: Alamat) -> None:
        if not nik.strip():
            raise ValueError("NIK tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")
        self._nik = nik.strip()
        self._nama = nama.strip()
        self._alamat = alamat

    @property
    def nik(self) -> str:
        return self._nik

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def alamat(self) -> Alamat:
        return self._alamat

    def identitas(self) -> str:
        return f"{self._nama} ({self._nik})"

    def kontak(self) -> str:
        return f"{self._nama} — {self._alamat.lengkap()}"
