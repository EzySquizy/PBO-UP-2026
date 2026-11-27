
"""Kontrak perilaku untuk objek yang dapat disewakan."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Sewaan(Protocol):
    """Kontrak untuk semua objek yang dapat disewakan."""

    @property
    def kode(self) -> str:
        """Kode unik objek sewaan."""
        ...

    @property
    def nama(self) -> str:
        """Nama objek sewaan."""
        ...

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        ...

    def keterangan(self) -> str:
        """Mengembalikan keterangan objek sewaan."""
        ...
