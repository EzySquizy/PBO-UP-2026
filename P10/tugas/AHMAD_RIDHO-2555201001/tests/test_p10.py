
"""Pengujian hierarki eksepsi dan transaksi P10."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.galat import (
    AlatSudahAdaDalamSewa,
    AturanUsahaDilanggar,
    BarisPendataanRusak,
    BatasAlatTerlampaui,
    DataTidakValid,
    HariTidakValid,
    NikTidakValid,
    SipalaError,
    TarifTidakValid,
    TeleponTidakValid,
    TransaksiTerkunci,
)
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.status_sewa import StatusSewa


class AlatTaniUji(AlatTani):
    """Implementasi konkret sederhana untuk pengujian P10."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        return 0

    def syarat_pemakaian(self) -> str:
        return "Tidak ada syarat khusus."


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Kampung Baru", "Penyasawan", "Kampar")
    return Penyewa("1401011234567890", "Budi", alamat)


def test_dua_cabang_dapat_dipisahkan_saat_ditangkap() -> None:
    assert issubclass(DataTidakValid, SipalaError)
    assert issubclass(DataTidakValid, ValueError)
    assert issubclass(TarifTidakValid, DataTidakValid)
    assert issubclass(NikTidakValid, DataTidakValid)
    assert issubclass(HariTidakValid, DataTidakValid)
    assert issubclass(TeleponTidakValid, DataTidakValid)
    assert issubclass(BarisPendataanRusak, DataTidakValid)

    assert issubclass(AturanUsahaDilanggar, SipalaError)
    assert issubclass(AlatSudahAdaDalamSewa, AturanUsahaDilanggar)
    assert issubclass(BatasAlatTerlampaui, AturanUsahaDilanggar)
    assert issubclass(TransaksiTerkunci, AturanUsahaDilanggar)

    assert issubclass(TarifTidakValid, ValueError) is True
    assert issubclass(TransaksiTerkunci, ValueError) is False

    with pytest.raises(DataTidakValid):
        AlatTani.baca_rupiah("bukan angka")

    sewa = Sewa("SW-001", buat_penyewa())
    alat = AlatTaniUji("TR-01", "Traktor", 150_000)
    sewa.tambah_alat(alat, 2)

    try:
        sewa.tambah_alat(alat, 2)
    except DataTidakValid:
        pytest.fail("Kesalahan aturan usaha tidak boleh menjadi DataTidakValid.")
    except AturanUsahaDilanggar:
        pass
    else:
        pytest.fail("Seharusnya terjadi pelanggaran aturan usaha.")


def test_baca_rupiah_gagal_menyimpan_penyebab_aslinya() -> None:
    with pytest.raises(TarifTidakValid) as hasil:
        AlatTani.baca_rupiah("bukan angka")

    assert isinstance(hasil.value.__cause__, ValueError)


def test_transaksi_gagal_dibatalkan_seluruhnya() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    alat_pertama = AlatTaniUji("TR-01", "Traktor", 150_000)
    alat_kedua = AlatTaniUji("PA-01", "Pompa Air", 100_000)

    with pytest.raises(AlatSudahAdaDalamSewa), sewa.transaksi():
        sewa.tambah_alat(alat_pertama, 2)
        sewa.tambah_alat(alat_kedua, 2)
        sewa.tambah_alat(alat_pertama, 2)

    assert len(sewa.baris) == 0


def test_batas_maksimal_sepuluh_jenis_alat() -> None:
    sewa = Sewa("SW-002", buat_penyewa())

    for nomor in range(10):
        alat = AlatTaniUji(
            f"TR-{nomor:02d}",
            f"Alat {nomor}",
            100_000,
        )
        sewa.tambah_alat(alat, 2)

    alat_ke_sebelas = AlatTaniUji("TR-10", "Alat 10", 100_000)

    with pytest.raises(BatasAlatTerlampaui):
        sewa.tambah_alat(alat_ke_sebelas, 2)

    assert len(sewa.baris) == 10


def test_status_selesai_tidak_boleh_diubah() -> None:
    sewa = Sewa("SW-003", buat_penyewa())

    sewa.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(TransaksiTerkunci):
        sewa.ubah_status(StatusSewa.BATAL)

    assert sewa.status == StatusSewa.SELESAI
