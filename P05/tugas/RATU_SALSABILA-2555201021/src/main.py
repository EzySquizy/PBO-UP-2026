"""Program utama praktikum P05."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def main() -> None:
    """Menampilkan demonstrasi transaksi penyewaan alat tani."""
    alamat = Alamat("Suka Maju", "Kumantan", "Bangkinang Kota")
    penyewa = Penyewa(
        "1400000000000001",
        "Ratu Salsabila",
        alamat,
        "081234567890",
    )

    traktor = AlatTani("TR-01", "Traktor Roda Dua", 150_000)
    pompa = AlatTani("PA-01", "Pompa Air 3 Inci", 75_000)

    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(traktor, 3)
    sewa.tambah_alat(pompa, 2)

    print("--- NOTA PENYEWAAN ALAT TANI ---")
    print(sewa.nota())


if __name__ == "__main__":
    main()
