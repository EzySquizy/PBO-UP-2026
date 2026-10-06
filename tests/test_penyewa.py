
from src.model.penyewa import Penyewa


def test_identitas_penyewa():
    penyewa = Penyewa("140101", "Budi", "Penyasawan")
    assert penyewa.identitas() == "Budi (140101) — Desa Penyasawan"


def test_kontak_tanpa_telepon():
    penyewa = Penyewa("140102", "Andi", "Bangkinang")
    assert penyewa.kontak() == "Andi belum mencantumkan nomor telepon"


def test_kontak_dengan_telepon():
    penyewa = Penyewa("140103", "Siti", "Kampar", "081234567890")
    assert penyewa.kontak() == "Siti dapat dihubungi di 081234567890"
