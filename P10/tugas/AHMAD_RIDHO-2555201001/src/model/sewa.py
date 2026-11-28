
"""Transaksi penyewaan alat pertanian."""

from collections.abc import Iterator
from contextlib import contextmanager

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.galat import (
    AlatSudahAdaDalamSewa,
    BatasAlatTerlampaui,
    DataTidakValid,
    TransaksiTerkunci,
)
from src.model.penyewa import Penyewa
from src.model.status_sewa import StatusSewa


class Sewa:
    """Transaksi penyewaan alat pertanian."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise DataTidakValid("Nomor sewa tidak boleh kosong.")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []
        self._status = StatusSewa.DIPESAN

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        return self._penyewa

    @property
    def status(self) -> StatusSewa:
        return self._status

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        return tuple(self._baris)

    def ubah_status(self, status: StatusSewa) -> None:
        """Mengubah status transaksi sewa."""
        if not self._status.boleh_diubah():
            raise TransaksiTerkunci(
                f"Transaksi berstatus {self._status.value} "
                "tidak dapat diubah statusnya."
            )

        self._status = status

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        if not self._status.boleh_diubah():
            raise TransaksiTerkunci(
                f"Transaksi berstatus {self._status.value} "
                "tidak dapat ditambah alat."
            )

        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise BatasAlatTerlampaui(
                "Maksimal 10 jenis alat dalam satu sewa."
            )

        for item in self._baris:
            if item.kode_alat == alat.kode:
                raise AlatSudahAdaDalamSewa(
                    f"Alat dengan kode {alat.kode} sudah ditambahkan."
                )

        item = BarisSewa(alat, jumlah_hari)
        self._baris.append(item)

    @contextmanager
    def transaksi(self) -> Iterator[Sewa]:
        """Membatalkan seluruh perubahan jika transaksi gagal."""
        semula = list(self._baris)

        try:
            yield self
        except Exception:
            self._baris = semula
            raise

    def total(self) -> int:
        return sum(item.subtotal() for item in self._baris)

    def nota(self) -> str:
        hasil = [
            "NOTA PENYEWAAN",
            f"Nomor: {self._nomor}",
            f"Penyewa: {self._penyewa.identitas()}",
            f"Status: {self._status.value}",
            "-" * 50,
        ]

        for item in self._baris:
            hasil.append(item.baris_nota())

        hasil.extend([
            "-" * 50,
            f"TOTAL: {AlatTani.format_rupiah(self.total())}",
        ])

        return "\n".join(hasil)
