
"""Pengujian kelas Petugas dan PeriodeTugas."""

from dataclasses import FrozenInstanceError

import pytest
from src.model.alamat import Alamat
from src.model.periode_tugas import PeriodeTugas
from src.model.petugas import Petugas


def buat_petugas() -> Petugas:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    periode = PeriodeTugas("2026-01-01", "2026-12-31")
    return Petugas(
        "PTG001",
        "Budi",
        "Admin",
        alamat,
        periode,
        "081234567890",
    )


def test_petugas_dibuat_dengan_data_valid() -> None:
    petugas = buat_petugas()
    assert petugas.nama == "Budi"


def test_nip_petugas_bersifat_baca_saja() -> None:
    petugas = buat_petugas()
    with pytest.raises(AttributeError):
        petugas.nip = "PTG002"  # type: ignore[misc]


def test_nip_kosong_ditolak() -> None:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    periode = PeriodeTugas("2026-01-01", "2026-12-31")
    with pytest.raises(ValueError):
        Petugas("", "Budi", "Admin", alamat, periode)


def test_nama_kosong_ditolak() -> None:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    periode = PeriodeTugas("2026-01-01", "2026-12-31")
    with pytest.raises(ValueError):
        Petugas("PTG001", "   ", "Admin", alamat, periode)


def test_telepon_tidak_valid_ditolak() -> None:
    petugas = buat_petugas()
    with pytest.raises(ValueError):
        petugas.telepon = "123"


def test_telepon_valid_bisa_diubah() -> None:
    petugas = buat_petugas()
    petugas.telepon = "081298765432"
    assert petugas.telepon == "081298765432"


def test_periode_tugas_bersifat_tetap() -> None:
    periode = PeriodeTugas("2026-01-01", "2026-12-31")
    with pytest.raises(FrozenInstanceError):
        periode.tanggal_mulai = "2026-02-01"  # type: ignore[misc]


def test_format_tanggal_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas("tanggal-salah", "2026-12-31")


def test_tanggal_selesai_sebelum_mulai_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas("2026-12-31", "2026-01-01")
