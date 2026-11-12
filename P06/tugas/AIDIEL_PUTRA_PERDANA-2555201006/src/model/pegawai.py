class Pegawai:
    """Kelas induk untuk pegawai instansi di Kabupaten Kampar."""
    
    def __init__(self, nip: str, nama: str, gaji_harian: int) -> None:
        if gaji_harian <= 0:
            raise ValueError(f"gaji harian harus lebih dari nol, diterima {gaji_harian}")
        self._nip = nip
        self._nama = nama
        self._gaji_harian = gaji_harian

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        """Menghitung gaji dasar berdasarkan hari kehadiran."""
        return self._gaji_harian * jumlah_hari

    def keterangan(self) -> str:
        return f"[{self._nip}] {self._nama} - Rp{self._gaji_harian}/hari"

    def __str__(self) -> str:
        """Untuk dibaca manusia: dipakai print() dan f-string."""
        return self.keterangan()

    def __repr__(self) -> str:
        """Untuk dibaca pemrogram: dipakai saat menampilkan isi koleksi."""
        return (f"{type(self).__name__}(nip={self._nip!r}, "
                f"nama={self._nama!r}, gaji_harian={self._gaji_harian!r})")

    def __eq__(self, lain: object) -> bool:
        """Dua pegawai dianggap sama bila NIP-nya sama, karena NIP adalah identitas."""
        if not isinstance(lain, Pegawai):
            return NotImplemented
        return self._nip == lain._nip

    def __hash__(self) -> int:
        """Wajib ditulis bersama __eq__ agar objek dapat dimasukkan set."""
        return hash(self._nip)