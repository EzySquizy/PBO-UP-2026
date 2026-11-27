
"""Mengelola daftar harga berbagai objek yang dapat disewakan."""

from collections.abc import Sequence

from .sewaan import Sewaan


class DaftarHarga:
    """Menyimpan dan menghitung biaya seluruh objek sewaan."""

    def __init__(self, alat: Sequence[Sewaan]) -> None:
        """Membuat daftar harga dan menyalin daftar objek sewaan."""
        if not alat:
            raise ValueError("Daftar alat tidak boleh kosong.")

        self._alat: list[Sewaan] = list(alat)

    def biaya_semua(self, jumlah_hari: int) -> list[int]:
        """Menghitung biaya sewa setiap objek."""
        return [
            alat.biaya_sewa(jumlah_hari)
            for alat in self._alat
        ]

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        """Menghitung total biaya jika semua objek disewa."""
        return sum(self.biaya_semua(jumlah_hari))

    def termurah(self, jumlah_hari: int) -> Sewaan:
        """Mencari objek dengan biaya sewa paling murah."""
        return min(
            self._alat,
            key=lambda alat: alat.biaya_sewa(jumlah_hari),
        )
