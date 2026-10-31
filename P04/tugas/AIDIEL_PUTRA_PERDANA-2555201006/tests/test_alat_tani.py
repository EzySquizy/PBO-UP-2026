"""Pengujian untuk kelas AlatTani."""

import pytest
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_keterangan_format_rupiah() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua — Rp150.000/hari"


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("PA-01", "Pompa Air", 75000)
    assert alat.biaya_sewa(0) == 0


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_nol_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000


def test_tarif_tidak_wajar_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 6_000_000


def test_kode_tidak_punya_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore[misc]


def test_nama_tidak_punya_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Traktor Baru"  # type: ignore[misc]


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("   ", "Traktor", 150000)

def test_tarif_wajar_bisa_ditanya_tanpa_objek() -> None:
    assert AlatTani.tarif_wajar(150000) is True
    assert AlatTani.tarif_wajar(6_000_000) is False


def test_dari_baris_csv_berhasil_membuat_objek() -> None:
    # Menggunakan titik koma (;) sesuai PEMISAH_BARIS di model
    baris = "TR-99;Traktor Bajak;200000"
    alat = AlatTani.dari_baris_csv(baris)
    
    assert alat.kode == "TR-99"
    assert alat.nama == "Traktor Bajak"
    assert alat.tarif_harian == 200000


def test_dari_baris_csv_ditolak_jika_tarif_bukan_angka() -> None:
    baris = "PA-99;Pompa Air;Dua Ratus Ribu"
    
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv(baris)


def test_pencacah_jumlah_terdaftar_naik_saat_objek_dibuat() -> None:
    awal = AlatTani._jumlah_terdaftar
    
    _ = AlatTani("X-01", "Alat Uji 1", 100000)
    _ = AlatTani("X-02", "Alat Uji 2", 100000)
    
    assert AlatTani._jumlah_terdaftar == awal + 2