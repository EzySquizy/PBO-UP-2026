
from src.model.petugas import Petugas


def test_identitas_petugas():
    petugas = Petugas("P001", "Budi", "Admin", "Penyasawan")
    assert petugas.identitas() == "Budi (P001) - Admin"


def test_lokasi_tugas():
    petugas = Petugas("P002", "Andi", "Operator", "Bangkinang")
    assert petugas.lokasi_tugas() == "Andi bertugas di Desa Bangkinang"


def test_data_dua_petugas_independen():
    petugas1 = Petugas("P001", "Budi", "Admin", "Penyasawan")
    petugas2 = Petugas("P002", "Andi", "Operator", "Bangkinang")

    assert petugas1.identitas() == "Budi (P001) - Admin"
    assert petugas2.identitas() == "Andi (P002) - Operator"


def test_kontak_default():
    petugas = Petugas("P003", "Siti", "Admin", "Kampar")
    assert petugas.kontak() == "Siti belum mencantumkan nomor telepon"
