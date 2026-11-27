
from src.model.sewaan import Sewaan
from src.model.status_sewa import StatusSewa
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.format_nilai import sebagai_teks
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok
from src.ui.perintah_konsol import PerintahKonsol


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
        print(
            f"{alat.nama}: "
            f"{AlatTani.format_rupiah(alat.biaya_sewa(3))}"
        )

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

    print("\n========== DEMONSTRASI P07 ==========")

    daftar = DaftarHarga([traktor, pompa, perontok])

    print("\n--- Polimorfisme DaftarHarga ---")
    print(f"Jumlah alat: {daftar.jumlah_alat}")
    print("Biaya sewa selama 3 hari:")
    print(daftar.tabel(3))
    print(
        "Alat termurah: "
        f"{daftar.termurah(3).nama}"
    )
    print(
        "Total jika semua alat disewa: "
        f"{AlatTani.format_rupiah(daftar.total_bila_semua_disewa(3))}"
    )

    print("\n--- Penerjemah perintah match ---")
    konsol = PerintahKonsol(daftar)

    for perintah in (
        "bantuan",
        "daftar 3",
        "harga TR-01 3",
        "termurah 3",
        "ngawur",
    ):
        print(f"\n> {perintah}")
        print(konsol.jalankan(perintah))

    print("\n--- Pemformatan nilai singledispatch ---")
    print(f"Bilangan bulat: {sebagai_teks(150000)}")
    print(f"Persentase: {sebagai_teks(0.825)}")
    print(f"Daftar harga: {sebagai_teks([150000, 75000])}")
    print(f"Teks umum: {sebagai_teks('PBO P07')}")
    print("\n========== DEMONSTRASI P09 ==========")

    print("\n--- Kelas Abstrak ABC ---")
    print(f"Traktor: {traktor.syarat_pemakaian()}")
    print(f"Pompa Air: {pompa.syarat_pemakaian()}")
    print(f"Mesin Perontok: {perontok.syarat_pemakaian()}")

    print("\n--- Protocol Sewaan ---")
    print(
        f"Traktor memenuhi Protocol Sewaan: "
        f"{isinstance(traktor, Sewaan)}"
    )

    print("\n--- Enum StatusSewa ---")
    print(f"Status awal transaksi: {transaksi.status.keterangan()}")
    transaksi.ubah_status(StatusSewa.BERJALAN)
    print(f"Status setelah diubah: {transaksi.status.keterangan()}")


if __name__ == "__main__":
    main()
