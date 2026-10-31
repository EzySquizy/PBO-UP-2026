from src.mahasiswa import Mahasiswa


def test_data_mahasiswa() -> None:
    mahasiswa = Mahasiswa(
        nama="Farel Anugrah",
        nim="2555201007",
        desa="Rumbio",
    )

    assert mahasiswa.nama == "Farel Anugrah"
    assert mahasiswa.nim == "2555201007"
    assert mahasiswa.desa == "Rumbio"


def test_perkenalan() -> None:
    mahasiswa = Mahasiswa(
        nama="Farel Anugrah",
        nim="2555201007",
        desa="Rumbio",
    )

    assert mahasiswa.perkenalan() == "Saya Farel Anugrah (2555201007), dari Rumbio."