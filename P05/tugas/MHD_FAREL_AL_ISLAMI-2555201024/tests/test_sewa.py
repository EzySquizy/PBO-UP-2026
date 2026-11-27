"""Pengujian untuk kelas Sewa."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


@pytest.fixture
def penyewa() -> Penyewa:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa("1406012509900001", "Budi Santoso", alamat, "0812-3456-7890")


def test_sewa_menyimpan_nomor_dan_penyewa(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)

    assert sewa.nomor == "SW-001"
    assert sewa.penyewa is penyewa


def test_nomor_kosong_ditolak(penyewa: Penyewa) -> None:
    with pytest.raises(ValueError):
        Sewa(" ", penyewa)


def test_tambah_alat_membuat_baris_sewa(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)
    alat = AlatTani("TR-01", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert len(sewa.baris) == 1
    assert sewa.baris[0].alat is alat


def test_baris_tidak_dapat_diubah_langsung(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)

    assert isinstance(sewa.baris, tuple)


def test_total_beberapa_alat(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 3)
    sewa.tambah_alat(AlatTani("PA-01", "Pompa Air", 75_000), 5)

    assert sewa.total() == 825_000


def test_alat_duplikat_ditolak(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 3)

    with pytest.raises(ValueError):
        sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 2)


def test_batas_maksimal_sepuluh_alat(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)

    for nomor in range(10):
        sewa.tambah_alat(
            AlatTani(f"TR-{nomor:02}", f"Traktor {nomor}", 150_000),
            1,
        )

    with pytest.raises(ValueError):
        sewa.tambah_alat(AlatTani("TR-10", "Traktor 10", 150_000), 1)


def test_nota_memuat_identitas_dan_total(penyewa: Penyewa) -> None:
    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 3)

    nota = sewa.nota()

    assert "NOTA SEWA SW-001" in nota
    assert "Budi Santoso" in nota
    assert "Traktor" in nota
    assert "450.000" in nota
