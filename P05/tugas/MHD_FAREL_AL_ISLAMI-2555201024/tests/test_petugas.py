
"""Pengujian untuk kelas Petugas."""

import dataclasses

import pytest
from src.model.petugas import PeriodeTugas, Petugas


def test_info_petugas() -> None:
    periode = PeriodeTugas(2024, 2026)
    petugas = Petugas("P-01", "Farel", "Administrator", periode, True)
    assert "Farel" in petugas.info_petugas()
    assert "Administrator" in petugas.info_petugas()


def test_dua_objek_petugas_punya_data_sendiri() -> None:
    p1 = Petugas("P-01", "Farel", "Admin", PeriodeTugas(2024, 2026))
    p2 = Petugas("P-02", "Islami", "Kasir", PeriodeTugas(2025, 2027))
    assert p1.info_petugas() != p2.info_petugas()


def test_id_petugas_tidak_punya_setter() -> None:
    petugas = Petugas("P-01", "Farel", "Admin", PeriodeTugas(2024, 2026))
    with pytest.raises(AttributeError):
        petugas.id_petugas = "P-99"  # type: ignore


def test_id_petugas_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Farel", "Admin", PeriodeTugas(2024, 2026))


def test_jabatan_kosong_ditolak_lewat_setter() -> None:
    petugas = Petugas("P-01", "Farel", "Admin", PeriodeTugas(2024, 2026))
    with pytest.raises(ValueError):
        petugas.jabatan = ""
    assert petugas.jabatan == "Admin"


def test_konstruktor_menolak_jabatan_kosong() -> None:
    """Menguji bahwa konstruktor menolak jabatan kosong melalui setter."""
    with pytest.raises(ValueError):
        Petugas("P-01", "Farel", "", PeriodeTugas(2024, 2026))


def test_konstruktor_menolak_status_aktif_tidak_valid() -> None:
    """Menguji bahwa konstruktor menolak tipe data status aktif yang bukan boolean."""
    with pytest.raises(TypeError):
        Petugas(
            "P-01",
            "Farel",
            "Admin",
            PeriodeTugas(2024, 2026),
            status_aktif="aktif",  # type: ignore
        )


def test_periode_tugas_tidak_dapat_diubah() -> None:
    periode = PeriodeTugas(2024, 2026)
    with pytest.raises(dataclasses.FrozenInstanceError):
        periode.mulai = 2025  # type: ignore


def test_periode_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(2026, 2024)
