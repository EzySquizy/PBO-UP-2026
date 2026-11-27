"""Tes untuk model BarisSewa dan Sewa pada P05."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Pongkai", "Kuok", "Kuok")
    return Penyewa("1234567890123456", "Budi", alamat)


def buat_alat(kode: str = "TR-01") -> AlatTani:
    return AlatTani(kode, "Traktor", 150_000)


def buat_sewa() -> Sewa:
    return Sewa("SW-2026-001", buat_penyewa())


def test_subtotal_baris_sewa() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.subtotal() == 450_000


def test_jumlah_hari_tidak_valid() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_tarif_historis_tetap() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 200_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000


def test_referensi_alat_tersimpan() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 2)

    assert baris.alat is alat


def test_tambah_alat_ke_sewa() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    assert sewa.jumlah_alat() == 1


def test_total_sewa() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat("TR-01"), 3)
    sewa.tambah_alat(
        AlatTani("PM-01", "Pompa", 75_000), 5
    )

    assert sewa.total() == 825_000


def test_alat_duplikat_ditolak() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat("TR-01"), 3)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat("TR-01"), 2)


def test_maksimal_sepuluh_alat() -> None:
    sewa = buat_sewa()

    for nomor in range(10):
        sewa.tambah_alat(
            AlatTani(f"AL-{nomor}", "Alat", 50_000), 1
        )

    with pytest.raises(ValueError):
        sewa.tambah_alat(
            AlatTani("AL-10", "Alat", 50_000), 1
        )


def test_baris_sewa_berupa_tuple() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 2)

    assert isinstance(sewa.baris, tuple)


def test_baris_sewa_tidak_bisa_diubah_dari_luar() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 2)

    with pytest.raises(AttributeError):
        sewa.baris.append(BarisSewa(buat_alat("TR-02"), 1))  # type: ignore[attr-defined]


def test_penyewa_tetap_ada_setelah_sewa_dihapus() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-2026-001", penyewa)

    del sewa

    assert penyewa.nama == "Budi"


def test_nomor_sewa_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())


def test_nota_sewa() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    nota = sewa.nota()

    assert "NOTA SEWA SW-2026-001" in nota
    assert "Budi" in nota
    assert "Rp450.000" in nota
    assert "TOTAL" in nota
