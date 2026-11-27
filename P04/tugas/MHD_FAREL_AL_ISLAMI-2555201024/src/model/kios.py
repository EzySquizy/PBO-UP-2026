
"""Model domain: produk pertanian yang dijual oleh Kios UMKM."""

from typing import Final


class Kios:
    """Satu produk pertanian yang dijual oleh kios."""

    PERSEN_KEUNTUNGAN_MINIMUM: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM: Final[int] = 5

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

        if harga_modal <= 0:
            raise ValueError("harga modal harus lebih dari nol")

        if not self.harga_jual_wajar(harga_modal, harga_jual):
            raise ValueError(
                "harga jual harus memenuhi keuntungan minimum "
                f"{self.PERSEN_KEUNTUNGAN_MINIMUM}%"
            )

        if stok < 0:
            raise ValueError("stok tidak boleh negatif")

        self._kode = kode
        self._nama = nama
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        self._stok = stok

        Kios._jumlah_produk += 1

    @staticmethod
    def harga_jual_wajar(harga_modal: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual memenuhi keuntungan minimum."""
        if harga_modal <= 0:
            return False

        keuntungan_minimum = (
            harga_modal * Kios.PERSEN_KEUNTUNGAN_MINIMUM // 100
        )
        return harga_jual >= harga_modal + keuntungan_minimum

    @classmethod
    def jumlah_produk(cls) -> int:
        """Mengembalikan jumlah objek produk yang berhasil dibuat."""
        return cls._jumlah_produk

    @classmethod
    def dari_baris_teks(cls, baris: str) -> Kios:
        """Membuat objek produk dari lima kolom teks."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM:
            raise ValueError("baris harus terdiri dari lima kolom")

        kode, nama, modal, jual, stok = bagian

        try:
            harga_modal = int(modal.strip())
            harga_jual = int(jual.strip())
            jumlah_stok = int(stok.strip())
        except ValueError as exc:
            raise ValueError(
                "harga modal, harga jual, dan stok harus berupa angka"
            ) from exc

        return cls(
            kode.strip(),
            nama.strip(),
            harga_modal,
            harga_jual,
            jumlah_stok,
        )

    def keterangan(self) -> str:
        """Menghasilkan informasi produk dengan format rata."""
        harga = f"Rp{self._harga_jual:,}".replace(",", ".")

        return (
            f"{self._kode:<8} | "
            f"{self._nama:<20} | "
            f"{self._stok:>5} | "
            f"{harga:>14}"
        )

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga_modal(self) -> int:
        return self._harga_modal

    @property
    def harga_jual(self) -> int:
        return self._harga_jual

    @property
    def stok(self) -> int:
        return self._stok
