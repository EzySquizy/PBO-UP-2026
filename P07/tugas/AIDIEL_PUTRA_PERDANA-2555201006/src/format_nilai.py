from __future__ import annotations

from functools import singledispatch


@singledispatch
def format_nilai(nilai: object) -> str:
    """Format bawaan untuk tipe umum."""
    return str(nilai)


@format_nilai.register(int)
def _format_int(nilai: int) -> str:
    return "Rp" + f"{nilai:,}".replace(",", ".")


@format_nilai.register(float)
def _format_float(nilai: float) -> str:
    return f"{nilai * 100:.1f}%"


@format_nilai.register(list)
def _format_list(nilai: list[object]) -> str:
    if not nilai:
        return "-"
    return ", ".join(format_nilai(item) for item in nilai)