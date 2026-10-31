from src.mahasiswa import Mahasiswa


def main() -> None:
    mahasiswa = Mahasiswa(
        nama="Farel Anugrah",
        nim="2555201007",
        desa="Rumbio",
    )
    print(mahasiswa.perkenalan())


if __name__ == "__main__":
    main()
