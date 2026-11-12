"""Model induk untuk pegawai instansi Kabupaten Kampar."""


class Pegawai:
    """Menyimpan identitas dan penghasilan dasar seorang pegawai."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama pegawai tidak boleh kosong.")
        if gaji_pokok <= 0:
            raise ValueError("Gaji pokok harus lebih dari nol.")

        self._nip = nip
        self._nama = nama
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        """Mengembalikan nomor identitas pegawai."""
        return self._nip

    @property
    def nama(self) -> str:
        """Mengembalikan nama pegawai."""
        return self._nama

    @property
    def gaji_pokok(self) -> int:
        """Mengembalikan gaji pokok pegawai."""
        return self._gaji_pokok

    def hitung_penghasilan(self, jumlah_periode: int) -> int:
        """Menghitung penghasilan dasar berdasarkan jumlah periode."""
        if jumlah_periode <= 0:
            raise ValueError("Jumlah periode harus lebih dari nol.")

        return self._gaji_pokok * jumlah_periode

    def __str__(self) -> str:
        return f"{self._nip} - {self._nama}"

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
