
"""Mengelola daftar harga alat pertanian secara polimorfik."""

from src.model.alat_tani import AlatTani


class DaftarHarga:
    """Menyusun daftar harga tanpa perlu tahu jenis alatnya satu per satu."""

    def __init__(self, alat: list[AlatTani]) -> None:
        if not alat:
            raise ValueError("daftar harga tidak dapat disusun dari daftar kosong")

        self._alat = list(alat)

    @property
    def jumlah_alat(self) -> int:
        """Mengembalikan jumlah alat yang terdaftar."""
        return len(self._alat)

    def biaya_semua(self, jumlah_hari: int) -> list[tuple[str, int]]:
        """Menghitung biaya setiap alat untuk sejumlah hari."""
        return [
            (alat.nama, alat.biaya_sewa(jumlah_hari))
            for alat in self._alat
        ]

    def biaya_berdasarkan_kode(
        self,
        kode: str,
        jumlah_hari: int,
    ) -> tuple[str, int]:
        """Mencari biaya sewa alat berdasarkan kode."""
        for alat in self._alat:
            if alat.kode == kode:
                return alat.nama, alat.biaya_sewa(jumlah_hari)

        raise ValueError(f"alat dengan kode {kode} tidak ditemukan")

    def termurah(self, jumlah_hari: int) -> AlatTani:
        """Mengembalikan objek alat dengan biaya sewa paling murah."""
        return min(
            self._alat,
            key=lambda alat: alat.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        """Menghitung total biaya jika semua alat disewa."""
        return sum(
            alat.biaya_sewa(jumlah_hari)
            for alat in self._alat
        )

    def tabel(self, jumlah_hari: int) -> str:
        """Menyajikan seluruh biaya dalam bentuk tabel sederhana."""
        hasil = self.biaya_semua(jumlah_hari)
        baris = [
            f"{nama}: {AlatTani.format_rupiah(biaya)}"
            for nama, biaya in hasil
        ]
        return "\n".join(baris)
