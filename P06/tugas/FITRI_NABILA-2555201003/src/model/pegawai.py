class Pegawai:
    """Kelas induk pegawai kontrak di instansi Pemkab Kampar."""
    
    def __init__(self, nip: str, nama: str, honor_harian: int) -> None:
        if honor_harian <= 0:
            raise ValueError(f"Honor harian harus di atas nol, diterima {honor_harian}")
        self._nip = nip
        self._nama = nama
        self._honor_harian = honor_harian

    def hitung_gaji(self, jumlah_hari: int) -> int:
        """Menghitung honor dasar berdasarkan absensi."""
        return self._honor_harian * jumlah_hari

    def keterangan(self) -> str:
        return f"[{self._nip}] {self._nama} (Rp{self._honor_harian}/hari)"

    def __str__(self) -> str:
        """Tampilan ramah pengguna untuk print()."""
        return self.keterangan()

    def __repr__(self) -> str:
        """Tampilan untuk debugging bagi pemrogram."""
        return (f"{type(self).__name__}(nip={self._nip!r}, "
                f"nama={self._nama!r}, honor_harian={self._honor_harian!r})")

    def __eq__(self, lain: object) -> bool:
        """Dua pegawai adalah orang yang sama jika NIP-nya sama."""
        if not isinstance(lain, Pegawai):
            return NotImplemented
        return self._nip == lain._nip

    def __hash__(self) -> int:
        """Syarat wajib pendamping __eq__ agar bisa masuk set/dict."""
        return hash(self._nip)