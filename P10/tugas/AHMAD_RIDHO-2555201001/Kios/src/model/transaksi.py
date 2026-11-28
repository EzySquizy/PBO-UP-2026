from collections.abc import Iterator
from contextlib import contextmanager

from src.model.kios import Kios


@contextmanager
def transaksi_kios() -> Iterator[list[Kios]]:
    """Mengelola pendaftaran produk dengan mekanisme rollback."""
    jumlah_awal = Kios.jumlah_produk()
    produk_terdaftar: list[Kios] = []

    try:
        yield produk_terdaftar
    except Exception:
        Kios._pulihkan_jumlah_produk(jumlah_awal)
        produk_terdaftar.clear()
        raise
