"""Pengujian untuk kelas Penyewa."""
from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    p = Penyewa("1406012509900001", "Budi Santoso", "Kuok", "0812-3456-7890")
    assert "Budi Santoso" in p.identitas()
    assert "1406012509900001" in p.identitas()


def test_kontak_tanpa_telepon() -> None:
    p = Penyewa("1406014403950002", "Siti Aminah", "Salo")
    assert "belum mencantumkan" in p.kontak()


def test_dua_penyewa_punya_data_sendiri() -> None:
    p1 = Penyewa("111", "Andi", "Bangkinang", "0811")
    p2 = Penyewa("222", "Rina", "Kampar", "0822")
    assert p1.identitas() != p2.identitas()