
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat1 = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    alamat2 = Alamat("Pasar", "Bangkinang", "Bangkinang")

    penyewa1 = Penyewa(
        "1401011234567890",
        "Budi",
        alamat1,
        "081234567890",
    )
    penyewa2 = Penyewa(
        "1401021234567890",
        "Andi",
        alamat2,
    )

    print(penyewa1.identitas())
    print(penyewa1.kontak())
    print(penyewa2.identitas())
    print(penyewa2.kontak())

    print(
        f"\nSebelum pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
    )
    pompa = AlatTani(
        "PA-01",
        "Pompa Air 3 Inci",
        75_000,
    )

    print(traktor.keterangan())
    print(pompa.keterangan())

    biaya = AlatTani.format_rupiah(traktor.biaya_sewa(3))
    print(f"Biaya sewa traktor 3 hari: {biaya}")

    alat_csv = AlatTani.dari_baris_csv(
        "PA-01;Pompa Air 3 Inci;75000"
    )
    AlatTani("TR-02", "Traktor Tambahan", 200_000)

    print(alat_csv.keterangan())

    print(
        f"Sesudah pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    print("\n--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon):>14} → {status}")


if __name__ == "__main__":
    main()
