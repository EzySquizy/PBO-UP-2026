"""Pengujian untuk kelas Petugas."""
from src.model.petugas import Petugas


def test_info_petugas() -> None:
    petugas = Petugas("P-01", "Farel", "Administrator", True)
    assert "Farel" in petugas.info_petugas()
    assert "Administrator" in petugas.info_petugas()


def test_tugas_pelayanan() -> None:
    petugas = Petugas("P-02", "Islami", "Kasir")
    hasil = petugas.tugas_pelayanan(5)
    assert "5" in hasil
    assert "Islami" in hasil


def test_dua_objek_petugas_punya_data_sendiri() -> None:
    p1 = Petugas("P-01", "Farel", "Admin")
    p2 = Petugas("P-02", "Islami", "Kasir")
    assert p1.info_petugas() != p2.info_petugas()


def test_status_aktif_default() -> None:
    petugas = Petugas("P-03", "Muhammad", "Lapangan")
    assert petugas.status_aktif is True