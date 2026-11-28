
"""Hierarki eksepsi untuk pengelolaan data dan aturan bisnis kios."""


class KesalahanKiosError(Exception):
    """Induk seluruh kesalahan yang berasal dari aturan Kios."""


class KesalahanDataError(KesalahanKiosError, ValueError):
    """Induk eksepsi untuk kesalahan data masukan."""


class KesalahanAturanBisnis(KesalahanKiosError):
    """Induk eksepsi untuk pelanggaran aturan bisnis kios."""


class KodeProdukTidakValid(KesalahanDataError):
    """Kode produk kosong atau tidak valid."""


class NamaProdukTidakValid(KesalahanDataError):
    """Nama produk kosong atau tidak valid."""


class FormatBarisTidakValid(KesalahanDataError):
    """Format baris data produk tidak sesuai."""


class HargaBukanAngka(KesalahanDataError):
    """Harga produk tidak dapat dikonversi menjadi angka."""


class ModalTidakValid(KesalahanAturanBisnis):
    """Harga modal tidak memenuhi aturan bisnis."""


class HargaJualTidakWajar(KesalahanAturanBisnis):
    """Harga jual tidak memenuhi ketentuan margin."""


class HargaJualDiBawahMinimum(KesalahanAturanBisnis):
    """Harga jual berada di bawah batas minimum."""


class HargaJualDiAtasMaksimum(KesalahanAturanBisnis):
    """Harga jual melebihi batas maksimum."""
