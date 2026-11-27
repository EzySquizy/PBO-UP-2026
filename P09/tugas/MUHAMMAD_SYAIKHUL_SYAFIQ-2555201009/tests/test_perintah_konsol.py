"""Pengujian penerjemah perintah konsol."""

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


def buat_konsol() -> PerintahKonsol:
    """Membuat konsol dengan beberapa jenis alat."""
    alat = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 600),
        Perontok("PR-01", "Mesin Perontok", 125_000, 2),
    ]
    return PerintahKonsol(DaftarHarga(alat))


def test_perintah_kosong() -> None:
    konsol = buat_konsol()
    assert konsol.jalankan("") == "Perintah kosong. Ketik 'bantuan'."


def test_perintah_bantuan() -> None:
    konsol = buat_konsol()
    assert konsol.jalankan("bantuan") == PerintahKonsol.BANTUAN


def test_perintah_tanda_tanya() -> None:
    konsol = buat_konsol()
    assert konsol.jalankan("?") == PerintahKonsol.BANTUAN


def test_perintah_daftar() -> None:
    konsol = buat_konsol()
    hasil = konsol.jalankan("daftar 1")
    assert "Traktor Kubota" in hasil
    assert "Pompa Air" in hasil
    assert "Mesin Perontok" in hasil


def test_perintah_harga_alat() -> None:
    konsol = buat_konsol()
    daftar = DaftarHarga([
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
    ])
    biaya = daftar.biaya_berdasarkan_kode("TR-01", 3)[1]
    hasil = konsol.jalankan("harga TR-01 3")
    assert hasil == (
        f"Traktor Kubota, 3 hari: {AlatTani.format_rupiah(biaya)}"
    )


def test_perintah_harga_kode_tidak_ditemukan() -> None:
    konsol = buat_konsol()
    assert (
        konsol.jalankan("harga XX-99 1")
        == "Alat berkode XX-99 tidak ada dalam daftar."
    )


def test_perintah_termurah() -> None:
    konsol = buat_konsol()
    hasil = konsol.jalankan("termurah 3")
    assert hasil.startswith("Termurah untuk 3 hari: ")


def test_perintah_tidak_dikenal() -> None:
    konsol = buat_konsol()
    assert (
        konsol.jalankan("ngawur")
        == "Perintah 'ngawur' tidak dikenal. Ketik 'bantuan'."
    )


def test_perintah_daftar_dengan_argumen_berlebih() -> None:
    konsol = buat_konsol()
    assert (
        konsol.jalankan("daftar 1 2 3")
        == "Perintah 'daftar' tidak dikenal. Ketik 'bantuan'."
    )


def test_perintah_harga_tanpa_jumlah_hari() -> None:
    konsol = buat_konsol()
    assert (
        konsol.jalankan("harga TR-01")
        == "Perintah 'harga' tidak dikenal. Ketik 'bantuan'."
    )


def test_perintah_hari_bukan_angka() -> None:
    konsol = buat_konsol()
    assert (
        konsol.jalankan("daftar besok")
        == "Perintah 'daftar' tidak dikenal. Ketik 'bantuan'."
    )