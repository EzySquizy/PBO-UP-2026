from src.mahasiswa import Mahasiswa


def test_data_mahasiswa() -> None:
    mahasiswa = Mahasiswa(
        "Nayla Wiksha",
        "2555201008",
        "Kampar",
    )

    assert mahasiswa.nama == "Nayla Wiksha"
    assert mahasiswa.nim == "2555201008"
    assert mahasiswa.asal_desa == "Kampar"


def test_perkenalan() -> None:
    mahasiswa = Mahasiswa(
        "Nayla Wiksha",
        "2555201008",
        "Kampar",
    )

    assert mahasiswa.perkenalan() == (
        "Halo, saya Nayla Wiksha, NIM 2555201008, asal Kampar."
    )