from typing import Final

class Kios:
    """Model data untuk satu jenis produk di UMKM Kios Bangkinang."""

    PERSEN_LABA_MINIMUM: Final[int] = 15 
    HARGA_MODAL_MAKS: Final[int] = 1_000_000
    PEMISAH_DATA: Final[str] = ";"

    _jumlah_macam_produk: int = 0

    def __init__(self, kode: str, nama: str, modal: int) -> None:
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama produk tidak boleh kosong.")
        
        self._kode = kode
        self._nama = nama
        self._modal = 0
        self.modal = modal
        
        Kios._jumlah_macam_produk += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def modal(self) -> int:
        return self._modal

    @modal.setter
    def modal(self, nilai: int) -> None:
        if not Kios.harga_masuk_akal(nilai):
            raise ValueError(f"Harga modal {nilai} ditolak (batas: 1 - {Kios.HARGA_MODAL_MAKS}).")
        self._modal = nilai

    def hitung_harga_jual(self) -> int:
        """Menghitung harga jual menggunakan margin persentase."""
        laba = self._modal * Kios.PERSEN_LABA_MINIMUM // 100
        return self._modal + laba

    def daftar_tampil(self) -> str:
        """Pemformatan teks rapi menggunakan f-string untuk daftar harga rak."""
        return f"[{self._kode:<5}] {self._nama:<15} | Modal: Rp{self._modal:>7,} | Jual: Rp{self.hitung_harga_jual():>7,}"

    @staticmethod
    def harga_masuk_akal(nilai: int) -> bool:
        """Memeriksa apakah harga wajar (tidak minus dan tidak lewat batas)."""
        return 0 < nilai <= Kios.HARGA_MODAL_MAKS

    @classmethod
    def dari_baris_pendataan(cls, baris: str) -> "Kios":
        """Membangun objek dari baris berformat seperti: BRS01;Beras KuriK;15000"""
        potongan = baris.strip().split(cls.PEMISAH_DATA)
        if len(potongan) != 3:
            raise ValueError(f"Baris harus 3 bagian, diterima {len(potongan)}.")
        
        kode, nama, harga_teks = potongan
        
        if not harga_teks.strip().isdigit():
            raise ValueError("Harga modal harus berupa angka bulat penuh.")
            
        return cls(kode.strip(), nama.strip(), int(harga_teks.strip()))

    @classmethod
    def total_produk_terdaftar(cls) -> int:
        return cls._jumlah_macam_produk