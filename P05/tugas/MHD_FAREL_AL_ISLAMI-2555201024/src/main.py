
"""Program utama untuk mendemonstrasikan enkapsulasi dan anggota kelas P04."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.kios import Kios
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def demonstrasi_penyewa() -> None:
    print("=== DEMONSTRASI PENYEWA ===")
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


def demonstrasi_staticmethod() -> None:
    print("\n=== DEMONSTRASI STATICMETHOD ===")
    print(f"Tarif Rp150.000 wajar: {AlatTani.tarif_wajar(150_000)}")
    print(f"Tarif Rp5.000 tidak wajar: {AlatTani.tarif_wajar(5_000)}")
    print(f"Format rupiah: {AlatTani.format_rupiah(150_000)}")


def demonstrasi_classmethod() -> None:
    print("\n=== DEMONSTRASI CLASSMETHOD ===")
    print(f"Jumlah alat terdaftar: {AlatTani.jumlah_terdaftar()}")
    alat_csv = AlatTani.dari_baris_csv("PA-01;Pompa Air Honda;75000")
    print(alat_csv.keterangan())
    print(f"Jumlah alat terdaftar: {AlatTani.jumlah_terdaftar()}")


def demonstrasi_denda(alat: AlatTani) -> None:
    print("\n=== DEMONSTRASI DENDA ===")
    denda = alat.denda_keterlambatan(3)
    print(f"Denda keterlambatan 3 hari: {AlatTani.format_rupiah(denda)}")


def demonstrasi_validasi(alat: AlatTani) -> None:
    print("\n=== PERCOBAAN MENEMBUS PENJAGAAN ===")
    for tarif in (0, -5_000):
        try:
            alat.tarif_harian = tarif
        except ValueError as e:
            print(f"Ditolak (tarif {tarif}): {e}")
    print(f"Tarif tetap utuh: {alat.keterangan()}")


def demonstrasi_kios() -> None:
    print("\n=== DEMONSTRASI KIOS UMKM ===")

    produk_beras = Kios("PR-01", "Beras Lokal", 15_000, 18_000, 50)
    produk_jagung = Kios.dari_baris_teks(
        "PR-02;Jagung Manis;10000;12000;30"
    )

    print(f"{'KODE':<8} | {'NAMA PRODUK':<20} | {'STOK':>5} | {'HARGA JUAL':>14}")
    print("-" * 61)
    print(produk_beras.keterangan())
    print(produk_jagung.keterangan())

    print(
        "Harga jual memenuhi keuntungan minimum: "
        f"{Kios.harga_jual_wajar(15_000, 18_000)}"
    )
    print(f"Jumlah produk terdaftar: {Kios.jumlah_produk()}")



def demonstrasi_sewa() -> None:
    print("\n=== DEMONSTRASI TRANSAKSI SEWA P05 ===")
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat,
        "0812-3456-7890",
    )
    transaksi = Sewa("SW-2026-001", penyewa)
    transaksi.tambah_alat(
        AlatTani("TR-01", "Traktor Roda Dua Kubota", 150_000),
        3,
    )
    transaksi.tambah_alat(
        AlatTani("PA-01", "Pompa Air Honda", 75_000),
        5,
    )
    print(transaksi.nota())

def main() -> None:
    demonstrasi_penyewa()

    print("\n=== DEMONSTRASI ALAT TANI ===")
    alat = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150_000)
    print(alat.keterangan())

    demonstrasi_staticmethod()
    demonstrasi_classmethod()
    demonstrasi_denda(alat)
    demonstrasi_validasi(alat)
    demonstrasi_kios()
    demonstrasi_sewa()


if __name__ == "__main__":
    main()
