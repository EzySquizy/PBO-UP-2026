
"""Pengujian format nilai menggunakan singledispatch."""

from src.format_nilai import sebagai_teks


def test_format_bilangan_bulat() -> None:
    assert sebagai_teks(150_000) == "Rp150.000"


def test_format_bilangan_pecahan() -> None:
    assert sebagai_teks(0.825) == "82.5%"


def test_format_daftar() -> None:
    assert sebagai_teks([150_000, 75_000]) == "Rp150.000, Rp75.000"


def test_format_teks_bawaan() -> None:
    assert sebagai_teks("SIPALA") == "SIPALA"


def test_format_daftar_berisi_tipe_berbeda() -> None:
    assert sebagai_teks([150_000, 0.825, "SIPALA"]) == (
        "Rp150.000, 82.5%, SIPALA"
    )
