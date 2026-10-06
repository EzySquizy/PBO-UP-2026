
from src.model.penyewa import Penyewa
from src.model.alat_tani import AlatTani


def main() -> None:
    penyewa1 = Penyewa(
        "140101",
        "Budi",
        "Penyasawan",
        "081234567890",
    )
    penyewa2 = Penyewa(
        "140102",
        "Andi",
        "Bangkinang",
    )

    traktor = AlatTani("TR-01", "Traktor", 150000)
    traktor._tarif_harian = -5000
    pompa = AlatTani("AL-02", "Pompa Air", 50000)

    print(penyewa1.identitas())
    print(penyewa1.kontak())
    print(penyewa2.identitas())
    print(penyewa2.kontak())

    print(traktor.keterangan())
    print(f"Biaya sewa 2 hari: Rp{traktor.biaya_sewa(2):,}".replace(",", "."))
    print(pompa.keterangan())
    print(f"Biaya sewa 3 hari: Rp{pompa.biaya_sewa(3):,}".replace(",", "."))


if __name__ == "__main__":
    main()
