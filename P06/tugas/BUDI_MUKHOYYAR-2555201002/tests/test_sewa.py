import pytest
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.baris_sewa import BarisSewa
from src.model.alat_tani import AlatTani

def buat_penyewa() -> Penyewa:
    from src.model.penyewa import Penyewa
    from src.model.alamat import Alamat
    alamat_budi = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa("1406012509900001", "Budi Santoso", alamat_budi)

def test_salinan_tidak_ikut_berubah_saat_tarif_alat_naik() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)
    alat.tarif_harian = 175_000
    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000

def test_komposisi_tidak_dapat_dibongkar_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 3)
    with pytest.raises(AttributeError):
        sewa.baris.append(None) # type: ignore[attr-defined]
    assert sewa.jumlah_alat() == 1

def test_penyewa_tetap_hidup_setelah_sewa_dihapus() -> None:
    budi = buat_penyewa()
    sewa = Sewa("SW-001", budi)
    del sewa
    assert budi._nama == "Budi Santoso"

def test_nomor_sewa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa("", buat_penyewa())


def test_alat_yang_sama_tidak_boleh_ditambahkan_dua_kali() -> None:
    sewa = Sewa("SW-002", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 2)

    assert len(sewa.baris) == 1


def test_jumlah_hari_nol_ditolak() -> None:
    sewa = Sewa("SW-003", buat_penyewa())
    alat = AlatTani("TR-02", "Pompa Air", 75_000)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 0)

    assert len(sewa.baris) == 0
