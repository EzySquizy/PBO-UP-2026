from __future__ import annotations

from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun laporan penghasilan dari koleksi Pegawai secara polimorfik."""

    def __init__(self, daftar_pegawai: list[Pegawai]) -> None:
        if not daftar_pegawai:
            raise ValueError("daftar pegawai tidak dapat kosong")
        self._pegawai: list[Pegawai] = list(daftar_pegawai)

    @property
    def jumlah_pegawai(self) -> int:
        return len(self._pegawai)

    def rekap_penghasilan(self, jumlah_hari: int) -> list[tuple[str, int]]:
        """Mengembalikan daftar (keterangan_pegawai, total_penghasilan) untuk seluruh pegawai."""
        if jumlah_hari < 0:
            raise ValueError("jumlah hari tidak boleh negatif")
        return [
            (pegawai.keterangan(), pegawai.hitung_penghasilan(jumlah_hari))
            for pegawai in self._pegawai
        ]

    def tertinggi(self, jumlah_hari: int) -> Pegawai:
        """Mengembalikan objek Pegawai dengan penghasilan tertinggi pada jumlah hari tertentu."""
        if jumlah_hari < 0:
            raise ValueError("jumlah hari tidak boleh negatif")
        return max(self._pegawai, key=lambda p: p.hitung_penghasilan(jumlah_hari))

    def terendah(self, jumlah_hari: int) -> Pegawai:
        """Mengembalikan objek Pegawai dengan penghasilan terendah pada jumlah hari tertentu."""
        if jumlah_hari < 0:
            raise ValueError("jumlah hari tidak boleh negatif")
        return min(self._pegawai, key=lambda p: p.hitung_penghasilan(jumlah_hari))

    def total(self, jumlah_hari: int) -> int:
        """Menghitung total penghasilan seluruh pegawai pada jumlah hari tertentu."""
        if jumlah_hari < 0:
            raise ValueError("jumlah hari tidak boleh negatif")
        return sum(pegawai.hitung_penghasilan(jumlah_hari) for pegawai in self._pegawai)