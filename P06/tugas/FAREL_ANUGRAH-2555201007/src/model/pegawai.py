"""Hierarki pegawai untuk instansi Kabupaten Kampar."""

from typing import Final


class Pegawai:
    """Kelas induk untuk seluruh jenis pegawai."""

    JUMLAH_HARI_KERJA_BULANAN: Final[int] = 22

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong.")
        if gaji_pokok < 0:
            raise ValueError("Gaji pokok tidak boleh negatif.")

        self._nip = nip
        self._nama = nama
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        """Mengembalikan NIP pegawai."""
        return self._nip

    @property
    def nama(self) -> str:
        """Mengembalikan nama pegawai."""
        return self._nama

    @property
    def gaji_pokok(self) -> int:
        """Mengembalikan gaji pokok pegawai."""
        return self._gaji_pokok

    def hitung_penghasilan(self, hari_kerja: int = 22) -> int:
        """Menghitung gaji berdasarkan jumlah hari kerja."""
        if not 0 <= hari_kerja <= self.JUMLAH_HARI_KERJA_BULANAN:
            raise ValueError("Hari kerja harus antara 0 dan 22.")

        return (
            self._gaji_pokok
            * hari_kerja
            // self.JUMLAH_HARI_KERJA_BULANAN
        )

    def __str__(self) -> str:
        """Format informasi pegawai."""
        return f"[{self._nip}] {self._nama}"

    def __repr__(self) -> str:
        """Representasi teknis pegawai."""
        return (
            f"{self.__class__.__name__}("
            f"nip={self._nip!r}, "
            f"nama={self._nama!r}, "
            f"gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Pegawai dianggap sama jika NIP-nya sama."""
        if not isinstance(other, Pegawai):
            return NotImplemented
        return self._nip == other._nip

    def __hash__(self) -> int:
        """Hash berdasarkan NIP."""
        return hash(self._nip)


class PegawaiTetap(Pegawai):
    """Pegawai tetap dengan tambahan tunjangan jabatan."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan_jabatan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tunjangan_jabatan < 0:
            raise ValueError("Tunjangan tidak boleh negatif.")

        self._tunjangan_jabatan = tunjangan_jabatan

    @property
    def tunjangan_jabatan(self) -> int:
        """Mengembalikan tunjangan jabatan."""
        return self._tunjangan_jabatan

    def hitung_penghasilan(self, hari_kerja: int = 22) -> int:
        """Menambahkan tunjangan pada gaji berdasarkan hari kerja."""
        gaji = super().hitung_penghasilan(hari_kerja)
        tunjangan = (
            self._tunjangan_jabatan
            * hari_kerja
            // self.JUMLAH_HARI_KERJA_BULANAN
        )
        return gaji + tunjangan


class PegawaiHarian(Pegawai):
    """Pegawai harian dengan penghasilan berdasarkan jam kerja."""

    def __init__(
        self,
        nip: str,
        nama: str,
        tarif_per_jam: int,
        jam_kerja_bulanan: int,
    ) -> None:
        super().__init__(nip, nama, 0)

        if tarif_per_jam <= 0:
            raise ValueError("Tarif per jam harus lebih dari nol.")
        if jam_kerja_bulanan <= 0:
            raise ValueError("Jam kerja harus lebih dari nol.")

        self._tarif_per_jam = tarif_per_jam
        self._jam_kerja_bulanan = jam_kerja_bulanan

    @property
    def tarif_per_jam(self) -> int:
        """Mengembalikan tarif per jam."""
        return self._tarif_per_jam

    @property
    def jam_kerja_bulanan(self) -> int:
        """Mengembalikan jumlah jam kerja bulanan."""
        return self._jam_kerja_bulanan

    def hitung_penghasilan(self, hari_kerja: int = 22) -> int:
        """Menghitung penghasilan dari tarif dan jam kerja."""
        if not 0 <= hari_kerja <= self.JUMLAH_HARI_KERJA_BULANAN:
            raise ValueError("Hari kerja harus antara 0 dan 22.")

        jam_kerja = (
            self._jam_kerja_bulanan
            * hari_kerja
            // self.JUMLAH_HARI_KERJA_BULANAN
        )
        return self._tarif_per_jam * jam_kerja


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan batas maksimal hari kerja bulanan."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        batas_hari_kerja: int = 22,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if not 1 <= batas_hari_kerja <= self.JUMLAH_HARI_KERJA_BULANAN:
            raise ValueError("Batas hari kerja harus antara 1 dan 22.")

        self._batas_hari_kerja = batas_hari_kerja

    @property
    def batas_hari_kerja(self) -> int:
        """Mengembalikan batas hari kerja kontrak."""
        return self._batas_hari_kerja

    def hitung_penghasilan(self, hari_kerja: int = 22) -> int:
        """Mengubah jumlah hari sebelum memanggil metode induk."""
        hari_kerja_efektif = min(hari_kerja, self._batas_hari_kerja)
        return super().hitung_penghasilan(hari_kerja_efektif)
