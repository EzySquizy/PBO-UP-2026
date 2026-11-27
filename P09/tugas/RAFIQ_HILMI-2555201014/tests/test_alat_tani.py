
"""Pengujian untuk class AlatTani."""

import pytest
from src.model.alat_tani import AlatTani


class AlatTaniUji(AlatTani):
    """Kelas konkret untuk menguji AlatTani."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        return 0

    def syarat_pemakaian(self) -> str:
        return "Tidak ada syarat khusus."

def test_membuat_alat_tani() -> None:
    alat = AlatTaniUji("AT-01", "Alat Pertanian", 50_000)
    assert alat.kode == "AT-01"
    assert alat.nama == "Alat Pertanian"
    assert alat.tarif_harian == 50_000


def test_kode_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("", "Alat Pertanian", 50_000)


def test_nama_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("AT-01", "", 50_000)


def test_tarif_minimum_diterima() -> None:
    alat = AlatTaniUji("AT-01", "Alat", AlatTani.TARIF_MINIMUM)
    assert alat.tarif_harian == AlatTani.TARIF_MINIMUM


def test_tarif_maksimum_diterima() -> None:
    alat = AlatTaniUji("AT-01", "Alat", AlatTani.TARIF_MAKSIMUM)
    assert alat.tarif_harian == AlatTani.TARIF_MAKSIMUM


def test_tarif_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("AT-01", "Alat", 9_000)


def test_tarif_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("AT-01", "Alat", 5_000_001)


def test_mengubah_tarif() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 50_000)
    alat.tarif_harian = 75_000
    assert alat.tarif_harian == 75_000


def test_tarif_wajar() -> None:
    assert AlatTani.tarif_wajar(50_000) is True


def test_tarif_tidak_wajar() -> None:
    assert AlatTani.tarif_wajar(5_000) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_biaya_sewa() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 50_000)
    assert alat.biaya_sewa(3) == 150_000


def test_denda_keterlambatan() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 100_000)
    assert alat.denda_keterlambatan(2) == 20_000


def test_denda_nol_hari() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 100_000)
    assert alat.denda_keterlambatan(0) == 0


def test_denda_hari_minus_ditolak() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 100_000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)


def test_keterangan_alat() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 50_000)
    assert alat.keterangan() == "[AT-01] Alat — Rp50.000/hari"


def test_str_alat() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 50_000)
    assert str(alat) == alat.keterangan()


def test_repr_alat() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 50_000)
    assert "AlatTani" in repr(alat)


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    pertama = AlatTaniUji("AT-01", "Alat A", 50_000)
    kedua = AlatTaniUji("AT-01", "Alat B", 75_000)
    assert pertama == kedua


def test_dua_alat_dengan_kode_berbeda_tidak_sama() -> None:
    pertama = AlatTaniUji("AT-01", "Alat A", 50_000)
    kedua = AlatTaniUji("AT-02", "Alat B", 50_000)
    assert pertama != kedua


def test_hash_alat() -> None:
    alat = AlatTaniUji("AT-01", "Alat", 50_000)
    assert hash(alat) == hash("AT-01")


def test_dari_baris_csv() -> None:
    alat = AlatTaniUji.dari_baris_csv(
        "AT-01;Alat Pertanian;50000"
    )
    assert alat.kode == "AT-01"
    assert alat.nama == "Alat Pertanian"
    assert alat.tarif_harian == 50_000


def test_csv_dengan_jumlah_bagian_salah() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji.dari_baris_csv("AT-01;Alat")


def test_csv_dengan_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji.dari_baris_csv("AT-01;Alat;mahal")


def test_jumlah_terdaftar() -> None:
    sebelum = AlatTani.jumlah_terdaftar()
    AlatTaniUji("AT-99", "Alat Baru", 50_000)
    assert AlatTani.jumlah_terdaftar() == sebelum + 1
