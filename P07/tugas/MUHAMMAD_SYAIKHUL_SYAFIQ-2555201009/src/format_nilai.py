
"""Pemformatan nilai menggunakan singledispatch."""

from functools import singledispatch


@singledispatch
def sebagai_teks(nilai: object) -> str:
    """Memformat nilai secara umum."""
    return str(nilai)


@sebagai_teks.register
def _(nilai: int) -> str:
    """Memformat bilangan bulat sebagai rupiah."""
    return "Rp" + f"{nilai:,}".replace(",", ".")


@sebagai_teks.register
def _(nilai: float) -> str:
    """Memformat bilangan desimal sebagai persentase."""
    return f"{nilai * 100:.1f}%"


@sebagai_teks.register(list)
def _(nilai: list[object]) -> str:
    """Memformat setiap anggota daftar."""
    return ", ".join(sebagai_teks(butir) for butir in nilai)
