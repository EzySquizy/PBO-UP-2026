
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
        if not kode.strip():
            raise ValueError("kode tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")

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
        if not AlatTani.tarif_wajar(nilai):
            minimum = AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)
            maksimum = AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)
            raise ValueError(
                f"tarif harus antara {minimum} dan {maksimum}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa kewajaran tarif tanpa membuat objek."""
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah bilangan menjadi format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah alat yang berhasil didaftarkan."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> AlatTani:
        """Membuat objek dari baris berkode;nama;tarif."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError(
                "baris harus berisi kode, nama, dan tarif"
            )

        kode, nama, tarif = bagian

        if not kode.strip() or not nama.strip():
            raise ValueError("kode dan nama tidak boleh kosong")

        try:
            nilai_tarif = int(tarif.strip())
        except ValueError as kesalahan:
            raise ValueError("tarif harus berupa bilangan bulat") from kesalahan

        return cls(kode.strip(), nama.strip(), nilai_tarif)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari nol")
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda berdasarkan persentase tarif harian."""
        if hari_terlambat < 0:
            raise ValueError("hari terlambat tidak boleh negatif")

        per_hari = (
            self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        )
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        tarif = self.format_rupiah(self._tarif_harian)
        return f"[{self._kode}] {self._nama} - {tarif}/hari"
