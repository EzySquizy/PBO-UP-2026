
"""Model petugas dalam sistem penyewaan alat tani."""

from src.model.alamat import Alamat
from src.model.periode_tugas import PeriodeTugas


class Petugas:
    """Mewakili petugas dalam sistem penyewaan alat tani."""

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

    # Identitas NIP dibuat hanya-baca agar tidak berubah setelah petugas dibuat.
    @property
    def nip(self) -> str:
        return self._nip

    # Nama dibuat hanya-baca agar perubahan identitas tetap terkontrol.
    @property
    def nama(self) -> str:
        return self._nama

    # Jabatan dibuat hanya-baca agar perubahan jabatan tidak sembarangan.
    @property
    def jabatan(self) -> str:
        return self._jabatan

    # Alamat dibuat hanya-baca karena nilainya memakai objek Alamat yang tetap.
    @property
    def alamat(self) -> Alamat:
        return self._alamat

    # Periode tugas dibuat hanya-baca agar rentang tugas tidak berubah sembarangan.
    @property
    def periode_tugas(self) -> PeriodeTugas:
        return self._periode_tugas

    # Telepon dapat diubah, tetapi nilainya harus melewati validasi setter.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        nomor = nilai.replace("-", "").replace(" ", "")

        if nilai != "-" and (
            not nomor.isdigit() or len(nomor) < 10
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
