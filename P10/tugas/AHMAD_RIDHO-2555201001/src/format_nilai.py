
"""Pemformat nilai menggunakan singledispatch."""

from functools import singledispatch


@singledispatch
def format_nilai(nilai: object) -> str:
    """Format bawaan untuk tipe data yang belum didukung."""
    return str(nilai)


@format_nilai.register(int)
def _(nilai: int) -> str:
    """Memformat bilangan bulat sebagai Rupiah."""
    return "Rp" + f"{nilai:,}".replace(",", ".")


@format_nilai.register(float)
def _(nilai: float) -> str:
    """Memformat bilangan desimal sebagai persentase."""
    return f"{nilai}%"


@format_nilai.register(list)
def _(nilai: list[object]) -> str:
    """Memformat setiap elemen dalam daftar."""
    return "[" + ", ".join(format_nilai(item) for item in nilai) + "]"
