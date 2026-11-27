
"""Menyusun daftar harga berbagai jenis alat pertanian."""

from .alat_tani import AlatTani


class DaftarHarga:
    """Menyusun daftar harga tanpa perlu tahu jenis alatnya satu per satu."""

    def __init__(self, alat: list[AlatTani]) -> None:
        if not alat:
            raise ValueError("daftar harga tidak dapat disusun dari daftar kosong")
        self._alat = list(alat)

    @property
    def jumlah_alat(self) -> int:
        """Jumlah alat dalam daftar harga."""
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
        """Mencari biaya sewa alat berdasarkan kode."""
        for alat in self._alat:
            if alat.kode == kode:
                return alat.nama, alat.biaya_sewa(jumlah_hari)
        return None

    def termurah(self, jumlah_hari: int) -> AlatTani:
        return min(
            self._alat,
            key=lambda alat: alat.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        return sum(
            alat.biaya_sewa(jumlah_hari)
            for alat in self._alat
        )
