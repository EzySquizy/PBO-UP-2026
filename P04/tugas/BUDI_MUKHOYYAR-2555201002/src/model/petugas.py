"""Model domain: petugas UPJA yang melayani penyewaan."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai beku untuk rentang waktu atau hari bertugas."""
    hari_mulai: str
    hari_selesai: str

    def __post_init__(self) -> None:
        if not self.hari_mulai.strip() or not self.hari_selesai.strip():
            raise ValueError("hari mulai dan selesai tidak boleh kosong")


class Petugas:
    """Petugas UPJA yang melayani penyewaan alat pertanian."""

    def __init__(self, nama: str, jabatan: str, periode: PeriodeTugas, tarif_per_jam: int = 100000) -> None:
        if not nama.strip():
            raise ValueError("nama petugas tidak boleh kosong")

        self._nama = nama
        self._jabatan = jabatan
        self._periode = periode
        self._tarif_per_jam = 0
        self.tarif_per_jam = tarif_per_jam  # Lewat setter untuk validasi konstruktor

    @property
    def nama(self) -> str:
        """Baca-saja: Nama petugas melekat pada identitas dan tidak boleh diubah."""
        return self._nama

    @property
    def jabatan(self) -> str:
        """Baca-saja: Jabatan awal petugas disetel saat pendaftaran."""
        return self._jabatan

    @property
    def periode(self) -> PeriodeTugas:
        """Baca-saja: Periode tugas bersifat tetap dan tidak dapat diubah isinya."""
        return self._periode

    @property
    def tarif_per_jam(self) -> int:
        """Baca-tulis terjaga: Tarif per jam dapat disesuaikan dengan aturan UPJA."""
        return self._tarif_per_jam

    @tarif_per_jam.setter
    def tarif_per_jam(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError(f"tarif harus lebih dari nol, diterima {nilai}")
        if nilai > 1_000_000:
            raise ValueError(f"tarif tidak wajar, diterima {nilai}")
        self._tarif_per_jam = nilai

    def hitung_pendapatan(self, jumlah_jam: int) -> int:
        """Menghitung total pendapatan petugas berdasarkan jam kerja."""
        if jumlah_jam < 0:
            raise ValueError("jumlah jam kerja tidak boleh minus")
        return self._tarif_per_jam * jumlah_jam

    def cetak_identitas(self) -> str:
        """Mengembalikan informasi ringkas identitas dan periode petugas."""
        format_uang = "{:,.0f}".format(self._tarif_per_jam).replace(",", ".")
        return f"{self._nama} ({self._jabatan}) [{self._periode.hari_mulai} s.d {self._periode.hari_selesai}] — Tarif: Rp {format_uang}"