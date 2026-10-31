"""Pengujian unit untuk kelas Petugas dan objek nilai terkait."""

import dataclasses
import pytest
from src.model.petugas import NomorPegawai, Petugas


def test_info_petugas_normal() -> None:
    nomor = NomorPegawai("P", "001")
    petugas = Petugas(nomor, "Helmy", "Admin Lapangan", True)
    assert petugas.info_petugas() == "[P-001] Helmy - Admin Lapangan (Aktif)"


def test_status_keaktifan() -> None:
    nomor = NomorPegawai("P", "002")
    petugas_aktif = Petugas(nomor, "Faisal", "Kasir", True)
    assert "aktif" in petugas_aktif.status_keaktifan()

def test_id_petugas_tidak_punya_setter() -> None:
    """Membuktikan atribut id_petugas bersifat baca-saja (read-only)."""
    nomor1 = NomorPegawai("P", "001")
    nomor2 = NomorPegawai("P", "999")
    petugas = Petugas(nomor1, "Helmy", "Admin")
    with pytest.raises(AttributeError):
        petugas.id_petugas = nomor2  # type: ignore[misc]


def test_jabatan_kosong_ditolak() -> None:
    """Membuktikan setter jabatan menolak string kosong."""
    nomor = NomorPegawai("P", "001")
    petugas = Petugas(nomor, "Helmy", "Admin")
    with pytest.raises(ValueError):
        petugas.jabatan = ""


def test_nomor_pegawai_tidak_sah_ditolak() -> None:
    """Membuktikan objek nilai NomorPegawai menolak format angka salah."""
    with pytest.raises(ValueError):
        NomorPegawai("P", "AB")  # Bukan digit


def test_nomor_pegawai_beku_tidak_dapat_diubah() -> None:
    """Membuktikan objek NomorPegawai bersifat beku (frozen=True)."""
    nomor = NomorPegawai("P", "001")
    with pytest.raises(dataclasses.FrozenInstanceError):
        nomor.nomor = "999"  # type: ignore[misc]