
"""Pengujian fitur polimorfisme P07."""

import pytest
from src.format_nilai import format_nilai
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PenerjemahPerintah


def test_biaya_semua() -> None:
    alat = [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa", 75_000, 600),
        Perontok("PR-01", "Perontok", 200_000, 900),
    ]
    daftar = DaftarHarga(alat)

    assert daftar.biaya_semua(3) == [
        ("Traktor", 750_000),
        ("Pompa", 603_000),
        ("Perontok", 600_000),
    ]


def test_termurah() -> None:
    alat = [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa", 75_000, 600),
        Perontok("PR-01", "Perontok", 200_000, 900),
    ]
    daftar = DaftarHarga(alat)

    assert daftar.termurah(3) is alat[2]


def test_total_bila_semua_disewa() -> None:
    alat = [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa", 75_000, 600),
        Perontok("PR-01", "Perontok", 200_000, 900),
    ]
    daftar = DaftarHarga(alat)

    assert daftar.total_bila_semua_disewa(3) == 1_953_000


def test_daftar_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_jenis_alat_baru_tidak_perlu_mengubah_daftar_harga() -> None:
    class Penggiling(AlatTani):
        """Jenis alat baru untuk menguji polimorfisme."""

        ONGKOS_ANGKUT = 50_000

        def biaya_tambahan(self, _jumlah_hari: int) -> int:
            return self.ONGKOS_ANGKUT

        def syarat_pemakaian(self) -> str:
            return "Digunakan sesuai petunjuk."

    penggiling = Penggiling("PG-01", "Penggiling Gabah", 120_000)
    daftar = DaftarHarga([penggiling])

    assert daftar.biaya_semua(3) == [
        ("Penggiling Gabah", 410_000)
    ]
    assert daftar.total_bila_semua_disewa(3) == 410_000


def test_format_nilai_integer() -> None:
    assert format_nilai(150000) == "Rp150.000"


def test_format_nilai_float() -> None:
    assert format_nilai(75.5) == "75.5%"


def test_format_nilai_list() -> None:
    assert format_nilai([1000, 25.5, "Padi"]) == (
        "[Rp1.000, 25.5%, Padi]"
    )


def test_format_nilai_tipe_lain() -> None:
    assert format_nilai("PBO") == "PBO"


def test_perintah_bantuan() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert "Perintah tersedia" in penerjemah.terjemahkan("bantuan")


def test_perintah_daftar() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert penerjemah.terjemahkan("daftar 2") == "Traktor: Rp500.000"


def test_perintah_harga() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert penerjemah.terjemahkan("harga TR-01 2") == "Traktor: Rp500.000"


def test_perintah_kode_tidak_ditemukan() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert "tidak ditemukan" in penerjemah.terjemahkan("harga XX-01 2")


def test_perintah_termurah() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert penerjemah.terjemahkan("termurah 2") == "Traktor: Rp500.000"


def test_perintah_kosong() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert penerjemah.terjemahkan("") == "Perintah tidak boleh kosong."


def test_perintah_tidak_dikenal() -> None:
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8)
    ]
    penerjemah = PenerjemahPerintah(alat)

    assert "tidak dikenali" in penerjemah.terjemahkan("halo")
