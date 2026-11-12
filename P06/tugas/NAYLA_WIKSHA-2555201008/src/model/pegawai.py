
class Pegawai:
    """Mewakili pegawai pada instansi di Kabupaten Kampar."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        gaji_pokok: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong")
        if gaji_pokok <= 0:
            raise ValueError("Gaji pokok harus lebih dari nol")

        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def jabatan(self) -> str:
        return self._jabatan

    @property
    def gaji_pokok(self) -> int:
        return self._gaji_pokok

    def hitung_penghasilan(self) -> int:
        return self._gaji_pokok

    def __str__(self) -> str:
        return (
            f"{self._nama} | NIP: {self._nip} | "
            f"Jabatan: {self._jabatan} | "
            f"Penghasilan: Rp{self.hitung_penghasilan():,}"
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"nip={self._nip!r}, nama={self._nama!r}, "
            f"jabatan={self._jabatan!r}, "
            f"gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, Pegawai):
            return NotImplemented
        return self._nip == lain._nip

    def __hash__(self) -> int:
        return hash(self._nip)
