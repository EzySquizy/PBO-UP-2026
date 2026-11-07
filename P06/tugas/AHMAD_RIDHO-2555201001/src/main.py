"""Program utama demonstrasi pewarisan alat tani."""

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

    print("--- DEMONSTRASI PEWARISAN ALAT TANI ---")

    print(f"\n{traktor}")
    print(f"Biaya sewa 1 hari: {Traktor.format_rupiah(traktor.biaya_sewa(1))}")
    print(f"Biaya sewa 3 hari: {Traktor.format_rupiah(traktor.biaya_sewa(3))}")

    print(f"\n{pompa}")
    print(f"Konsumsi solar: {pompa.konsumsi_solar_harian()} liter/hari")
    print(f"Biaya sewa 1 hari: {PompaAir.format_rupiah(pompa.biaya_sewa(1))}")
    print(f"Biaya sewa 3 hari: {PompaAir.format_rupiah(pompa.biaya_sewa(3))}")

    print(f"\n{perontok}")
    print(f"Biaya sewa 1 hari: {Perontok.format_rupiah(perontok.biaya_sewa(1))}")
    print(f"Biaya sewa 3 hari: {Perontok.format_rupiah(perontok.biaya_sewa(3))}")


if __name__ == "__main__":
    main()
