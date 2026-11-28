from src.model.errors import (
    KesalahanAturanBisnis,
    KesalahanDataError,
    KesalahanKiosError,
)


def test_cabang_data_dapat_ditangkap_sebagai_value_error() -> None:
    assert issubclass(KesalahanDataError, KesalahanKiosError)
    assert issubclass(KesalahanDataError, ValueError)


def test_cabang_bisnis_terpisah_dari_value_error() -> None:
    assert issubclass(KesalahanAturanBisnis, KesalahanKiosError)
    assert not issubclass(KesalahanAturanBisnis, ValueError)
