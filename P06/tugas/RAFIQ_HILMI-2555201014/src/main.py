
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewa import Sewa
from src.model.traktor import Traktor


def main() -> None:
    alamat = Alamat("Dusun I", "Kuok", "Kuok")
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat,
    )

    traktor = Traktor(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
        8,
    )

    pompa = PompaAir(
        "PA-01",
        "Pompa Air 3 Inci",
        75_000,
        600,
    )

    perontok = Perontok(
        "PR-01",
        "Mesin Perontok Padi",
        200_000,
        900,
    )

    sewa = Sewa("SW-2026-001", penyewa)
    sewa.tambah_alat(traktor, 3)
    sewa.tambah_alat(pompa, 5)
    sewa.tambah_alat(perontok, 1)

    print(sewa.nota())


if __name__ == "__main__":
    main()
