"""Model gerobak dorong yang memenuhi kontrak Sewaan tanpa mewarisi AlatTani."""


class GerobakDorong:
    """Gerobak dorong untuk kebutuhan pengangkutan hasil pertanian."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")
        if tarif_harian <= 0:
            raise ValueError("tarif harian harus lebih dari nol")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    def biaya_sewa(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari nol")
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
