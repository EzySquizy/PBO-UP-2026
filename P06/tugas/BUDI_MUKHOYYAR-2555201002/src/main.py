
"""Program utama untuk mendemonstrasikan fitur PBO P04."""

from src.model.alat_tani import AlatTani


def main() -> None:
    print("Sebelum pendataan, alat terdaftar:", AlatTani.jumlah_terdaftar())

    # Dua alat yang ditampilkan sesuai panduan P04.
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

    # Dua alat tambahan agar jumlah objek terdaftar menjadi empat.
    AlatTani("TR-02", "Traktor Roda Empat", 250_000)
    AlatTani("PA-02", "Pompa Air 2 Inci", 50_000)

    print(traktor.keterangan())
    print(pompa.keterangan())
    print("Sesudah pendataan, alat terdaftar:", AlatTani.jumlah_terdaftar())

    print("\n--- Memeriksa tarif tanpa membuat objek ---")
    contoh_tarif = [5_000, 150_000, 6_000_000]

    for nilai in contoh_tarif:
        status = "wajar" if AlatTani.tarif_wajar(nilai) else "ditolak"
        rupiah = AlatTani.format_rupiah(nilai)
        print(f"{rupiah:>14} → {status}")


if __name__ == "__main__":
    main()
