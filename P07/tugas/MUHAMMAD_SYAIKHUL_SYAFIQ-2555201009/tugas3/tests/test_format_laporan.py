"""Pengujian format nilai dengan singledispatch."""

from src.ui.format_laporan import format_nilai


def test_format_integer() -> None:
    assert format_nilai(10) == "Bilangan bulat: 10"


def test_format_float() -> None:
    assert format_nilai(3.5) == "Bilangan desimal: 3.50"


def test_format_string() -> None:
    assert format_nilai("Andi") == "Teks: Andi"


def test_format_list() -> None:
    assert format_nilai([1, 2]) == "Daftar berisi 2 data"


def test_format_list_kosong() -> None:
    assert format_nilai([]) == "Daftar berisi 0 data"


def test_format_tipe_lain() -> None:
    assert format_nilai(True) == "Bilangan bulat: True"