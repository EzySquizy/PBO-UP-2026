
"""Model domain: produk yang dijual oleh UMKM Kios."""

from typing import Final


class Kios:
    """Satu produk yang dijual oleh UMKM Kios."""

    # Konstanta kelas: aturan usaha yang berlaku untuk semua produk.
    MARGIN_MINIMUM_PERSEN: Final[int] = 10
    HARGA_MINIMUM: Final[int] = 1
    STOK_MINIMUM: Final[int] = 0
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_BARIS: Final[int] = 5

    # Atribut kelas: pencacah jumlah produk.
    _jumlah_produk_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        harga_jual: int,
        stok: int,
    ) -> None:
        """Membuat produk baru dengan data yang tervalidasi."""
        kode_bersih = kode.strip()
        nama_bersih = nama.strip()

        if not kode_bersih:
            raise ValueError("Kode produk tidak boleh kosong.")

        if not nama_bersih:
            raise ValueError("Nama produk tidak boleh kosong.")

        if harga_modal < self.HARGA_MINIMUM:
            raise ValueError("Harga modal harus lebih dari nol.")

        if not self.harga_wajar(harga_modal, harga_jual):
            raise ValueError(
                "Harga jual harus memenuhi margin minimum 10%."
            )

        if stok < self.STOK_MINIMUM:
            raise ValueError("Stok tidak boleh minus.")

        self._kode = kode_bersih
        self._nama = nama_bersih
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        self._stok = stok

        Kios._jumlah_produk_terdaftar += 1

    @property
    def kode(self) -> str:
        """Mengembalikan kode produk."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama produk."""
        return self._nama

    @property
    def harga_modal(self) -> int:
        """Mengembalikan harga modal produk."""
        return self._harga_modal

    @property
    def harga_jual(self) -> int:
        """Mengembalikan harga jual produk."""
        return self._harga_jual

    @property
    def stok(self) -> int:
        """Mengembalikan jumlah stok produk."""
        return self._stok

    @classmethod
    def jumlah_produk_terdaftar(cls) -> int:
        """Mengembalikan jumlah seluruh produk yang pernah dibuat."""
        return cls._jumlah_produk_terdaftar

    @classmethod
    def dari_baris(cls, baris: str) -> Kios:
        """Membuat produk dari baris pendataan teks."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_BARIS:
            raise ValueError(
                f"Baris harus berisi {cls.JUMLAH_KOLOM_BARIS} bagian, "
                f"diterima {len(bagian)}."
            )

        kode, nama, modal, jual, stok = bagian

        if not modal.strip().isdigit():
            raise ValueError("Harga modal harus berupa angka.")

        if not jual.strip().isdigit():
            raise ValueError("Harga jual harus berupa angka.")

        if not stok.strip().isdigit():
            raise ValueError("Stok harus berupa angka.")

        return cls(
            kode.strip(),
            nama.strip(),
            int(modal),
            int(jual),
            int(stok),
        )

    @staticmethod
    def harga_wajar(harga_modal: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual memenuhi margin minimum."""
        if harga_modal < Kios.HARGA_MINIMUM:
            return False

        if harga_jual < Kios.HARGA_MINIMUM:
            return False

        return (
            harga_jual * 100
            >= harga_modal * (100 + Kios.MARGIN_MINIMUM_PERSEN)
        )

    def format_laporan(self) -> str:
        """Menyusun informasi produk dengan perataan f-string."""
        harga = f"Rp{self._harga_jual:>12,}".replace(",", ".")

        return (
            f"{self._kode:<8} "
            f"{self._nama:<20} "
            f"{harga} "
            f"{self._stok:>5} unit"
        )
