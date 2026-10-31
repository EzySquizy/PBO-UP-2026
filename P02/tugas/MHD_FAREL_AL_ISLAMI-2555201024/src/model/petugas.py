"""Model domain: pengurus UPJA yang melayani penyewaan."""


class Petugas:
    """Pengurus UPJA yang bertugas melayani penyewaan alat tani."""

    def __init__(
        self, id_petugas: str, nama: str, jabatan: str, status_aktif: bool = True
    ) -> None:
        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._status_aktif = status_aktif

    @property
    def id_petugas(self) -> str:
        return self._id_petugas

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def jabatan(self) -> str:
        return self._jabatan

    @property
    def status_aktif(self) -> bool:
        return self._status_aktif

    def info_petugas(self) -> str:
        """Mengembalikan baris informasi ringkas petugas."""
        status = "Aktif" if self._status_aktif else "Non-Aktif"
        return f"[{self._id_petugas}] {self._nama} - {self._jabatan} ({status})"

    def tugas_pelayanan(self, jumlah_transaksi: int) -> str:
        """Menghitung beban layanan transaksi yang ditangani petugas."""
        return f"Petugas {self._nama} telah melayani {jumlah_transaksi} transaksi penyewaan."