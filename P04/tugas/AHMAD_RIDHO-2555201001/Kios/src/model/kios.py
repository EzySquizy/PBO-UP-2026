
from typing import Final

from src.model.produk import Produk


class Kios:
    """UMKM di Bangkinang yang menjual kebutuhan hasil pertanian."""

    MARGIN_MINIMUM: Final[float] = 0.10
    HARGA_MINIMUM: Final[int] = 1_000
    HARGA_MAKSIMUM: Final[int] = 10_000_000
    JUMLAH_KOLOM: Final[int] = 4

    _jumlah_produk: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        harga_jual: int,
    ) -> None:
        if harga_modal <= 0:
            raise ValueError("Harga modal harus lebih dari nol.")
        if not self.harga_jual_wajar(harga_modal, harga_jual):
            raise ValueError("Harga jual tidak memenuhi ketentuan.")

        self._produk = Produk(kode, nama)
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        Kios._jumlah_produk += 1

    @classmethod
    def dari_baris(cls, baris: str) -> Kios:
        bagian = baris.split(";")
        if len(bagian) != cls.JUMLAH_KOLOM:
            raise ValueError("Baris harus berisi empat kolom.")

        kode, nama, modal, jual = bagian

        try:
            return cls(kode, nama, int(modal), int(jual))
        except ValueError as exc:
            raise ValueError("Data produk tidak valid.") from exc

    @staticmethod
    def harga_jual_wajar(harga_modal: int, harga_jual: int) -> bool:
        if harga_modal <= 0 or harga_jual <= 0:
            return False

        harga_minimum_margin = harga_modal * (
            1 + Kios.MARGIN_MINIMUM
        )

        return (
            harga_jual >= harga_minimum_margin
            and Kios.HARGA_MINIMUM
            <= harga_jual
            <= Kios.HARGA_MAKSIMUM
        )

    @classmethod
    def jumlah_produk(cls) -> int:
        return cls._jumlah_produk

    def informasi(self) -> str:
        return (
            f"{self._produk.kode:<8} | {self._produk.nama:<20} | "
            f"Modal: Rp{self._harga_modal:>10,} | "
            f"Jual: Rp{self._harga_jual:>10,}"
        )
