"""Pengujian untuk kelas Petugas dan objek nilai PeriodeTugas."""

import dataclasses
import pytest
from src.model.petugas import PeriodeTugas, Petugas


def test_hitung_pendapatan() -> None:
    """Menguji perhitungan pendapatan petugas dengan nilai benar."""
    periode = PeriodeTugas("Senin", "Jumat")
    petugas = Petugas("Aidiel Putra Perdana", "Operator", periode, 150000)
    assert petugas.hitung_pendapatan(3) == 450000


def test_cetak_identitas() -> None:
    """Menguji format string identitas petugas."""
    periode = PeriodeTugas("Senin", "Jumat")
    petugas = Petugas("Aidiel Putra Perdana", "Operator", periode, 150000)
    assert petugas.cetak_identitas() == "Aidiel Putra Perdana (Operator) [Senin s.d Jumat] — Tarif: Rp 150.000"


def test_parameter_default() -> None:
    """Menguji nilai default tarif per jam jika tidak diisi."""
    periode = PeriodeTugas("Selasa", "Kamis")
    petugas = Petugas("Siti Aminah", "Operator", periode)
    assert petugas.tarif_per_jam == 100000


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    """Membuktikan tarif bernilai minus ditolak saat pembuatan objek."""
    periode = PeriodeTugas("Senin", "Jumat")
    with pytest.raises(ValueError):
        Petugas("Budi", "Admin", periode, -50000)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    """Membuktikan setter menolak nilai minus dan nilai lama tetap utuh."""
    periode = PeriodeTugas("Senin", "Jumat")
    petugas = Petugas("Budi", "Admin", periode, 100000)
    
    with pytest.raises(ValueError):
        petugas.tarif_per_jam = -10000
    
    assert petugas.tarif_per_jam == 100000  # Nilai lama tidak berubah


def test_nama_tidak_punya_setter() -> None:
    """Membuktikan property nama bersifat baca-saja (tidak bisa diubah)."""
    periode = PeriodeTugas("Senin", "Jumat")
    petugas = Petugas("Budi", "Admin", periode, 100000)
    
    with pytest.raises(AttributeError):
        petugas.nama = "Joko"  # type: ignore[misc]


def test_periode_beku() -> None:
    """Membuktikan objek nilai PeriodeTugas beku dan tidak dapat diubah isinya."""
    periode = PeriodeTugas("Senin", "Jumat")
    with pytest.raises(dataclasses.FrozenInstanceError):
        periode.hari_mulai = "Minggu"  # type: ignore[misc]