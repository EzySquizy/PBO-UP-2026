"""Model petugas dalam sistem penyewaan alat tani."""

from src.model.alamat import Alamat
from src.model.periode_tugas import PeriodeTugas


class Petugas:
    """Mewakili petugas dalam sistem penyewaan alat tani."""

    MIN_DIGIT_TELEPON: int = 10

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        alamat: Alamat,
        periode_tugas: PeriodeTugas,
        telepon: str = "-",
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama petugas tidak boleh kosong")

        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._alamat = alamat
        self._periode_tugas = periode_tugas
        self._telepon = "-"
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
    def alamat(self) -> Alamat:
        return self._alamat

    @property
    def periode_tugas(self) -> PeriodeTugas:
        return self._periode_tugas

    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        nomor = nilai.replace("-", "").replace(" ", "")

        if nilai != "-" and (
            not nomor.isdigit()
            or len(nomor) < self.MIN_DIGIT_TELEPON
        ):
            raise ValueError(
                "telepon harus berupa angka minimal 10 digit atau '-'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        return f"{self._nama} ({self._nip}) - {self._jabatan}"

    def lokasi_tugas(self) -> str:
        return f"{self._nama} bertugas di {self._alamat.singkat()}"

    def kontak(self) -> str:
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"

        return f"{self._nama} dapat dihubungi di {self._telepon}"
