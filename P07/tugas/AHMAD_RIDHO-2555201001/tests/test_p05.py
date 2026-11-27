import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Dusun Satu", "Penyasawan", "Kampar")
    return Penyewa(
        "1400000000000001",
        "Budi Santoso",
        alamat,
    )


def test_salinan_tarif_tidak_ikut_berubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000


def test_jumlah_hari_nol_ditolak() -> None:
    alat = AlatTani("TR-02", "Pompa Air", 75_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    alat = AlatTani("TR-03", "Mesin Bajak", 100_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, -1)


def test_komposisi_tidak_dapat_diubah_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    alat = AlatTani("TR-04", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]

    assert len(sewa.baris) == 1


def test_penyewa_tetap_hidup_setelah_sewa_dihapus() -> None:
    budi = buat_penyewa()
    sewa = Sewa("SW-002", budi)

    del sewa

    assert budi.nama == "Budi Santoso"


def test_nomor_sewa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())


def test_alat_duplikat_ditolak() -> None:
    sewa = Sewa("SW-003", buat_penyewa())
    alat = AlatTani("TR-05", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 3)
