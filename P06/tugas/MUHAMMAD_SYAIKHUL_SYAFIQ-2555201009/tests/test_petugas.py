
"""Pengujian untuk kelas Petugas."""

from dataclasses import FrozenInstanceError

import pytest
from src.model.periode_tugas import PeriodeTugas
from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi")
    assert petugas.identitas() == "Andi (PT-01) - Admin"


def test_kontak_dengan_nomor_telepon() -> None:
    petugas = Petugas(
        "PT-02", "Budi", "Operator", "budi", "081234567890"
    )
    assert petugas.kontak() == "Budi dapat dihubungi di 081234567890"


def test_dua_objek_menyimpan_data_masing_masing() -> None:
    petugas_a = Petugas("PT-01", "Andi", "Admin", "andi")
    petugas_b = Petugas(
        "PT-02", "Budi", "Operator", "budi", "081234567890"
    )
    assert petugas_a.identitas() == "Andi (PT-01) - Admin"
    assert petugas_b.identitas() == "Budi (PT-02) - Operator"
    assert petugas_a.kontak() == "Andi belum mencantumkan nomor telepon"
    assert petugas_b.kontak() == "Budi dapat dihubungi di 081234567890"


def test_id_petugas_baca_saja() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi")
    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-02"  # type: ignore[misc]


def test_nama_petugas_baca_saja() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi")
    with pytest.raises(AttributeError):
        petugas.nama = "Budi"  # type: ignore[misc]


def test_username_baca_saja() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi")
    with pytest.raises(AttributeError):
        petugas.username = "budi"  # type: ignore[misc]


def test_id_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Andi", "Admin", "andi")


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "", "Admin", "andi")


def test_username_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Andi", "Admin", "")


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Andi", "Admin", "andi", "12AB")


def test_setter_telepon_menerima_nomor_valid() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi")
    petugas.telepon = "081298765432"
    assert petugas.telepon == "081298765432"


def test_setter_telepon_menolak_nomor_tidak_valid() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi", "081234567890")
    with pytest.raises(ValueError):
        petugas.telepon = "123"
    assert petugas.telepon == "081234567890"


def test_periode_tugas_valid() -> None:
    periode = PeriodeTugas(10, 2026)
    assert periode.keterangan() == "10/2026"


def test_periode_bulan_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(13, 2026)


def test_periode_tahun_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        PeriodeTugas(1, 1999)


def test_periode_tugas_tidak_dapat_diubah() -> None:
    periode = PeriodeTugas(10, 2026)
    with pytest.raises(FrozenInstanceError):
        periode.bulan = 12  # type: ignore[misc]


def test_petugas_menggunakan_periode_yang_diberikan() -> None:
    periode = PeriodeTugas(10, 2026)
    petugas = Petugas("PT-01", "Andi", "Admin", "andi", periode=periode)
    assert petugas.periode == periode
