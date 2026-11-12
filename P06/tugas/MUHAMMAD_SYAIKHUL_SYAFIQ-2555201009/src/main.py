
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok


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

    print(
        "Sebelum pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    traktor = Traktor(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
        8,
    )
    pompa = PompaAir.dari_baris_csv(
        "PA-01;Pompa Air 3 Inci;75000;600"
    )
    perontok = Perontok.dari_baris_csv(
        "PR-01;Mesin Perontok Padi;200000;900"
    )

    print("--- Data penyewa ---")
    print(budi.identitas())
    print(budi.alamat.lengkap())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())

    print("\n--- Data alat P06 ---")
    for alat in (traktor, pompa, perontok):
        print(alat.keterangan())

    print(
        "Sesudah pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    print("\n--- Biaya sewa setiap jenis alat ---")
    for alat in (traktor, pompa, perontok):
        print(f"{alat.nama}: {AlatTani.format_rupiah(alat.biaya_sewa(3))}")

    print("\n--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f"{AlatTani.format_rupiah(calon):>14} -> {status}")

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

    transaksi = Sewa("SW-001", budi)
    transaksi.tambah_alat(traktor, 3)
    transaksi.tambah_alat(pompa, 5)
    transaksi.tambah_alat(perontok, 1)

    print("\n--- Transaksi penyewaan P06 ---")
    print(transaksi.nota())


if __name__ == "__main__":
    main()
