

"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("12345", "Budi Santoso", "Kuok")
    assert penyewa.identitas() == "Budi Santoso (12345) — Desa Kuok"


def test_kontak_penyewa_dengan_telepon() -> None:
    penyewa = Penyewa("12345", "Budi Santoso", "Kuok", "081234567890")
    assert penyewa.kontak() == "Budi Santoso dapat dihubungi di 081234567890"


def test_kontak_penyewa_tanpa_telepon() -> None:
    penyewa = Penyewa("67890", "Siti Aminah", "Salo")
    assert penyewa.kontak() == "Siti Aminah belum mencantumkan nomor telepon"
