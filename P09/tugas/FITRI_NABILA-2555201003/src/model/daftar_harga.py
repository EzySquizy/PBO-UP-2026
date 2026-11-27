"""Menyusun daftar harga berbagai jenis objek sewaan."""

from .alat_tani import AlatTani
from .sewaan import Sewaan


class DaftarHarga:
    """Menyusun daftar harga berdasarkan kontrak Sewaan."""

    def __init__(self, alat: list[Sewaan]) -> None:
        if not alat:
            raise ValueError("daftar harga tidak dapat disusun dari daftar kosong")
        self._alat = list(alat)

    @property
    def jumlah_alat(self) -> int:
        """Jumlah objek dalam daftar harga."""
        return len(self._alat)

    def biaya_semua(self, jumlah_hari: int) -> list[tuple[str, int]]:
        return [
            (alat.nama, alat.biaya_sewa(jumlah_hari))
            for alat in self._alat
        ]

    def tabel(self, jumlah_hari: int) -> str:
        """Menyusun seluruh biaya sewa dalam bentuk tabel."""
        baris = [
            f"{nama:<25} {AlatTani.format_rupiah(biaya)}"
            for nama, biaya in self.biaya_semua(jumlah_hari)
        ]
        return "\n".join(baris)

    def harga_satu_alat(
        self,
        kode: str,
        jumlah_hari: int,
    ) -> tuple[str, int] | None:
        """Mencari biaya sewa objek berdasarkan kode."""
        for alat in self._alat:
            if alat.kode == kode:
                return alat.nama, alat.biaya_sewa(jumlah_hari)
        return None

    def termurah(self, jumlah_hari: int) -> Sewaan:
        """Mengembalikan objek dengan biaya sewa termurah."""
        return min(
            self._alat,
            key=lambda alat: alat.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        """Menghitung total biaya jika semua objek disewa."""
        return sum(
            alat.biaya_sewa(jumlah_hari)
            for alat in self._alat
        )
