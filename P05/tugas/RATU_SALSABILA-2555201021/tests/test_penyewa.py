"""Pengujian enkapsulasi untuk kelas Penyewa."""

import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_penyewa(
    nik: str = "1234567890123456",
    telepon: str = "081234567890",
) -> Penyewa:
    alamat = Alamat("Kumantan", "Kumantan", "Bangkinang")
    return Penyewa(nik, "Ratu Salsabila", alamat, telepon)


def test_identitas_memuat_nama() -> None:
    assert "Ratu Salsabila" in buat_penyewa().identitas()


def test_kontak_tanpa_telepon() -> None:
    assert "belum mencantumkan nomor telepon" in buat_penyewa(telepon="-").kontak()


def test_kontak_dengan_telepon() -> None:
    assert "081234567890" in buat_penyewa().kontak()


def test_nik_dapat_dibaca() -> None:
    assert buat_penyewa().nik == "1234567890123456"


@pytest.mark.parametrize("nik", ["123", "123456789012345a", "", "12345678901234567"])
def test_nik_tidak_valid_ditolak(nik: str) -> None:
    with pytest.raises(ValueError):
        buat_penyewa(nik=nik)


def test_nik_hanya_bisa_dibaca() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(AttributeError):
        penyewa.nik = "6543210987654321"  # type: ignore[misc]


def test_alamat_disimpan_sebagai_objek() -> None:
    assert isinstance(buat_penyewa()._alamat, Alamat)


def test_telepon_bisa_diubah() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "081234567899"
    assert penyewa.telepon == "081234567899"


@pytest.mark.parametrize("telepon", ["123", "abcdefghij", "12345678901234", "08123abc890"])
def test_telepon_tidak_valid_ditolak(telepon: str) -> None:
    with pytest.raises(ValueError):
        buat_penyewa(telepon=telepon)


def test_telepon_tidak_valid_saat_diubah() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(ValueError):
        penyewa.telepon = "123"
