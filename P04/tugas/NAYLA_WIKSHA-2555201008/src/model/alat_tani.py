
from typing import Final


class AlatTani:
    """Mewakili alat tani dengan tarif sewa yang tervalidasi."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_CSV: Final[int] = 3

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        """Menginisialisasi data alat tani."""
        if not kode.strip():
            raise ValueError("Kode alat tani tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama alat tani tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

        AlatTani._jumlah_terdaftar += 1

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa apakah tarif berada dalam rentang yang wajar."""
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Memformat angka menjadi nominal rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah objek alat tani yang terdaftar."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> AlatTani:
        """Membuat objek dari baris berformat kode;nama;tarif."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError("Baris harus berisi kode, nama, dan tarif")

        kode, nama, tarif_teks = bagian

        try:
            tarif = int(tarif_teks)
        except ValueError:
            raise ValueError("Tarif harus berupa angka") from None

        return cls(kode.strip(), nama.strip(), tarif)

    @property
    def kode(self) -> str:
        """Mengembalikan kode alat tani."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama alat tani."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Mengembalikan tarif sewa harian."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        """Mengubah tarif setelah memvalidasi nilainya."""
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                "Tarif harus antara "
                f"{self.format_rupiah(self.TARIF_MINIMUM)} dan "
                f"{self.format_rupiah(self.TARIF_MAKSIMUM)}"
            )

        self._tarif_harian = nilai

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda berdasarkan persentase tarif harian."""
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif")

        denda_per_hari = (
            self._tarif_harian * self.PERSEN_DENDA_HARIAN // 100
        )
        return denda_per_hari * hari_terlambat
