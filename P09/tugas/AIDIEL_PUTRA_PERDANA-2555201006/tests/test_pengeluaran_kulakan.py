import pytest
from src.model.barang import Barang
from src.model.pengeluaran_kulakan import PengeluaranKulakan
from src.model.rekap_laporan import CatatanKeuangan


def test_pengeluaran_kulakan_memenuhi_protocol_bukan_turunan_barang() -> None:
    kulakan = PengeluaranKulakan("FAK-01", "Agen Sembako Bangkinang", 250_000)
    assert isinstance(kulakan, CatatanKeuangan)
    assert not isinstance(kulakan, Barang)
    assert kulakan.nominal_pemasukan() == 0
    assert kulakan.nominal_pengeluaran() == 250_000


def test_pengeluaran_kulakan_menolak_biaya_tidak_valid() -> None:
    with pytest.raises(ValueError):
        PengeluaranKulakan("FAK-02", "Distributor Pekanbaru", 0)