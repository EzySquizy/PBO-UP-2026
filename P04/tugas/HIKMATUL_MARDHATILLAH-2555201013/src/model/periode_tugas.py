"""Value object untuk periode tugas petugas."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PeriodeTugas:
    """Periode tugas yang tidak dapat diubah setelah dibuat."""

    mulai: date
    selesai: date

    def __post_init__(self) -> None:
        if self.selesai < self.mulai:
            raise ValueError(
                "tanggal selesai tidak boleh sebelum tanggal mulai"
            )