
"""Pengujian penerjemah perintah konsol."""

from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import proses_perintah


def buat_daftar() -> DaftarHarga:
    """Membuat daftar alat untuk pengujian."""
    return DaftarHarga(
        [
            Traktor("TR-01", "Traktor", 150_000, 20),
            PompaAir("PA-01", "Pompa Air", 100_000, 100),
            Perontok("PR-01", "Perontok", 200_000),
        ]
    )


def test_perintah_kosong() -> None:
    """Perintah kosong ditolak."""
    assert proses_perintah("", buat_daftar()) == (
        "Perintah tidak boleh kosong."
    )


def test_perintah_bantuan() -> None:
    """Perintah bantuan menampilkan daftar perintah."""
    hasil = proses_perintah("bantuan", buat_daftar())
    assert "Perintah tersedia" in hasil


def test_perintah_tanda_tanya() -> None:
    """Tanda tanya juga menampilkan bantuan."""
    hasil = proses_perintah("?", buat_daftar())
    assert "Perintah tersedia" in hasil


def test_perintah_daftar() -> None:
    """Perintah daftar menampilkan biaya semua alat."""
    hasil = proses_perintah("daftar 3", buat_daftar())
    assert hasil == "Rp750.000\nRp363.000\nRp600.000"


def test_perintah_daftar_hari_tidak_valid() -> None:
    """Jumlah hari harus berupa angka."""
    hasil = proses_perintah("daftar tiga", buat_daftar())
    assert hasil == "Perintah tidak dikenal: daftar"


def test_perintah_harga() -> None:
    """Perintah harga menampilkan biaya alat berdasarkan kode."""
    hasil = proses_perintah("harga TR-01 3", buat_daftar())
    assert hasil == "Rp750.000"


def test_perintah_harga_kode_tidak_ditemukan() -> None:
    """Kode alat yang tidak tersedia ditolak."""
    hasil = proses_perintah("harga XX-01 3", buat_daftar())
    assert hasil == "Alat dengan kode XX-01 tidak ditemukan."


def test_perintah_harga_hari_tidak_valid() -> None:
    """Jumlah hari harus berupa angka."""
    hasil = proses_perintah("harga TR-01 tiga", buat_daftar())
    assert hasil == "Perintah tidak dikenal: harga"


def test_perintah_termurah() -> None:
    """Perintah termurah menampilkan nama alat termurah."""
    hasil = proses_perintah("termurah 3", buat_daftar())
    assert hasil == "Alat termurah: Pompa Air"


def test_perintah_termurah_hari_tidak_valid() -> None:
    """Jumlah hari harus berupa angka."""
    hasil = proses_perintah("termurah tiga", buat_daftar())
    assert hasil == "Perintah tidak dikenal: termurah"


def test_perintah_tidak_dikenal() -> None:
    """Perintah yang tidak tersedia ditolak."""
    hasil = proses_perintah("hapus", buat_daftar())
    assert hasil == "Perintah tidak dikenal: hapus"


def test_perintah_dengan_spasi() -> None:
    """Spasi di awal dan akhir perintah diabaikan."""
    hasil = proses_perintah("  termurah 3  ", buat_daftar())
    assert hasil == "Alat termurah: Pompa Air"


def test_perintah_format_tidak_valid() -> None:
    """Format perintah yang tidak sesuai ditolak."""
    hasil = proses_perintah("harga", buat_daftar())
    assert hasil == "Perintah tidak dikenal: harga"


def test_perintah_daftar_tanpa_jumlah_hari() -> None:
    """Perintah daftar harus menyertakan jumlah hari."""
    hasil = proses_perintah("daftar", buat_daftar())
    assert hasil == "Perintah tidak dikenal: daftar"


def test_perintah_keluar_tidak_dikenal() -> None:
    """Perintah keluar belum tersedia."""
    assert proses_perintah("keluar", buat_daftar()) == (
        "Perintah tidak dikenal: keluar"
    )


def test_perintah_simpan_tidak_dikenal() -> None:
    """Perintah simpan belum tersedia."""
    assert proses_perintah("simpan", buat_daftar()) == (
        "Perintah tidak dikenal: simpan"
    )


def test_perintah_cetak_tidak_dikenal() -> None:
    """Perintah cetak belum tersedia."""
    assert proses_perintah("cetak", buat_daftar()) == (
        "Perintah tidak dikenal: cetak"
    )


def test_perintah_xyz_tidak_dikenal() -> None:
    """Perintah acak tidak dikenali."""
    assert proses_perintah("xyz", buat_daftar()) == (
        "Perintah tidak dikenal: xyz"
    )
