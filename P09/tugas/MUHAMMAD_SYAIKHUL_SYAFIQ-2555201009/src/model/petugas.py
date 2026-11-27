
"""Model domain: petugas yang melayani penyewaan alat pertanian."""

from src.model.periode_tugas import PeriodeTugas


class Petugas:
    """Mewakili petugas yang melayani penyewaan alat pertanian."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        username: str,
        telepon: str = "-",
        periode: PeriodeTugas | None = None,
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")
        if not username.strip():
            raise ValueError("username tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._username = username
        self._telepon = "-"
        self.telepon = telepon
        self._periode = periode or PeriodeTugas(1, 2026)

    # Property baca-saja karena ID petugas merupakan identitas tetap.
    @property
    def id_petugas(self) -> str:
        return self._id_petugas

    # Property baca-saja agar nama tidak berubah setelah objek dibuat.
    @property
    def nama(self) -> str:
        return self._nama

    # Property baca-saja karena username menjadi identitas akun petugas.
    @property
    def username(self) -> str:
        return self._username

    # Property baca-saja agar periode memakai objek nilai beku.
    @property
    def periode(self) -> PeriodeTugas:
        return self._periode

    # Setter digunakan karena nomor telepon boleh berubah setelah divalidasi.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._telepon = nilai
            return

        bersih = nilai.replace("-", "").replace(" ", "")
        if not bersih.isdigit() or len(bersih) < 10:
            raise ValueError(
                "telepon harus berupa angka dengan minimal 10 digit"
            )
        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas singkat petugas."""
        return f"{self._nama} ({self._id_petugas}) - {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
