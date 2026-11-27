
from src.model.status_sewa import StatusSewa
"""Pengujian untuk kelas Sewa."""

import pytest

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok


class AlatUji(AlatTani):
    """Kelas konkret untuk membantu pengujian Sewa."""

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        return 0

    def syarat_pemakaian(self) -> str:
        return "Tidak ada syarat khusus."


def buat_penyewa() -> Penyewa:
    alamat = Alamat(
        dusun="Pulau Belimbing",
        desa="Kuok",
        kecamatan="Kuok",
    )
    return Penyewa(
        nik="0000000000000000",
        nama="Budi Santoso",
        alamat=alamat,
    )


def buat_alat(kode: str = "TR-01") -> AlatTani:
    return AlatUji(
        kode=kode,
        nama=f"Alat {kode}",
        tarif_harian=150_000,
    )


def test_sewa_menyimpan_penyewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)

    assert sewa.penyewa is penyewa


def test_baris_sewa_tidak_dapat_diubah_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)

    assert isinstance(sewa.baris, tuple)
    assert len(sewa.baris) == 1


def test_tambah_alat_menghitung_total() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 3)

    assert sewa.total() == 450_000


def test_alat_yang_sama_tidak_boleh_ditambahkan_dua_kali() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    alat = buat_alat()

    sewa.tambah_alat(alat, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 3)


def test_maksimal_sepuluh_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    for nomor in range(10):
        sewa.tambah_alat(buat_alat(f"TR-{nomor:02d}"), 1)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat("TR-10"), 1)


def test_nota_menggunakan_snapshot_tarif() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    alat = buat_alat()

    sewa.tambah_alat(alat, 2)
    alat.tarif_harian = 200_000

    assert "Rp150.000" in sewa.nota()
    assert "Rp300.000" in sewa.nota()


def test_nomor_sewa_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())


def test_sewa_menghitung_biaya_traktor() -> None:
    sewa = Sewa("SW-TR", buat_penyewa())
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 8)

    sewa.tambah_alat(alat, 2)

    assert sewa.total() == 500_000


def test_sewa_menghitung_biaya_pompa_air() -> None:
    sewa = Sewa("SW-PA", buat_penyewa())
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)

    sewa.tambah_alat(alat, 3)

    assert sewa.total() == 603_000


def test_sewa_menghitung_minimum_biaya_perontok() -> None:
    sewa = Sewa("SW-PR", buat_penyewa())
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)

    sewa.tambah_alat(alat, 1)

    assert sewa.total() == 400_000


def test_sewa_menggabungkan_beberapa_jenis_alat() -> None:
    sewa = Sewa("SW-ALL", buat_penyewa())

    sewa.tambah_alat(
        Traktor("TR-01", "Traktor Kubota", 150_000, 8), 2
    )
    sewa.tambah_alat(
        PompaAir("PA-01", "Pompa Air", 75_000, 600), 3
    )
    sewa.tambah_alat(
        Perontok("PR-01", "Mesin Perontok", 200_000, 900), 1
    )

    assert sewa.total() == 1_503_000


def test_pompa_dari_baris_csv_valid() -> None:
    alat = PompaAir.dari_baris_csv(
        "PA-02;Pompa Air Diesel;75000;600"
    )

    assert alat.kode == "PA-02"
    assert alat.nama == "Pompa Air Diesel"
    assert alat.tarif_harian == 75_000
    assert alat.debit == 600


def test_pompa_dari_baris_csv_kolom_kurang() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA-02;Pompa Air;75000")


def test_pompa_dari_baris_csv_debit_bukan_angka() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv(
            "PA-02;Pompa Air;75000;besar"
        )


def test_perontok_dari_baris_csv_valid() -> None:
    alat = Perontok.dari_baris_csv(
        "PR-02;Mesin Perontok;200000;900"
    )

    assert alat.kode == "PR-02"
    assert alat.nama == "Mesin Perontok"
    assert alat.tarif_harian == 200_000
    assert alat.kapasitas == 900


def test_perontok_dari_baris_csv_kolom_kurang() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR-02;Mesin Perontok;200000")


def test_perontok_dari_baris_csv_kapasitas_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv(
            "PR-02;Mesin Perontok;200000;besar"
        )
def test_status_awal_sewa_adalah_dibuat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    assert sewa.status is StatusSewa.DIBUAT


def test_status_sewa_dapat_diubah() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    sewa.ubah_status(StatusSewa.BERJALAN)

    assert sewa.status is StatusSewa.BERJALAN


def test_status_sewa_menolak_nilai_tidak_valid() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    with pytest.raises(ValueError):
        sewa.ubah_status("selesai")  # type: ignore[arg-type]


def test_sewa_selesai_menolak_penambahan_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat(), 1)


def test_sewa_dibatalkan_menolak_penambahan_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.ubah_status(StatusSewa.DIBATALKAN)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat(), 1)


def test_keterangan_status_sewa() -> None:
    assert StatusSewa.DIBUAT.keterangan() == (
        "Transaksi telah dibuat."
    )