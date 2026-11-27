import pytest

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


def buat_alat() -> AlatTani:
    return AlatTani(
        kode="TR-01",
        nama="Traktor Roda Dua",
        tarif_harian=150000,
    )


def test_baris_menyimpan_referensi_alat() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    assert baris.alat is alat


def test_snapshot_tarif_tidak_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 200000

    assert baris.tarif_saat_sewa == 150000
    assert baris.subtotal() == 450000


def test_snapshot_nama_tidak_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 2)

    assert baris.nama_alat == "Traktor Roda Dua"


def test_jumlah_hari_harus_positif() -> None:
    alat = buat_alat()

    with pytest.raises(ValueError):
        BarisSewa(alat, 0)