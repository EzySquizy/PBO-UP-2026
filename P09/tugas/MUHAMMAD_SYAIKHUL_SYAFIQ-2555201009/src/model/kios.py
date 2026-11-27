
"""Model kios UMKM yang menjual produk pertanian."""

from typing import Final


class Kios:
    """Mewakili satu produk yang dijual oleh kios."""

    PERSEN_MINIMUM_LABA: Final[int] = 10
    HARGA_MINIMUM: Final[int] = 1_000
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_produk: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        harga_jual: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode produk tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama produk tidak boleh kosong")
        if harga_modal < self.HARGA_MINIMUM:
            raise ValueError("harga modal terlalu rendah")
        if not self.harga_jual_wajar(harga_modal, harga_jual):
            raise ValueError(
                "harga jual harus memenuhi modal dan laba minimum"
            )

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        Kios._jumlah_produk += 1

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

    @staticmethod
    def harga_jual_wajar(harga_modal: int, harga_jual: int) -> bool:
        if harga_modal < Kios.HARGA_MINIMUM:
            return False
        harga_minimum = (
            harga_modal * (100 + Kios.PERSEN_MINIMUM_LABA) // 100
        )
        return harga_jual >= harga_minimum

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_produk(cls) -> int:
        return cls._jumlah_produk

    @classmethod
    def dari_baris(cls, baris: str) -> Kios:
        bagian = baris.strip().split(cls.PEMISAH_BARIS)
        if len(bagian) != 4:
            raise ValueError(
                "baris produk harus berisi 4 kolom: "
                "kode;nama;harga_modal;harga_jual"
            )

        kode, nama, modal_teks, jual_teks = (
            bagian[0].strip(),
            bagian[1].strip(),
            bagian[2].strip(),
            bagian[3].strip(),
        )

        if not kode or not nama:
            raise ValueError("kode dan nama produk tidak boleh kosong")

        try:
            harga_modal = int(modal_teks)
            harga_jual = int(jual_teks)
        except ValueError as kesalahan:
            raise ValueError("harga harus berupa bilangan bulat") from kesalahan

        return cls(kode, nama, harga_modal, harga_jual)

    def keterangan(self) -> str:
        return (
            f"{self._kode:<8} | {self._nama:<24} | "
            f"Modal: {self.format_rupiah(self._harga_modal):>12} | "
            f"Jual: {self.format_rupiah(self._harga_jual):>12}"
        )
