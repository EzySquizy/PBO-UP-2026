from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Menyimpan alamat penyewa yang bersifat tetap."""

    dusun: str
    desa: str
    kecamatan: str

    def __post_init__(self) -> None:
        """Memvalidasi desa dan kecamatan."""
        if not self.desa.strip():
            raise ValueError("Desa tidak boleh kosong")
        if not self.kecamatan.strip():
            raise ValueError("Kecamatan tidak boleh kosong")

    def lengkap(self) -> str:
        """Mengembalikan alamat lengkap."""
        return (
            f"Dusun {self.dusun}, "
            f"Desa {self.desa}, "
            f"Kecamatan {self.kecamatan}"
        )

    def singkat(self) -> str:
        """Mengembalikan alamat singkat."""
        return f"{self.desa}, {self.kecamatan}"
