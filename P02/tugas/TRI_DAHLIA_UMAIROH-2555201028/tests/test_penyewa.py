from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("1401", "Budi", "Bangkinang", "08123456789")
    assert penyewa.identitas() == "Budi (1401) — Desa Bangkinang"


def test_kontak_penyewa_dengan_nomor() -> None:
    penyewa = Penyewa("1401", "Budi", "Bangkinang", "08123456789")
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_penyewa_tanpa_nomor() -> None:
    penyewa = Penyewa("1402", "Siti", "Kampar")
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"
