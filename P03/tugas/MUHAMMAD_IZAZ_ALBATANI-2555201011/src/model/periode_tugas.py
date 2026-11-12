
"""Objek nilai beku untuk periode penugasan petugas."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PeriodeTugas:
    """Mewakili rentang tanggal penugasan petugas."""

    mulai: date
    selesai: date

    def __post_init__(self) -> None:
        if self.selesai < self.mulai:
            raise ValueError("Tanggal selesai tidak boleh sebelum tanggal mulai")

    def keterangan(self) -> str:
        """Mengembalikan keterangan periode tugas."""
        return f"{self.mulai:%d-%m-%Y} sampai {self.selesai:%d-%m-%Y}"
