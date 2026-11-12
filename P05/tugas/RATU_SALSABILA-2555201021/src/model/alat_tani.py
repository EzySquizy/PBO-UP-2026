
"""Model domain: alat yang disewakan UPJA."""

from typing import Final


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        """Membuat alat tani dan menghitung jumlah alat terdaftar."""
        self._kode = kode
        self._nama = nama
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        """Mengembalikan kode alat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama alat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Mengembalikan tarif sewa harian."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        """Memastikan tarif berada dalam rentang yang valid."""
        if not AlatTani.tarif_wajar(nilai):
            minimum = AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)
            maksimum = AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)
            raise ValueError(
                f"Tarif harian harus antara {minimum} dan {maksimum}."
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa apakah tarif berada dalam rentang yang diperbolehkan."""
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah objek alat yang telah dibuat."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        """Membuat objek alat dari baris berkode, nama, dan tarif."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError(
                "Baris CSV harus berisi kode, nama, dan tarif."
            )

        kode, nama, tarif = (bagian_item.strip() for bagian_item in bagian)

        if not tarif.isdigit():
            raise ValueError("Tarif harus berupa bilangan bulat.")

        return cls(kode, nama, int(tarif))

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari."""
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda berdasarkan jumlah hari keterlambatan."""
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif.")

        per_hari = (
            self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        )
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        tarif = AlatTani.format_rupiah(self._tarif_harian)
        return f"[{self._kode}] {self._nama} — {tarif}/hari"
