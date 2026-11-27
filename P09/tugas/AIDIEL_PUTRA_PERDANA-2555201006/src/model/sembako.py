from src.model.barang import Barang


class Sembako(Barang):
    """Kategori bahan pokok seperti beras, gula, dan minyak goreng."""

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_jual: int,
        stok: int,
        minimal_grosir: int = 5,
        potongan_per_unit: int = 500,
    ) -> None:
        super().__init__(kode, nama, harga_jual, stok)
        if minimal_grosir <= 0:
            raise ValueError("minimal grosir harus lebih dari nol")
        if potongan_per_unit < 0 or potongan_per_unit >= harga_jual:
            raise ValueError("potongan per unit tidak valid")
        self._minimal_grosir = minimal_grosir
        self._potongan_per_unit = potongan_per_unit

    def hitung_subtotal(self, jumlah: int) -> int:
        if jumlah <= 0:
            raise ValueError("jumlah beli harus lebih dari nol")
        if jumlah >= self._minimal_grosir:
            return (self._harga_jual - self._potongan_per_unit) * jumlah
        return self._harga_jual * jumlah

    def aturan_penyimpanan(self) -> str:
        return "Simpan di atas palet kayu tertutup agar bebas lembap dan hama."