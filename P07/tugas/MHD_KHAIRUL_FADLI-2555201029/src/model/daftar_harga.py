"""Daftar harga untuk berbagai jenis alat tani."""

from src.model.alat_tani import AlatTani


class DaftarHarga:
    """Mengelola kumpulan alat tani secara polimorfis."""

    def __init__(self, alat: list[AlatTani]) -> None:
        if not alat:
            raise ValueError("daftar alat tidak boleh kosong")

        self._alat = list(alat)

    def biaya_semua(self, jumlah_hari: int) -> list[int]:
        """Menghitung biaya setiap alat."""
        return [
            item.biaya_sewa(jumlah_hari)
            for item in self._alat
        ]

    def termurah(self, jumlah_hari: int) -> AlatTani:
        """Mengembalikan alat dengan biaya sewa termurah."""
        return min(
            self._alat,
            key=lambda item: item.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        """Menghitung total biaya jika semua alat disewa."""
        return sum(self.biaya_semua(jumlah_hari))
