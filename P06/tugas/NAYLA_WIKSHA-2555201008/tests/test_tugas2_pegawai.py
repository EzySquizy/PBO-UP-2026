
import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap


def test_pegawai_menyimpan_identitas() -> None:
    pegawai = Pegawai("123", "Andi", "Staf", 3_000_000)

    assert pegawai.nip == "123"
    assert pegawai.nama == "Andi"
    assert pegawai.jabatan == "Staf"


def test_pegawai_menghitung_penghasilan() -> None:
    pegawai = Pegawai("123", "Andi", "Staf", 3_000_000)

    assert pegawai.hitung_penghasilan() == 3_000_000


def test_pegawai_memiliki_string() -> None:
    pegawai = Pegawai("123", "Andi", "Staf", 3_000_000)

    assert "Andi" in str(pegawai)


def test_pegawai_memiliki_repr() -> None:
    pegawai = Pegawai("123", "Andi", "Staf", 3_000_000)

    assert "Pegawai" in repr(pegawai)


def test_pegawai_sama_berdasarkan_nip() -> None:
    pertama = Pegawai("123", "Andi", "Staf", 3_000_000)
    kedua = Pegawai("123", "Budi", "Admin", 4_000_000)

    assert pertama == kedua


def test_pegawai_berbeda_nip() -> None:
    pertama = Pegawai("123", "Andi", "Staf", 3_000_000)
    kedua = Pegawai("456", "Budi", "Admin", 3_000_000)

    assert pertama != kedua


def test_pegawai_dapat_digunakan_sebagai_key_dictionary() -> None:
    pegawai = Pegawai("123", "Andi", "Staf", 3_000_000)
    data = {pegawai: "Pegawai aktif"}

    assert data[pegawai] == "Pegawai aktif"


def test_pegawai_tetap_menghitung_tunjangan() -> None:
    pegawai = PegawaiTetap(
        "123", "Andi", "Staf", 3_000_000, 500_000
    )

    assert pegawai.hitung_penghasilan() == 3_500_000


def test_pegawai_tetap_menyimpan_tunjangan() -> None:
    pegawai = PegawaiTetap(
        "123", "Andi", "Staf", 3_000_000, 500_000
    )

    assert pegawai.tunjangan == 500_000


def test_pegawai_harian_menghitung_penghasilan() -> None:
    pegawai = PegawaiHarian(
        "124", "Budi", "Petugas", 100_000, 20
    )

    assert pegawai.hitung_penghasilan() == 2_000_000


def test_pegawai_harian_menyimpan_hari_kerja() -> None:
    pegawai = PegawaiHarian(
        "124", "Budi", "Petugas", 100_000, 20
    )

    assert pegawai.hari_kerja == 20


def test_pegawai_kontrak_menyesuaikan_gaji() -> None:
    pegawai = PegawaiKontrak(
        "125", "Citra", "Administrasi", 3_000_000
    )

    assert pegawai.hitung_penghasilan() == 2_700_000


def test_pegawai_kontrak_menyimpan_persentase() -> None:
    pegawai = PegawaiKontrak(
        "125", "Citra", "Administrasi", 3_000_000
    )

    assert pegawai.persentase_gaji == 90


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Andi", "Staf", 3_000_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("123", "", "Staf", 3_000_000)


def test_jabatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("123", "Andi", "", 3_000_000)


def test_gaji_pokok_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("123", "Andi", "Staf", 0)


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("123", "Andi", "Staf", 3_000_000, -100)

