"""Pengujian untuk kelas Petugas dan PeriodeTugas."""

import dataclasses

import pytest
from src.model.petugas import PeriodeTugas, Petugas


def test_petugas_identitas() -> None:
    periode = PeriodeTugas(2025, 2026)
    petugas = Petugas("PT-01", "Ahmad", "Ketua", periode, "081234567890")
    assert petugas.identitas() == "Ahmad (PT-01) — Ketua (2025-2026)"


def test_petugas_kontak() -> None:
    periode = PeriodeTugas(2025, 2026)
    petugas = Petugas("PT-02", "Budi", "Operator", periode, "0812-1111-2222")
    assert petugas.kontak() == "Budi dapat dihubungi di 0812-1111-2222"


def test_id_petugas_tidak_punya_setter() -> None:
    periode = PeriodeTugas(2025, 2026)
    petugas = Petugas("PT-01", "Ahmad", "Ketua", periode)
    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-99"  # type: ignore[misc]


def test_telepon_tidak_valid_ditolak() -> None:
    periode = PeriodeTugas(2025, 2026)
    petugas = Petugas("PT-01", "Ahmad", "Ketua", periode)
    with pytest.raises(ValueError):
        petugas.telepon = "123"


def test_periode_tugas_tidak_dapat_diubah() -> None:
    p = PeriodeTugas(2025, 2026)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.mulai = 2024  # type: ignore[misc]


def test_periode_tugas_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(2026, 2025)
