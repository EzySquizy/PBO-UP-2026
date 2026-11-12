"""Pengujian untuk kelas Petugas."""

from dataclasses import FrozenInstanceError
from datetime import date

import pytest
from src.model.periode_tugas import PeriodeTugas
from src.model.petugas import Petugas


def buat_periode() -> PeriodeTugas:
    return PeriodeTugas(date(2026, 1, 1), date(2026, 12, 31))


def buat_petugas() -> Petugas:
    return Petugas(
        "PT-001",
        "Izaz",
        "Operator",
        "Kuok",
        buat_periode(),
        "081234567890",
    )


def test_identitas_petugas() -> None:
    petugas = buat_petugas()
    assert petugas.identitas() == "Izaz (PT-001) — Operator"


def test_informasi_tugas_petugas() -> None:
    petugas = buat_petugas()
    assert petugas.informasi_tugas() == "Izaz bertugas di Desa Kuok"


def test_dua_petugas_memiliki_data_sendiri() -> None:
    petugas_a = buat_petugas()
    petugas_b = Petugas(
        "PT-002", "Reyhan", "Admin", "Salo", buat_periode()
    )

    assert petugas_a.nip != petugas_b.nip
    assert petugas_a.nama != petugas_b.nama


def test_setter_telepon_menolak_nilai_tidak_valid() -> None:
    petugas = buat_petugas()
    telepon_lama = petugas.telepon

    with pytest.raises(ValueError):
        petugas.telepon = "123"

    assert petugas.telepon == telepon_lama


def test_setter_jabatan_menolak_nilai_kosong() -> None:
    petugas = buat_petugas()
    jabatan_lama = petugas.jabatan

    with pytest.raises(ValueError):
        petugas.jabatan = " "

    assert petugas.jabatan == jabatan_lama


def test_setter_desa_menolak_nilai_kosong() -> None:
    petugas = buat_petugas()
    desa_lama = petugas.desa_tugas

    with pytest.raises(ValueError):
        petugas.desa_tugas = ""

    assert petugas.desa_tugas == desa_lama


def test_nip_hanya_bisa_dibaca() -> None:
    petugas = buat_petugas()

    with pytest.raises(AttributeError):
        petugas.nip = "PT-999"  # type: ignore[misc]


def test_periode_tugas_bersifat_beku() -> None:
    periode = buat_periode()

    with pytest.raises(FrozenInstanceError):
        periode.mulai = date(2027, 1, 1)  # type: ignore[misc]


def test_periode_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(date(2026, 12, 31), date(2026, 1, 1))
