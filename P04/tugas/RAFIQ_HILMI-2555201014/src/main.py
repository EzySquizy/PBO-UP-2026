
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alat_tani import AlatTani


def uji_validasi_tarif(traktor: AlatTani) -> None:
    """Menguji penolakan tarif yang tidak valid."""
    print("\n--- Percobaan menembus penjagaan ---")

    for tarif in (0, -5000):
        try:
            traktor.tarif_harian = tarif
        except ValueError as e:
            print(f"Ditolak (tarif {tarif}):", e)

    print("Tarif tetap utuh:", traktor.keterangan())


def tampilkan_pemeriksaan_tarif() -> None:
    """Menampilkan hasil pemeriksaan beberapa tarif."""
    print("\n--- Memeriksa tarif tanpa membuat objek ---")

    for calon in (5000, 150000, 6000000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon):>14} → {status}")


def main() -> None:
    print("Sebelum pendataan, alat terdaftar:", AlatTani.jumlah_terdaftar())

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    pompa = AlatTani.dari_baris_csv("PA-01;Pompa Air 3 Inci;75000")
    AlatTani("TR-02", "Traktor Roda Empat", 200000)
    AlatTani("PA-02", "Pompa Air 2 Inci", 100000)

    print(traktor.keterangan())
    print(pompa.keterangan())

    print("Sesudah pendataan, alat terdaftar:", AlatTani.jumlah_terdaftar())

    tampilkan_pemeriksaan_tarif()

    print("\n--- Denda keterlambatan ---")
    print(AlatTani.format_rupiah(traktor.denda_keterlambatan(2)))


if __name__ == "__main__":
    main()

