
"""Program utama untuk demonstrasi P04 dan P07."""

from src.format_nilai import sebagai_teks
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


def demonstrasi_p04() -> None:
    """Menampilkan demonstrasi fitur P04."""
    print("=== Demonstrasi P04 ===")
    print(f"Sebelum pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    alat1 = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    print(f" {alat1.keterangan()}")

    alat2 = AlatTani("PA-01", "Pompa Air 3 Inci", 75000)
    print(f" {alat2.keterangan()}")

    _ = AlatTani.dari_baris_csv("TR-02;Traktor Rotary;200000")
    _ = AlatTani.dari_baris_csv("PA-02;Pompa Air 4 Inci;85000")

    print(f"Sesudah pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    print("--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon)} -> {status}")


def buat_daftar_harga() -> DaftarHarga:
    """Membuat daftar harga berisi beberapa jenis alat."""
    daftar_alat = [
        Traktor("TR-03", "Traktor Kubota", 150_000, 20),
        PompaAir("PA-03", "Pompa Air 3 Inci", 75_000, 100),
        Perontok("PR-01", "Perontok Padi", 50_000, 500),
        AlatTani("GR-01", "Gerobak Dorong", 25_000),
    ]
    return DaftarHarga(daftar_alat)


def demonstrasi_format_nilai() -> None:
    """Menampilkan demonstrasi singledispatch."""
    print("\nContoh format nilai:")
    print(sebagai_teks(150_000))
    print(sebagai_teks(0.825))
    print(sebagai_teks([150_000, 75_000]))


def jalankan_konsol(daftar: DaftarHarga) -> None:
    """Menerima dan menjalankan perintah pengguna."""
    perintah = PerintahKonsol(daftar)

    print("\n=== Konsol Daftar Harga ===")
    print("Ketik 'bantuan' untuk melihat perintah.")
    print("Ketik 'keluar' untuk mengakhiri program.")

    while True:
        try:
            masukan = input("> ").strip()
        except EOFError:
            print("\nInput interaktif tidak tersedia. Konsol dihentikan.")
            break

        if masukan.lower() == "keluar":
            print("Program selesai.")
            break

        print(perintah.jalankan(masukan))


def main() -> None:
    """Menjalankan demonstrasi P04 dan P07."""
    demonstrasi_p04()

    print("\n=== Demonstrasi P07 ===")
    daftar = buat_daftar_harga()
    print(f"Jumlah alat: {daftar.jumlah_alat}")

    demonstrasi_format_nilai()
    jalankan_konsol(daftar)


if __name__ == "__main__":
    main()
