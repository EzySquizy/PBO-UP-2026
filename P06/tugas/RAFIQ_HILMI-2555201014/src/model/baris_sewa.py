
"""Model domain: satu baris alat dalam transaksi penyewaan."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan detail alat dan tarif saat penyewaan terjadi."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari 0.")

        self._alat = alat
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian
        self._jumlah_hari = jumlah_hari

    @property
    def alat(self) -> AlatTani:
        """Mengembalikan rujukan ke alat."""
        return self._alat

    @property
    def kode_alat(self) -> str:
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        return self._nama_alat

    @property
    def tarif_saat_sewa(self) -> int:
        return self._tarif_saat_sewa

    @property
    def jumlah_hari(self) -> int:
        return self._jumlah_hari

    def subtotal(self) -> int:
        """Menghitung biaya dengan mempertahankan tarif saat penyewaan."""
        biaya_sekarang = self._alat.biaya_sewa(self._jumlah_hari)
        tarif_sekarang = self._alat.tarif_harian * self._jumlah_hari

        biaya_tambahan = biaya_sekarang - tarif_sekarang

        return (
            self._tarif_saat_sewa * self._jumlah_hari
            + biaya_tambahan
        )

    def baris_nota(self) -> str:
        """Menghasilkan rincian biaya untuk nota."""
        nama = self._nama_alat
        rupiah = AlatTani.format_rupiah
        return (
            f"{nama:<30} "
            f"{self._jumlah_hari:>2} hr x "
            f"{rupiah(self._tarif_saat_sewa):>12} = "
            f"{rupiah(self.subtotal()):>12}"
        )
