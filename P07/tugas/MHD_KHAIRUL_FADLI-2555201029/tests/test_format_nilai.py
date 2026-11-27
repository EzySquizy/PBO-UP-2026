
"""Pengujian format nilai menggunakan singledispatch."""

from src.format_nilai import format_nilai


def test_format_nilai_integer() -> None:
    """Bilangan bulat diformat sebagai Rupiah."""
    assert format_nilai(150_000) == "Rp150.000"


def test_format_nilai_integer_nol() -> None:
    """Nilai nol diformat sebagai Rupiah."""
    assert format_nilai(0) == "Rp0"


def test_format_nilai_float() -> None:
    """Bilangan desimal diformat sebagai persentase."""
    assert format_nilai(0.75) == "75.0%"


def test_format_nilai_float_kecil() -> None:
    """Persentase kecil tetap diformat dengan benar."""
    assert format_nilai(0.125) == "12.5%"


def test_format_nilai_string() -> None:
    """Tipe data lain menggunakan format umum."""
    assert format_nilai("Praktikum P07") == "Praktikum P07"


def test_format_nilai_boolean() -> None:
    """Nilai boolean menggunakan format umum."""
    assert format_nilai(True) == "True"


def test_format_nilai_list_integer() -> None:
    """Daftar bilangan bulat diformat secara rekursif."""
    assert format_nilai([100_000, 200_000]) == (
        "[Rp100.000, Rp200.000]"
    )


def test_format_nilai_list_campuran() -> None:
    """Daftar dengan berbagai tipe data diformat."""
    assert format_nilai([100_000, 0.5, "UPJA"]) == (
        "[Rp100.000, 50.0%, UPJA]"
    )


def test_format_nilai_list_kosong() -> None:
    """Daftar kosong menghasilkan tanda kurung siku kosong."""
    assert format_nilai([]) == "[]"


def test_format_nilai_list_bersarang() -> None:
    """Daftar bersarang diformat secara rekursif."""
    assert format_nilai([[100_000], [0.5]]) == (
        "[[Rp100.000], [50.0%]]"
    )


def test_format_nilai_float_nol() -> None:
    """Persentase nol diformat dengan benar."""
    assert format_nilai(0.0) == "0.0%"


def test_format_nilai_integer_negatif() -> None:
    """Bilangan bulat negatif tetap diformat sebagai Rupiah."""
    assert format_nilai(-50_000) == "Rp-50.000"
