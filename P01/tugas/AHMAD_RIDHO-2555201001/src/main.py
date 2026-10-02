"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar."""

from src.mahasiswa import Mahasiswa


def main() -> None:
    saya = Mahasiswa("Budi Santoso", "2410123456", "Kuok")
    print(saya.perkenalan())


if __name__ == "__main__":
    main()