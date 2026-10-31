
"""Model domain: produk yang dijual oleh UMKM Kios."""

from typing import Final


class Kios:
    """Mewakili satu produk yang dijual oleh UMKM."""

    HARGA_MINIMUM: Final[int] = 1
    HARGA_MAKSIMUM: Final[int] = 100_000_000
    MARGIN_MINIMUM_PERSEN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_beli: int,
        harga_jual: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode produk tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama produk tidak boleh kosong")
        if not self.harga_dalam_batas(harga_beli):
            raise ValueError("harga beli harus lebih dari nol dan tidak melebihi batas")
        if not self.harga_jual_wajar(harga_beli, harga_jual):
            raise ValueError("harga jual tidak memenuhi aturan kewajaran")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_beli = harga_beli
        self._harga_jual = harga_jual

        Kios._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        """Kode produk yang tidak dapat diubah."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama produk yang tidak dapat diubah."""
        return self._nama

    @property
    def harga_beli(self) -> int:
        """Harga beli produk."""
        return self._harga_beli

    @property
    def harga_jual(self) -> int:
        """Harga jual produk."""
        return self._harga_jual

    @staticmethod
    def harga_dalam_batas(nilai: int) -> bool:
        """Memeriksa apakah harga berada dalam batas yang diizinkan."""
        return Kios.HARGA_MINIMUM <= nilai <= Kios.HARGA_MAKSIMUM

    @staticmethod
    def harga_jual_wajar(harga_beli: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual memenuhi margin minimum."""
        if not Kios.harga_dalam_batas(harga_beli):
            return False
        if not Kios.harga_dalam_batas(harga_jual):
            return False

        margin = harga_beli * Kios.MARGIN_MINIMUM_PERSEN // 100
        return harga_jual >= harga_beli + margin

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil didaftarkan."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Kios":
        """Membuat produk dari baris kode;nama;harga_beli;harga_jual."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError(
                f"baris harus berisi 4 bagian, diterima {len(bagian)}"
            )

        kode, nama, harga_beli, harga_jual = bagian

        if not harga_beli.strip().isdigit():
            raise ValueError("harga beli harus berupa angka")
        if not harga_jual.strip().isdigit():
            raise ValueError("harga jual harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(harga_beli),
            int(harga_jual),
        )

    def keterangan(self) -> str:
        """Menghasilkan keterangan produk dengan kolom yang rapi."""
        return (
            f"{self._kode:<8} "
            f"{self._nama:<25} "
            f"{self.format_rupiah(self._harga_jual):>15}"
        )
