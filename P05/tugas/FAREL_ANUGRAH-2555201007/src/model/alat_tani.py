"""Model domain alat pertanian."""

from typing import Final


class AlatTani:
    """Satu unit alat pertanian dan tarif sewanya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_BARIS: Final[int] = 3

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

        AlatTani._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        """Kode alat yang tidak dapat diubah setelah dibuat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat yang tidak dapat diubah setelah dibuat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Tarif sewa per hari dalam rupiah."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                "tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} "
                "dan "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}, "
                f"diterima {AlatTani.format_rupiah(nilai)}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa apakah tarif berada dalam batas yang ditentukan."""
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format mata uang rupiah."""
        return f"Rp{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah alat yang telah didaftarkan."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> AlatTani:
        """Membuat objek AlatTani dari baris CSV sederhana."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_BARIS:
            raise ValueError(
                "baris CSV harus memiliki 3 bagian: kode;nama;tarif"
            )

        kode, nama, tarif = (item.strip() for item in bagian)

        try:
            nilai_tarif = int(tarif)
        except ValueError as exc:
            raise ValueError("tarif harus berupa angka bulat") from exc

        return cls(kode, nama, nilai_tarif)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda sebesar 10 persen per hari keterlambatan."""
        if hari_terlambat < 0:
            raise ValueError("hari terlambat tidak boleh negatif")

        denda_per_hari = (
            self._tarif_harian * self.PERSEN_DENDA_HARIAN // 100
        )
        return denda_per_hari * hari_terlambat

    def keterangan(self) -> str:
        """Mengembalikan keterangan alat dan tarif sewanya."""
        return (
            f"[{self._kode}] {self._nama} — "
            f"{self.format_rupiah(self._tarif_harian)}/hari"
        )
