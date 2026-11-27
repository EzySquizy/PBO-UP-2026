
"""Mengelola daftar harga sewa berbagai jenis alat pertanian."""

from src.model.alat_tani import AlatTani


class DaftarHarga:
    """Menyajikan biaya sewa alat tanpa bergantung pada kelas turunannya."""

    def __init__(self, alat: list[AlatTani]) -> None:
        if not alat:
            raise ValueError("daftar harga tidak dapat disusun dari daftar kosong")
        self._alat = list(alat)

    @property
    def jumlah_alat(self) -> int:
        """Mengembalikan jumlah alat dalam daftar."""
        return len(self._alat)

    def biaya_semua(self, jumlah_hari: int) -> list[tuple[str, int]]:
        """Menghitung biaya setiap alat untuk jumlah hari tertentu."""
        return [
            (alat.nama, alat.biaya_sewa(jumlah_hari))
            for alat in self._alat
        ]

    def harga_satu_alat(
        self, kode: str, jumlah_hari: int
    ) -> tuple[str, int] | None:
        """Mencari nama dan biaya alat berdasarkan kode."""
        for alat in self._alat:
            if alat.kode == kode:
                return alat.nama, alat.biaya_sewa(jumlah_hari)
        return None

    def termurah(self, jumlah_hari: int) -> AlatTani:
        """Mengembalikan alat dengan biaya sewa paling murah."""
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
        """Menyusun tampilan ringkas biaya sewa semua alat."""
        baris = [f"Daftar harga sewa untuk {jumlah_hari} hari:"]
        for nama, biaya in self.biaya_semua(jumlah_hari):
            baris.append(f"{nama}: {AlatTani.format_rupiah(biaya)}")
        return "\n".join(baris)
