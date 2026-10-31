
"""Model domain: petugas UPJA."""


class Petugas:
    """Mewakili petugas yang mengurus penyewaan alat pertanian."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama petugas tidak boleh kosong")
        if not jabatan.strip():
            raise ValueError("jabatan tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._telepon = "-"
        self.telepon = telepon

    # Baca-saja: ID melekat pada identitas petugas.
    @property
    def id_petugas(self) -> str:
        """ID petugas yang tidak dapat diubah setelah dibuat."""
        return self._id_petugas

    # Baca-saja: nama disimpan sebagai identitas petugas.
    @property
    def nama(self) -> str:
        """Nama petugas."""
        return self._nama

    # Baca-saja: jabatan tidak diubah langsung dari luar kelas.
    @property
    def jabatan(self) -> str:
        """Jabatan petugas."""
        return self._jabatan

    # Baca-tulis terjaga: nomor telepon boleh diperbarui jika sah.
    @property
    def telepon(self) -> str:
        """Nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._telepon = "-"
            return

        bersih = nilai.replace("-", "").replace(" ", "")
        if not bersih.isdigit() or len(bersih) < 10:
            raise ValueError(
                f"nomor telepon tidak sah, diterima '{nilai}'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas singkat petugas."""
        return f"{self._nama} ({self._id_petugas}) - {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
