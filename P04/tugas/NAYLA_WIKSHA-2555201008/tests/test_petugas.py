
import pytest
from src.model.petugas import PeriodeTugas, Petugas


def buat_periode() -> PeriodeTugas:
    return PeriodeTugas("2026-01-01", "2026-12-31")


def buat_petugas() -> Petugas:
    return Petugas(
        "PTG001",
        "Budi Santoso",
        "Pengurus UPJA",
        "081234567890",
        buat_periode(),
    )


def test_nip_petugas() -> None:
    assert buat_petugas().nip == "PTG001"


def test_nama_petugas() -> None:
    assert buat_petugas().nama == "Budi Santoso"


def test_jabatan_petugas() -> None:
    assert buat_petugas().jabatan == "Pengurus UPJA"


def test_telepon_bisa_diubah() -> None:
    petugas = buat_petugas()
    petugas.telepon = "081111111111"
    assert petugas.telepon == "081111111111"


def test_periode_petugas() -> None:
    assert buat_petugas().periode.tanggal_mulai == "2026-01-01"


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Budi", "Pengurus UPJA", "081234567890", buat_periode())


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PTG001", " ", "Pengurus UPJA", "081234567890", buat_periode())


def test_jabatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PTG001", "Budi", " ", "081234567890", buat_periode())


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        buat_petugas().telepon = "abc"


def test_nip_hanya_bisa_dibaca() -> None:
    with pytest.raises(AttributeError):
        buat_petugas().nip = "PTG002"  # type: ignore[misc]


def test_periode_tidak_bisa_diubah() -> None:
    with pytest.raises(AttributeError):
        buat_periode().tanggal_mulai = "2026-02-01"  # type: ignore[misc]


def test_tanggal_mulai_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(" ", "2026-12-31")


def test_tanggal_selesai_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas("2026-01-01", " ")
