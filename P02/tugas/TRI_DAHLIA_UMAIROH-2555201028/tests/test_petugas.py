from src.model.petugas import Petugas


def test_petugas_menyimpan_data() -> None:
    petugas = Petugas(
        nama="Budi Santoso",
        id_petugas="PTG001",
        no_hp="081234567890",
        wilayah="Kuok",
    )

    assert petugas.nama == "Budi Santoso"
    assert petugas.id_petugas == "PTG001"
    assert petugas.no_hp == "081234567890"
    assert petugas.wilayah == "Kuok"


def test_dua_petugas_menyimpan_data_masing_masing() -> None:
    petugas1 = Petugas(
        nama="Budi Santoso",
        id_petugas="PTG001",
        no_hp="081234567890",
        wilayah="Kuok",
    )
    petugas2 = Petugas(
        nama="Siti Aminah",
        id_petugas="PTG002",
        no_hp="082345678901",
        wilayah="Bangkinang",
    )

    assert petugas1.nama != petugas2.nama
    assert petugas1.id_petugas != petugas2.id_petugas
    assert petugas1.wilayah != petugas2.wilayah


def test_petugas_aktif_dan_informasi() -> None:
    petugas = Petugas(
        nama="Budi Santoso",
        id_petugas="PTG001",
        no_hp="081234567890",
        wilayah="Kuok",
    )

    assert petugas.aktif() is True
    assert petugas.informasi() == "Budi Santoso (PTG001) - Kuok"
