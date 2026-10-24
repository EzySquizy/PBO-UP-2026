
"""Objek nilai periode tugas petugas yang tidak dapat diubah."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PeriodeTugas:
    """Menyimpan tanggal mulai dan selesai tugas."""

    tanggal_mulai: str
    tanggal_selesai: str

    def __post_init__(self) -> None:
        try:
            mulai = date.fromisoformat(self.tanggal_mulai)
            selesai = date.fromisoformat(self.tanggal_selesai)
        except ValueError as exc:
            raise ValueError("tanggal harus berformat YYYY-MM-DD") from exc

        if selesai < mulai:
            raise ValueError(
                "tanggal selesai tidak boleh sebelum tanggal mulai"
            )
