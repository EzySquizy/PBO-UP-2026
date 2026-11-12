
"""Model domain: alat yang disewakan UPJA."""

from typing import Final


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_CSV: Final[int] = 3

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

        AlatTani._jumlah_terdaftar += 1

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa apakah tarif berada dalam batas wajar."""
        return (
            AlatTani.TARIF_MINIMUM
            <= nilai
            <= AlatTani.TARIF_MAKSIMUM
        )

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah objek AlatTani yang telah dibuat."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> AlatTani:
        """Membuat objek AlatTani dari baris CSV sederhana."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "baris CSV harus berisi kode, nama, dan tarif"
            )

        kode, nama, tarif = bagian

        if not tarif.strip().isdigit():
            raise ValueError("tarif harus berupa angka")

        return cls(kode.strip(), nama.strip(), int(tarif))

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda keterlambatan pengembalian alat."""
        if hari_terlambat < 0:
            raise ValueError("hari terlambat tidak boleh negatif")

        per_hari = (
            self._tarif_harian
            * AlatTani.PERSEN_DENDA_HARIAN
            // 100
        )
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = self.format_rupiah(self._tarif_harian)
        return f"[{self._kode}] {self._nama} — {rupiah}/hari"

    @property
    def kode(self) -> str:
        """Kode alat. Tidak dapat diubah setelah alat dibuat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat. Tidak dapat diubah setelah alat dibuat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Tarif sewa per hari dalam rupiah."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not self.tarif_wajar(nilai):
            raise ValueError(
                "tarif harus antara "
                f"{self.format_rupiah(self.TARIF_MINIMUM)} dan "
                f"{self.format_rupiah(self.TARIF_MAKSIMUM)}, "
                f"diterima {nilai}"
            )

        self._tarif_harian = nilai
