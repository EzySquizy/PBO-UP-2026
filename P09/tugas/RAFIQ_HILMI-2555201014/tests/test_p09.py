"""Pengujian khusus untuk penugasan terstruktur P09."""

from typing import Any, cast

import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.sewa import Sewa
from src.model.sewaan import Sewaan
from src.model.status_sewa import StatusSewa


def test_kelas_abstrak_alat_tani_tidak_dapat_dibuat() -> None:
    kelas_alat = cast(Any, AlatTani)

    with pytest.raises(TypeError):
        kelas_alat("AT-01", "Alat Tani", 50_000)


def test_gerobak_dorong_memenuhi_protocol_sewaan() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)
    assert isinstance(gerobak, Sewaan)


def test_gerobak_dorong_bukan_turunan_alat_tani() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)
    assert not isinstance(gerobak, AlatTani)


def test_daftar_harga_menerima_gerobak_tanpa_pewarisan() -> None:
    alat: list[Sewaan] = [
        GerobakDorong("GD-01", "Gerobak Dorong", 50_000)
    ]
    daftar = DaftarHarga(alat)
    assert daftar.biaya_semua(2) == [("Gerobak Dorong", 100_000)]


def test_enum_menolak_status_yang_tidak_dikenal() -> None:
    with pytest.raises(ValueError):
        StatusSewa("tidak_dikenal")


def test_status_sewa_menentukan_boleh_diubah() -> None:
    assert StatusSewa.DIPESAN.boleh_diubah() is True
    assert StatusSewa.BERJALAN.boleh_diubah() is True
    assert StatusSewa.SELESAI.boleh_diubah() is False
    assert StatusSewa.BATAL.boleh_diubah() is False


def test_sewa_selesai_tidak_dapat_ditambah_alat() -> None:
    sewa = Sewa("SW-01")
    sewa.ubah_status(StatusSewa.SELESAI)
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)

    with pytest.raises(ValueError):
        sewa.tambah_alat(gerobak)
