class PengeluaranKulakan:
    """Catatan pengeluaran saat pemilik memesan ulang stok ke pemasok."""

    def __init__(self, kode_faktur: str, pemasok: str, total_biaya: int) -> None:
        if not kode_faktur.strip():
            raise ValueError("kode faktur tidak boleh kosong")
        if total_biaya <= 0:
            raise ValueError("total biaya kulakan harus lebih dari nol")
        self._kode_faktur = kode_faktur
        self._pemasok = pemasok
        self._total_biaya = total_biaya

    @property
    def kode_catatan(self) -> str:
        return self._kode_faktur

    def keterangan_singkat(self) -> str:
        return f"[{self._kode_faktur}] Kulakan ke {self._pemasok}"

    def nominal_pemasukan(self) -> int:
        return 0

    def nominal_pengeluaran(self) -> int:
        return self._total_biaya