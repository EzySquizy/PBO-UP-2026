"""Program utama untuk mendemonstrasikan fitur P05."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def main() -> None:
    alamat_budi = Alamat("Pulau Jambu", "Kuok", "Kuok")
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )

    print(budi.identitas())
    print(
        f"Dusun {budi.alamat.dusun}, "
        f"Desa {budi.alamat.desa}, "
        f"Kec. {budi.alamat.kecamatan}"
    )

    print("\n-- Demonstrasi fitur P04")

    alat = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150_000)
    print(alat.keterangan())

    print("Tarif wajar:", AlatTani.tarif_wajar(150_000))
    print("Format rupiah:", AlatTani.format_rupiah(150_000))
    print("Jumlah alat terdaftar:", AlatTani.jumlah_terdaftar())

    alat_csv = AlatTani.dari_baris_csv(
        "TR-02;Traktor Roda Empat;250000"
    )
    print("Hasil CSV:", alat_csv.keterangan())
    print("Jumlah alat terdaftar:", AlatTani.jumlah_terdaftar())

    print(
        "Denda keterlambatan 3 hari:",
        AlatTani.format_rupiah(alat.denda_keterlambatan(3)),
    )

    print("\n-- Demonstrasi fitur P05")

    sewa = Sewa("SW-001", budi)
    sewa.tambah_alat(alat, 3)
    sewa.tambah_alat(alat_csv, 2)

    print(sewa.nota())

    print("\nTotal pembayaran:", AlatTani.format_rupiah(sewa.total()))

    print("\n-- Percobaan menembus penjagaan")
    try:
        alat.tarif_harian = 0
    except ValueError as e:
        print(f"Ditolak: {e}")

    print("Tarif tetap utuh:", alat.keterangan())


if __name__ == "__main__":
    main()