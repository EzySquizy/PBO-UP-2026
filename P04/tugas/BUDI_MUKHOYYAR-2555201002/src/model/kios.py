
"""Model produk untuk UMKM Kios di Bangkinang."""

from typing import Final


class Kios:
    """Satu produk hasil pertanian yang dijual oleh kios."""

    # Konstanta kelas: aturan yang berlaku untuk semua produk.
    MARGIN_MINIMUM_PERSEN: Final[int] = 10
    HARGA_MINIMUM: Final[int] = 1
    STOK_MINIMUM: Final[int] = 0

    # Pencacah milik kelas, bukan milik objek.
    _jumlah_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        harga_jual: int,
        stok: int = 0,
    ) -> None:
        """Mendaftarkan satu produk baru."""
        if not kode.strip():
            raise ValueError("kode produk tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama produk tidak boleh kosong")
        if harga_modal < self.HARGA_MINIMUM:
            raise ValueError("harga modal harus lebih dari nol")
        if not self.harga_wajar(harga_modal, harga_jual):
            raise ValueError("harga jual belum memenuhi margin minimum")
        if stok < self.STOK_MINIMUM:
            raise ValueError("stok tidak boleh negatif")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        self._stok = stok

        # Pencacah harus dinaikkan melalui nama kelas.
        Kios._jumlah_terdaftar += 1

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil didaftarkan."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris(cls, baris: str) -> "Kios":
        """Membuat produk dari teks: kode;nama;modal;jual;stok."""
        bagian = [item.strip() for item in baris.split(";")]

        if len(bagian) != 5:
            raise ValueError(
                "baris harus berisi kode;nama;modal;jual;stok"
            )

        kode, nama, modal_teks, jual_teks, stok_teks = bagian

        try:
            harga_modal = int(modal_teks)
            harga_jual = int(jual_teks)
            stok = int(stok_teks)
        except ValueError as exc:
            raise ValueError("harga dan stok harus berupa bilangan bulat") from exc

        return cls(kode, nama, harga_modal, harga_jual, stok)

    @staticmethod
    def harga_wajar(harga_modal: int, harga_jual: int) -> bool:
        """Memeriksa margin harga tanpa perlu membuat objek Kios."""
        if harga_modal < 1 or harga_jual < 1:
            return False

        return (
            harga_jual * 100
            >= harga_modal * (100 + Kios.MARGIN_MINIMUM_PERSEN)
        )

    def format_daftar(self) -> str:
        """Menghasilkan satu baris daftar produk yang rapi."""
        return (
            f"{self._kode:<8} "
            f"{self._nama:<20} "
            f"Modal Rp{self._harga_modal:>10,} "
            f"Jual Rp{self._harga_jual:>10,} "
            f"Stok {self._stok:>5}"
        ).replace(",", ".")

    def ringkasan(self) -> str:
        """Menghasilkan informasi singkat tentang produk."""
        return (
            f"{self._nama}: harga jual Rp"
            f"{self._harga_jual:,}".replace(",", ".")
            + f", stok {self._stok}"
        )
