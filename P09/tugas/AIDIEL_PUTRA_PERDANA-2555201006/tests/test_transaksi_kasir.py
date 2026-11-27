import pytest
from src.model.barang import Barang
from src.model.sembako import Sembako
from src.model.metode_pembayaran import MetodePembayaran
from src.model.transaksi_kasir import TransaksiKasir
from src.model.rekap_laporan import CatatanKeuangan


def test_transaksi_kasir_memenuhi_protocol_bukan_turunan_barang() -> None:
    trx = TransaksiKasir("NOTA-01", "Ibu Susi Zelvianti")
    assert isinstance(trx, CatatanKeuangan)
    assert not isinstance(trx, Barang)


def test_pembayaran_cash_dan_qris_serta_kunci_harga_historis() -> None:
    minyak = Sembako("SB-02", "Minyak Goreng 1L", 18_000, 20)
    trx = TransaksiKasir("NOTA-02", "Fitri Nabila")
    trx.tambah_barang(minyak, 2)

    minyak.harga_jual = 21_000
    assert trx.total_belanja() == 36_000
    assert trx.bayar(MetodePembayaran.CASH, 50_000) == 14_000

    with pytest.raises(ValueError):
        trx.tambah_barang(minyak, 1)