"""Program utama tugas individu pewarisan pegawai."""

from src.pegawai_harian import PegawaiHarian
from src.pegawai_kontrak import PegawaiKontrak
from src.pegawai_tetap import PegawaiTetap


def main() -> None:
    pegawai_tetap = PegawaiTetap(
        "198001", "Andi", 4_000_000, 500_000
    )
    pegawai_harian = PegawaiHarian(
        "198002", "Budi", 3_000_000, 150_000
    )
    pegawai_kontrak = PegawaiKontrak(
        "198003", "Citra", 3_500_000, 6
    )

    daftar_pegawai = [
        ("Pegawai Tetap", pegawai_tetap, 1),
        ("Pegawai Harian", pegawai_harian, 20),
        ("Pegawai Kontrak", pegawai_kontrak, 6),
    ]

    for jenis, pegawai, periode in daftar_pegawai:
        penghasilan = pegawai.hitung_penghasilan(periode)
        print(f"{jenis}: {pegawai}")
        print(f"Penghasilan: Rp{penghasilan:,}".replace(",", "."))
        print("-" * 40)


if __name__ == "__main__":
    main()
