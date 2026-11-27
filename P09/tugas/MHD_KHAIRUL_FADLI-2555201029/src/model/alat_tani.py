
"""Model abstrak alat yang disewakan UPJA."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Final


class AlatTani(ABC):
    """Kelas abstrak untuk seluruh alat pertanian."""

    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_CSV: Final[int] = 3
    JUMLAH_TERDAFTAR: ClassVar[int] = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")

        if not nama.strip():
            raise ValueError("nama alat tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self.tarif_harian = tarif_harian
        AlatTani.JUMLAH_TERDAFTAR += 1

    @property
    def kode(self) -> str:
        """Kode unik alat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Tarif sewa per hari."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError("tarif harian harus lebih dari nol")
        self._tarif_harian = nilai

    @classmethod
    def dari_baris_csv(
        cls,
        baris: str,
    ) -> AlatTani:
        """Membuat objek AlatTani dari baris CSV sederhana."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError("format CSV alat tidak valid")

        try:
            tarif = int(bagian[2])
        except ValueError as exc:
            raise ValueError("tarif harus berupa angka") from exc

        return cls(bagian[0], bagian[1], tarif)

    @abstractmethod
    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung biaya tambahan sesuai jenis alat."""
        ...

    @abstractmethod
    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat pemakaian alat."""
        ...

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Memvalidasi dan menentukan jumlah hari yang ditagihkan."""
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari nol")
        return jumlah_hari

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa beserta biaya tambahannya."""
        hari = self.hari_ditagih(jumlah_hari)
        return (
            self._tarif_harian * hari
            + self.biaya_tambahan(hari)
        )

    def keterangan(self) -> str:
        """Mengembalikan keterangan alat."""
        return (
            f"[{self._kode}] {self._nama} - "
            f"{self.format_rupiah(self._tarif_harian)}/hari"
        )

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Memformat angka menjadi rupiah."""
        return f"Rp{nilai:,}".replace(",", ".")

    def __str__(self) -> str:
        return self.keterangan()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self._kode!r}, {self._nama!r}, "
            f"{self._tarif_harian!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AlatTani):
            return NotImplemented
        return self._kode == other._kode

    def __hash__(self) -> int:
        return hash(self._kode)
