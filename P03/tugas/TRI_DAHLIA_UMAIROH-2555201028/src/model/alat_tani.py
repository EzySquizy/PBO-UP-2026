from typing import Final


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        riwayat: list[str] | None = None,
    ) -> None:
        self._kode = kode
        self._nama = nama
        self.tarif_harian = tarif_harian
        self._riwayat = list(riwayat) if riwayat else []
        AlatTani._jumlah_terdaftar += 1

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah objek AlatTani yang sudah dibuat."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        """Membuat AlatTani dari satu baris data dipisahkan titik koma."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError("Baris harus memiliki 3 bagian.")

        kode, nama, tarif = bagian

        if not tarif.strip().isdigit():
            raise ValueError("Tarif harus berupa angka.")

        return cls(kode.strip(), nama.strip(), int(tarif))
    
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
        """Tarif sewa alat per hari."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                f"tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} dan "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}, "
                f"diterima {nilai}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa kewajaran tarif tanpa perlu membuat alat terlebih dahulu."""
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi tulisan rupiah bergaya Indonesia."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda berdasarkan jumlah hari keterlambatan."""
        if hari_terlambat < 0:
            raise ValueError("Hari terlambat tidak boleh negatif.")

        per_hari = (
            self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        )
        return per_hari * hari_terlambat