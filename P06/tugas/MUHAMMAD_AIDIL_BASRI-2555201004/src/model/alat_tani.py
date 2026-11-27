"""Model domain: alat pertanian yang disewakan."""

from typing import Final


class AlatTani:
    """Menyimpan data alat pertanian dan tarif sewanya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_CSV: Final[int] = 4
    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama alat tidak boleh kosong")
        self._kode = kode.strip()
        self._nama = nama.strip()
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
        if not self.tarif_wajar(nilai):
            raise ValueError(
                f"tarif harus antara Rp{self.TARIF_MINIMUM:,} dan "
                f"Rp{self.TARIF_MAKSIMUM:,}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return f"Rp{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar

    def biaya_sewa(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari 0")
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        return (
            f"[{self._kode}] {self._nama} — "
            f"{self.format_rupiah(self._tarif_harian)}/hari"
        )
    def __str__(self) -> str:
        """Menghasilkan tampilan alat yang mudah dibaca."""
        return self.keterangan()

    def __repr__(self) -> str:
        """Menghasilkan representasi objek untuk keperluan pengembang."""
        return (
            f"{type(self).__name__}("
            f"kode={self._kode!r}, "
            f"nama={self._nama!r}, "
            f"tarif_harian={self._tarif_harian!r})"
        )

    def __eq__(self, lain: object) -> bool:
        """Membandingkan alat berdasarkan kode unik."""
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode

    def __hash__(self) -> int:
        """Menghasilkan hash berdasarkan kode unik alat."""
        return hash(self._kode)
