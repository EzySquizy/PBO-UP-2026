"""Kesalahan yang disengaja nomor 1: menelan eksepsi.

Pengurus UPJA memasukkan sepuluh baris pendataan alat. Tiga di antaranya
cacat. Karena kegagalannya ditelan diam-diam, program melaporkan pendataan
berhasil, dan tidak seorang pun tahu bahwa tiga alat hilang dari daftar.
"""

import sys

sys.path.insert(0, "kode")

from src.model.traktor import Traktor      # noqa: E402

BARIS_PENDATAAN = [
    "TR-01;Traktor Kubota;150000;8",
    "TR-02;Traktor Yanmar;140000;7",
    "TR-03;Traktor Quick;seratus tiga puluh ribu;6",   # tarif bukan angka
    "TR-04;Traktor Kubota Besar;160000;9",
    "TR-05;Traktor tanpa daya;155000",                  # kurang satu bagian
    "TR-06;Traktor Iseki;145000;8",
    "TR-07;Traktor Mitsubishi;148000;8",
    "TR-08;Traktor kecil;;5",                           # tarif kosong
    "TR-09;Traktor Yanmar Kecil;135000;6",
    "TR-10;Traktor Kubota Mini;138000;5",
]


def daftarkan_cara_buruk(baris: list[str]) -> list[Traktor]:
    """Mendaftarkan alat sambil menelan setiap kegagalan."""
    hasil = []
    for satu in baris:
        try:
            hasil.append(Traktor.dari_baris_csv(satu))
        except Exception:
            pass          # SALAH: kegagalan hilang tanpa jejak
    return hasil


def main() -> None:
    terdaftar = daftarkan_cara_buruk(BARIS_PENDATAAN)
    print(f"Baris yang dimasukkan pengurus : {len(BARIS_PENDATAAN)}")
    print(f"Alat yang berhasil terdaftar   : {len(terdaftar)}")
    print()
    print("Program tidak melaporkan satu pun kegagalan.")
    print("Pengurus mengira sepuluh alat sudah terdaftar seluruhnya.")
    print("Tiga alat hilang, dan baru ketahuan ketika ada petani mencarinya.")


if __name__ == "__main__":
    main()
