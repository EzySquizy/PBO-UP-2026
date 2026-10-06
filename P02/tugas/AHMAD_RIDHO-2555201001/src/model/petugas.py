
class Petugas:
    """Mewakili petugas dalam sistem penyewaan alat tani."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        desa: str,
        telepon: str = "-",
    ) -> None:
        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._desa = desa
        self._telepon = telepon

    def identitas(self) -> str:
        return f"{self._nama} ({self._nip}) - {self._jabatan}"

    def lokasi_tugas(self) -> str:
        return f"{self._nama} bertugas di Desa {self._desa}"

    def kontak(self) -> str:
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
