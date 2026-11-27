"""Penyusun laporan penghasilan pegawai secara polimorfis."""

from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Mengelola laporan penghasilan berbagai jenis pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError("daftar pegawai tidak boleh kosong")

        self._pegawai = list(pegawai)

    def rekap_penghasilan(
        self,
        hari_kerja: int,
    ) -> list[tuple[str, int]]:
        """Menghasilkan rekap nama dan penghasilan setiap pegawai."""
        return [
            (item.nama, item.hitung_penghasilan(hari_kerja))
            for item in self._pegawai
        ]

    def penghasilan_tertinggi(self, hari_kerja: int) -> Pegawai:
        """Mengembalikan pegawai dengan penghasilan tertinggi."""
        return max(
            self._pegawai,
            key=lambda item: item.hitung_penghasilan(hari_kerja),
        )

    def penghasilan_terendah(self, hari_kerja: int) -> Pegawai:
        """Mengembalikan pegawai dengan penghasilan terendah."""
        return min(
            self._pegawai,
            key=lambda item: item.hitung_penghasilan(hari_kerja),
        )

    def total_penghasilan(self, hari_kerja: int) -> int:
        """Menghitung total penghasilan seluruh pegawai."""
        return sum(
            item.hitung_penghasilan(hari_kerja)
            for item in self._pegawai
        )
