
"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-001", "Izaz", "Operator", "Kuok")
    assert petugas.identitas() == "Izaz (PT-001) — Operator"


def test_informasi_tugas_petugas() -> None:
    petugas = Petugas("PT-001", "Izaz", "Operator", "Kuok")
    assert petugas.informasi_tugas() == "Izaz bertugas di Desa Kuok"


def test_dua_petugas_memiliki_data_sendiri() -> None:
    petugas_a = Petugas("PT-001", "Izaz", "Operator", "Kuok")
    petugas_b = Petugas("PT-002", "Reyhan", "Admin", "Salo")

    assert petugas_a.identitas() == "Izaz (PT-001) — Operator"
    assert petugas_b.identitas() == "Reyhan (PT-002) — Admin"
    assert petugas_a.informasi_tugas() != petugas_b.informasi_tugas()
