
"""Program utama demonstrasi sistem penyewaan UPJA."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    """Menjalankan demonstrasi penyewaan alat."""
    traktor = AlatTani("ALT-001", "Traktor Roda Dua", 150000)

    alamat_budi = Alamat("Suka Maju", "Kuok", "Kuok")
    alamat_siti = Alamat("Salo", "Salo", "Salo")

    budi = Penyewa(
        "1406014403950001",
        "Budi Santoso",
        alamat_budi,
        "081234567890",
    )

    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        alamat_siti,
    )

    print("=== DEMONSTRASI P03 ===")
    print(traktor.keterangan())
    print(budi.identitas())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())


if __name__ == "__main__":
    main()
