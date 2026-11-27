from src.model.barang import Barang
from src.model.metode_pembayaran import MetodePembayaran


class BarisBelanja:
    """Menyimpan salinan historis nama dan subtotal barang saat transaksi dibuat."""

    def __init__(self, barang: Barang, jumlah: int) -> None:
        self._kode_barang = barang.kode
        self._nama_barang = barang.nama
        self._jumlah = jumlah
        self._subtotal_historis = barang.hitung_subtotal(jumlah)

    @property
    def subtotal(self) -> int:
        return self._subtotal_historis


class TransaksiKasir:
    """Mencatat transaksi kasir, pemotongan stok otomatis, dan hitung kembalian."""

    def __init__(self, nomor_nota: str, kasir: str) -> None:
        if not nomor_nota.strip():
            raise ValueError("nomor nota tidak boleh kosong")
        self._nomor_nota = nomor_nota
        self._kasir = kasir
        self._daftar_baris: list[BarisBelanja] = []
        self._metode: MetodePembayaran | None = None
        self._uang_bayar: int = 0
        self._kembalian: int = 0

    @property
    def kode_catatan(self) -> str:
        return self._nomor_nota

    @property
    def kembalian(self) -> int:
        return self._kembalian

    def tambah_barang(self, barang: Barang, jumlah: int) -> None:
        if self._metode is not None:
            raise ValueError("transaksi yang sudah dibayar tidak dapat diubah")
        baris = BarisBelanja(barang, jumlah)
        barang.kurangi_stok(jumlah)
        self._daftar_baris.append(baris)

    def total_belanja(self) -> int:
        return sum(baris.subtotal for baris in self._daftar_baris)

    def bayar(self, metode: MetodePembayaran, uang_dibayar: int) -> int:
        total = self.total_belanja()
        if total <= 0:
            raise ValueError("transaksi kosong tidak dapat dibayar")
        if metode.perlu_kembalian():
            if uang_dibayar < total:
                raise ValueError("uang tunai kurang dari total belanja")
            self._kembalian = uang_dibayar - total
        else:
            if uang_dibayar != total:
                raise ValueError("nominal transfer atau QRIS harus sesuai total belanja")
            self._kembalian = 0
        self._metode = metode
        self._uang_bayar = uang_dibayar
        return self._kembalian

    def keterangan_singkat(self) -> str:
        metode_teks = self._metode.value if self._metode else "belum bayar"
        return f"[{self._nomor_nota}] Kasir {self._kasir} ({metode_teks})"

    def nominal_pemasukan(self) -> int:
        return self.total_belanja() if self._metode is not None else 0

    def nominal_pengeluaran(self) -> int:
        return 0