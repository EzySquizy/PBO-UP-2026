
"""Model domain: rincian alat dalam satu transaksi sewa."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan rincian alat dalam satu transaksi sewa."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari 0.")

        self._alat = alat
        self._jumlah_hari = jumlah_hari

        # Snapshot data alat dan biaya saat transaksi dibuat.
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian
        self._subtotal_saat_sewa = alat.biaya_sewa(jumlah_hari)

    @property
    def alat(self) -> AlatTani:
        return self._alat

    @property
    def jumlah_hari(self) -> int:
        return self._jumlah_hari

    @property
    def kode_alat(self) -> str:
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        return self._nama_alat

    @property
    def tarif_saat_sewa(self) -> int:
        return self._tarif_saat_sewa

    def subtotal(self) -> int:
        """Mengembalikan biaya yang sudah disimpan saat transaksi dibuat."""
        return self._subtotal_saat_sewa

    def baris_nota(self) -> str:
        return (
            f"{self._nama_alat:<30} "
            f"{self._jumlah_hari:>2} hr × "
            f"{AlatTani.format_rupiah(self._tarif_saat_sewa):>12} = "
            f"{AlatTani.format_rupiah(self.subtotal()):>14}"
        )
