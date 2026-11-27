
"""Pengujian untuk fungsi sebagai_teks."""

from src.format_nilai import sebagai_teks


def test_format_nilai_teks() -> None:
    assert sebagai_teks("Halo") == "Halo"


def test_format_nilai_integer() -> None:
    assert sebagai_teks(150_000) == "Rp150.000"


def test_format_nilai_integer_nol() -> None:
    assert sebagai_teks(0) == "Rp0"


def test_format_nilai_float() -> None:
    assert sebagai_teks(0.15) == "15.0%"


def test_format_nilai_float_satu() -> None:
    assert sebagai_teks(1.0) == "100.0%"


def test_format_nilai_float_desimal() -> None:
    assert sebagai_teks(0.256) == "25.6%"


def test_format_nilai_list_integer() -> None:
    assert sebagai_teks([100_000, 200_000]) == "Rp100.000, Rp200.000"


def test_format_nilai_list_campuran() -> None:
    assert sebagai_teks([150_000, 0.15, "Selesai"]) == (
        "Rp150.000, 15.0%, Selesai"
    )


def test_format_nilai_list_kosong() -> None:
    assert sebagai_teks([]) == ""


def test_format_nilai_list_bersarang() -> None:
    assert sebagai_teks([[100_000, 0.15], "Selesai"]) == (
        "Rp100.000, 15.0%, Selesai"
    )
