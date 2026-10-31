
"""Model domain: petani yang menyewa alat dari UPJA."""


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    def __init__(
        self,
        nik: str,
        nama: str,
        desa: str,
        telepon: str = "-",
    ) -> None:
        self._nik = nik
        self._nama = nama
        self._desa = desa
        self._telepon = telepon

    def identitas(self) -> str:
        """Mengembalikan identitas singkat penyewa."""
        return f"{self._nama} ({self._nik}) — Desa {self._desa}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak penyewa."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
