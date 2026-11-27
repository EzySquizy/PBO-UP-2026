"""Model domain: satu baris alat dalam transaksi penyewaan."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan referensi alat dan salinan data saat transaksi dibuat."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError(
                f"jumlah hari harus lebih dari nol, diterima {jumlah_hari}"
            )
        self._alat = alat
        self._jumlah_hari = jumlah_hari
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
        return self._subtotal_saat_sewa

    def baris_nota(self) -> str:
        """Menghasilkan satu baris nota dari data historis yang disalin."""
        nama = self._nama_alat[:30]
        tarif = AlatTani.format_rupiah(self._tarif_saat_sewa)
        subtotal = AlatTani.format_rupiah(self.subtotal())
        return f"{nama:<30} {self._jumlah_hari:>3} hr x {tarif:>12} = {subtotal:>12}"
