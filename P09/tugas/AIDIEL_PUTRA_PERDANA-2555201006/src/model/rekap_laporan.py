from typing import Protocol, runtime_checkable


@runtime_checkable
class CatatanKeuangan(Protocol):
    """Kontrak struktural untuk setiap catatan arus kas masuk atau keluar warung."""

    @property
    def kode_catatan(self) -> str: ...

    def keterangan_singkat(self) -> str: ...

    def nominal_pemasukan(self) -> int: ...

    def nominal_pengeluaran(self) -> int: ...


class RekapLaporan:
    """Menghitung omzet harian, pengeluaran kulakan, dan keuntungan bersih SRC Datuk."""

    def __init__(self, catatan: list[CatatanKeuangan]) -> None:
        self._catatan = list(catatan)

    def total_omzet(self) -> int:
        return sum(item.nominal_pemasukan() for item in self._catatan)

    def total_pengeluaran(self) -> int:
        return sum(item.nominal_pengeluaran() for item in self._catatan)

    def keuntungan_bersih(self) -> int:
        return self.total_omzet() - self.total_pengeluaran()