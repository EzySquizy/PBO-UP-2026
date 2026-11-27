"""Model domain petugas UPJA."""

from typing import Final

from src.model.kontak_petugas import KontakPetugas


class Petugas:
    """Identitas petugas yang mengelola penyewaan alat pertanian."""

    PANJANG_NIP: Final[int] = 18
    PANJANG_MINIMUM_TELEPON: Final[int] = 10

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        kontak: KontakPetugas,
        telepon: str,
    ) -> None:
        if len(nip) != self.PANJANG_NIP or not nip.isdigit():
            raise ValueError("NIP harus terdiri dari 18 digit angka")

        if not nama.strip():
            raise ValueError("Nama petugas tidak boleh kosong")

        if not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong")

        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._kontak = kontak
        self._telepon = ""
        self.telepon = telepon

    # Property untuk membaca NIP tanpa mengubahnya.
    @property
    def nip(self) -> str:
        return self._nip

    # Property untuk membaca nama petugas.
    @property
    def nama(self) -> str:
        return self._nama

    # Property untuk membaca jabatan petugas.
    @property
    def jabatan(self) -> str:
        return self._jabatan

    # Property untuk membaca objek kontak petugas.
    @property
    def kontak(self) -> KontakPetugas:
        return self._kontak

    # Property untuk membaca nomor telepon.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        bersih = nilai.replace("-", "").replace(" ", "")

        if not bersih.isdigit() or len(bersih) < self.PANJANG_MINIMUM_TELEPON:
            raise ValueError("Nomor telepon petugas tidak valid")

        self._telepon = nilai

    def identitas(self) -> str:
        return f"{self._nama} ({self._nip}) - {self._jabatan}"

    def informasi_kontak(self) -> str:
        return (
            f"Telepon: {self._telepon}, "
            f"Email: {self._kontak.email_lengkap}"
        )
