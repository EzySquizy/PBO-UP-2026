"""Pengujian model BarisSewa dan Sewa."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa("1406012509900001", "Budi Santoso", alamat)


def test_baris_sewa_menyimpan_tarif_saat_transaksi() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    baris = BarisSewa(alat, 2)

    alat.tarif_harian = 200_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 300_000


def test_baris_sewa_menolak_jumlah_hari_nol() -> None:
    alat = AlatTani("TR-02", "Traktor", 150_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, 0)


def test_baris_sewa_menolak_jumlah_hari_minus() -> None:
    alat = AlatTani("TR-03", "Traktor", 150_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, -1)


def test_sewa_menyimpan_penyewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-01", penyewa)

    assert sewa.penyewa is penyewa


def test_sewa_menolak_nomor_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())


def test_sewa_menambahkan_alat() -> None:
    sewa = Sewa("SW-02", buat_penyewa())
    alat = AlatTani("TR-04", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    assert len(sewa.baris) == 1


def test_sewa_menghitung_total() -> None:
    sewa = Sewa("SW-03", buat_penyewa())
    alat1 = AlatTani("TR-05", "Traktor", 150_000)
    alat2 = AlatTani("TR-06", "Pompa", 50_000)

    sewa.tambah_alat(alat1, 2)
    sewa.tambah_alat(alat2, 3)

    assert sewa.total() == 450_000


def test_sewa_menolak_alat_duplikat() -> None:
    sewa = Sewa("SW-04", buat_penyewa())
    alat = AlatTani("TR-07", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 3)


def test_baris_sewa_tidak_bisa_diubah_dari_luar() -> None:
    sewa = Sewa("SW-05", buat_penyewa())
    alat = AlatTani("TR-08", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)
    daftar = sewa.baris

    assert isinstance(daftar, tuple)
    assert len(daftar) == 1


def test_sewa_menolak_alat_ke_11() -> None:
    sewa = Sewa("SW-06", buat_penyewa())

    for nomor in range(10):
        alat = AlatTani(
            f"TR-{nomor + 10}",
            f"Alat {nomor}",
            100_000,
        )
        sewa.tambah_alat(alat, 1)

    alat_ke_11 = AlatTani("TR-99", "Alat tambahan", 100_000)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat_ke_11, 1)
