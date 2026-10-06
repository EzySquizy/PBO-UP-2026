class Mahasiswa:
    """Mewakili data seorang mahasiswa."""

    def __init__(self, nama: str, nim: str, asal_desa: str) -> None:
        self._nama = nama
        self._nim = nim
        self._asal_desa = asal_desa

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def asal_desa(self) -> str:
        return self._asal_desa

    def perkenalan(self) -> str:
        return (
            f"Halo, saya {self.nama}, NIM {self.nim}, "
            f"asal {self.asal_desa}."
        )