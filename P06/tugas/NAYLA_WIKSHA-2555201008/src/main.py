
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewa import Sewa
from src.model.traktor import Traktor


def demo_p06() -> None:
    print("\n--- FITUR P06: PEWARISAN ---")

    traktor = Traktor("TR-02", "Traktor Kubota", 150_000, 12)
    pompa = PompaAir("PA-01", "Pompa Air Diesel", 100_000, 500)
    perontok = Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900)

    daftar_alat = [traktor, pompa, perontok]

    for item in daftar_alat:
        print(f"\nAlat: {item}")
        print(
            f"Biaya sewa 3 hari: "
            f"{AlatTani.format_rupiah(item.biaya_sewa(3))}"
        )

    print("\n--- MINIMUM SEWA PERONTOK ---")
    print(
        "Biaya sewa 1 hari: "
        f"{AlatTani.format_rupiah(perontok.biaya_sewa(1))}"
    )

    print("\n--- PERBANDINGAN OBJEK ---")
    traktor_lain = Traktor("TR-02", "Traktor Model Lain", 300_000, 15)
    print(f"Traktor sama berdasarkan kode: {traktor == traktor_lain}")
    print(f"Hash traktor: {hash(traktor)}")
    print(f"Hash traktor lain: {hash(traktor_lain)}")


def main() -> None:
    alamat = Alamat(
        dusun="Kampung Baru",
        desa="Penyasawan",
        kecamatan="Kampar",
    )

    penyewa = Penyewa(
        nik="1234567890123456",
        nama="Budi Santoso",
        alamat=alamat,
        telepon="081234567890",
    )

    alat = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150_000)

    print("--- DATA PENYEWA ---")
    print(penyewa.identitas())
    print(f"Alamat lengkap: {alamat.lengkap()}")

    print("\n--- FITUR P05: ALAT TANI ---")
    print(alat)
    print(f"Representasi: {alat!r}")

    demo_p06()

    print("\n--- FITUR P05: TRANSAKSI SEWA ---")
    alat_baru = AlatTani.dari_baris_csv("TR-03;Cultivator;200000")
    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(alat, 3)
    sewa.tambah_alat(alat_baru, 3)
    print(sewa.nota())


if __name__ == "__main__":
    main()
