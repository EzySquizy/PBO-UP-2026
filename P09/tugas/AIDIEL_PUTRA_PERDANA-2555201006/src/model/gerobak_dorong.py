class GerobakDorong:
    """Gerobak milik desa. Bukan turunan AlatTani."""

    def __init__(self, tarif_harian: int) -> None:
        if tarif_harian <= 0:
            raise ValueError(f"tarif harus lebih dari nol, diterima {tarif_harian}")
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        return "GD-01"

    @property
    def nama(self) -> str:
        return "Gerobak Dorong"

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        return "[GD-01] Gerobak Dorong"