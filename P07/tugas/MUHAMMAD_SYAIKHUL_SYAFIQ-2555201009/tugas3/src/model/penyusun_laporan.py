
"""Penyusun laporan penghasilan seluruh jenis pegawai."""

from .pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun laporan penghasilan pegawai secara polimorfis."""

    def rekap_penghasilan(
        self,
        daftar_pegawai: list[Pegawai],
        jumlah_hari: int,
    ) -> list[tuple[str, int]]:
        """Membuat rekap nama dan penghasilan setiap pegawai."""
        return [
            (pegawai.nama, pegawai.hitung_gaji(jumlah_hari))
            for pegawai in daftar_pegawai
        ]

    def penghasilan_tertinggi(
        self,
        daftar_pegawai: list[Pegawai],
        jumlah_hari: int,
    ) -> Pegawai:
        """Mencari pegawai dengan penghasilan tertinggi."""
        if not daftar_pegawai:
            raise ValueError("daftar pegawai tidak boleh kosong")

        return max(
            daftar_pegawai,
            key=lambda pegawai: pegawai.hitung_gaji(jumlah_hari),
        )

    def penghasilan_terendah(
        self,
        daftar_pegawai: list[Pegawai],
        jumlah_hari: int,
    ) -> Pegawai:
        """Mencari pegawai dengan penghasilan terendah."""
        if not daftar_pegawai:
            raise ValueError("daftar pegawai tidak boleh kosong")

        return min(
            daftar_pegawai,
            key=lambda pegawai: pegawai.hitung_gaji(jumlah_hari),
        )

    def total_penghasilan(
        self,
        daftar_pegawai: list[Pegawai],
        jumlah_hari: int,
    ) -> int:
        """Menghitung total penghasilan seluruh pegawai."""
        return sum(
            pegawai.hitung_gaji(jumlah_hari)
            for pegawai in daftar_pegawai
        )
