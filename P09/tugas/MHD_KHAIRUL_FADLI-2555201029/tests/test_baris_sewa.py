
"""Pengujian untuk kelas BarisSewa."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


class AlatUji(AlatTani):
    """Alat konkret khusus untuk pengujian BarisSewa."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Menghitung biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat pemakaian."""
        return "Untuk pengujian."


def buat_alat() -> AlatUji:
    """Membuat alat konkret untuk pengujian."""
    return AlatUji("AT001", "Traktor", 150_000)


def test_baris_sewa_menyimpan_objek_alat() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    assert baris.alat is alat


def test_baris_sewa_menyimpan_jumlah_hari() -> None:
    baris = BarisSewa(buat_alat(), 3)

    assert baris.jumlah_hari == 3


def test_baris_sewa_menyimpan_kode_alat() -> None:
    baris = BarisSewa(buat_alat(), 3)

    assert baris.kode_alat == "AT001"


def test_baris_sewa_menyimpan_nama_alat() -> None:
    baris = BarisSewa(buat_alat(), 3)

    assert baris.nama_alat == "Traktor"


def test_baris_sewa_menyimpan_tarif_saat_sewa() -> None:
    baris = BarisSewa(buat_alat(), 3)

    assert baris.tarif_saat_sewa == 150_000


def test_subtotal_dihitung_dari_tarif_dan_hari() -> None:
    baris = BarisSewa(buat_alat(), 3)

    assert baris.subtotal() == 450_000


def test_jumlah_hari_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), -2)


def test_subtotal_tidak_berubah_setelah_tarif_alat_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.subtotal() == 450_000
    assert baris.tarif_saat_sewa == 150_000

