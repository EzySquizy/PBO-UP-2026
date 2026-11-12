"""Model domain: petugas UPJA."""

from typing import Final

from src.model.periode_tugas import PeriodeTugas

PANJANG_TELEPON_MINIMUM: Final[int] = 10


class Petugas:
    """Menyimpan identitas dan informasi tugas petugas UPJA."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        desa_tugas: str,
        periode_tugas: PeriodeTugas,
        telepon: str = "-",
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")

        self._nip = nip.strip()
        self._nama = nama.strip()
        self._jabatan = ""
        self._desa_tugas = ""
        self._telepon = "-"
        self._periode_tugas = periode_tugas

        self.jabatan = jabatan
        self.desa_tugas = desa_tugas
        self.telepon = telepon

    # NIP merupakan identitas tetap sehingga hanya boleh dibaca.
    @property
    def nip(self) -> str:
        return self._nip

    # Nama petugas merupakan identitas tetap sehingga hanya boleh dibaca.
    @property
    def nama(self) -> str:
        return self._nama

    # Jabatan dapat berubah, tetapi harus memiliki isi.
    @property
    def jabatan(self) -> str:
        return self._jabatan

    @jabatan.setter
    def jabatan(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Jabatan tidak boleh kosong")
        self._jabatan = nilai.strip()

    # Desa tugas dapat berubah, tetapi tidak boleh kosong.
    @property
    def desa_tugas(self) -> str:
        return self._desa_tugas

    @desa_tugas.setter
    def desa_tugas(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Desa tugas tidak boleh kosong")
        self._desa_tugas = nilai.strip()

    # Nomor telepon dapat berubah jika memenuhi format yang sah.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._telepon = nilai
            return

        bersih = nilai.replace("-", "").replace(" ", "")

        if (
            not bersih.isdigit()
            or len(bersih) < PANJANG_TELEPON_MINIMUM
        ):
            raise ValueError("Nomor telepon harus minimal 10 digit")

        self._telepon = nilai

    # Periode tugas merupakan objek nilai beku yang hanya boleh dibaca.
    @property
    def periode_tugas(self) -> PeriodeTugas:
        return self._periode_tugas

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self._nama} ({self._nip}) — {self._jabatan}"

    def informasi_tugas(self) -> str:
        """Mengembalikan informasi penempatan petugas."""
        return f"{self._nama} bertugas di Desa {self._desa_tugas}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
