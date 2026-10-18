
from src.model.penyewa import Penyewa
from src.model.alat_tani import AlatTani
from src.model.alamat import Alamat


def main() -> None:
    alamat1 = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    alamat2 = Alamat("Pasar", "Bangkinang", "Bangkinang")

    penyewa1 = Penyewa(
        "1401011234567890", "Budi", alamat1, "081234567890"
    )
    penyewa2 = Penyewa(
        "1401021234567890", "Andi", alamat2
    )

    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("AL-02", "Pompa Air", 50000)

    print(penyewa1.identitas())
    print(penyewa1.kontak())
    print(penyewa2.identitas())
    print(penyewa2.kontak())
    print(traktor.keterangan())

    biaya = f"{traktor.biaya_sewa(3):,}".replace(",", ".")
    print(f"Biaya sewa traktor 3 hari: Rp{biaya}")

    print(pompa.keterangan())


if __name__ == "__main__":
    main()
