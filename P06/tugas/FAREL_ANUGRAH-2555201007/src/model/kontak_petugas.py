"""Objek nilai untuk menyimpan kontak petugas."""

from dataclasses import dataclass


@dataclass(frozen=True)
class KontakPetugas:
    """Informasi kontak petugas yang tidak dapat diubah."""

    email: str
    alamat_kantor: str

    def __post_init__(self) -> None:
        if "@" not in self.email:
            raise ValueError("Email petugas tidak valid")

        if not self.alamat_kantor.strip():
            raise ValueError("Alamat kantor tidak boleh kosong")

    # Property untuk membaca email petugas.
    @property
    def email_lengkap(self) -> str:
        return self.email

    # Property untuk membaca alamat kantor.
    @property
    def lokasi_kantor(self) -> str:
        return self.alamat_kantor
