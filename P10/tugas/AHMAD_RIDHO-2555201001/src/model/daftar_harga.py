
"""Daftar harga untuk berbagai jenis alat pertanian."""

from collections.abc import Sequence

from src.model.galat import DataTidakValid
from src.model.sewaan import Sewaan


class DaftarHarga:
    """Mengelola perhitungan harga sewa semua jenis alat."""

    def __init__(self, alat: Sequence[Sewaan]) -> None:
        if not alat:
            raise DataTidakValid(
                "daftar harga tidak dapat disusun dari daftar kosong"
            )
        self._alat = list(alat)

    def biaya_semua(self, jumlah_hari: int) -> list[tuple[str, int]]:
        return [
            (alat.nama, alat.biaya_sewa(jumlah_hari))
            for alat in self._alat
        ]

    def termurah(self, jumlah_hari: int) -> Sewaan:
        return min(
            self._alat,
            key=lambda alat: alat.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        return sum(
            alat.biaya_sewa(jumlah_hari)
            for alat in self._alat
        )
