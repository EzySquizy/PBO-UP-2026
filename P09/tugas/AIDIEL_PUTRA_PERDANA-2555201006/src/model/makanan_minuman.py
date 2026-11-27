from src.model.barang import Barang


class MakananMinuman(Barang):
    """Kategori makanan ringan dan minuman kemasan dengan pantauan kedaluwarsa."""

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_jual: int,
        stok: int,
        tanggal_kedaluwarsa: str,
    ) -> None:
        super().__init__(kode, nama, harga_jual, stok)
        if not tanggal_kedaluwarsa.strip():
            raise ValueError("tanggal kedaluwarsa wajib diisi")
        self._tanggal_kedaluwarsa = tanggal_kedaluwarsa

    @property
    def tanggal_kedaluwarsa(self) -> str:
        return self._tanggal_kedaluwarsa

    def hitung_subtotal(self, jumlah: int) -> int:
        if jumlah <= 0:
            raise ValueError("jumlah beli harus lebih dari nol")
        return self._harga_jual * jumlah

    def aturan_penyimpanan(self) -> str:
        return f"Susun di rak depan berdasarkan FEFO (kedaluwarsa: {self._tanggal_kedaluwarsa})."