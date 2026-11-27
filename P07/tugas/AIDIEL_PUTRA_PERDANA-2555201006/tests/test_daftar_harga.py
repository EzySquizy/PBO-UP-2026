import pytest

from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def _contoh_alat() -> list[AlatTani]:
    return [
        Traktor("TR-01", "Traktor Roda Dua Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air 3 Inci", 75_000, 600),
        Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900),
    ]


def test_daftar_kosong_menimbulkan_value_error() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_salinan_daftar_tidak_bocor_ke_luar() -> None:
    sumber = _contoh_alat()
    daftar = DaftarHarga(sumber)
    sumber.clear()

    assert len(daftar.biaya_semua(1)) == 3


def test_biaya_semua_dan_total_sewa() -> None:
    daftar = DaftarHarga(_contoh_alat())

    hasil = daftar.biaya_semua(3)
    assert hasil == [
        ("Traktor Roda Dua Kubota", 750_000),
        ("Pompa Air 3 Inci", 603_000),
        ("Mesin Perontok Padi", 600_000),
    ]
    assert daftar.total_bila_semua_disewa(3) == 1_953_000


def test_termurah_berubah_untuk_jangka_waktu_berbeda() -> None:
    daftar = DaftarHarga(_contoh_alat())

    assert daftar.termurah(1).kode == "PA-01"
    assert daftar.termurah(3).kode == "PR-01"


def test_alat_jenis_baru_langsung_ikut_terhitung() -> None:
    """Menambah jenis alat tidak menuntut perubahan pada DaftarHarga."""

    class Penggiling(AlatTani):
        """Jenis alat keempat yang dibuat khusus untuk pengujian ini."""

        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + 25_000

    tambahan = Penggiling("PG-01", "Penggiling", 100_000)
    daftar = DaftarHarga([*_contoh_alat(), tambahan])

    assert len(daftar.biaya_semua(1)) == 4
    assert daftar.total_bila_semua_disewa(1) == (
        250_000 + 201_000 + 400_000 + 125_000
    )


def test_biaya_sewa_1_hari_semua_alat() -> None:
    daftar = DaftarHarga(_contoh_alat())

    assert daftar.biaya_semua(1) == [
        ("Traktor Roda Dua Kubota", 250_000),
        ("Pompa Air 3 Inci", 201_000),
        ("Mesin Perontok Padi", 400_000),
    ]
    assert daftar.total_bila_semua_disewa(1) == 851_000


def test_termurah_mengembalikan_objek_alat_tani() -> None:
    daftar = DaftarHarga(_contoh_alat())

    alat_murah = daftar.termurah(1)
    assert isinstance(alat_murah, AlatTani)
    assert alat_murah.nama == "Pompa Air 3 Inci"