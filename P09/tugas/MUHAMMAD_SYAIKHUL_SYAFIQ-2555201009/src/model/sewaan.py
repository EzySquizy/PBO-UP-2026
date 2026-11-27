
"""Kontrak struktural untuk objek yang dapat disewakan."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Sewaan(Protocol):
    """Kontrak untuk objek yang memiliki informasi dan biaya sewa."""

    @property
    def kode(self) -> str:
        """Mengembalikan kode objek sewaan."""
        ...

    @property
    def nama(self) -> str:
        """Mengembalikan nama objek sewaan."""
        ...

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        ...
