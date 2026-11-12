
from src.model.alat_tani import AlatTani


class BarisSewa:
    """Mewakili satu baris alat dalam transaksi penyewaan."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        """Menyimpan referensi alat dan snapshot data saat penyewaan."""
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        self._alat = alat
        self._jumlah_hari = jumlah_hari

        # Snapshot data saat transaksi dibuat.
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian

    @property
    def kode_alat(self) -> str:
        """Mengembalikan kode alat saat penyewaan."""
        return self._kode_alat

    @property
    def jumlah_hari(self) -> int:
        """Mengembalikan lama penyewaan."""
        return self._jumlah_hari

    @property
    def tarif_saat_sewa(self) -> int:
        """Mengembalikan tarif saat transaksi dibuat."""
        return self._tarif_saat_sewa

    def subtotal(self) -> int:
        """Menghitung subtotal berdasarkan tarif saat penyewaan."""
        return self._tarif_saat_sewa * self._jumlah_hari

    def baris_nota(self) -> str:
        """Menghasilkan teks satu baris nota penyewaan."""
        return (
            f"{self._kode_alat} | {self._nama_alat} | "
            f"{self._jumlah_hari} hari | "
            f"{AlatTani.format_rupiah(self._tarif_saat_sewa)} | "
            f"{AlatTani.format_rupiah(self.subtotal())}"
        )
