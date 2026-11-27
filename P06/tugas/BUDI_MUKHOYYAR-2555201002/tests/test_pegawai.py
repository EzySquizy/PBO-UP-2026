
import pytest

from src.model.pegawai.pegawai import Pegawai
from src.model.pegawai.pegawai_tetap import PegawaiTetap
from src.model.pegawai.pegawai_honorer import PegawaiHonorer
from src.model.pegawai.pegawai_kontrak import PegawaiKontrak


def test_pegawai_dapat_dibuat() -> None:
    pegawai = Pegawai("001", "Budi", 3000000)
    assert pegawai.nip == "001"
    assert pegawai.nama == "Budi"


def test_nip_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Budi", 3000000)


def test_nama_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "", 3000000)


def test_gaji_pokok_tidak_boleh_negatif() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "Budi", -1000)


def test_penghasilan_pegawai() -> None:
    pegawai = Pegawai("001", "Budi", 3000000)
    assert pegawai.hitung_penghasilan() == 3000000


def test_penghasilan_tidak_boleh_negatif() -> None:
    pegawai = Pegawai("001", "Budi", 3000000)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(-4000000)


def test_pegawai_tetap_menghitung_tunjangan() -> None:
    pegawai = PegawaiTetap("002", "Andi", 3000000, 500000)
    assert pegawai.hitung_penghasilan() == 3500000


def test_tunjangan_pegawai_tetap_tidak_boleh_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("002", "Andi", 3000000, -100000)


def test_pegawai_honorer_menghitung_jam_kerja() -> None:
    pegawai = PegawaiHonorer("003", "Siti", 25000, 80)
    assert pegawai.hitung_penghasilan() == 2000000


def test_tarif_honorer_harus_positif() -> None:
    with pytest.raises(ValueError):
        PegawaiHonorer("003", "Siti", 0, 80)


def test_jam_kerja_honorer_tidak_boleh_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiHonorer("003", "Siti", 25000, -5)


def test_pegawai_kontrak_menghitung_penyesuaian() -> None:
    pegawai = PegawaiKontrak("004", "Rina", 3000000, 200000)
    assert pegawai.hitung_penghasilan() == 3500000


def test_transportasi_kontrak_tidak_boleh_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiKontrak("004", "Rina", 3000000, -100000)


def test_str_pegawai() -> None:
    pegawai = Pegawai("001", "Budi", 3000000)
    assert str(pegawai) == "001 - Budi"


def test_repr_pegawai() -> None:
    pegawai = Pegawai("001", "Budi", 3000000)
    assert "Pegawai" in repr(pegawai)
    assert "001" in repr(pegawai)


def test_dua_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pegawai1 = Pegawai("001", "Budi", 3000000)
    pegawai2 = Pegawai("001", "Andi", 4000000)
    assert pegawai1 == pegawai2


def test_dua_pegawai_dengan_nip_berbeda_tidak_sama() -> None:
    pegawai1 = Pegawai("001", "Budi", 3000000)
    pegawai2 = Pegawai("002", "Andi", 4000000)
    assert pegawai1 != pegawai2


def test_pegawai_dapat_digunakan_sebagai_dictionary_key() -> None:
    pegawai = Pegawai("001", "Budi", 3000000)
    data_pegawai = {pegawai: "Pegawai tetap"}
    assert data_pegawai[pegawai] == "Pegawai tetap"
