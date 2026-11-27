from src.model.barang import Barang


class KebutuhanHarian(Barang):
    """Kategori perlengkapan rumah tangga harian seperti sabun dan deterjen."""

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_jual: int,
        stok: int,
        zona_rak: str = "Non-Pangan",
    ) -> None:
        super().__init__(kode, nama, harga_jual, stok)
        if not zona_rak.strip():
            raise ValueError("zona rak tidak boleh kosong")
        self._zona_rak = zona_rak

    def hitung_subtotal(self, jumlah: int) -> int:
        if jumlah <= 0:
            raise ValueError("jumlah beli harus lebih dari nol")
        return self._harga_jual * jumlah

    def aturan_penyimpanan(self) -> str:
        return f"Pisahkan di rak {self._zona_rak}, jauh dari bahan pangan dan sembako."