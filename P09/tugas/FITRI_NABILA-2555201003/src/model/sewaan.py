"""Kontrak struktural untuk objek yang dapat disewakan."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Sewaan(Protocol):
    """Kontrak untuk objek yang memiliki informasi dan biaya sewa."""

    @property
    def kode(self) -> str:
        ...

    @property
    def nama(self) -> str:
        ...

    def biaya_sewa(self, jumlah_hari: int) -> int:
        ...

    def keterangan(self) -> str:
        ...
