
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat = Alamat(
        dusun="Kampung Baru",
        desa="Penyasawan",
        kecamatan="Kampar",
    )

    alat = AlatTani(
        kode="TR-01",
        nama="Traktor Roda Dua Kubota",
        tarif_harian=150_000,
    )

    penyewa = Penyewa(
        nik="1234567890123456",
        nama="Budi Santoso",
        alamat=alamat,
        telepon="081234567890",
    )

    print("--- Data Penyewa ---")
    print(penyewa.identitas())
    print(f"Alamat lengkap: {alamat.lengkap()}")
    print(f"Alat: [{alat.kode}] {alat.nama}")
    print(
        f"Tarif: {AlatTani.format_rupiah(alat.tarif_harian)}/hari"
    )

    print("\n--- Percobaan menembus penjagaan ---")
    for tarif in (0, -5000, 6_000_000):
        try:
            alat.tarif_harian = tarif
        except ValueError as error:
            print(f"Ditolak (tarif {tarif}): {error}")

    print(
        f"Tarif tetap utuh: [{alat.kode}] {alat.nama} "
        f"— {AlatTani.format_rupiah(alat.tarif_harian)}/hari"
    )

    print("\n--- Fitur P04 ---")
    print(f"Jumlah alat terdaftar: {AlatTani.jumlah_terdaftar()}")
    print(
        "Denda keterlambatan 2 hari: "
        f"{AlatTani.format_rupiah(alat.denda_keterlambatan(2))}"
    )

    alat_baru = AlatTani.dari_baris_csv("TR-02;Cultivator;200000")
    print(
        f"Alat dari baris: [{alat_baru.kode}] {alat_baru.nama} "
        f"— {AlatTani.format_rupiah(alat_baru.tarif_harian)}/hari"
    )
    print(f"Tarif Rp150.000 wajar: {AlatTani.tarif_wajar(150_000)}")


if __name__ == "__main__":
    main()
