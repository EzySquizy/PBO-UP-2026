"""Hierarki eksepsi khusus untuk aturan usaha SIPALA."""


class SipalaError(Exception):
    """Induk seluruh kegagalan yang berasal dari aturan SIPALA."""


class DataTidakValid(SipalaError, ValueError):
    """Masukan tidak memenuhi bentuk yang sah."""


class TarifTidakValid(DataTidakValid):
    """Tarif di luar rentang yang wajar bagi UPJA."""


class NikTidakValid(DataTidakValid):
    """NIK tidak memenuhi format yang ditentukan."""


class HariTidakValid(DataTidakValid):
    """Jumlah hari tidak memenuhi ketentuan."""


class TeleponTidakValid(DataTidakValid):
    """Nomor telepon tidak memenuhi format yang ditentukan."""


class BarisPendataanRusak(DataTidakValid):
    """Baris pendataan tidak memiliki format yang benar."""


class AturanUsahaDilanggar(SipalaError):
    """Masukan sah, tetapi tidak diizinkan menurut aturan usaha UPJA."""


class AlatSudahAdaDalamSewa(AturanUsahaDilanggar):
    """Alat yang sama tidak boleh dimasukkan dua kali."""


class BatasAlatTerlampaui(AturanUsahaDilanggar):
    """Jumlah alat dalam satu transaksi melewati batas."""


class TransaksiTerkunci(AturanUsahaDilanggar):
    """Transaksi yang sudah selesai tidak boleh diubah."""
