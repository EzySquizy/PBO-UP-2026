"""Format data menggunakan singledispatch."""

from functools import singledispatch


@singledispatch
def format_data(data: object) -> str:
    """Menangani tipe data yang belum didukung."""
    return f"Tipe data {type(data).__name__} tidak didukung."


@format_data.register
def _(data: int) -> str:
    return f"Bilangan bulat: {data}"


@format_data.register
def _(data: float) -> str:
    return f"Bilangan desimal: {data}"


@format_data.register
def _(data: str) -> str:
    return f"Teks: {data}"
