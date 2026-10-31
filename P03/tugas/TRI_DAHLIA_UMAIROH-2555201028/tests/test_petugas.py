import pytest

from src.model.petugas import IdentitasPetugas, Petugas


def test_petugas_menyimpan_kode() -> None:
    petugas = Petugas("PT-01", "Dahlia", IdentitasPetugas("dahlia@example.com"))
    assert petugas.kode == "PT-01"


def test_petugas_menyimpan_nama() -> None:
    petugas = Petugas("PT-01", "Dahlia", IdentitasPetugas("dahlia@example.com"))
    assert petugas.nama == "Dahlia"


def test_petugas_status_awal_aktif() -> None:
    petugas = Petugas("PT-01", "Dahlia", IdentitasPetugas("dahlia@example.com"))
    assert petugas.status == "Aktif"


def test_petugas_status_bisa_diubah() -> None:
    petugas = Petugas("PT-01", "Dahlia", IdentitasPetugas("dahlia@example.com"))
    petugas.status = "Nonaktif"
    assert petugas.status == "Nonaktif"


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Dahlia", IdentitasPetugas("dahlia@example.com"))


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "", IdentitasPetugas("dahlia@example.com"))


def test_status_tidak_valid_ditolak() -> None:
    petugas = Petugas("PT-01", "Dahlia", IdentitasPetugas("dahlia@example.com"))
    with pytest.raises(ValueError):
        petugas.status = "Selesai"


def test_email_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        IdentitasPetugas("email-tidak-valid")
