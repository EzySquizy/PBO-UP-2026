"""Program utama untuk mendemonstrasikan anggota kelas."""

from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir


def main() -> None:
    print(f"Sebelum pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    alat1 = Traktor("TR-01", "Traktor Roda Dua Kubota", 150000, 8)
    print(f" {alat1.keterangan()}")

    alat2 = PompaAir("PA-01", "Pompa Air 3 Inci", 75000, 600)
    print(f" {alat2.keterangan()}")

    _ = Traktor("TR-02", "Traktor Rotary", 200000, 10)
    _ = PompaAir("PA-02", "Pompa Air 4 Inci", 85000, 800)

    print(f"Sesudah pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    print("--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon)} → {status}")


if __name__ == "__main__":
    main()