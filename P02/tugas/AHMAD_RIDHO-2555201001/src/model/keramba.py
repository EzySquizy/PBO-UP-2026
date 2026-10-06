
class Keramba:
    """Mewakili keramba untuk budidaya ikan patin."""

    def __init__(
        self,
        kode: str,
        luas_m2: float,
        jumlah_benih: int,
    ) -> None:
        self._kode = kode
        self._luas_m2 = luas_m2
        self._jumlah_benih = jumlah_benih

    def estimasi_panen(
        self,
        tingkat_kelangsungan_hidup: float = 0.8,
        berat_rata_rata_kg: float = 0.5,
    ) -> float:
        return (
            self._jumlah_benih
            * tingkat_kelangsungan_hidup
            * berat_rata_rata_kg
        )
