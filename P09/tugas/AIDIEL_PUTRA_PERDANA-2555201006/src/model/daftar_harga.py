from src.model.alat_tani import AlatTani

class DaftarHarga:
    """Menyusun daftar harga tanpa perlu tahu jenis alatnya satu per satu."""

    def __init__(self, alat: list[AlatTani]) -> None:
        if not alat:
            raise ValueError("daftar harga tidak dapat disusun dari daftar kosong")
        self._alat = list(alat)

    def biaya_semua(self, jumlah_hari: int) -> list[tuple[str, int]]:
        return [(alat.nama, alat.biaya_sewa(jumlah_hari)) for alat in self._alat]

    def termurah(self, jumlah_hari: int) -> AlatTani:
        return min(self._alat, key=lambda alat: alat.biaya_sewa(jumlah_hari))

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        return sum(alat.biaya_sewa(jumlah_hari) for alat in self._alat)
