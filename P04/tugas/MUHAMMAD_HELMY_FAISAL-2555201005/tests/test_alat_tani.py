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


def test_tarif_nol_ditolak() -> None:
    """Menguji bahwa tarif 0 ditolak karena setter mengharuskan > 0."""
    with pytest.raises(ValueError):
        AlatTani("CG-01", "Cangkul", 0)


def test_keterangan_tarif_ribuan() -> None:
    alat = AlatTani("SB-01", "Mesin Babat Rumput", 15000)
    assert alat.keterangan() == "[SB-01] Mesin Babat Rumput — Rp15.000/hari"


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


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
        alat.nama = "Mesin Bajak"  # type: ignore[misc]

def test_tarif_wajar_statik_tanpa_objek() -> None:
    """Mengecek batas kewajaran tarif langsung via kelas tanpa instansiasi."""
    assert AlatTani.tarif_wajar(75000) is True
    assert AlatTani.tarif_wajar(2000) is False
    assert AlatTani.tarif_wajar(10_000_000) is False


def test_dari_baris_csv_berhasil_buat_objek() -> None:
    """Membuat objek dari teks CSV dengan pemisah titik koma."""
    teks = "MB-01;Mesin Bensin Semprot;85000"
    alat = AlatTani.dari_baris_csv(teks)

    assert alat.kode == "MB-01"
    assert alat.nama == "Mesin Bensin Semprot"
    assert alat.tarif_harian == 85000


def test_dari_baris_csv_gagal_jika_tarif_bukan_angka() -> None:
    """Memastikan CSV dengan tarif teks/bukan angka menolak dengan ValueError."""
    teks = "MB-01;Mesin Bensin Semprot;gratis"
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv(teks)


def test_jumlah_terdaftar_bertambah_sesuai_selisih() -> None:
    """Mengecek pencacah kelas bertambah saat objek baru diinisialisasi."""
    posisi_awal = AlatTani.jumlah_terdaftar()

    _ = AlatTani("TST-1", "Alat Coba A", 20000)
    _ = AlatTani("TST-2", "Alat Coba B", 30000)

    assert AlatTani.jumlah_terdaftar() == posisi_awal + 2