
"""Contoh menjalankan aplikasi SIPALA dari terminal."""

from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


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


if __name__ == "__main__":
    main()
