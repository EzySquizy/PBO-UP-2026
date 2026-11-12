
import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def buat_alamat() -> Alamat:
    return Alamat("Kampung Baru", "Penyasawan", "Kampar")


def buat_alat() -> AlatTani:
    return AlatTani("TR-01", "Traktor", 150_000)


def buat_penyewa() -> Penyewa:
    return Penyewa(
        "1234567890123456",
        "Budi Santoso",
        buat_alamat(),
        "081234567890",
    )


def test_alamat_lengkap() -> None:
    assert "Dusun Kampung Baru" in buat_alamat().lengkap()


def test_alamat_singkat() -> None:
    assert buat_alamat().singkat() == "Penyasawan, Kampar"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Kampung Baru", " ", "Kampar")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Kampung Baru", "Penyasawan", " ")


def test_alamat_tidak_bisa_diubah() -> None:
    with pytest.raises(AttributeError):
        buat_alamat().desa = "Desa Baru"  # type: ignore[misc]


def test_tarif_awal() -> None:
    assert buat_alat().tarif_harian == 150_000


def test_tarif_bisa_diubah() -> None:
    alat = buat_alat()
    alat.tarif_harian = 200_000
    assert alat.tarif_harian == 200_000


def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150_000)


def test_nama_alat_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", " ", 150_000)


def test_kode_hanya_bisa_dibaca() -> None:
    with pytest.raises(AttributeError):
        buat_alat().kode = "TR-02"  # type: ignore[misc]


def test_nik_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("123", "Budi", buat_alamat(), "081234567890")


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        buat_penyewa().telepon = "abc"


def test_identitas_penyewa() -> None:
    assert "Budi Santoso" in buat_penyewa().identitas()

def test_konstanta_kelas() -> None:
    assert AlatTani.TARIF_MINIMUM == 10_000
    assert AlatTani.TARIF_MAKSIMUM == 5_000_000
    assert AlatTani.PERSEN_DENDA_HARIAN == 10
    assert AlatTani.PEMISAH_BARIS == ";"


def test_tarif_wajar() -> None:
    assert AlatTani.tarif_wajar(10_000)
    assert AlatTani.tarif_wajar(150_000)
    assert AlatTani.tarif_wajar(5_000_000)


def test_tarif_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 9_999)


def test_tarif_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_jumlah_terdaftar_bertambah() -> None:
    sebelum = AlatTani.jumlah_terdaftar()
    AlatTani("TR-99", "Alat Uji", 100_000)
    assert AlatTani.jumlah_terdaftar() == sebelum + 1


def test_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv("TR-02;Cultivator;200000")
    assert alat.kode == "TR-02"
    assert alat.nama == "Cultivator"
    assert alat.tarif_harian == 200_000


def test_baris_csv_tidak_lengkap_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-02;Cultivator")


def test_tarif_csv_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-02;Cultivator;mahal")


def test_denda_keterlambatan() -> None:
    alat = buat_alat()
    assert alat.denda_keterlambatan(2) == 30_000


def test_hari_terlambat_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        buat_alat().denda_keterlambatan(-1)
