from typing import Final

"""Model domain untuk barang dagangan UMKM Kios Pertanian di Bangkinang."""


class Kios:
    """Mengelola data produk beserta harga pokok dan harga jualnya."""

    # --- Konstanta Kelas (3 konstanta Final, 1 berupa persentase) ---
    PERSEN_MARGIN_UNTUNG: Final[int] = 20
    BATAS_HARGA_POKOK_MAKS: Final[int] = 2_000_000
    PEMISAH_BARIS: Final[str] = "|"

    # --- Atribut Kelas (Pencacah barang terdaftar) ---
    _total_produk_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, harga_pokok: int) -> None:
        if not kode.strip():
            raise ValueError("Kode barang tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama barang tidak boleh kosong.")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_pokok = 0
        self.harga_pokok = harga_pokok

        Kios._total_produk_terdaftar += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga_pokok(self) -> int:
        return self._harga_pokok

    @harga_pokok.setter
    def harga_pokok(self, nilai: int) -> None:
        if not Kios.cek_harga_valid(nilai):
            raise ValueError(
                f"Harga pokok {nilai} tidak valid (harus 1 s.d. {Kios.BATAS_HARGA_POKOK_MAKS})."
            )
        self._harga_pokok = nilai

    def hitung_harga_jual(self) -> int:
        """Menghitung harga jual berdasarkan persentase margin keuntungan."""
        laba = self._harga_pokok * Kios.PERSEN_MARGIN_UNTUNG // 100
        return self._harga_pokok + laba

    def format_baris_tabel(self) -> str:
        """Mencetak baris produk berformat rapi menggunakan f-string alignment."""
        return (
            f"[{self._kode:<6}] {self._nama:<18} | "
            f"Modal: Rp{self._harga_pokok:>8,} | "
            f"Jual: Rp{self.hitung_harga_jual():>8,}"
        )

    @staticmethod
    def cek_harga_valid(nilai: int) -> bool:
        """Pemeriksaan kewajaran harga pokok."""
        return 0 < nilai <= Kios.BATAS_HARGA_POKOK_MAKS

    @classmethod
    def dari_teks_pembatas(cls, baris: str) -> "Kios":
        """Membangun objek dari format teks: KODE|NAMA|HARGA."""
        elemen = baris.strip().split(cls.PEMISAH_BARIS)
        if len(elemen) != 3:
            raise ValueError(
                f"Format baris harus 3 bagian terpisah '{cls.PEMISAH_BARIS}', diterima {len(elemen)}."
            )

        kd, nm, hg = elemen
        if not hg.strip().isdigit():
            raise ValueError(f"Harga harus berupa angka bulat positif, diterima '{hg}'.")

        return cls(kd, nm, int(hg))

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._total_produk_terdaftar