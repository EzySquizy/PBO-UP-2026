import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_alat(kode: str = "TR-01") -> AlatTani:
    return AlatTani(kode, "Traktor", 150_000)


def buat_penyewa() -> Penyewa:
    alamat = Alamat(
        dusun="Kampung Baru",
        desa="Penyasawan",
        kecamatan="Kampar",
    )
    return Penyewa(
        nik="1234567890123456",
        nama="Budi Santoso",
        alamat=alamat,
        telepon="081234567890",
    )


def buat_sewa() -> Sewa:
    return Sewa("SW-001", buat_penyewa())


def test_baris_sewa_menghitung_subtotal() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.subtotal() == 450_000


def test_baris_sewa_menolak_jumlah_hari_nol() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_baris_sewa_menolak_jumlah_hari_negatif() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), -1)


def test_baris_sewa_menyimpan_snapshot_tarif() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000


def test_baris_sewa_menyimpan_kode_alat() -> None:
    baris = BarisSewa(buat_alat("TR-02"), 2)
    assert baris.kode_alat == "TR-02"


def test_baris_sewa_menyimpan_jumlah_hari() -> None:
    baris = BarisSewa(buat_alat(), 5)
    assert baris.jumlah_hari == 5


def test_baris_sewa_menghasilkan_nota() -> None:
    baris = BarisSewa(buat_alat(), 2)
    assert "TR-01" in baris.baris_nota()
    assert "Rp150.000" in baris.baris_nota()
    assert "Rp300.000" in baris.baris_nota()


def test_sewa_menolak_nomor_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("", buat_penyewa())


def test_sewa_menolak_nomor_berisi_spasi() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())


def test_sewa_menambahkan_alat() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    assert len(sewa.baris) == 1


def test_sewa_menolak_alat_duplikat() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat(), 3)


def test_sewa_menolak_lebih_dari_sepuluh_alat() -> None:
    sewa = buat_sewa()

    for nomor in range(10):
        alat = buat_alat(f"TR-{nomor:02d}")
        sewa.tambah_alat(alat, 1)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat("TR-10"), 1)


def test_sewa_baris_berupa_tuple() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 2)

    assert isinstance(sewa.baris, tuple)


def test_sewa_menghitung_total() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat("TR-01"), 3)
    sewa.tambah_alat(
        AlatTani("TR-02", "Cultivator", 200_000),
        3,
    )

    assert sewa.total() == 1_050_000


def test_sewa_menghasilkan_nota() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_alat(), 3)

    nota = sewa.nota()

    assert "NOTA SEWA SW-001" in nota
    assert "Budi Santoso" in nota
    assert "TR-01" in nota
    assert "TOTAL: Rp450.000" in nota
