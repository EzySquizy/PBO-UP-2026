
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
        """Memeriksa apakah tarif berada dalam rentang yang diizinkan."""
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah objek alat yang berhasil dibuat."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> AlatTani:
        """Membuat objek alat dari tiga kolom data yang dipisahkan titik koma."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError("baris harus terdiri dari tiga kolom")

        kode, nama, tarif = bagian

        if not tarif.strip().isdigit():
            raise ValueError("tarif harus berupa angka")

        return cls(kode.strip(), nama.strip(), int(tarif.strip()))

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda keterlambatan sebesar 10 persen per hari."""
        if hari_terlambat < 0:
            raise ValueError("hari terlambat tidak boleh negatif")

        per_hari = (
            self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        )
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        """Mengembalikan informasi alat beserta tarif hariannya."""
        return (
            f"[{self._kode}] {self._nama} — "
            f"{self.format_rupiah(self._tarif_harian)}/hari"
        )

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
                f"tarif harus antara "
                f"{self.format_rupiah(self.TARIF_MINIMUM)} dan "
                f"{self.format_rupiah(self.TARIF_MAKSIMUM)}, "
                f"diterima {nilai}"
            )
        self._tarif_harian = nilai
