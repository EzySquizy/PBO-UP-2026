"""Model satu baris alat dalam transaksi penyewaan."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Satu alat dalam satu transaksi beserta salinan keterangan saat itu."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError(
                f"jumlah hari harus lebih dari nol, diterima {jumlah_hari}"
            )

        # Referensi alat sebagai bentuk agregasi.
        self._alat = alat
        self._jumlah_hari = jumlah_hari

        # Salinan data historis saat penyewaan terjadi.
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian

    @property
    def alat(self) -> AlatTani:
        """Mengembalikan referensi alat yang digunakan."""
        return self._alat

    @property
    def kode_alat(self) -> str:
        """Kode alat pada saat penyewaan."""
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        """Nama alat pada saat penyewaan."""
        return self._nama_alat

    @property
    def jumlah_hari(self) -> int:
        """Lama penyewaan dalam hari."""
        return self._jumlah_hari

    @property
    def tarif_saat_sewa(self) -> int:
        """Tarif alat ketika transaksi dibuat."""
        return self._tarif_saat_sewa

    def subtotal(self) -> int:
        """Menghitung biaya berdasarkan tarif historis."""
        return self._tarif_saat_sewa * self._jumlah_hari

    def baris_nota(self) -> str:
        """Menyusun satu baris keterangan pada nota."""
        nama = f"{self._nama_alat:<30}"
        hari = f"{self._jumlah_hari:>3} hr"
        tarif = AlatTani.format_rupiah(self._tarif_saat_sewa)
        subtotal = AlatTani.format_rupiah(self.subtotal())

        return f"{nama} {hari} x {tarif:>12} = {subtotal:>12}"
