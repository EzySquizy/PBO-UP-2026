"""Model pegawai pada instansi di Kabupaten Kampar."""


class Pegawai:
    """Mewakili pegawai pada sebuah instansi."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")
        if gaji_pokok <= 0:
            raise ValueError("gaji pokok harus lebih dari nol")

        self._nip = nip
        self._nama = nama
        self._gaji_pokok = gaji_pokok

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        """Menghitung penghasilan berdasarkan jumlah bulan kerja."""
        if jumlah_bulan <= 0:
            raise ValueError("jumlah bulan harus lebih dari nol")

        return self._gaji_pokok * jumlah_bulan

    def __str__(self) -> str:
        return f"{self._nama} ({self._nip})"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"nip={self._nip!r}, "
            f"nama={self._nama!r}, "
            f"gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, Pegawai):
            return NotImplemented
        return self._nip == lain._nip

    def __hash__(self) -> int:
        return hash(self._nip)
