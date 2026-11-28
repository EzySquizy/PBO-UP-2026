
"""Model alat pertanian yang disewakan."""

from abc import ABC, abstractmethod
from typing import Final

from .galat import (
    BarisPendataanRusak,
    DataTidakValid,
    HariTidakValid,
    TarifTidakValid,
)


class AlatTani(ABC):
    """Mewakili alat pertanian yang disewakan."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_CSV: Final[int] = 3

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise DataTidakValid("kode alat tidak boleh kosong")
        if not nama.strip():
            raise DataTidakValid("nama alat tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not AlatTani.tarif_wajar(nilai):
            raise TarifTidakValid(
                f"tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} dan "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}, "
                f"diterima {nilai}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @staticmethod
    def baca_rupiah(teks: str) -> int:
        """Membaca nominal rupiah dengan format Indonesia."""
        bersih = teks.strip().replace("Rp", "").replace(".", "").replace(" ", "")
        try:
            return int(bersih)
        except ValueError as penyebab:
            raise TarifTidakValid(
                f"tarif tidak dapat dibaca dari '{teks}'"
            ) from penyebab

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> AlatTani:
        """Membuat alat dari satu baris pendataan."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise BarisPendataanRusak(
                f"baris harus berisi {cls.JUMLAH_KOLOM_CSV} bagian, "
                f"diterima {len(bagian)}: '{baris}'"
            )

        kode, nama, tarif = bagian

        return cls(
            kode.strip(),
            nama.strip(),
            cls.baca_rupiah(tarif),
        )

    @abstractmethod
    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung biaya tambahan sesuai jenis alat."""

    @abstractmethod
    def syarat_pemakaian(self) -> str:
        """Menjelaskan syarat penggunaan alat."""

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Memvalidasi dan menentukan jumlah hari yang ditagihkan."""
        if jumlah_hari <= 0:
            raise HariTidakValid(
                f"jumlah hari harus lebih dari nol, diterima {jumlah_hari}"
            )
        return jumlah_hari

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung total biaya sewa termasuk biaya tambahan."""
        hari = self.hari_ditagih(jumlah_hari)
        return self._tarif_harian * hari + self.biaya_tambahan(hari)

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        if hari_terlambat < 0:
            raise HariTidakValid(
                f"hari terlambat tidak boleh minus, diterima {hari_terlambat}"
            )

        per_hari = self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        return (
            f"[{self._kode}] {self._nama} — "
            f"{self.format_rupiah(self._tarif_harian)}/hari"
        )

    def __str__(self) -> str:
        return self.keterangan()

    def __repr__(self) -> str:
        return (
            f"AlatTani(kode={self._kode!r}, "
            f"nama={self._nama!r}, tarif_harian={self._tarif_harian!r})"
        )

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode

    def __hash__(self) -> int:
        return hash(self._kode)
