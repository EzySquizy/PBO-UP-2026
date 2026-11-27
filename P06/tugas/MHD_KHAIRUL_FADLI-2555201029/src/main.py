
"""Program utama untuk mendemonstrasikan fitur P06."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewa import Sewa
from src.model.traktor import Traktor


def buat_penyewa() -> Penyewa:
    """Membuat data penyewa Budi."""
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat,
        "0812-3456-7890",
    )


def demonstrasi_penyewa(budi: Penyewa) -> None:
    """Menampilkan informasi penyewa."""
    print(budi.identitas())
    print(
        f"Dusun {budi.alamat.dusun}, "
        f"Desa {budi.alamat.desa}, "
        f"Kec. {budi.alamat.kecamatan}"
    )


def demonstrasi_alat() -> tuple[AlatTani, AlatTani]:
    """Menampilkan fitur dasar alat tani."""
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
    return alat, alat_csv


def demonstrasi_sewa(
    budi: Penyewa,
    alat: AlatTani,
    alat_csv: AlatTani,
) -> None:
    """Menampilkan nota penyewaan."""
    print("\n-- Demonstrasi fitur P05")

    sewa = Sewa("SW-001", budi)
    sewa.tambah_alat(alat, 3)
    sewa.tambah_alat(alat_csv, 2)

    print(sewa.nota())
    print("\nTotal pembayaran:", AlatTani.format_rupiah(sewa.total()))


def demonstrasi_pewarisan() -> None:
    """Menampilkan fitur pewarisan tiga jenis alat tani."""
    print("\n-- Demonstrasi fitur P06: Pewarisan")

    daftar: list[tuple[AlatTani, int]] = [
        (
            Traktor("TR-03", "Traktor P06", 150_000, 20),
            3,
        ),
        (
            PompaAir("PA-01", "Pompa Air P06", 100_000, 100),
            3,
        ),
        (
            Perontok("PR-01", "Mesin Perontok P06", 200_000),
            1,
        ),
    ]

    for alat, hari in daftar:
        biaya = alat.biaya_sewa(hari)
        print(alat)
        print(
            f"Biaya sewa {hari} hari: "
            f"{AlatTani.format_rupiah(biaya)}"
        )


def demonstrasi_penjagaan(alat: AlatTani) -> None:
    """Menguji perlindungan atribut tarif."""
    print("\n-- Percobaan menembus penjagaan")
    try:
        alat.tarif_harian = 0
    except ValueError as e:
        print(f"Ditolak: {e}")

    print("Tarif tetap utuh:", alat.keterangan())


def main() -> None:
    """Menjalankan seluruh demonstrasi."""
    budi = buat_penyewa()
    demonstrasi_penyewa(budi)
    alat, alat_csv = demonstrasi_alat()
    demonstrasi_sewa(budi, alat, alat_csv)
    demonstrasi_pewarisan()
    demonstrasi_penjagaan(alat)


if __name__ == "__main__":
    main()
