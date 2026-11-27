
"""Model gerobak dorong yang memenuhi kontrak Sewaan."""


class GerobakDorong:
    """Gerobak dorong yang dapat disewakan tanpa mewarisi AlatTani."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
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
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari sewa harus lebih dari nol.")
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
