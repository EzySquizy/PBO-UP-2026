"""Penyusun laporan penghasilan berbagai jenis pegawai."""

from src.kepegawaian.pegawai import Pegawai


class PenyusunLaporan:
    """Mengelola rekap penghasilan seluruh jenis pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError("daftar pegawai tidak boleh kosong")
        self._pegawai = list(pegawai)

    def rekap_penghasilan(
        self,
        jumlah_bulan: int,
    ) -> list[tuple[str, int]]:
        """Menghasilkan rekap nama dan penghasilan setiap pegawai."""
        return [
            (str(orang), orang.hitung_penghasilan(jumlah_bulan))
            for orang in self._pegawai
        ]

    def penghasilan_tertinggi(self, jumlah_bulan: int) -> Pegawai:
        """Mengembalikan pegawai dengan penghasilan tertinggi."""
        return max(
            self._pegawai,
            key=lambda orang: orang.hitung_penghasilan(jumlah_bulan),
        )

    def penghasilan_terendah(self, jumlah_bulan: int) -> Pegawai:
        """Mengembalikan pegawai dengan penghasilan terendah."""
        return min(
            self._pegawai,
            key=lambda orang: orang.hitung_penghasilan(jumlah_bulan),
        )

    def total_penghasilan(self, jumlah_bulan: int) -> int:
        """Menjumlahkan penghasilan seluruh pegawai."""
        return sum(
            orang.hitung_penghasilan(jumlah_bulan)
            for orang in self._pegawai
        )
