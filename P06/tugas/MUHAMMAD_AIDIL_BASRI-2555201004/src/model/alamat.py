"""Model domain: alamat penyewa."""


class Alamat:
    """Menyimpan informasi alamat penyewa."""

    def __init__(self, jalan: str, kelurahan: str, kota: str) -> None:
        if not jalan.strip():
            raise ValueError("jalan tidak boleh kosong")
        if not kelurahan.strip():
            raise ValueError("kelurahan tidak boleh kosong")
        if not kota.strip():
            raise ValueError("kota tidak boleh kosong")
        self._jalan = jalan.strip()
        self._kelurahan = kelurahan.strip()
        self._kota = kota.strip()

    @property
    def jalan(self) -> str:
        return self._jalan

    @property
    def kelurahan(self) -> str:
        return self._kelurahan

    @property
    def kota(self) -> str:
        return self._kota

    def lengkap(self) -> str:
        return f"{self._jalan}, {self._kelurahan}, {self._kota}"
