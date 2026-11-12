"""Pengujian untuk class Sewa."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    return Penyewa("1234567890123456", "Budi", alamat)


def buat_alat(kode: str = "TR-01") -> AlatTani:
    return AlatTani(kode, "Traktor", 150_000)


def buat_sewa() -> Sewa:
    return Sewa("SW-001", buat_penyewa())


def test_nomor_sewa_tersimpan() -> None:
    assert buat_sewa().nomor == "SW-001"


def test_penyewa_tersimpan() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)
    assert sewa.penyewa is penyewa


def test_nomor_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa(" ", buat_penyewa())


def test_sewa_awalnya_tidak_memiliki_alat() -> None:
    assert buat_sewa().jumlah_alat() == 0


def test_tambah_satu_alat() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)
    assert sewa.jumlah_alat() == 1


def test_tambah_alat_menghitung_total() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)
    assert sewa.total() == 450_000


def test_dua_alat_menghitung_total() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat("TR-01"), 3)
    sewa.tambah_alat(buat_alat("TR-02"), 2)
    assert sewa.total() == 750_000


def test_alat_duplikat_ditolak() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat(), 2)


def test_maksimal_sepuluh_alat() -> None:
    sewa = buat_sewa()

    for nomor in range(10):
        sewa.tambah_alat(buat_alat(f"TR-{nomor}"), 1)

    assert sewa.jumlah_alat() == 10


def test_alat_ke_sebelas_ditolak() -> None:
    sewa = buat_sewa()

    for nomor in range(10):
        sewa.tambah_alat(buat_alat(f"TR-{nomor}"), 1)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat("TR-11"), 1)


def test_property_baris_mengembalikan_tuple() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    assert isinstance(sewa.baris, tuple)


def test_baris_tidak_bisa_diubah_dari_luar() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    baris = sewa.baris

    with pytest.raises(AttributeError):
        baris.append("data palsu")  # type: ignore[attr-defined]

    assert sewa.jumlah_alat() == 1


def test_penyewa_tetap_ada_setelah_sewa_dihapus() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)

    del sewa

    assert penyewa.identitas() == "Budi (1234567890123456) — Kuok, Kuok"


def test_nota_menampilkan_nomor_sewa() -> None:
    assert "SW-001" in buat_sewa().nota()


def test_nota_menampilkan_total() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    assert "Rp450.000" in sewa.nota()
