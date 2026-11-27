
"""Pengujian fitur abstraksi, Protocol, dan Enum P09."""

import pytest

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.penyewa import Penyewa
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewa import Sewa
from src.model.sewaan import Sewaan
from src.model.status_sewa import StatusSewa
from src.model.traktor import Traktor


def test_alat_tani_tidak_dapat_dibuat_langsung() -> None:
    with pytest.raises(TypeError):
        AlatTani(  # type: ignore[abstract]
            "AT-01", "Alat Tani", 100_000
        )


def test_gerobak_dorong_memenuhi_protocol_sewaan() -> None:
    gerobak = GerobakDorong(
        "GD-01", "Gerobak Dorong", 50_000
    )

    assert isinstance(gerobak, Sewaan)
    assert not isinstance(gerobak, AlatTani)


def test_daftar_harga_menerima_gerobak_dorong() -> None:
    gerobak = GerobakDorong(
        "GD-01", "Gerobak Dorong", 50_000
    )
    daftar = DaftarHarga([gerobak])

    assert daftar.biaya_semua(2) == [
        ("Gerobak Dorong", 100_000)
    ]
    assert daftar.termurah(2) is gerobak
    assert daftar.total_bila_semua_disewa(2) == 100_000


def test_rumus_baku_biaya_sewa_tetap_sama() -> None:
    traktor = Traktor("TR-01", "Traktor", 150_000, 8)
    pompa = PompaAir("PA-01", "Pompa", 75_000, 600)
    perontok = Perontok("PR-01", "Perontok", 200_000, 900)

    assert traktor.biaya_sewa(1) == 250_000
    assert traktor.biaya_sewa(3) == 750_000
    assert pompa.biaya_sewa(1) == 201_000
    assert pompa.biaya_sewa(3) == 603_000
    assert perontok.biaya_sewa(1) == 400_000
    assert perontok.biaya_sewa(3) == 600_000


def test_status_sewa_boleh_diubah() -> None:
    assert StatusSewa.DIPESAN.boleh_diubah()
    assert StatusSewa.BERJALAN.boleh_diubah()
    assert not StatusSewa.SELESAI.boleh_diubah()
    assert not StatusSewa.BATAL.boleh_diubah()


def test_sewa_menolak_penambahan_alat_setelah_selesai() -> None:
    penyewa = Penyewa(
        "1234567890123456",
        "Budi",
        Alamat("Dusun 1", "Ridan Permai", "Bangkinang"),
    )
    transaksi = Sewa("SW-01", penyewa)
    alat = Traktor("TR-01", "Traktor", 150_000, 8)

    transaksi.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(ValueError):
        transaksi.tambah_alat(alat, 2)
