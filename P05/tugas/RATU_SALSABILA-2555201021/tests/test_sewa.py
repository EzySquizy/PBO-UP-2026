
"""Pengujian untuk kelas Sewa."""

import pytest

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa

def buat_penyewa() -> Penyewa:
    alamat = Alamat("Dusun Suka Maju", "Kumantan", "Bangkinang Kota")
    return Penyewa("1400000000000001", "Ratu Salsabila", alamat)

def test_sewa_menyimpan_nomor_dan_penyewa() -> None:
    orang = buat_penyewa()
    sewa = Sewa("SW-01", orang)

    assert sewa.nomor == "SW-01"
    assert sewa.penyewa is orang

def test_nomor_sewa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa("", buat_penyewa())

def test_baris_sewa_dibuat_di_dalam_sewa() -> None:
    sewa = Sewa("SW-01", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150000)

    sewa.tambah_alat(alat, 3)

    assert len(sewa.baris) == 1
    assert sewa.baris[0].alat is alat

def test_property_baris_mengembalikan_tuple() -> None:
    sewa = Sewa("SW-01", buat_penyewa())

    assert isinstance(sewa.baris, tuple)

def test_baris_tidak_bisa_diubah_dari_luar() -> None:
    sewa = Sewa("SW-01", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150000)

    sewa.tambah_alat(alat, 3)

    assert isinstance(sewa.baris, tuple)

    salinan = list(sewa.baris)
    salinan.append(sewa.baris[0])

    assert len(salinan) == 2
    assert len(sewa.baris) == 1

def test_total_sewa() -> None:
    sewa = Sewa("SW-01", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150000)

    sewa.tambah_alat(alat, 3)

    assert sewa.total() == 450000

def test_tarif_historis_dipakai_dalam_total() -> None:
    sewa = Sewa("SW-01", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150000)

    sewa.tambah_alat(alat, 3)
    alat.tarif_harian = 175000

    assert sewa.total() == 450000

def test_alat_yang_sama_tidak_boleh_ditambahkan_dua_kali() -> None:
    sewa = Sewa("SW-01", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150000)

    sewa.tambah_alat(alat, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 3)

def test_batas_maksimal_alat_dalam_sewa() -> None:
    sewa = Sewa("SW-01", buat_penyewa())

    for nomor in range(10):
        alat = AlatTani(f"TR-{nomor:02d}", f"Alat {nomor}", 150000)
        sewa.tambah_alat(alat, 1)

    alat_tambahan = AlatTani("TR-10", "Alat tambahan", 150000)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat_tambahan, 1)

def test_nota_memuat_identitas_dan_total() -> None:
    sewa = Sewa("SW-01", buat_penyewa())
    alat = AlatTani("TR-01", "Traktor", 150000)

    sewa.tambah_alat(alat, 3)
    nota = sewa.nota()

    assert "SW-01" in nota
    assert "Ratu Salsabila" in nota
    assert "Traktor" in nota
    assert "Rp450.000" in nota