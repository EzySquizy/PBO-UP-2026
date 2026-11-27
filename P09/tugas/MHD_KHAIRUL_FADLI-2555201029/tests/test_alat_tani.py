
"""Pengujian untuk kelas abstrak AlatTani dan turunannya."""

import dataclasses

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


class AlatUji(AlatTani):
    """Implementasi konkret AlatTani khusus untuk pengujian."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Menghitung biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat pemakaian."""
        return "Untuk keperluan pengujian."


def test_alat_tani_merupakan_kelas_abstrak() -> None:
    with pytest.raises(TypeError):
        AlatTani("TR-01", "Traktor", 150_000)  # type: ignore[abstract]


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatUji("TR-01", "Traktor Roda Dua", 150_000)
    assert alat.biaya_sewa(3) == 450_000


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatUji("TR-01", "Traktor Roda Dua", 150_000)
    assert alat.biaya_sewa(1) == 150_000


def test_biaya_sewa_nol_hari_ditolak() -> None:
    alat = AlatUji("TR-01", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.biaya_sewa(0)


def test_biaya_sewa_hari_negatif_ditolak() -> None:
    alat = AlatUji("TR-01", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_keterangan_alat() -> None:
    alat = AlatUji("TR-01", "Traktor Roda Dua", 150_000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua - Rp150.000/hari"


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatUji("TR-01", "Traktor", 150_000)
    b = AlatUji("PA-01", "Pompa", 75_000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatUji("TR-01", "Traktor", -5_000)


def test_tarif_nol_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatUji("TR-01", "Traktor", 0)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatUji("TR-01", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5_000
    assert alat.tarif_harian == 150_000


def test_kode_tidak_punya_setter() -> None:
    alat = AlatUji("TR-01", "Traktor", 150_000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore[misc]


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_dari_baris_csv() -> None:
    alat = AlatUji.dari_baris_csv("TR-20;Traktor;200000")
    assert alat.kode == "TR-20"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 200_000


def test_csv_dengan_format_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatUji.dari_baris_csv("TR-20;Traktor")


def test_csv_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatUji.dari_baris_csv("TR-20;Traktor;mahal")


def test_str_alat_tani() -> None:
    alat = AlatUji("TR-40", "Traktor", 150_000)
    assert str(alat) == alat.keterangan()


def test_repr_alat_tani() -> None:
    alat = AlatUji("TR-41", "Traktor", 150_000)
    hasil = repr(alat)
    assert "AlatUji" in hasil
    assert "TR-41" in hasil


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    a = AlatUji("TR-50", "Traktor", 150_000)
    b = AlatUji("TR-50", "Traktor berbeda", 200_000)
    assert a == b


def test_dua_alat_dengan_kode_berbeda_tidak_sama() -> None:
    a = AlatUji("TR-51", "Traktor", 150_000)
    b = AlatUji("TR-52", "Traktor", 150_000)
    assert a != b


def test_alat_tani_dibandingkan_objek_lain() -> None:
    alat = AlatUji("TR-53", "Traktor", 150_000)
    assert alat != "TR-53"


def test_alat_tani_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat = AlatUji("TR-54", "Traktor", 150_000)
    data = {alat: "tersedia"}
    assert data[alat] == "tersedia"


def test_traktor_mewarisi_alat_tani() -> None:
    alat = Traktor("TR-60", "Traktor", 150_000, 20)
    assert isinstance(alat, AlatTani)


def test_traktor_menghitung_biaya_operator() -> None:
    alat = Traktor("TR-61", "Traktor", 150_000, 20)
    assert alat.biaya_sewa(3) == 750_000


def test_traktor_tenaga_kuda_tidak_valid() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-62", "Traktor", 150_000, 0)


def test_pompa_air_mewarisi_alat_tani() -> None:
    alat = PompaAir("PA-60", "Pompa Air", 100_000, 100)
    assert isinstance(alat, AlatTani)


def test_pompa_air_menghitung_konsumsi_solar() -> None:
    alat = PompaAir("PA-61", "Pompa Air", 100_000, 100)
    assert alat.konsumsi_solar_harian() == 3


def test_pompa_air_menghitung_biaya_sewa() -> None:
    alat = PompaAir("PA-62", "Pompa Air", 100_000, 100)
    assert alat.biaya_sewa(3) == 363_000


def test_pompa_air_debit_tidak_valid() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-63", "Pompa Air", 100_000, 0)


def test_perontok_mewarisi_alat_tani() -> None:
    alat = Perontok("PR-60", "Perontok", 200_000)
    assert isinstance(alat, AlatTani)


def test_perontok_minimum_ditagih_dua_hari() -> None:
    alat = Perontok("PR-61", "Perontok", 200_000)
    assert alat.biaya_sewa(1) == 400_000


def test_perontok_tiga_hari() -> None:
    alat = Perontok("PR-62", "Perontok", 200_000)
    assert alat.biaya_sewa(3) == 600_000


def test_perontok_satu_dan_dua_hari_biayanya_sama() -> None:
    satu_hari = Perontok("PR-63", "Perontok", 200_000)
    dua_hari = Perontok("PR-64", "Perontok", 200_000)
    assert satu_hari.biaya_sewa(1) == dua_hari.biaya_sewa(2)


def test_pompa_air_dari_baris_csv() -> None:
    alat = PompaAir.dari_baris_csv("PA-70;Pompa Air;100000;100")
    assert alat.kode == "PA-70"
    assert alat.nama == "Pompa Air"
    assert alat.tarif_harian == 100_000
    assert alat.debit == 100


def test_pompa_air_csv_format_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-70;Pompa Air;100000")


def test_perontok_dari_baris_csv() -> None:
    alat = Perontok.dari_baris_csv("PR-70;Mesin Perontok;200000")
    assert alat.kode == "PR-70"
    assert alat.nama == "Mesin Perontok"
    assert alat.tarif_harian == 200_000


def test_perontok_csv_format_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-70;Mesin Perontok")

