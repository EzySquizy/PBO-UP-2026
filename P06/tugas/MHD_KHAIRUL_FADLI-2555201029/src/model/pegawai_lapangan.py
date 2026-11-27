
"""Model pegawai lapangan."""

from typing import Final

from .pegawai import Pegawai


class PegawaiLapangan(Pegawai):
    """Pegawai lapangan yang memperoleh tambahan uang transport."""

    TRANSPORT_PER_HARI: Final[int] = 50_000

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        uang_transport: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if uang_transport < 0:
            raise ValueError("uang transport tidak boleh negatif")

        self._uang_transport = uang_transport

    @property
    def uang_transport(self) -> int:
        """Mengembalikan uang transport per hari."""
        return self._uang_transport

    def hitung_penghasilan(self, hari_kerja: int) -> int:
        """Menambahkan komponen transport pada penghasilan."""
        penghasilan_pokok = super().hitung_penghasilan(hari_kerja)
        biaya_transport = self._uang_transport * hari_kerja

        return penghasilan_pokok + biaya_transport
