
class Pegawai:
    """Kelas induk pegawai Kantor Camat Bangkinang Kota."""

    def __init__(self, nip: str, nama: str, gaji_pokok: int) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama pegawai tidak boleh kosong")
        if gaji_pokok < 0:
            raise ValueError("Gaji pokok tidak boleh negatif")

        self._nip = nip.strip()
        self._nama = nama.strip()
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    def hitung_penghasilan(self, penyesuaian: int = 0) -> int:
        """Menghitung gaji pokok ditambah atau dikurangi penyesuaian."""
        hasil = self._gaji_pokok + penyesuaian

        if hasil < 0:
            raise ValueError("Penghasilan tidak boleh negatif")

        return hasil

    def __str__(self) -> str:
        return f"{self._nip} - {self._nama}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nip={self._nip!r}, nama={self._nama!r}, "
            f"gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pegawai):
            return NotImplemented
        return self._nip == other._nip

    def __hash__(self) -> int:
        return hash(self._nip)
