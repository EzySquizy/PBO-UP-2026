
"""Fungsi untuk mengubah berbagai jenis nilai menjadi teks."""

from functools import singledispatch

from src.model.alat_tani import AlatTani


@singledispatch
def sebagai_teks(nilai: object) -> str:
    """Mengubah nilai umum menjadi teks."""
    return str(nilai)


@sebagai_teks.register
def _(nilai: int) -> str:
    """Mengubah bilangan bulat menjadi format rupiah."""
    return AlatTani.format_rupiah(nilai)


@sebagai_teks.register
def _(nilai: float) -> str:
    """Mengubah bilangan desimal menjadi persentase."""
    return f"{nilai * 100:.1f}%"


@sebagai_teks.register(list)
def _(nilai: list[object]) -> str:
    """Mengubah isi daftar menjadi teks secara berulang."""
    return ", ".join(sebagai_teks(item) for item in nilai)
