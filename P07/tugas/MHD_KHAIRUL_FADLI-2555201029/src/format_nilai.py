
"""Pemformat nilai menggunakan singledispatch."""

from functools import singledispatch

from src.model.alat_tani import AlatTani


@singledispatch
def format_nilai(nilai: object) -> str:
    """Format nilai umum."""
    return str(nilai)


@format_nilai.register(bool)
def _(nilai: bool) -> str:
    """Format nilai boolean."""
    return str(nilai)


@format_nilai.register(int)
def _(nilai: int) -> str:
    """Format bilangan bulat sebagai Rupiah."""
    return AlatTani.format_rupiah(nilai)


@format_nilai.register(float)
def _(nilai: float) -> str:
    """Format bilangan desimal sebagai persentase."""
    return f"{nilai:.1%}"


@format_nilai.register(list)
def _(nilai: list[object]) -> str:
    """Format isi daftar secara rekursif."""
    return "[" + ", ".join(
        format_nilai(item) for item in nilai
    ) + "]"
