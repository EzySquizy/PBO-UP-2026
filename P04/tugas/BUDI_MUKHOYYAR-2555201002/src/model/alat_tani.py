
from typing import Final

"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    # Konstanta kelas
    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")
        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah alat yang sudah pernah dibuat."""
        return cls._jumlah_terdaftar

    
    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        """Membuat objek AlatTani dari baris data."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError(
                "Baris harus berisi kode, nama, dan tarif harian."
            )

        kode, nama, tarif_teks = bagian

        try:
            tarif = int(tarif_teks)
        except ValueError as exc:
            raise ValueError("Tarif harian harus berupa angka.") from exc

        return cls(kode.strip(), nama.strip(), tarif)


    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa apakah tarif berada dalam rentang yang wajar."""
        return (
            AlatTani.TARIF_MINIMUM
            <= nilai
            <= AlatTani.TARIF_MAKSIMUM
        )

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format mata uang rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

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
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                "Tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} "
                "dan "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}."
            )
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    
    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda berdasarkan jumlah hari keterlambatan."""
        return (
            self._tarif_harian
            * self.PERSEN_DENDA_HARIAN
            * hari_terlambat
            // 100
        )


    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
