
"""
TUGAS 1 P04 - PEMROGRAMAN BERORIENTASI OBJEK

UMKM   : Kios Sembako Bangkinang
Produk : Beras, gula, minyak goreng, dan hasil pertanian lainnya
"""

from typing import Final


class ValidasiProduk:
    """Menyediakan validasi data produk."""

    BATAS_HARGA_MINIMUM: Final[int] = 1_000
    BATAS_HARGA_MAKSIMUM: Final[int] = 10_000_000

    @staticmethod
    def harga_wajar(harga: int) -> bool:
        """Memeriksa kewajaran harga modal."""
        return (
            isinstance(harga, int)
            and not isinstance(harga, bool)
            and ValidasiProduk.BATAS_HARGA_MINIMUM
            <= harga
            <= ValidasiProduk.BATAS_HARGA_MAKSIMUM
        )

    @staticmethod
    def nama_valid(nama: str) -> bool:
        """Memeriksa nama barang."""
        return isinstance(nama, str) and bool(nama.strip())

    @staticmethod
    def stok_valid(stok: int) -> bool:
        """Memeriksa stok berupa bilangan bulat nonnegatif."""
        return (
            isinstance(stok, int)
            and not isinstance(stok, bool)
            and stok >= 0
        )


class Kios:
    """Merepresentasikan produk pada Kios Sembako Bangkinang."""

    BATAS_HARGA_MINIMUM: Final[int] = 1_000
    BATAS_HARGA_MAKSIMUM: Final[int] = 10_000_000
    MARGIN_KEUNTUNGAN_MINIMUM: Final[float] = 10.0
    PEMISAH_DATA: Final[str] = ";"
    JUMLAH_KOLOM: Final[int] = 3

    _jumlah_produk: int = 0

    def __init__(self, nama_barang: str, harga_modal: int, stok: int) -> None:
        if not ValidasiProduk.nama_valid(nama_barang):
            raise ValueError("Nama barang tidak boleh kosong.")

        if not self.harga_wajar(harga_modal):
            raise ValueError("Harga modal tidak wajar.")

        if not ValidasiProduk.stok_valid(stok):
            raise ValueError("Stok harus bilangan bulat nonnegatif.")

        self._nama_barang = nama_barang.strip()
        self._harga_modal = harga_modal
        self._stok = stok
        Kios._jumlah_produk += 1

    @property
    def nama_barang(self) -> str:
        return self._nama_barang

    @property
    def harga_modal(self) -> int:
        return self._harga_modal

    @property
    def stok(self) -> int:
        return self._stok

    @staticmethod
    def harga_wajar(harga: int) -> bool:
        """Memeriksa kewajaran harga tanpa membuat objek."""
        return ValidasiProduk.harga_wajar(harga)

    @classmethod
    def dari_baris_teks(cls, baris: str) -> Kios:
        """Membuat produk dari teks: nama barang;harga modal;stok."""
        if not isinstance(baris, str):
            raise TypeError("Data produk harus berupa teks.")

        bagian = baris.split(cls.PEMISAH_DATA)

        if len(bagian) != cls.JUMLAH_KOLOM:
            raise ValueError("Format: nama barang;harga modal;stok.")

        try:
            nama = bagian[0].strip()
            harga = int(bagian[1].strip())
            stok = int(bagian[2].strip())
        except ValueError as exc:
            raise ValueError(
                "Harga modal dan stok harus berupa bilangan bulat."
            ) from exc

        return cls(nama, harga, stok)

    @classmethod
    def jumlah_produk(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil didaftarkan."""
        return cls._jumlah_produk

    def harga_jual(self) -> int:
        """Menghitung harga jual berdasarkan margin minimum."""
        return round(
            self._harga_modal
            * (1 + self.MARGIN_KEUNTUNGAN_MINIMUM / 100)
        )

    def __str__(self) -> str:
        """Menampilkan informasi produk dengan format rapi."""
        return (
            f"{self._nama_barang:<20} | "
            f"Modal: Rp{self._harga_modal:>10,} | "
            f"Jual: Rp{self.harga_jual():>10,} | "
            f"Stok: {self._stok:>5}"
        )
