
"""Memformat nilai berdasarkan tipe data menggunakan singledispatch."""

from functools import singledispatch


@singledispatch
def sebagai_teks(nilai: object) -> str:
    """Bentuk umum untuk tipe yang tidak memiliki format khusus."""
    return str(nilai)


@sebagai_teks.register(int)
def _bilangan_bulat(nilai: int) -> str:
    """Memformat bilangan bulat sebagai Rupiah."""
    return "Rp" + f"{nilai:,}".replace(",", ".")


@sebagai_teks.register(float)
def _bilangan_pecahan(nilai: float) -> str:
    """Memformat bilangan pecahan sebagai persentase."""
    return f"{nilai * 100:.1f}%"


@sebagai_teks.register(list)
def _daftar(nilai: list[object]) -> str:
    """Memformat setiap elemen daftar secara rekursif."""
    return ", ".join(sebagai_teks(butir) for butir in nilai)
