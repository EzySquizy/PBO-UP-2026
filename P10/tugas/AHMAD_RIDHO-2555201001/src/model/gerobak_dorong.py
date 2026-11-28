
"""Model gerobak dorong yang dapat disewakan."""

from src.model.alat_tani import AlatTani
from src.model.galat import DataTidakValid, HariTidakValid, TarifTidakValid


class GerobakDorong:
    """Gerobak dorong yang disewakan tanpa mewarisi AlatTani."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        if not kode.strip():
            raise DataTidakValid("kode gerobak tidak boleh kosong")
        if not nama.strip():
            raise DataTidakValid("nama gerobak tidak boleh kosong")
        if not AlatTani.tarif_wajar(tarif_harian):
            raise TarifTidakValid("tarif gerobak tidak wajar")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa gerobak."""
        if jumlah_hari <= 0:
            raise HariTidakValid("jumlah hari harus lebih dari nol")
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Menampilkan informasi gerobak."""
        return (
            f"[{self._kode}] {self._nama} — "
            f"{AlatTani.format_rupiah(self._tarif_harian)}/hari"
        )
