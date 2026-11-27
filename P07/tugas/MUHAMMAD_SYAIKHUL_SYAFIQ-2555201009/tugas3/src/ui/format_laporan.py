
"""Pemformat nilai laporan berdasarkan tipe data."""

from functools import singledispatch


@singledispatch
def format_nilai(nilai: object) -> str:
    """Memformat tipe data yang tidak didukung."""
    return str(nilai)


@format_nilai.register
def _(nilai: int) -> str:
    """Memformat bilangan bulat."""
    return f"Bilangan bulat: {nilai}"


@format_nilai.register
def _(nilai: float) -> str:
    """Memformat bilangan desimal."""
    return f"Bilangan desimal: {nilai:.2f}"


@format_nilai.register
def _(nilai: str) -> str:
    """Memformat teks."""
    return f"Teks: {nilai}"

@format_nilai.register(list)
def _(nilai: list[object]) -> str:
    return f"Daftar berisi {len(nilai)} data"
