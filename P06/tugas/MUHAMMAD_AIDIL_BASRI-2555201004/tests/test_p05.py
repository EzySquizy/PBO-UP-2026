"""Pengujian model SIPALA P05: validasi, perhitungan, dan relasi."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_alamat() -> Alamat:
    return Alamat("Pulau Jambu", "Kuok", "Kampar")


def buat_penyewa() -> Penyewa:
    return Penyewa("1406012509900001", "Budi Santoso", buat_alamat())


def buat_alat(kode: str = "TR-01", tarif: int = 150_000) -> AlatTani:
    return AlatTani(kode, "Traktor", tarif)


# Alamat: validasi, enkapsulasi, dan representasi


def test_alamat_menyimpan_jalan() -> None:
    assert buat_alamat().jalan == "Pulau Jambu"


def test_alamat_menyimpan_kelurahan() -> None:
    assert buat_alamat().kelurahan == "Kuok"


def test_alamat_menyimpan_kota() -> None:
    assert buat_alamat().kota == "Kampar"


def test_alamat_membersihkan_spasi() -> None:
    assert Alamat(" Jalan A ", " Desa B ", " Kota C ").jalan == "Jalan A"


def test_alamat_menolak_jalan_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat(" ", "Kuok", "Kampar")


def test_alamat_menolak_kelurahan_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Jalan", " ", "Kampar")


def test_alamat_menolak_kota_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Jalan", "Kuok", " ")


def test_alamat_lengkap() -> None:
    assert buat_alamat().lengkap() == "Pulau Jambu, Kuok, Kampar"


# AlatTani: validasi dan method kelas


def test_alat_menyimpan_kode() -> None:
    assert buat_alat().kode == "TR-01"


def test_alat_menyimpan_nama() -> None:
    assert buat_alat().nama == "Traktor"


def test_alat_menyimpan_tarif() -> None:
    assert buat_alat().tarif_harian == 150_000


def test_alat_menolak_kode_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTani(" ", "Traktor", 150_000)


def test_alat_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-02", " ", 150_000)


def test_alat_menolak_tarif_di_bawah_minimum() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-03", "Traktor", 9_999)


def test_alat_menolak_tarif_di_atas_maksimum() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-04", "Traktor", 5_000_001)


def test_alat_menerima_tarif_minimum() -> None:
    assert buat_alat("TR-05", AlatTani.TARIF_MINIMUM).tarif_harian == 10_000


def test_alat_menerima_tarif_maksimum() -> None:
    assert buat_alat("TR-06", AlatTani.TARIF_MAKSIMUM).tarif_harian == 5_000_000


def test_alat_tarif_wajar() -> None:
    assert AlatTani.tarif_wajar(100_000) is True


def test_alat_tarif_tidak_wajar() -> None:
    assert AlatTani.tarif_wajar(1) is False


def test_alat_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_alat_biaya_sewa() -> None:
    assert buat_alat().biaya_sewa(3) == 450_000


def test_alat_biaya_sewa_menolak_nol_hari() -> None:
    with pytest.raises(ValueError):
        buat_alat().biaya_sewa(0)


def test_alat_keterangan() -> None:
    assert "[TR-01] Traktor" in buat_alat().keterangan()


# Penyewa dan asosiasi Penyewa—Sewa


def test_penyewa_menyimpan_nik() -> None:
    assert buat_penyewa().nik == "1406012509900001"


def test_penyewa_menyimpan_nama() -> None:
    assert buat_penyewa().nama == "Budi Santoso"


def test_penyewa_menolak_nik_kosong() -> None:
    with pytest.raises(ValueError):
        Penyewa(" ", "Budi", buat_alamat())


def test_penyewa_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Penyewa("123", " ", buat_alamat())


def test_penyewa_memiliki_alamat_sebagai_komposisi() -> None:
    alamat = buat_alamat()
    penyewa = Penyewa("123", "Budi", alamat)
    assert penyewa.alamat is alamat


def test_penyewa_identitas() -> None:
    assert buat_penyewa().identitas() == "Budi Santoso (1406012509900001)"


def test_penyewa_kontak() -> None:
    assert "Pulau Jambu" in buat_penyewa().kontak()


def test_asosiasi_penyewa_tetap_ada_setelah_sewa_dihapus() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-01", penyewa)
    del sewa
    assert penyewa.nama == "Budi Santoso"


# BarisSewa dan agregasi BarisSewa—AlatTani


def test_baris_menyimpan_referensi_alat() -> None:
    alat = buat_alat()
    assert BarisSewa(alat, 2).alat is alat


def test_baris_menyimpan_jumlah_hari() -> None:
    assert BarisSewa(buat_alat(), 2).jumlah_hari == 2


def test_baris_menyimpan_sal_in_kode() -> None:
    assert BarisSewa(buat_alat(), 2).kode_alat == "TR-01"


def test_baris_menyimpan_sal_in_nama() -> None:
    assert BarisSewa(buat_alat(), 2).nama_alat == "Traktor"


def test_baris_menyimpan_tarif_saat_transaksi() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 2)
    alat.tarif_harian = 200_000
    assert baris.tarif_saat_sewa == 150_000


def test_baris_subtotal_menggunakan_tarif_salinan() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)
    alat.tarif_harian = 200_000
    assert baris.subtotal() == 450_000


def test_baris_menolak_jumlah_hari_nol() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_baris_menolak_jumlah_hari_minus() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), -1)


def test_baris_nota_memuat_nama_alat() -> None:
    assert "Traktor" in BarisSewa(buat_alat(), 2).baris_nota()


# Sewa, komposisi Sewa—BarisSewa, batas dan nota


def test_sewa_menyimpan_nomor() -> None:
    assert Sewa("SW-01", buat_penyewa()).nomor == "SW-01"


def test_sewa_menyimpan_penyewa() -> None:
    penyewa = buat_penyewa()
    assert Sewa("SW-02", penyewa).penyewa is penyewa


def test_sewa_menolak_nomor_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa(" ", buat_penyewa())


def test_sewa_awalnya_kosong() -> None:
    assert Sewa("SW-03", buat_penyewa()).jumlah_alat() == 0


def test_sewa_menambahkan_alat() -> None:
    sewa = Sewa("SW-04", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert sewa.jumlah_alat() == 1


def test_sewa_membuat_baris_sewa_di_dalamnya() -> None:
    sewa = Sewa("SW-05", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert isinstance(sewa.baris[0], BarisSewa)


def test_sewa_baris_berupa_tuple() -> None:
    assert isinstance(Sewa("SW-06", buat_penyewa()).baris, tuple)


def test_komposisi_baris_tidak_bisa_diubah_dari_luar() -> None:
    sewa = Sewa("SW-07", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]
    assert sewa.jumlah_alat() == 1


def test_sewa_menolak_alat_duplikat() -> None:
    sewa = Sewa("SW-08", buat_penyewa())
    alat = buat_alat()
    sewa.tambah_alat(alat, 1)
    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 2)


def test_sewa_menolak_alat_ke_sebelas() -> None:
    sewa = Sewa("SW-09", buat_penyewa())
    for i in range(10):
        sewa.tambah_alat(AlatTani(f"TR-{i:02}", f"Alat {i}", 100_000), 1)
    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat("TR-99"), 1)


def test_sewa_menerima_sepuluh_alat() -> None:
    sewa = Sewa("SW-10", buat_penyewa())
    for i in range(10):
        sewa.tambah_alat(AlatTani(f"PA-{i:02}", f"Pompa {i}", 100_000), 1)
    assert sewa.jumlah_alat() == 10


def test_sewa_menghitung_total() -> None:
    sewa = Sewa("SW-11", buat_penyewa())
    sewa.tambah_alat(buat_alat("TR-11", 150_000), 2)
    sewa.tambah_alat(buat_alat("TR-12", 50_000), 3)
    assert sewa.total() == 450_000


def test_sewa_total_kosong_nol() -> None:
    assert Sewa("SW-12", buat_penyewa()).total() == 0


def test_nota_memuat_nomor_sewa() -> None:
    assert "SW-13" in Sewa("SW-13", buat_penyewa()).nota()


def test_nota_memuat_identitas_penyewa() -> None:
    assert "Budi Santoso" in Sewa("SW-14", buat_penyewa()).nota()


def test_nota_memuat_total() -> None:
    sewa = Sewa("SW-15", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert "Rp300.000" in sewa.nota()


def test_nota_menggunakan_tarif_historis() -> None:
    alat = buat_alat()
    sewa = Sewa("SW-16", buat_penyewa())
    sewa.tambah_alat(alat, 2)
    alat.tarif_harian = 200_000
    assert "Rp300.000" in sewa.nota()
