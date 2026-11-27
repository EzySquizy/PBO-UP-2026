
"""Model pegawai struktural."""

from .pegawai import Pegawai


class PegawaiStruktural(Pegawai):
    """Pegawai struktural dengan penyesuaian hari kerja."""

    TAMBAHAN_HARI_KERJA: int = 2

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tingkat_jabatan: str,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if not tingkat_jabatan.strip():
            raise ValueError("tingkat jabatan tidak boleh kosong")

        self._tingkat_jabatan = tingkat_jabatan.strip()

    @property
    def tingkat_jabatan(self) -> str:
        """Mengembalikan tingkat jabatan struktural."""
        return self._tingkat_jabatan

    def hitung_penghasilan(self, hari_kerja: int) -> int:
        """Menambahkan hari kerja sebelum meneruskan ke induk."""
        hari_disetarakan = hari_kerja + self.TAMBAHAN_HARI_KERJA
        return super().hitung_penghasilan(hari_disetarakan)
