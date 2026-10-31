
from src.model.kios import Kios


def main() -> None:
    print("=== Kios Hasil Pertanian Bangkinang ===")
    print(f"Produk terdaftar sebelum pendataan: {Kios.jumlah_produk()}")

    produk_kios = [
        Kios("BR001", "Beras", 14_000, 16_000),
        Kios("GL001", "Gula pasir", 16_000, 18_000),
        Kios("MG001", "Minyak goreng", 17_000, 19_000),
    ]

    for produk in produk_kios:
        print(produk.informasi())

    print(f"Produk terdaftar sesudah pendataan: {Kios.jumlah_produk()}")

    print("\n=== Pemeriksaan Harga Jual ===")
    for modal, jual in [(14_000, 16_000), (14_000, 14_000)]:
        status = (
            "Wajar"
            if Kios.harga_jual_wajar(modal, jual)
            else "Tidak wajar"
        )
        print(f"Modal Rp{modal:,} | Jual Rp{jual:,} | {status}")


if __name__ == "__main__":
    main()
