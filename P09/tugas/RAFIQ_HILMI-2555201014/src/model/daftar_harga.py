
"""Model untuk menyusun daftar harga sewa alat tani."""

from src.model.alat_tani import AlatTani
from src.model.sewaan import Sewaan


class DaftarHarga:
    """Menyusun daftar harga tanpa memeriksa jenis alat satu per satu."""

    def __init__(self, alat: list[Sewaan]) -> None:
        if not alat:
            raise ValueError(
                "daftar harga tidak dapat disusun dari daftar kosong"
            )

        self._alat = list(alat)

    @property
    def jumlah_alat(self) -> int:
        """Mengembalikan jumlah alat yang tersedia."""
        return len(self._alat)

    def biaya_semua(
        self, jumlah_hari: int
    ) -> list[tuple[str, int]]:
        """Menghitung biaya sewa seluruh alat."""
        return [
            (alat.nama, alat.biaya_sewa(jumlah_hari))
            for alat in self._alat
        ]

    def termurah(self, jumlah_hari: int) -> Sewaan:
        """Mencari alat dengan biaya sewa paling murah."""
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

    def cari(self, kode: str) -> Sewaan | None:
        """Mencari alat berdasarkan kode."""
        for alat in self._alat:
            if alat.kode == kode:
                return alat
        return None

    def tabel(self, jumlah_hari: int) -> str:
        """Menampilkan daftar biaya sewa seluruh alat."""
        baris = [f"Daftar harga sewa untuk {jumlah_hari} hari:"]

        for alat in self._alat:
            baris.append(
                f"{alat.nama}: "
                f"{AlatTani.format_rupiah(alat.biaya_sewa(jumlah_hari))}"
            )

        return "\n".join(baris)
