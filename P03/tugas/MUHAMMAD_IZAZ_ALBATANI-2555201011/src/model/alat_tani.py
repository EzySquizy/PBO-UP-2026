"""Model domain: alat yang disewakan UPJA."""

from typing import Final

BATAS_TARIF_MAKSIMUM: Final[int] = 5_000_000


class AlatTani:
    """Menyimpan informasi alat pertanian dan tarif sewanya."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif: int,
    ) -> None:
        if tarif <= 0:
            raise ValueError(
                f"tarif harus lebih dari nol, diterima {tarif}"
            )
        if tarif > BATAS_TARIF_MAKSIMUM:
            raise ValueError(
                f"tarif tidak wajar, diterima {tarif}"
            )

        self._kode = kode
        self._nama = nama
        self._tarif = tarif

    # Kode alat merupakan identitas tetap sehingga hanya boleh dibaca.
    @property
    def kode(self) -> str:
        return self._kode

    # Nama alat hanya boleh dibaca melalui objek.
    @property
    def nama(self) -> str:
        return self._nama

    # Tarif alat dijaga agar tidak diubah langsung.
    @property
    def tarif(self) -> int:
        return self._tarif

    def biaya_sewa(self, hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        if hari <= 0:
            raise ValueError("lama sewa harus lebih dari nol hari")
        return self._tarif * hari

    def keterangan(self) -> str:
        """Mengembalikan keterangan alat dan tarif sewanya."""
        tarif_format = f"{self._tarif:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{tarif_format}/hari"
