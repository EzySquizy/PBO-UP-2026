"""Kesalahan yang disengaja nomor 2: urutan except dari umum ke khusus.

Cabang yang lebih umum ditulis lebih dulu, sehingga cabang khusus di
bawahnya tidak pernah tercapai. Python tidak memberi peringatan apa pun,
dan pesan yang sampai ke pengurus UPJA menjadi keliru.
"""

import sys

sys.path.insert(0, "kode")

from src.model.galat import (      # noqa: E402
    AturanUsahaDilanggar,
    DataTidakValid,
    SipalaError,
    TarifTidakValid,
    TransaksiTerkunci,
)


def tangani_cara_buruk(galat: SipalaError) -> str:
    """Urutan cabangnya terbalik: yang umum ditulis lebih dulu."""
    try:
        raise galat
    except SipalaError:
        return "Terjadi kesalahan pada sistem. Hubungi pengurus."
    except TarifTidakValid:
        return "Tarif tidak wajar. Silakan periksa kembali angkanya."
    except TransaksiTerkunci:
        return "Transaksi ini sudah ditutup dan tidak dapat diubah."


def tangani_cara_benar(galat: SipalaError) -> str:
    """Urutan dari yang paling khusus ke yang paling umum."""
    try:
        raise galat
    except TarifTidakValid:
        return "Tarif tidak wajar. Silakan periksa kembali angkanya."
    except TransaksiTerkunci:
        return "Transaksi ini sudah ditutup dan tidak dapat diubah."
    except DataTidakValid:
        return "Ada masukan yang tidak sah. Silakan ketik ulang."
    except AturanUsahaDilanggar:
        return "Tindakan itu tidak diizinkan menurut aturan UPJA."


def main() -> None:
    contoh = [
        TarifTidakValid("tarif -5000 di luar rentang"),
        TransaksiTerkunci("transaksi berstatus selesai"),
    ]
    print(f"{'Galat':<22}{'cara buruk':<46}cara benar")
    print("-" * 118)
    for galat in contoh:
        nama = type(galat).__name__
        print(f"{nama:<22}{tangani_cara_buruk(galat):<46}{tangani_cara_benar(galat)}")
    print()
    print("Cabang khusus tidak pernah tercapai, karena cabang umum menangkapnya lebih dulu.")
    print("Python tidak memberi peringatan apa pun.")


if __name__ == "__main__":
    main()
