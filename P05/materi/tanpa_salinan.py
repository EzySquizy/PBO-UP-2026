"""Kesalahan yang disengaja nomor 1: baris sewa tidak menyimpan salinan tarif.

Baris sewa hanya menyimpan rujukan ke alatnya, lalu membaca tarif dari alat
itu setiap kali dibutuhkan. Akibatnya, ketika UPJA menyesuaikan tarif pada
musim berikutnya, seluruh nota lama ikut berubah dengan sendirinya.
"""

import sys

sys.path.insert(0, "kode")

from src.model.alat_tani import AlatTani      # noqa: E402


class BarisSewaTanpaSalinan:
    """Baris sewa yang membaca tarif dari alat, bukan dari salinan."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        self._alat = alat
        self._jumlah_hari = jumlah_hari

    def subtotal(self) -> int:
        return self._alat.tarif_harian * self._jumlah_hari    # SALAH: baca ulang

    def baris_nota(self) -> str:
        tarif = AlatTani.format_rupiah(self._alat.tarif_harian)
        return f"{self._alat.nama} {self._jumlah_hari} hr x {tarif} = {AlatTani.format_rupiah(self.subtotal())}"


def main() -> None:
    traktor = AlatTani("TR-01", "Traktor Roda Dua", 150_000)
    nota_maret = BarisSewaTanpaSalinan(traktor, 3)

    print("Nota Maret, saat dicetak :", nota_maret.baris_nota())

    print("\nMusim berikutnya UPJA menaikkan tarif menjadi Rp175.000...")
    traktor.tarif_harian = 175_000

    print("Nota Maret, dibuka lagi  :", nota_maret.baris_nota())
    print("\nPetani membayar Rp450.000 pada bulan Maret,")
    print("tetapi arsip UPJA sekarang mencatat Rp525.000.")


if __name__ == "__main__":
    main()
