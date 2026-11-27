"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        return self._tarif_harian * jumlah_hari
