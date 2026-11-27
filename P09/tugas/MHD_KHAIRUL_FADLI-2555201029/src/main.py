
"""Program utama demonstrasi P09: ABC, Protocol, dan Enum."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa, StatusSewa
from src.model.sewaan import Sewaan
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


def demonstrasi_abc() -> Traktor:
    """Menampilkan penggunaan kelas abstrak."""
    print("\n-- Demonstrasi ABC")

    try:
        AlatTani(  # type: ignore[abstract]
            "AT-01",
            "Alat Abstrak",
            100_000,
        )
    except TypeError as error:
        print("AlatTani tidak dapat dibuat langsung:")
        print(error)

    traktor = Traktor(
        "TR-01",
        "Traktor Roda Dua",
        150_000,
        20,
    )

    print("Objek konkret:", traktor.keterangan())
    print("Syarat:", traktor.syarat_pemakaian())
    print(
        "Biaya sewa 3 hari:",
        AlatTani.format_rupiah(traktor.biaya_sewa(3)),
    )

    return traktor


def demonstrasi_protocol(traktor: Traktor) -> None:
    """Menampilkan penggunaan kontrak Protocol."""
    print("\n-- Demonstrasi Protocol")

    gerobak = GerobakDorong(
        "GD-01",
        "Gerobak Dorong",
        50_000,
    )

    print(
        "Gerobak termasuk AlatTani:",
        isinstance(gerobak, AlatTani),
    )
    print(
        "Gerobak memenuhi Sewaan:",
        isinstance(gerobak, Sewaan),
    )

    daftar = DaftarHarga([traktor, gerobak])

    for biaya in daftar.biaya_semua(3):
        print("Biaya sewa:", AlatTani.format_rupiah(biaya))

    termurah = daftar.termurah(3)
    print("Objek termurah:", termurah.nama)

    print(
        "Total seluruh sewaan:",
        AlatTani.format_rupiah(
            daftar.total_bila_semua_disewa(3)
        ),
    )


def demonstrasi_enum(
    penyewa: Penyewa,
    traktor: Traktor,
) -> None:
    """Menampilkan penggunaan Enum pada transaksi sewa."""
    print("\n-- Demonstrasi Enum")

    transaksi = Sewa("SW-009", penyewa)
    transaksi.tambah_alat(traktor, 3)

    print("Status awal:", transaksi.status.value)

    transaksi.ubah_status(StatusSewa.BERJALAN)
    print("Status sekarang:", transaksi.status.value)

    transaksi.ubah_status(StatusSewa.SELESAI)
    print("Status akhir:", transaksi.status.value)

    print("\n", transaksi.nota())

    try:
        StatusSewa("seleai")
    except ValueError as error:
        print("\nStatus tidak dikenal ditolak:")
        print(error)


def main() -> None:
    """Menjalankan seluruh demonstrasi P09."""
    penyewa = buat_penyewa()

    print("=== PRAKTIKUM P09 ===")
    print(penyewa.identitas())

    traktor = demonstrasi_abc()
    demonstrasi_protocol(traktor)
    demonstrasi_enum(penyewa, traktor)


if __name__ == "__main__":
    main()
