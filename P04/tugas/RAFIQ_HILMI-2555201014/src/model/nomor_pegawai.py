
"""Objek nilai untuk menyimpan nomor identitas petugas."""

from dataclasses import dataclass


@dataclass(frozen=True)
class NomorPegawai:
    """Nomor identitas petugas yang tidak dapat diubah setelah dibuat."""

    nilai: str

    def __post_init__(self) -> None:
        """Menolak nomor pegawai yang kosong atau hanya berisi spasi."""
        if not self.nilai.strip():
            raise ValueError("Nomor pegawai tidak boleh kosong.")
