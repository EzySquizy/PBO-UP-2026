"""Model domain kios UMKM penjual produk pertanian."""

from typing import Final


class Kios:
    """Mewakili satu produk yang terdaftar pada kios."""

    MARGIN_MINIMUM_PERSEN: Final[int] = 15
    HARGA_MINIMUM: Final[int] = 1_000
    STOK_MINIMUM: Final[int] = 0
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_BARIS: Final[int] = 5

    _jumlah_produk: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        harga_jual: int,
        stok: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode produk tidak boleh kosong")

        if not nama.strip():
            raise ValueError("nama produk tidak boleh kosong")

        if harga_modal < self.HARGA_MINIMUM:
            raise ValueError("harga modal terlalu rendah")

        if not self.harga_jual_wajar(harga_modal, harga_jual):
            raise ValueError(
                "harga jual harus memenuhi margin keuntungan minimum "
                f"{self.MARGIN_MINIMUM_PERSEN}%"
            )

        if stok < self.STOK_MINIMUM:
            raise ValueError("stok tidak boleh negatif")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        self._stok = stok

        Kios._jumlah_produk += 1

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

    @staticmethod
    def harga_jual_wajar(harga_modal: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual memenuhi margin minimum."""
        if harga_modal < Kios.HARGA_MINIMUM:
            return False

        harga_minimum = (
            harga_modal * (100 + Kios.MARGIN_MINIMUM_PERSEN) // 100
        )
        return harga_jual >= harga_minimum

    @classmethod
    def jumlah_produk(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil didaftarkan."""
        return cls._jumlah_produk

    @classmethod
    def dari_baris(cls, baris: str) -> Kios:
        """Membuat produk dari format kode;nama;modal;jual;stok."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_BARIS:
            raise ValueError(
                "baris harus memiliki 5 bagian: "
                "kode;nama;harga_modal;harga_jual;stok"
            )

        kode, nama, modal, jual, stok = (
            item.strip() for item in bagian
        )

        try:
            harga_modal = int(modal)
            harga_jual = int(jual)
            jumlah_stok = int(stok)
        except ValueError as exc:
            raise ValueError("harga dan stok harus berupa angka bulat") from exc

        return cls(kode, nama, harga_modal, harga_jual, jumlah_stok)

    def tambah_stok(self, jumlah: int) -> None:
        """Menambahkan stok produk."""
        if jumlah <= 0:
            raise ValueError("jumlah penambahan stok harus positif")

        self._stok += jumlah

    def kurangi_stok(self, jumlah: int) -> None:
        """Mengurangi stok produk sesuai jumlah pembelian."""
        if jumlah <= 0:
            raise ValueError("jumlah pengurangan stok harus positif")

        if jumlah > self._stok:
            raise ValueError("stok tidak mencukupi")

        self._stok -= jumlah

    def format_inventaris(self) -> str:
        """Menampilkan informasi produk dengan format kolom rata."""
        return (
            f"{self._kode:<10} "
            f"{self._nama:<20} "
            f"{self._stok:>5} "
            f"Rp{self._harga_jual:>10,}"
        )

    def keterangan(self) -> str:
        """Mengembalikan ringkasan produk."""
        return (
            f"{self._nama} dijual seharga "
            f"Rp{self._harga_jual:,} dengan stok {self._stok}."
        )
