"""Model domain: petugas UPJA dan objek nilai penunjang."""

from dataclasses import dataclass


@dataclass(frozen=True)
class NomorPegawai:
    """Objek nilai beku untuk nomor identifikasi resmi pegawai."""
    prefix: str
    nomor: str

    def __post_init__(self) -> None:
        if not self.nomor.isdigit() or len(self.nomor) < 3:
            raise ValueError(f"nomor pegawai tidak sah, diterima '{self.nomor}'")

    def format_tampil(self) -> str:
        return f"{self.prefix}-{self.nomor}"


class Petugas:
    """Data petugas pengurus UPJA dengan atribut yang terjaga."""

    def __init__(
        self,
        id_petugas: NomorPegawai,
        nama: str,
        jabatan: str,
        status_aktif: bool = True,
    ) -> None:
        self._id_petugas = id_petugas  # Baca-saja (diuji via property tanpa setter)
        if not nama.strip():
            raise ValueError("nama petugas tidak boleh kosong")
        self._nama = nama
        self._jabatan = "Staff"
        self.jabatan = jabatan  # Lewat setter bervalidasi
        self._status_aktif = status_aktif

    @property
    def id_petugas(self) -> NomorPegawai:
        """ID petugas. Melekat seumur hidup, tidak dapat diubah (baca-saja)."""
        return self._id_petugas

    @property
    def nama(self) -> str:
        """Nama petugas (baca-saja)."""
        return self._nama

    @property
    def jabatan(self) -> str:
        """Jabatan petugas dengan setter bervalidasi."""
        return self._jabatan

    @jabatan.setter
    def jabatan(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("jabatan tidak boleh kosong")
        self._jabatan = nilai

    @property
    def status_aktif(self) -> bool:
        return self._status_aktif

    def info_petugas(self) -> str:
        status = "Aktif" if self._status_aktif else "Non-Aktif"
        return f"[{self._id_petugas.format_tampil()}] {self._nama} - {self._jabatan} ({status})"

    def status_keaktifan(self) -> str:
        if self._status_aktif:
            return f"Petugas {self._nama} sedang bertugas aktif."
        return f"Petugas {self._nama} sedang tidak aktif."