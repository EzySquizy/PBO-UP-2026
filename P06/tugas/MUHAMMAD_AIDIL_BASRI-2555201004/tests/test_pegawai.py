"""Pengujian hierarki dan overriding kelas Pegawai."""

import pytest
from src.model.pegawai import (
    Pegawai,
    PegawaiHarian,
    PegawaiProduksi,
    PegawaiTetap,
)


def test_pegawai_menyimpan_identitas() -> None:
    pegawai = Pegawai("198701012010011001", "Budi", 100_000)

    assert pegawai.nip == "198701012010011001"
    assert pegawai.nama == "Budi"
    assert pegawai.upah_harian == 100_000


def test_pegawai_menolak_nip_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Budi", 100_000)


def test_pegawai_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("198701012010011001", " ", 100_000)


def test_pegawai_menolak_upah_nol() -> None:
    with pytest.raises(ValueError):
        Pegawai("198701012010011001", "Budi", 0)


def test_pegawai_menghitung_penghasilan_dasar() -> None:
    pegawai = Pegawai("198701012010011001", "Budi", 100_000)

    assert pegawai.hitung_penghasilan(5) == 500_000


def test_pegawai_menolak_jumlah_hari_nol() -> None:
    pegawai = Pegawai("198701012010011001", "Budi", 100_000)

    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(0)


def test_pegawai_menghasilkan_str() -> None:
    pegawai = Pegawai("198701012010011001", "Budi", 100_000)

    assert str(pegawai) == "198701012010011001 - Budi"


def test_pegawai_repr_memuat_nama_kelas() -> None:
    pegawai = Pegawai("198701012010011001", "Budi", 100_000)

    assert repr(pegawai).startswith("Pegawai(")


def test_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pegawai1 = Pegawai("198701012010011001", "Budi", 100_000)
    pegawai2 = Pegawai("198701012010011001", "Budi Baru", 150_000)

    assert pegawai1 == pegawai2
    assert hash(pegawai1) == hash(pegawai2)


def test_pegawai_dapat_digunakan_sebagai_kunci_dict() -> None:
    pegawai = Pegawai("198701012010011001", "Budi", 100_000)
    data = {pegawai: "Aktif"}

    assert data[pegawai] == "Aktif"


def test_pegawai_tetap_menambahkan_tunjangan() -> None:
    pegawai = PegawaiTetap(
        "198701012010011002", "Siti", 100_000, 20_000
    )

    assert pegawai.hitung_penghasilan(5) == 600_000


def test_pegawai_tetap_menolak_tunjangan_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap(
            "198701012010011002", "Siti", 100_000, -20_000
        )


def test_pegawai_produksi_menghitung_upah_produksi() -> None:
    pegawai = PegawaiProduksi(
        "198701012010011003", "Andi", 100_000, 10, 2_000
    )

    assert pegawai.hitung_penghasilan(5) == 600_000


def test_pegawai_produksi_menolak_unit_nol() -> None:
    with pytest.raises(ValueError):
        PegawaiProduksi(
            "198701012010011003", "Andi", 100_000, 0, 2_000
        )


def test_pegawai_produksi_menolak_upah_per_unit_nol() -> None:
    with pytest.raises(ValueError):
        PegawaiProduksi(
            "198701012010011003", "Andi", 100_000, 10, 0
        )


def test_pegawai_harian_mengurangi_hari_tidak_hadir() -> None:
    pegawai = PegawaiHarian(
        "198701012010011004", "Rina", 100_000, 1
    )

    assert pegawai.hitung_penghasilan(5) == 400_000


def test_pegawai_harian_menolak_hari_tidak_hadir_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian(
            "198701012010011004", "Rina", 100_000, -1
        )


def test_pegawai_harian_menolak_semua_hari_tidak_dibayar() -> None:
    pegawai = PegawaiHarian(
        "198701012010011004", "Rina", 100_000, 5
    )

    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(5)
