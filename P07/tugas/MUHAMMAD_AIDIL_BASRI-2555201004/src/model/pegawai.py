"""Model hierarki pegawai instansi di Kabupaten Kampar."""


class Pegawai:
    """Kelas induk untuk seluruh jenis pegawai."""

    def __init__(
        self,
        nip: str,
        nama: str,
        upah_harian: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama pegawai tidak boleh kosong")
        if upah_harian <= 0:
            raise ValueError("upah harian harus lebih dari 0")

        self._nip = nip.strip()
        self._nama = nama.strip()
        self._upah_harian = upah_harian

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def upah_harian(self) -> int:
        return self._upah_harian

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        """Menghitung penghasilan dasar berdasarkan hari kerja."""
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari kerja harus lebih dari 0")

        return self._upah_harian * jumlah_hari

    def __str__(self) -> str:
        return f"{self._nip} - {self._nama}"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"nip={self._nip!r}, "
            f"nama={self._nama!r}, "
            f"upah_harian={self._upah_harian!r})"
        )

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, Pegawai):
            return False
        return self._nip == lain._nip

    def __hash__(self) -> int:
        return hash(self._nip)


class PegawaiTetap(Pegawai):
    """Pegawai tetap yang memperoleh tambahan tunjangan harian."""

    def __init__(
        self,
        nip: str,
        nama: str,
        upah_harian: int,
        tunjangan_harian: int,
    ) -> None:
        super().__init__(nip, nama, upah_harian)

        if tunjangan_harian < 0:
            raise ValueError("tunjangan tidak boleh negatif")

        self._tunjangan_harian = tunjangan_harian

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        dasar = super().hitung_penghasilan(jumlah_hari)
        return dasar + self._tunjangan_harian * jumlah_hari


class PegawaiProduksi(Pegawai):
    """Pegawai yang memperoleh tambahan berdasarkan hasil produksi."""

    def __init__(
        self,
        nip: str,
        nama: str,
        upah_harian: int,
        unit_per_hari: int,
        upah_per_unit: int,
    ) -> None:
        super().__init__(nip, nama, upah_harian)

        if unit_per_hari <= 0:
            raise ValueError("unit produksi harus lebih dari 0")
        if upah_per_unit <= 0:
            raise ValueError("upah per unit harus lebih dari 0")

        self._unit_per_hari = unit_per_hari
        self._upah_per_unit = upah_per_unit

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        dasar = super().hitung_penghasilan(jumlah_hari)
        hasil_produksi = (
            self._unit_per_hari * self._upah_per_unit * jumlah_hari
        )
        return dasar + hasil_produksi


class PegawaiHarian(Pegawai):
    """Pegawai harian yang penghasilannya disesuaikan dengan kehadiran."""

    def __init__(
        self,
        nip: str,
        nama: str,
        upah_harian: int,
        hari_tidak_hadir: int,
    ) -> None:
        super().__init__(nip, nama, upah_harian)

        if hari_tidak_hadir < 0:
            raise ValueError("hari tidak hadir tidak boleh negatif")

        self._hari_tidak_hadir = hari_tidak_hadir

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        hari_dibayar = jumlah_hari - self._hari_tidak_hadir
        return super().hitung_penghasilan(hari_dibayar)
