
from .model.alat_tani import AlatTani
from .model.penyewa import Penyewa
from .model.petugas import Petugas


def main() -> None:
    penyewa = Penyewa("1401", "Budi", "Bangkinang")
    petugas = Petugas("Siti", "PTG001", "081234567890", "Kuok")
    alat = AlatTani("AT001", "Traktor", 150000)

    print(penyewa.identitas())
    print(petugas.informasi())
    print(alat.keterangan())
    print(f"Biaya sewa 2 hari: Rp{alat.biaya_sewa(2):,}".replace(",", "."))


if __name__ == "__main__":
    main()
