
"""Titik masuk program P06: pewarisan alat pertanian."""

from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def main() -> None:
    """Menampilkan contoh pewarisan dan biaya sewa alat."""
    traktor = Traktor(
        kode="TR-01",
        nama="Traktor Roda Dua Kubota",
        tarif_harian=150_000,
        tenaga_kuda=15,
    )

    pompa = PompaAir(
        kode="PA-01",
        nama="Pompa Air 3 Inci",
        tarif_harian=75_000,
        debit=600,
    )

    perontok = Perontok(
        kode="PR-01",
        nama="Mesin Perontok Padi",
        tarif_harian=200_000,
        kapasitas=900,
    )

    daftar_alat: tuple[AlatTani, ...] = (
        traktor,
        pompa,
        perontok,
    )

    print("=== SISTEM INFORMASI ALAT PERTANIAN ===")
    print(
        "Jumlah alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    print("\n=== INFORMASI ALAT ===")

    for alat in daftar_alat:
        print(f"\n{alat}")
        print(f"Representasi: {alat!r}")

    print("\n=== ATRIBUT KHUSUS ===")
    print(f"Tenaga kuda traktor: {traktor.tenaga_kuda} HP")
    print(f"Debit pompa air: {pompa.debit} liter/menit")
    print(f"Kapasitas perontok: {perontok.kapasitas} kg/jam")
    print(
        "Konsumsi solar pompa: "
        f"{pompa.konsumsi_solar_harian()} liter/hari"
    )

    print("\n=== BIAYA SEWA SATU HARI ===")

    for alat in daftar_alat:
        biaya = alat.biaya_sewa(1)
        print(
            f"{alat.nama}: "
            f"{AlatTani.format_rupiah(biaya)}"
        )

    print("\n=== BIAYA SEWA TIGA HARI ===")

    for alat in daftar_alat:
        biaya = alat.biaya_sewa(3)
        print(
            f"{alat.nama}: "
            f"{AlatTani.format_rupiah(biaya)}"
        )

    print("\n=== PEMERIKSAAN PEWARISAN ===")
    for alat in daftar_alat:
        print(
            f"{alat.nama} merupakan AlatTani: "
            f"{isinstance(alat, AlatTani)}"
        )


if __name__ == "__main__":
    main()
