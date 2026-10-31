
"""Model domain: petugas UPJA."""


class Petugas:
    """Menyimpan identitas dan informasi tugas petugas UPJA."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        desa_tugas: str,
        telepon: str = "-",
    ) -> None:
        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._desa_tugas = desa_tugas
        self._telepon = telepon

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self._nama} ({self._nip}) — {self._jabatan}"

    def informasi_tugas(self) -> str:
        """Mengembalikan informasi penempatan petugas."""
        return f"{self._nama} bertugas di Desa {self._desa_tugas}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
