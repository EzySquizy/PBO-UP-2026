class Mahasiswa:
    """Mewakili data seorang mahasiswa."""

    def __init__(self, nama: str, nim: str, desa: str) -> None:
        self._nama = nama
        self._nim = nim
        self._desa = desa

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def desa(self) -> str:
        return self._desa

    def perkenalan(self) -> str:
        return f"Saya {self.nama} ({self.nim}), dari {self.desa}."
    


def main() -> None:
    mahasiswa = Mahasiswa(
        nama="Farel anugrah",
        nim="2555201007",
        desa="rumbio",
    )

    print(mahasiswa.perkenalan())


if __name__ == "__main__":
    main()