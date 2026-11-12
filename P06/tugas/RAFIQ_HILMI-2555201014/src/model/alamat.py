
"""Model nilai untuk menyimpan alamat penyewa."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Alamat yang nilainya tidak dapat diubah setelah dibuat."""

    dusun: str
    desa: str
    kecamatan: str

    def __post_init__(self) -> None:
        """Memastikan desa dan kecamatan tidak kosong."""
        if not self.desa.strip():
            raise ValueError("Desa tidak boleh kosong.")
        if not self.kecamatan.strip():
            raise ValueError("Kecamatan tidak boleh kosong.")

    def lengkap(self) -> str:
        """Mengembalikan alamat lengkap dalam satu baris."""
        return f"Dusun {self.dusun}, Desa {self.desa}, Kec. {self.kecamatan}"

    def singkat(self) -> str:
        """Mengembalikan alamat singkat."""
        return f"{self.desa}, {self.kecamatan}"
