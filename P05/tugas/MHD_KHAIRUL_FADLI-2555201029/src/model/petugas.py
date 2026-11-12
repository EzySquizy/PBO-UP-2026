
"""Model petugas UPJA."""

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai beku untuk periode tugas petugas."""

    mulai: int
    selesai: int

    def __post_init__(self) -> None:
        if self.mulai > self.selesai:
            raise ValueError(
                "tahun mulai tidak boleh lebih besar dari tahun selesai"
            )


class Petugas:
    """Petugas yang mengelola kegiatan UPJA dengan atribut terjaga."""

    PANJANG_TELEPON_MINIMUM: Final[int] = 10
    TELEPON_KOSONG: Final[str] = "-"

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        periode: PeriodeTugas,
        telepon: str = TELEPON_KOSONG,
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._periode = periode
        self.telepon = telepon

    @property
    def id_petugas(self) -> str:
        """ID petugas. Tidak dapat diubah setelah dibuat."""
        return self._id_petugas

    @property
    def nama(self) -> str:
        """Nama petugas. Baca-saja."""
        return self._nama

    @property
    def jabatan(self) -> str:
        """Jabatan petugas. Baca-saja."""
        return self._jabatan

    @property
    def periode(self) -> PeriodeTugas:
        """Periode tugas petugas (objek nilai beku)."""
        return self._periode

    @property
    def telepon(self) -> str:
        """Nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        bersih = nilai.replace("-", "").replace(" ", "")

        if bersih in ("", "-"):
            self._telepon = self.TELEPON_KOSONG
            return

        if (
            not bersih.isdigit()
            or len(bersih) < self.PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError(
                f"nomor telepon tidak sah, diterima '{nilai}'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas lengkap petugas."""
        return (
            f"{self._nama} ({self._id_petugas}) — "
            f"{self._jabatan} "
            f"({self._periode.mulai}-{self._periode.selesai})"
        )

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi petugas."""
        if self._telepon == self.TELEPON_KOSONG:
            return f"{self._nama} belum mencantumkan nomor telepon"

        return f"{self._nama} dapat dihubungi di {self._telepon}"
