
"""Pengujian untuk kelas Sewa."""

import pytest

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa("1406012509900001", "Budi Santoso", alamat)


def test_sewa_menyimpan_nomor_transaksi() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert sewa.nomor == "SW001"


def test_sewa_menyimpan_objek_penyewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW001", penyewa)

    assert sewa.penyewa is penyewa


def test_nomor_sewa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa(" ", buat_penyewa())


def test_baris_awalnya_kosong() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert sewa.baris == ()


def test_tambah_alat_membuat_baris_sewa() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert len(sewa.baris) == 1
    assert isinstance(sewa.baris[0], BarisSewa)


def test_tambah_alat_menyimpan_objek_yang_benar() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert sewa.baris[0].alat is alat


def test_tambah_alat_menyimpan_jumlah_hari() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 4)

    assert sewa.baris[0].jumlah_hari == 4


def test_total_satu_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert sewa.total() == 450_000


def test_total_beberapa_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    traktor = AlatTani("AT001", "Traktor", 150_000)
    pompa = AlatTani("AT002", "Pompa", 50_000)

    sewa.tambah_alat(traktor, 2)
    sewa.tambah_alat(pompa, 3)

    assert sewa.total() == 450_000


def test_alat_dengan_kode_sama_ditolak() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat1 = AlatTani("AT001", "Traktor", 150_000)
    alat2 = AlatTani("AT001", "Traktor Baru", 175_000)

    sewa.tambah_alat(alat1, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat2, 2)


def test_maksimal_sepuluh_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    for nomor in range(10):
        alat = AlatTani(
            f"AT{nomor:03}",
            f"Alat {nomor}",
            100_000,
        )
        sewa.tambah_alat(alat, 1)

    assert len(sewa.baris) == 10


def test_alat_ke_sebelas_ditolak() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    for nomor in range(10):
        alat = AlatTani(
            f"AT{nomor:03}",
            f"Alat {nomor}",
            100_000,
        )
        sewa.tambah_alat(alat, 1)

    alat_baru = AlatTani("AT010", "Alat Baru", 100_000)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat_baru, 1)


def test_baris_berupa_tuple() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert isinstance(sewa.baris, tuple)


def test_baris_tidak_bisa_diubah_dari_luar() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]


def test_penyewa_tetap_ada_setelah_referensi_sewa_dihapus() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW001", penyewa)

    del sewa

    assert penyewa.nik == "1406012509900001"


def test_nota_memuat_nomor_transaksi() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert "SW001" in sewa.nota()


def test_nota_memuat_identitas_penyewa() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert "Budi Santoso" in sewa.nota()


def test_nota_memuat_nama_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    assert "Traktor" in sewa.nota()


def test_nota_memuat_total_pembayaran() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    assert "Rp300.000" in sewa.nota()


def test_total_tidak_berubah_setelah_tarif_alat_diubah() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatTani("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)
    alat.tarif_harian = 175_000

    assert sewa.total() == 450_000
