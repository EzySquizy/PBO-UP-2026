
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat_budi = Alamat("Pulau Belimbing", "Kuok", "Kuok")
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )

    alamat_siti = Alamat("Salo Timur", "Salo", "Salo")
    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        alamat_siti,
    )

    print(f"Sebelum pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
    )
    pompa = AlatTani.dari_baris_csv("PA-01;Pompa Air 3 Inci;75000")
    traktor_tambahan = AlatTani.dari_baris_csv(
        "TR-02;Traktor Roda Dua;125000"
    )
    pompa_tambahan = AlatTani(
        "PA-02",
        "Pompa Air Cadangan",
        80_000,
    )

    print("--- Data penyewa ---")
    print(budi.identitas())
    print(budi.alamat.lengkap())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())

    print("\n--- Data alat ---")
    print(traktor.keterangan())
    print(pompa.keterangan())
    print(traktor_tambahan.keterangan())
    print(pompa_tambahan.keterangan())
    print(f"Sesudah pendataan, alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    print("\n--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon):>14}  ->  {status}")

    print("\n--- Percobaan menembus penjagaan ---")
    try:
        traktor.tarif_harian = -5_000
    except ValueError as kesalahan:
        print(f"Ditolak (tarif tidak wajar): {kesalahan}")

    try:
        Penyewa("123", "Nama Uji", alamat_budi)
    except ValueError as kesalahan:
        print(f"Ditolak (NIK tidak valid): {kesalahan}")

    print(
        "Denda keterlambatan 2 hari: "
        f"{AlatTani.format_rupiah(traktor.denda_keterlambatan(2))}"
    )


if __name__ == "__main__":
    main()
