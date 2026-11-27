"""Model domain: satu baris rincian alat dalam transaksi sewa."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan alat dan tarif pada saat transaksi dibuat."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari sewa harus lebih dari nol")

        self._alat = alat
        self._jumlah_hari = jumlah_hari
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian

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
        """Menghitung biaya berdasarkan tarif saat transaksi."""
        return self._tarif_saat_sewa * self._jumlah_hari

    def baris_nota(self) -> str:
        """Menghasilkan rincian alat untuk nota."""
        tarif = AlatTani.format_rupiah(self._tarif_saat_sewa)
        subtotal = AlatTani.format_rupiah(self.subtotal())
        return (
            f"{self._nama_alat} ({self._kode_alat}) | "
            f"{self._jumlah_hari} hari x {tarif} = {subtotal}"
        )
