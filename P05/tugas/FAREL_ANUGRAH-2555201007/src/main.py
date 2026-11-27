"""Titik masuk program P04: anggota kelas dan objek."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.kontak_petugas import KontakPetugas
from src.model.penyewa import Penyewa
from src.model.petugas import Petugas


def main() -> None:
    print(
        "Sebelum pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    alamat_budi = Alamat(
        dusun="Pongkai",
        desa="Kuok",
        kecamatan="Kuok",
    )
    alamat_siti = Alamat(
        dusun="Salo",
        desa="Salo",
        kecamatan="Salo",
    )

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )
    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        alamat_siti,
    )

    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
    )
    pompa = AlatTani.dari_baris_csv(
        "PA-01;Pompa Air 3 Inci;75000"
    )

    kontak_petugas = KontakPetugas(
        email="petugas@upja.id",
        alamat_kantor="Kantor UPJA Kuok",
    )

    petugas = Petugas(
        nip="198501152010011001",
        nama="Ahmad Fauzi",
        jabatan="Pengelola UPJA",
        kontak=kontak_petugas,
        telepon="081234567890",
    )

    print(budi.identitas())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())

    print(traktor.keterangan())
    print(pompa.keterangan())

    print(
        "Sesudah pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    print("\n--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = (
            "wajar"
            if AlatTani.tarif_wajar(calon)
            else "ditolak"
        )
        print(
            f"{AlatTani.format_rupiah(calon):>14}  ->  {status}"
        )

    print("\n--- Informasi petugas ---")
    print(petugas.identitas())
    print(petugas.informasi_kontak())


if __name__ == "__main__":
    main()
