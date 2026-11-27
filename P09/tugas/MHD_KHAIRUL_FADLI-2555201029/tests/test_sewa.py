
"""Pengujian untuk kelas Sewa dan StatusSewa."""

import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa, StatusSewa


class AlatUji(AlatTani):
    """Alat konkret khusus untuk pengujian transaksi."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Menghitung biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan."""
        return "Untuk keperluan pengujian."


def buat_penyewa() -> Penyewa:
    """Membuat objek penyewa untuk pengujian."""
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa("1406012509900001", "Budi Santoso", alamat)


def test_sewa_menyimpan_nomor_transaksi() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert sewa.nomor == "SW001"


def test_sewa_menyimpan_objek_penyewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW001", penyewa)

    assert sewa.penyewa is penyewa


def test_nomor_sewa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa(" ", buat_penyewa())


def test_baris_awalnya_kosong() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert sewa.baris == ()


def test_tambah_alat_membuat_baris_sewa() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert len(sewa.baris) == 1
    assert isinstance(sewa.baris[0], BarisSewa)


def test_tambah_alat_menyimpan_objek_yang_benar() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert sewa.baris[0].alat is alat


def test_tambah_alat_menyimpan_jumlah_hari() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 4)

    assert sewa.baris[0].jumlah_hari == 4


def test_total_satu_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)

    assert sewa.total() == 450_000


def test_total_beberapa_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    traktor = AlatUji("AT001", "Traktor", 150_000)
    pompa = AlatUji("AT002", "Pompa", 50_000)

    sewa.tambah_alat(traktor, 2)
    sewa.tambah_alat(pompa, 3)

    assert sewa.total() == 450_000


def test_alat_dengan_kode_sama_ditolak() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat1 = AlatUji("AT001", "Traktor", 150_000)
    alat2 = AlatUji("AT001", "Traktor Baru", 175_000)

    sewa.tambah_alat(alat1, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat2, 2)


def test_maksimal_sepuluh_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    for nomor in range(10):
        alat = AlatUji(
            f"AT{nomor:03}",
            f"Alat {nomor}",
            100_000,
        )
        sewa.tambah_alat(alat, 1)

    assert len(sewa.baris) == 10


def test_alat_ke_sebelas_ditolak() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    for nomor in range(10):
        alat = AlatUji(
            f"AT{nomor:03}",
            f"Alat {nomor}",
            100_000,
        )
        sewa.tambah_alat(alat, 1)

    alat_baru = AlatUji("AT010", "Alat Baru", 100_000)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat_baru, 1)


def test_baris_berupa_tuple() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert isinstance(sewa.baris, tuple)


def test_baris_tidak_bisa_diubah_dari_luar() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]


def test_penyewa_tetap_ada_setelah_referensi_sewa_dihapus() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW001", penyewa)

    del sewa

    assert penyewa.nik == "1406012509900001"


def test_nota_memuat_nomor_transaksi() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert "SW001" in sewa.nota()


def test_nota_memuat_identitas_penyewa() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert "Budi Santoso" in sewa.nota()


def test_nota_memuat_nama_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    assert "Traktor" in sewa.nota()


def test_nota_memuat_total_pembayaran() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 2)

    assert "Rp300.000" in sewa.nota()


def test_total_tidak_berubah_setelah_tarif_alat_diubah() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    alat = AlatUji("AT001", "Traktor", 150_000)

    sewa.tambah_alat(alat, 3)
    alat.tarif_harian = 175_000

    assert sewa.total() == 450_000


# Pengujian StatusSewa


def test_status_awal_sewa_adalah_dipesan() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    assert sewa.status == StatusSewa.DIPESAN


def test_status_dipesan_boleh_diubah() -> None:
    assert StatusSewa.DIPESAN.boleh_diubah()


def test_status_berjalan_boleh_diubah() -> None:
    assert StatusSewa.BERJALAN.boleh_diubah()


def test_status_selesai_tidak_boleh_diubah() -> None:
    assert not StatusSewa.SELESAI.boleh_diubah()


def test_status_batal_tidak_boleh_diubah() -> None:
    assert not StatusSewa.BATAL.boleh_diubah()


def test_sewa_dapat_mengubah_status() -> None:
    sewa = Sewa("SW001", buat_penyewa())

    sewa.ubah_status(StatusSewa.BERJALAN)

    assert sewa.status == StatusSewa.BERJALAN


def test_sewa_selesai_menolak_penambahan_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    sewa.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(ValueError):
        sewa.tambah_alat(
            AlatUji("AT001", "Traktor", 150_000),
            2,
        )


def test_sewa_batal_menolak_penambahan_alat() -> None:
    sewa = Sewa("SW001", buat_penyewa())
    sewa.ubah_status(StatusSewa.BATAL)

    with pytest.raises(ValueError):
        sewa.tambah_alat(
            AlatUji("AT001", "Traktor", 150_000),
            2,
        )


def test_enum_menolak_status_tidak_dikenal() -> None:
    with pytest.raises(ValueError):
        StatusSewa("seleai")

