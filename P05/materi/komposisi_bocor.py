"""Kesalahan yang disengaja nomor 2: komposisi yang bocor keluar.

Property mengembalikan daftar aslinya, bukan salinannya. Siapa pun yang
menerima daftar itu dapat menambah atau menghapus isinya, sehingga transaksi
kehilangan kendali atas baris yang seharusnya menjadi miliknya sendiri.
"""


class Sewa:
    """Transaksi sewa yang membocorkan daftar barisnya sendiri."""

    def __init__(self, nomor: str) -> None:
        self._nomor = nomor
        self._baris: list[str] = []

    @property
    def baris(self) -> list[str]:
        return self._baris          # SALAH: daftar aslinya, bukan salinan

    def tambah(self, kode_alat: str) -> None:
        self._baris.append(kode_alat)

    def jumlah_alat(self) -> int:
        return len(self._baris)


def main() -> None:
    sewa = Sewa("SW-2026-001")
    sewa.tambah("TR-01")
    sewa.tambah("PA-01")
    print("Jumlah alat awal   :", sewa.jumlah_alat())

    daftar = sewa.baris
    daftar.append("PR-99")          # tidak lewat tambah(), tidak ada pemeriksaan
    daftar.append("PR-99")          # bahkan boleh ganda
    print("Setelah disusupi   :", sewa.jumlah_alat(), sewa.baris)

    daftar.clear()
    print("Setelah dikosongkan:", sewa.jumlah_alat())
    print("\nTransaksi kehilangan kendali atas barisnya sendiri.")


if __name__ == "__main__":
    main()
