
"""Model domain: pegawai Dinas Pertanian Kabupaten Kampar."""

from types import NotImplementedType


class Pegawai:
    """Kelas induk untuk seluruh jenis pegawai."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok_harian: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if gaji_pokok_harian <= 0:
            raise ValueError("Gaji pokok harian harus lebih dari nol")

        self._nip = nip.strip()
        self._nama = nama.strip()
        self._gaji_pokok_harian = gaji_pokok_harian

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def gaji_pokok_harian(self) -> int:
        return self._gaji_pokok_harian

    def hitung_gaji(self, jumlah_hari: int) -> int:
        """Menghitung gaji pokok berdasarkan hari kerja."""
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")
        return self._gaji_pokok_harian * jumlah_hari

    def __str__(self) -> str:
        return f"{self._nama} ({self._nip})"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"nip={self._nip!r}, "
            f"nama={self._nama!r}, "
            f"gaji_pokok_harian={self._gaji_pokok_harian!r})"
        )

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Pegawai):
            return NotImplemented
        return self._nip == other._nip

    def __hash__(self) -> int:
        return hash(self._nip)
