
"""Model gerobak dorong yang memenuhi kontrak Sewaan."""



class GerobakDorong:
    """Gerobak dorong yang dapat disewakan tanpa mewarisi AlatTani."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode gerobak tidak boleh kosong")

        if not nama.strip():
            raise ValueError("nama gerobak tidak boleh kosong")

        if tarif_harian <= 0:
            raise ValueError("tarif harian harus lebih dari nol")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Mengembalikan kode gerobak."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama gerobak."""
        return self._nama

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa gerobak."""
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari nol")

        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan keterangan gerobak."""
        tarif = f"Rp{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — {tarif}/hari"
