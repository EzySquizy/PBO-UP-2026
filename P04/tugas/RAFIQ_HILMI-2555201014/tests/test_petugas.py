
"""Pengujian untuk kelas Petugas."""

from dataclasses import FrozenInstanceError

import pytest
from src.model.nomor_pegawai import NomorPegawai
from src.model.petugas import Petugas


def test_petugas_menyimpan_data() -> None:
    petugas = Petugas(
        "PT-01",
        "Rudi Hartono",
        "Admin",
        "0812-1111-2222",
    )

    assert petugas.id_petugas == "PT-01"
    assert petugas.nama == "Rudi Hartono"
    assert petugas.jabatan == "Admin"
    assert petugas.telepon == "0812-1111-2222"


def test_petugas_identitas() -> None:
    petugas = Petugas("PT-01", "Rudi Hartono", "Admin")

    assert petugas.identitas() == "Rudi Hartono (PT-01) — Admin"


def test_dua_petugas_punya_data_sendiri() -> None:
    a = Petugas("PT-01", "Rudi Hartono", "Admin")
    b = Petugas("PT-02", "Sari Aminah", "Kasir")

    assert a.identitas() != b.identitas()


def test_id_petugas_tidak_bisa_diubah() -> None:
    petugas = Petugas("PT-01", "Rudi Hartono", "Admin")

    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-02"  # type: ignore[misc]


def test_nama_tidak_bisa_diubah() -> None:
    petugas = Petugas("PT-01", "Rudi Hartono", "Admin")

    with pytest.raises(AttributeError):
        petugas.nama = "Nama Baru"  # type: ignore[misc]


def test_nomor_pegawai_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        NomorPegawai("")


def test_nomor_pegawai_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        NomorPegawai("   ")


def test_nomor_pegawai_tidak_bisa_diubah() -> None:
    nomor = NomorPegawai("PT-01")

    with pytest.raises(FrozenInstanceError):
        nomor.nilai = "PT-02"  # type: ignore[misc]


def test_telepon_tidak_valid_ditolak() -> None:
    petugas = Petugas("PT-01", "Rudi Hartono", "Admin")

    with pytest.raises(ValueError):
        petugas.telepon = "12345"


def test_telepon_huruf_ditolak() -> None:
    petugas = Petugas("PT-01", "Rudi Hartono", "Admin")

    with pytest.raises(ValueError):
        petugas.telepon = "abcdefghijk"


def test_telepon_valid_bisa_diperbarui() -> None:
    petugas = Petugas("PT-01", "Rudi Hartono", "Admin")
    petugas.telepon = "0812-3333-4444"

    assert petugas.telepon == "0812-3333-4444"
