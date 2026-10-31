
"""Pengujian untuk model Petugas dan PeriodeTugas."""

from datetime import date
from dataclasses import FrozenInstanceError

import pytest

from src.model.petugas import Petugas
from src.model.periode_tugas import PeriodeTugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Budi", "Admin", "08123456789")
    assert petugas.identitas() == "Budi (PT-01) - Admin"


def test_kontak_petugas_tanpa_nomor() -> None:
    petugas = Petugas("PT-02", "Siti", "Operator")
    assert petugas.kontak() == "Siti belum mencantumkan nomor telepon"


def test_telepon_dapat_diubah_jika_valid() -> None:
    petugas = Petugas("PT-03", "Andi", "Admin")
    petugas.telepon = "08123456789"
    assert petugas.telepon == "08123456789"


def test_id_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Budi", "Admin")


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "   ", "Admin")


def test_jabatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Budi", "")


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Budi", "Admin", "123")


def test_telepon_lama_tetap_tersimpan_jika_gagal() -> None:
    petugas = Petugas("PT-01", "Budi", "Admin", "08123456789")
    with pytest.raises(ValueError):
        petugas.telepon = "abc"
    assert petugas.telepon == "08123456789"


def test_id_petugas_baca_saja() -> None:
    petugas = Petugas("PT-01", "Budi", "Admin")
    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-02"  # type: ignore[misc]


def test_periode_tugas_valid() -> None:
    periode = PeriodeTugas(date(2026, 10, 1), date(2026, 10, 7))
    assert periode.mulai == date(2026, 10, 1)
    assert periode.selesai == date(2026, 10, 7)


def test_tanggal_periode_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(date(2026, 10, 7), date(2026, 10, 1))


def test_periode_tugas_tidak_bisa_diubah() -> None:
    periode = PeriodeTugas(date(2026, 10, 1), date(2026, 10, 7))
    with pytest.raises(FrozenInstanceError):
        periode.mulai = date(2026, 10, 2)  # type: ignore[misc]
