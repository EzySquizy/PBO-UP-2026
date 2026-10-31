"""Pengujian untuk kelas Penyewa."""

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa



def test_identitas_penyewa() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa("1234567890123456", "Budi", alamat, "08123456789")
    assert penyewa.identitas() == (
        "Budi (1234567890123456) " + chr(8212) + " Kuok, Kuok"
    )



def test_kontak_dengan_nomor() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa("1234567890123456", "Budi", alamat, "08123456789")
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_tanpa_nomor() -> None:
    alamat = Alamat("Dusun I", "Salo", "Salo")
    penyewa = Penyewa("1234567890123456", "Siti", alamat)
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"
