from abc import ABC, abstractmethod


class Barang(ABC):
    """Induk abstrak untuk seluruh barang dagangan di Warung SRC Datuk."""

    def __init__(self, kode: str, nama: str, harga_jual: int, stok: int) -> None:
        if not kode.strip():
            raise ValueError("kode barang tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama barang tidak boleh kosong")
        if harga_jual <= 0:
            raise ValueError("harga jual harus lebih dari nol")
        if stok < 0:
            raise ValueError("stok tidak boleh negatif")
        self._kode = kode
        self._nama = nama
        self._harga_jual = harga_jual
        self._stok = stok

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga_jual(self) -> int:
        return self._harga_jual

    @harga_jual.setter
    def harga_jual(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError("harga jual harus lebih dari nol")
        self._harga_jual = nilai

    @property
    def stok(self) -> int:
        return self._stok

    def kurangi_stok(self, jumlah: int) -> None:
        """Memotong stok otomatis saat transaksi kasir terjadi."""
        if jumlah <= 0:
            raise ValueError("jumlah pengurangan stok harus lebih dari nol")
        if jumlah > self._stok:
            raise ValueError(f"stok {self._nama} tidak mencukupi (sisa {self._stok})")
        self._stok -= jumlah

    def tambah_stok(self, jumlah: int) -> None:
        """Menambah stok saat barang kulakan dari pemasok tiba."""
        if jumlah <= 0:
            raise ValueError("jumlah penambahan stok harus lebih dari nol")
        self._stok += jumlah

    @abstractmethod
    def hitung_subtotal(self, jumlah: int) -> int:
        """Menghitung subtotal belanja sesuai aturan tiap kategori barang."""

    @abstractmethod
    def aturan_penyimpanan(self) -> str:
        """Menentukan aturan penataan barang di rak atau gudang SRC Datuk."""