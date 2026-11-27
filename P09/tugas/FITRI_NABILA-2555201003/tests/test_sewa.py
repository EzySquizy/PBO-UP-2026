
"""Pengujian untuk kelas Sewa."""

import pytest
from src.model.alamat import Alamat
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.status_sewa import StatusSewa
from src.model.traktor import Traktor


def buat_penyewa() -> Penyewa:
    alamat_budi = Alamat("Salo Timur", "Salo", "Salo")
    return Penyewa("1406012509900001", "Budi Santoso", alamat_budi)


def test_salinan_tidak_ikut_berubah_saat_tarif_alat_naik() -> None:
    alat = Traktor("TR-01", "Traktor", 150_000, 8)
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 175_000

    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000


def test_komposisi_tidak_dapat_dibongkar_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(Traktor("TR-01", "Traktor", 150_000, 8), 3)

    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]

    assert sewa.jumlah_alat() == 1


def test_penyewa_tetap_hidup_setelah_sewa_dihapus() -> None:
    budi = buat_penyewa()
    sewa = Sewa("SW-001", budi)

    del sewa

    assert budi._nama == "Budi Santoso"


def test_status_awal_sewa_adalah_dipesan() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    assert sewa.status == StatusSewa.DIPESAN


@pytest.mark.parametrize(
    "status",
    [StatusSewa.SELESAI, StatusSewa.BATAL],
)
def test_sewa_selesai_atau_batal_menolak_penambahan_alat(
    status: StatusSewa,
) -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.ubah_status(status)

    with pytest.raises(ValueError):
        sewa.tambah_alat(
            Traktor("TR-01", "Traktor", 150_000, 8),
            3,
        )

    assert sewa.jumlah_alat() == 0
