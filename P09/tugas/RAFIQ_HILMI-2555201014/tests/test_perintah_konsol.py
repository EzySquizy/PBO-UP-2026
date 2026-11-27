
"""Pengujian untuk class PerintahKonsol."""

import pytest
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewaan import Sewaan
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


@pytest.fixture
def konsol() -> PerintahKonsol:
    alat: list[Sewaan] = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 45),
        PompaAir("PA-01", "Pompa Air Honda", 80_000, 100),
        Perontok("PR-01", "Perontok Padi", 100_000, 10),
        GerobakDorong("GD-01", "Gerobak Dorong", 150_000),
    ]
    return PerintahKonsol(DaftarHarga(alat))


def test_perintah_bantuan(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("bantuan")
    assert "daftar <hari>" in hasil
    assert "harga <kode> <hari>" in hasil
    assert "termurah <hari>" in hasil


def test_perintah_tanda_tanya(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("?") == PerintahKonsol.BANTUAN


def test_perintah_kosong(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("") == "Perintah kosong. Ketik 'bantuan'."


def test_perintah_hanya_spasi(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("   ") == "Perintah kosong. Ketik 'bantuan'."


def test_perintah_daftar_satu_hari(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("daftar 1")
    assert "Daftar harga sewa untuk 1 hari:" in hasil
    assert "Traktor Kubota: Rp250.000" in hasil


def test_perintah_daftar_tiga_hari(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("daftar 3")
    assert "Traktor Kubota: Rp750.000" in hasil


def test_perintah_harga_traktor(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("harga TR-01 3")
    assert hasil == "Traktor Kubota, 3 hari: Rp750.000"


def test_perintah_harga_pompa(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("harga PA-01 1")
    assert hasil == "Pompa Air Honda, 1 hari: Rp101.000"


def test_perintah_harga_kode_tidak_ada(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("harga XX-99 1")
    assert hasil == "Alat berkode XX-99 tidak ada dalam daftar."


def test_perintah_termurah(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("termurah 3")
    assert hasil == "Termurah untuk 3 hari: Perontok Padi"


def test_perintah_tidak_dikenal(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("ngawur")
    assert hasil == "Perintah 'ngawur' tidak dikenal. Ketik 'bantuan'."


@pytest.mark.parametrize(
    "perintah",
    [
        "daftar",
        "daftar abc",
        "harga TR-01",
        "harga TR-01 abc",
        "termurah abc",
        "hapus 1",
    ],
)
def test_perintah_dengan_format_salah(
    konsol: PerintahKonsol,
    perintah: str,
) -> None:
    hasil = konsol.jalankan(perintah)
    assert "tidak dikenal" in hasil


def test_perintah_daftar_tiga_argumen(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("daftar 1 2 3")
    assert hasil == "Perintah 'daftar' tidak dikenal. Ketik 'bantuan'."


def test_perintah_tidak_peduli_huruf_besar(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("BANTUAN")
    assert hasil == PerintahKonsol.BANTUAN


def test_perintah_harga_kode_huruf_kecil(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("harga tr-01 3")
    assert hasil == "Traktor Kubota, 3 hari: Rp750.000"
