
"""Contoh menjalankan aplikasi SIPALA dari terminal."""

from src.format_nilai import sebagai_teks
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


def main() -> None:
    traktor = Traktor(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
        8,
    )

    pompa = PompaAir(
        "PA-01",
        "Pompa Air 3 Inci",
        75_000,
        600,
    )

    perontok = Perontok(
        "PR-01",
        "Mesin Perontok Padi",
        200_000,
        900,
    )

    alat_tani = [traktor, pompa, perontok]

    print("=== Demonstrasi Polimorfisme ===")
    for alat in alat_tani:
        print(alat)
        print(
            f"Biaya sewa 1 hari: "
            f"{alat.format_rupiah(alat.biaya_sewa(1))}"
        )
        print(
            f"Biaya sewa 3 hari: "
            f"{alat.format_rupiah(alat.biaya_sewa(3))}"
        )
        print()

    print("=== Demonstrasi Daftar Harga ===")
    daftar = DaftarHarga(alat_tani)
    print(daftar.tabel(3))
    print(
        "Total jika semua alat disewa 3 hari: "
        f"{traktor.format_rupiah(daftar.total_bila_semua_disewa(3))}"
    )

    print("\n=== Demonstrasi Perintah Konsol ===")
    konsol = PerintahKonsol(daftar)

    for perintah in [
        "bantuan",
        "daftar 3",
        "harga TR-01 3",
        "termurah 3",
        "harga XX-99 1",
    ]:
        print(f"\n> {perintah}")
        print(konsol.jalankan(perintah))


if __name__ == "__main__":
    main()

    print("\n=== Demonstrasi Singledispatch ===")
    print(sebagai_teks(150_000))
    print(sebagai_teks(0.825))
    print(sebagai_teks([150_000, 75_000]))
    print(sebagai_teks("SIPALA"))
