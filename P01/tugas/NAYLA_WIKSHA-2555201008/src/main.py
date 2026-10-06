from src.mahasiswa import Mahasiswa


def main() -> None:
    mahasiswa = Mahasiswa(
        "Nayla Wiksha",
        "2555201008",
        "Kampar",
    )
    print(mahasiswa.perkenalan())


if __name__ == "__main__":
    main()