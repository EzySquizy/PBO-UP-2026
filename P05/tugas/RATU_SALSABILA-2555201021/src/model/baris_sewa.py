"""Model domain: satu baris alat dalam transaksi penyewaan."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan alat dan salinan data saat penyewaan terjadi."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        """Membuat baris sewa dengan data historis alat."""
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol.")

        self._alat = alat
        self._jumlah_hari = jumlah_hari
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian

    @property
    def alat(self) -> AlatTani:
        """Mengembalikan rujukan ke alat."""
        return self._alat

    @property
    def jumlah_hari(self) -> int:
        """Mengembalikan jumlah hari penyewaan."""
        return self._jumlah_hari

    @property
    def kode_alat(self) -> str:
        """Mengembalikan salinan kode alat."""
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        """Mengembalikan salinan nama alat."""
        return self._nama_alat

    @property
    def tarif_saat_sewa(self) -> int:
        """Mengembalikan salinan tarif saat penyewaan."""
        return self._tarif_saat_sewa

    def subtotal(self) -> int:
        """Menghitung biaya berdasarkan tarif historis."""
        return self._tarif_saat_sewa * self._jumlah_hari

    def baris_nota(self) -> str:
        """Menghasilkan keterangan satu baris pada nota."""
        tarif = AlatTani.format_rupiah(self._tarif_saat_sewa)
        subtotal = AlatTani.format_rupiah(self.subtotal())
        return (
            f"{self._kode_alat} - {self._nama_alat} "
            f"({self._jumlah_hari} hari x {tarif}) = {subtotal}"
        )
