from dataclasses import dataclass


@dataclass(frozen=True)
class IdentitasPetugas:
    """Value object beku untuk identitas kontak petugas."""

    email: str

    def __post_init__(self) -> None:
        if "@" not in self.email:
            raise ValueError("email tidak valid")


class Petugas:
    """Mewakili petugas dengan data yang dijaga melalui enkapsulasi."""

    def __init__(
        self,
        kode: str,
        nama: str,
        identitas: IdentitasPetugas,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode tidak boleh kosong")

        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._identitas = identitas

        # Setter dipanggil dari konstruktor agar validasi tetap diterapkan.
        self.status = "Aktif"

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def identitas(self) -> IdentitasPetugas:
        return self._identitas

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, nilai: str) -> None:
        if nilai not in {"Aktif", "Nonaktif"}:
            raise ValueError("status harus Aktif atau Nonaktif")

        self._status = nilai