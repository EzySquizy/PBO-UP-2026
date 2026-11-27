
"""Kelas untuk menyusun laporan penghasilan pegawai."""

from src.pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun laporan penghasilan berbagai jenis pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError("Laporan tidak dapat dibuat dari daftar kosong.")

        self._pegawai = list(pegawai)

    def rekap_penghasilan(
        self, jumlah_periode: int
    ) -> list[tuple[str, int]]:
        """Membuat rekap nama dan penghasilan setiap pegawai."""
        return [
            (pegawai.nama, pegawai.hitung_penghasilan(jumlah_periode))
            for pegawai in self._pegawai
        ]

    def penghasilan_tertinggi(self, jumlah_periode: int) -> Pegawai:
        """Mencari pegawai dengan penghasilan tertinggi."""
        return max(
            self._pegawai,
            key=lambda pegawai: pegawai.hitung_penghasilan(jumlah_periode),
        )

    def penghasilan_terendah(self, jumlah_periode: int) -> Pegawai:
        """Mencari pegawai dengan penghasilan terendah."""
        return min(
            self._pegawai,
            key=lambda pegawai: pegawai.hitung_penghasilan(jumlah_periode),
        )

    def total_penghasilan(self, jumlah_periode: int) -> int:
        """Menghitung total penghasilan seluruh pegawai."""
        return sum(
            pegawai.hitung_penghasilan(jumlah_periode)
            for pegawai in self._pegawai
        )
