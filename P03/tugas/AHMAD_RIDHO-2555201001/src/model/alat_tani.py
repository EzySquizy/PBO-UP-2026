
class AlatTani:
    """Mewakili alat pertanian yang disewakan."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Kode alat. Tidak dapat diubah setelah alat dibuat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat. Tidak dapat diubah setelah alat dibuat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Tarif sewa per hari dalam rupiah."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError(
                f"tarif harus lebih dari nol, diterima {nilai}"
            )
        if nilai > 5_000_000:
            raise ValueError(
                f"tarif tidak wajar, diterima {nilai}"
            )
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        tarif = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{tarif}/hari"

