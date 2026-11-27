
"""Model domain: pengurus UPJA yang melayani penyewaan."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai: periode masa tugas petugas (beku)."""

    mulai: int
    selesai: int

    def __post_init__(self) -> None:
        if self.mulai > self.selesai:
            raise ValueError(
                "tahun mulai tidak boleh lebih besar dari tahun selesai"
            )


class Petugas:
    """Pengurus UPJA yang bertugas melayani penyewaan alat tani."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        periode: PeriodeTugas,
        status_aktif: bool = True,
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self.jabatan = jabatan
        self._periode = periode
        self.status_aktif = status_aktif

    @property
    def id_petugas(self) -> str:
        """ID petugas yang tidak dapat diubah."""
        return self._id_petugas

    @property
    def nama(self) -> str:
        """Nama petugas yang tidak dapat diubah."""
        return self._nama

    @property
    def jabatan(self) -> str:
        """Jabatan petugas."""
        return self._jabatan

    @jabatan.setter
    def jabatan(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("jabatan tidak boleh kosong")
        self._jabatan = nilai

    @property
    def periode(self) -> PeriodeTugas:
        """Periode tugas yang bersifat tetap."""
        return self._periode

    @property
    def status_aktif(self) -> bool:
        """Status keaktifan petugas."""
        return self._status_aktif

    @status_aktif.setter
    def status_aktif(self, nilai: bool) -> None:
        if not isinstance(nilai, bool):
            raise TypeError("status aktif harus berupa boolean")
        self._status_aktif = nilai

    def info_petugas(self) -> str:
        """Mengembalikan baris informasi ringkas petugas."""
        status = "Aktif" if self._status_aktif else "Non-Aktif"
        return (
            f"[{self._id_petugas}] {self._nama} - "
            f"{self._jabatan} ({status})"
        )

    def tugas_pelayanan(self, jumlah_transaksi: int) -> str:
        """Menghitung beban layanan transaksi yang ditangani petugas."""
        if jumlah_transaksi < 0:
            raise ValueError("jumlah transaksi tidak boleh negatif")
        return (
            f"Petugas {self._nama} telah melayani "
            f"{jumlah_transaksi} transaksi penyewaan."
        )
