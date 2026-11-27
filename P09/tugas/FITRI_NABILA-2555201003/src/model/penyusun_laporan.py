
"""Menyusun laporan penghasilan seluruh jenis pegawai."""

from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun laporan tanpa memeriksa jenis pegawai satu per satu."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError("laporan tidak dapat disusun dari daftar kosong")
        self._pegawai = list(pegawai)

    def rekap_penghasilan(
        self,
        jumlah_hari: int,
    ) -> list[tuple[str, int]]:
        """Menghasilkan nama dan penghasilan setiap pegawai."""
        return [
            (orang.keterangan(), orang.hitung_gaji(jumlah_hari))
            for orang in self._pegawai
        ]

    def tertinggi(self, jumlah_hari: int) -> Pegawai:
        """Mengembalikan pegawai dengan penghasilan tertinggi."""
        return max(
            self._pegawai,
            key=lambda orang: orang.hitung_gaji(jumlah_hari),
        )

    def terendah(self, jumlah_hari: int) -> Pegawai:
        """Mengembalikan pegawai dengan penghasilan terendah."""
        return min(
            self._pegawai,
            key=lambda orang: orang.hitung_gaji(jumlah_hari),
        )

    def total(self, jumlah_hari: int) -> int:
        """Menghitung total penghasilan seluruh pegawai."""
        return sum(
            orang.hitung_gaji(jumlah_hari)
            for orang in self._pegawai
        )
