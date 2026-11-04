from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Transaksi penyewaan alat pertanian."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("Nomor sewa tidak boleh kosong.")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("Maksimal 10 jenis alat dalam satu sewa.")

        for item in self._baris:
            if item.kode_alat == alat.kode:
                raise ValueError(
                    f"Alat dengan kode {alat.kode} sudah ditambahkan."
                )

        item = BarisSewa(alat, jumlah_hari)
        self._baris.append(item)

    def total(self) -> int:
        return sum(item.subtotal() for item in self._baris)

    def nota(self) -> str:
        hasil = [
            "NOTA PENYEWAAN",
            f"Nomor: {self._nomor}",
            f"Penyewa: {self._penyewa.identitas()}",
            "-" * 50,
        ]

        for item in self._baris:
            hasil.append(item.baris_nota())

        hasil.extend([
            "-" * 50,
            f"TOTAL: {AlatTani.format_rupiah(self.total())}",
        ])

        return "\n".join(hasil)
