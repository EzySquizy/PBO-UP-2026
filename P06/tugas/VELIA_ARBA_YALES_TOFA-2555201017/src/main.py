"""Program utama modul P05."""
from src.model.alat_tani import AlatTani


def main() -> None:
    print(f"Sebelum pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")
    alat1 = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    print(f" {alat1.keterangan()}")
    alat2 = AlatTani("PA-01", "Pompa Air 3 Inci", 75000)
    print(f" {alat2.keterangan()}")
    print(f"Sesudah pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")


if __name__ == "__main__":
    main()