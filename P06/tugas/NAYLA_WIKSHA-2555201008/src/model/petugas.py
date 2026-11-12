
from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class PeriodeTugas:
    """Menyimpan periode tugas petugas."""

    tanggal_mulai: str
    tanggal_selesai: str

    def __post_init__(self) -> None:
        """Memastikan periode tugas diisi dengan benar."""
        if not self.tanggal_mulai.strip():
            raise ValueError("Tanggal mulai tidak boleh kosong")
        if not self.tanggal_selesai.strip():
            raise ValueError("Tanggal selesai tidak boleh kosong")


class Petugas:
    """Menyimpan identitas dan tugas petugas UPJA."""

    PANJANG_TELEPON_MINIMUM: Final[int] = 10

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        telepon: str,
        periode: PeriodeTugas,
    ) -> None:
        """Menginisialisasi data petugas."""
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong")

        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._telepon = "-"
        self._periode = periode
        self.telepon = telepon

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def jabatan(self) -> str:
        return self._jabatan

    @property
    def periode(self) -> PeriodeTugas:
        return self._periode

    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._telepon = nilai
            return

        nomor = nilai.replace("-", "").replace(" ", "")
        if (
            not nomor.isdigit()
            or len(nomor) < self.PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError("Telepon harus berupa angka minimal 10 digit")

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan ringkasan identitas petugas."""
        return (
            f"{self._nama} | NIP: {self._nip} | "
            f"Jabatan: {self._jabatan} | Telepon: {self._telepon}"
        )
