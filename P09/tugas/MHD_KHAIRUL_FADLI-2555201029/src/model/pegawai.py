
"""Model induk pegawai instansi di Kabupaten Kampar."""

from typing import Final


class Pegawai:
    """Pegawai dengan identitas dan gaji pokok."""

    HARI_KERJA_SEBULAN: Final[int] = 30
    HARI_KERJA_MAKSIMUM: Final[int] = 31

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")

        if not nama.strip():
            raise ValueError("nama pegawai tidak boleh kosong")

        if gaji_pokok <= 0:
            raise ValueError("gaji pokok harus lebih dari nol")

        self._nip = nip.strip()
        self._nama = nama.strip()
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        """Mengembalikan NIP pegawai."""
        return self._nip

    @property
    def nama(self) -> str:
        """Mengembalikan nama pegawai."""
        return self._nama

    @property
    def gaji_pokok(self) -> int:
        """Mengembalikan gaji pokok."""
        return self._gaji_pokok

    def hitung_penghasilan(self, hari_kerja: int) -> int:
        """Menghitung gaji berdasarkan jumlah hari kerja."""
        if not 1 <= hari_kerja <= self.HARI_KERJA_MAKSIMUM:
            raise ValueError("hari kerja harus antara 1 dan 31")

        gaji_harian = self._gaji_pokok // self.HARI_KERJA_SEBULAN
        return gaji_harian * hari_kerja

    def __str__(self) -> str:
        """Representasi pegawai untuk pengguna."""
        return f"{self._nama} ({self._nip})"

    def __repr__(self) -> str:
        """Representasi pegawai untuk pengembang."""
        return (
            f"Pegawai(nip={self._nip!r}, "
            f"nama={self._nama!r}, "
            f"gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, lainnya: object) -> bool:
        """Membandingkan pegawai berdasarkan NIP."""
        if not isinstance(lainnya, Pegawai):
            return NotImplemented

        return self._nip == lainnya._nip

    def __hash__(self) -> int:
        """Menghasilkan hash berdasarkan NIP."""
        return hash(self._nip)
