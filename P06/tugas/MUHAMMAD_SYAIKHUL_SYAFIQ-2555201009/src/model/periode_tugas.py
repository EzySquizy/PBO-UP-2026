
"""Objek nilai beku untuk periode tugas petugas."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodeTugas:
    """Menyimpan bulan dan tahun periode tugas."""

    bulan: int
    tahun: int

    def __post_init__(self) -> None:
        if not 1 <= self.bulan <= 12:
            raise ValueError("bulan harus antara 1 dan 12")
        if self.tahun < 2000:
            raise ValueError("tahun harus minimal 2000")

    def keterangan(self) -> str:
        """Mengembalikan keterangan periode tugas."""
        return f"{self.bulan:02d}/{self.tahun}"
