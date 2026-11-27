from src.model.makanan_minuman import MakananMinuman
from src.model.kebutuhan_harian import KebutuhanHarian
from src.model.metode_pembayaran import MetodePembayaran
from src.model.transaksi_kasir import TransaksiKasir
from src.model.pengeluaran_kulakan import PengeluaranKulakan
from src.model.rekap_laporan import RekapLaporan


def test_rekap_laporan_menghitung_omzet_pengeluaran_dan_laba_bersih() -> None:
    snack = MakananMinuman("MM-01", "Biskuit Kaleng", 25_000, 15, "2027-05-10")
    sabun = KebutuhanHarian("KH-01", "Sabun Mandi Cair", 20_000, 10)

    trx = TransaksiKasir("NOTA-05", "Bpk. Tri Harianto")
    trx.tambah_barang(snack, 2)
    trx.tambah_barang(sabun, 1)
    trx.bayar(MetodePembayaran.QRIS, 70_000)

    kulakan = PengeluaranKulakan("FAK-02", "Distributor Pekanbaru", 40_000)
    rekap = RekapLaporan([trx, kulakan])

    assert rekap.total_omzet() == 70_000
    assert rekap.total_pengeluaran() == 40_000
    assert rekap.keuntungan_bersih() == 30_000