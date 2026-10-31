"""Model produk yang dijual oleh kios pertanian UMKM."""

from typing import Final


class Kios:
    """Mewakili satu produk yang dijual di kios pertanian."""

    MARGIN_MINIMUM: Final[int] = 10
    STOK_MINIMUM: Final[int] = 0
    HARGA_MINIMUM: Final[int] = 1
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_BAGIAN: Final[int] = 5

    _jumlah_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        stok: int,
        harga_modal: int,
        harga_jual: int,
    ) -> None:
        """Membuat produk setelah memvalidasi datanya."""
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama produk tidak boleh kosong.")
        if stok < self.STOK_MINIMUM:
            raise ValueError("Stok produk tidak boleh negatif.")
        if harga_modal < self.HARGA_MINIMUM:
            raise ValueError("Harga modal harus lebih dari nol.")
        if not self.harga_jual_wajar(harga_modal, harga_jual):
            raise ValueError("Harga jual tidak memenuhi batas keuntungan minimum.")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._stok = stok
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        Kios._jumlah_terdaftar += 1

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah produk yang telah didaftarkan."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris(cls, baris: str) -> Kios:
        """Membuat produk dari baris: kode;nama;stok;harga_modal;harga_jual."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_BAGIAN:
            raise ValueError("Baris produk harus berisi 5 bagian.")

        kode, nama, stok, harga_modal, harga_jual = bagian

        for nilai in (stok, harga_modal, harga_jual):
            if not nilai.strip().isdigit():
                raise ValueError("Stok dan harga harus berupa angka bulat.")

        return cls(
            kode.strip(),
            nama.strip(),
            int(stok),
            int(harga_modal),
            int(harga_jual),
        )

    @staticmethod
    def harga_jual_wajar(harga_modal: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual memberi margin minimum 10 persen."""
        if harga_modal < 1 or harga_jual < 1:
            return False

        keuntungan = harga_jual - harga_modal
        return keuntungan * 100 >= harga_modal * Kios.MARGIN_MINIMUM

    @property
    def kode(self) -> str:
        """Mengembalikan kode produk."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama produk."""
        return self._nama

    @property
    def stok(self) -> int:
        """Mengembalikan stok produk."""
        return self._stok

    @property
    def harga_modal(self) -> int:
        """Mengembalikan harga modal produk."""
        return self._harga_modal

    @property
    def harga_jual(self) -> int:
        """Mengembalikan harga jual produk."""
        return self._harga_jual

    def tambah_stok(self, jumlah: int) -> None:
        """Menambahkan stok dengan jumlah positif."""
        if jumlah <= 0:
            raise ValueError("Jumlah penambahan stok harus lebih dari nol.")
        self._stok += jumlah

    def kurangi_stok(self, jumlah: int) -> None:
        """Mengurangi stok jika jumlahnya tersedia."""
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari nol.")
        if jumlah > self._stok:
            raise ValueError("Stok tidak mencukupi.")
        self._stok -= jumlah

    def keuntungan_per_produk(self) -> int:
        """Menghitung keuntungan untuk setiap produk yang terjual."""
        return self._harga_jual - self._harga_modal

    def format_daftar(self) -> str:
        """Menampilkan produk dalam format kolom yang rapi."""
        return (
            f"{self._kode:<8} "
            f"{self._nama:<20} "
            f"{self._stok:>6} "
            f"Rp{self._harga_jual:>10,}".replace(",", ".")
        )





