
"""Pengujian daftar harga alat pertanian."""

import pytest

from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def buat_daftar() -> DaftarHarga:
    """Membuat daftar alat dengan jenis yang berbeda."""
    alat = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 600),
        Perontok("PR-01", "Mesin Perontok", 125_000, 2),
    ]
    return DaftarHarga(alat)


def test_daftar_harga_menyalin_daftar() -> None:
    alat = [Traktor("TR-01", "Traktor Kubota", 150_000, 8)]
    daftar = DaftarHarga(alat)

    alat.append(Traktor("TR-02", "Traktor Tambahan", 200_000, 8))

    assert daftar.jumlah_alat == 1


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_jumlah_alat_menghitung_semua_alat() -> None:
    daftar = buat_daftar()

    assert daftar.jumlah_alat == 3


def test_biaya_semua_menggunakan_polimorfisme() -> None:
    daftar = buat_daftar()

    hasil = daftar.biaya_semua(2)

    assert len(hasil) == 3
    assert all(isinstance(nama, str) for nama, _ in hasil)
    assert all(isinstance(biaya, int) for _, biaya in hasil)


def test_termurah_mengembalikan_objek_alat() -> None:
    daftar = buat_daftar()

    alat = daftar.termurah(1)

    assert alat.kode == "PA-01"
    assert alat.nama == "Pompa Air"
    assert alat.biaya_sewa(1) == 201_000


def test_total_bila_semua_disewa() -> None:
    daftar = buat_daftar()

    hasil = daftar.total_bila_semua_disewa(1)

    assert hasil == sum(biaya for _, biaya in daftar.biaya_semua(1))


def test_tabel_menampilkan_semua_nama_alat() -> None:
    daftar = buat_daftar()

    hasil = daftar.tabel(1)

    assert "Traktor Kubota" in hasil
    assert "Pompa Air" in hasil
    assert "Mesin Perontok" in hasil


def test_biaya_semua_menolak_jumlah_hari_nol() -> None:
    daftar = buat_daftar()

    with pytest.raises(ValueError):
        daftar.biaya_semua(0)


def test_termurah_menolak_jumlah_hari_negatif() -> None:
    daftar = buat_daftar()

    with pytest.raises(ValueError):
        daftar.termurah(-1)
class GerobakDorong:
    """Objek sewaan yang tidak mewarisi AlatTani."""

    @property
    def kode(self) -> str:
        return "GD-01"

    @property
    def nama(self) -> str:
        return "Gerobak Dorong"

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return 25_000 * jumlah_hari


def test_protocol_menerima_objek_tanpa_pewarisan() -> None:
    gerobak = GerobakDorong()
    daftar = DaftarHarga([gerobak])

    assert daftar.jumlah_alat == 1
    assert daftar.biaya_berdasarkan_kode("GD-01", 2) == (
        "Gerobak Dorong",
        50_000,
    )
    assert daftar.termurah(2) is gerobak
