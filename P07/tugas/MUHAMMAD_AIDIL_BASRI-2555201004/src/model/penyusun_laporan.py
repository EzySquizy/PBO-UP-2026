"""Menyusun laporan penghasilan berbagai jenis pegawai."""

from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun laporan tanpa bergantung pada jenis pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError(
                "laporan tidak dapat disusun dari daftar pegawai kosong"
            )
        self._pegawai = list(pegawai)

    def rekap_penghasilan(
        self, jumlah_hari: int
    ) -> list[tuple[str, int]]:
        """Mengembalikan nama dan penghasilan setiap pegawai."""
        return [
            (pegawai.nama, pegawai.hitung_penghasilan(jumlah_hari))
            for pegawai in self._pegawai
        ]

    def penghasilan_tertinggi(
        self, jumlah_hari: int
    ) -> tuple[str, int]:
        """Mengembalikan pegawai dengan penghasilan tertinggi."""
        return max(
            self.rekap_penghasilan(jumlah_hari),
            key=lambda data: data[1],
        )

    def penghasilan_terendah(
        self, jumlah_hari: int
    ) -> tuple[str, int]:
        """Mengembalikan pegawai dengan penghasilan terendah."""
        return min(
            self.rekap_penghasilan(jumlah_hari),
            key=lambda data: data[1],
        )

    def total_penghasilan(self, jumlah_hari: int) -> int:
        """Menghitung total penghasilan seluruh pegawai."""
        return sum(
            penghasilan
            for _, penghasilan in self.rekap_penghasilan(jumlah_hari)
        )
