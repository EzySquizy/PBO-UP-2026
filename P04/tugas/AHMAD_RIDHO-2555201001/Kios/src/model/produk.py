class Produk:
    """Mewakili satu produk yang dijual di kios."""

    def __init__(self, kode: str, nama: str) -> None:
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama produk tidak boleh kosong.")

        self._kode = kode
        self._nama = nama

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama
