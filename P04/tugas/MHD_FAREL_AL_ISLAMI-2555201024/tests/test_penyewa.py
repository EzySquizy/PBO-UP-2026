"""Pengujian untuk kelas Penyewa."""
import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    p = Penyewa("1406012509900001", "Budi Santoso", alamat, "0812-3456-7890")
    assert "Budi Santoso" in p.identitas()
    assert "1406012509900001" in p.identitas()


def test_kontak_tanpa_telepon() -> None:
    alamat = Alamat("", "Salo", "Salo")
    p = Penyewa("1406014403950002", "Siti Aminah", alamat)
    assert "belum mencantumkan" in p.kontak()


def test_dua_penyewa_punya_data_sendiri() -> None:
    a1 = Alamat("Dusun I", "Bangkinang", "Bangkinang")
    a2 = Alamat("Dusun II", "Kampar", "Kampar")
    p1 = Penyewa("1406012509900001", "Andi", a1, "081112345678")
    p2 = Penyewa("1406014403950002", "Rina", a2, "082212345678")
    assert p1.identitas() != p2.identitas()


def test_nik_tidak_valid_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("123", "Budi", alamat)  # NIK kurang dari 16 digit[cite: 16]


def test_telepon_tidak_sah_ditolak() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(ValueError):
        Penyewa("1406012509900001", "Budi", alamat, "123")  # Telepon terlalu pendek[cite: 16]
