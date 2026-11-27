
"""Pengujian polimorfisme pada DaftarHarga."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def buat_daftar() -> DaftarHarga:
    """Membuat daftar harga untuk pengujian."""
    return DaftarHarga(
        [
            Traktor("TR-01", "Traktor", 150_000, 20),
            PompaAir("PA-01", "Pompa Air", 100_000, 100),
            Perontok("PR-01", "Perontok", 200_000),
        ]
    )


def test_daftar_harga_menolak_daftar_kosong() -> None:
    """Daftar harga tidak boleh kosong."""
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_daftar_harga_menyalin_daftar_alat() -> None:
    """Perubahan daftar asal tidak mengubah daftar harga."""
    alat = [AlatTani("A-01", "Alat", 100_000)]
    daftar = DaftarHarga(alat)

    alat.clear()

    assert daftar.biaya_semua(2) == [200_000]


def test_biaya_semua_menggunakan_polimorfisme() -> None:
    """Setiap jenis alat menghitung biaya masing-masing."""
    daftar = buat_daftar()

    assert daftar.biaya_semua(3) == [
        750_000,
        363_000,
        600_000,
    ]


def test_total_bila_semua_disewa() -> None:
    """Total biaya semua alat dijumlahkan."""
    daftar = buat_daftar()

    assert daftar.total_bila_semua_disewa(3) == 1_713_000


def test_termurah_mengembalikan_alat_termurah() -> None:
    """Alat termurah ditentukan dari biaya sewanya."""
    daftar = buat_daftar()

    assert daftar.termurah(3).kode == "PA-01"


def test_termurah_dapat_berubah_berdasarkan_durasi() -> None:
    """Alat termurah dapat berubah sesuai lama penyewaan."""
    daftar = DaftarHarga(
        [
            AlatTani("A-01", "Alat A", 100_000),
            Perontok("PR-01", "Perontok", 200_000),
        ]
    )

    assert daftar.termurah(1).kode == "A-01"
    assert daftar.termurah(3).kode == "A-01"


def test_daftar_harga_menerima_subkelas_baru() -> None:
    """Subkelas baru dapat digunakan tanpa mengubah DaftarHarga."""

    class Penggiling(AlatTani):
        """Alat penggiling dengan ongkos angkut."""

        def biaya_sewa(self, jumlah_hari: int) -> int:
            """Menghitung biaya sewa dan ongkos angkut."""
            return super().biaya_sewa(jumlah_hari) + 50_000

    penggiling = Penggiling(
        "PG-01",
        "Penggiling Padi",
        120_000,
    )
    daftar = DaftarHarga([penggiling])

    assert daftar.biaya_semua(3) == [410_000]
    assert daftar.total_bila_semua_disewa(3) == 410_000
