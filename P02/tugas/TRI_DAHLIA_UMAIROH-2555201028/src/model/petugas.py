"""Model domain: petugas UPJA yang melayani penyewaan."""


class Petugas:
    """Mewakili petugas UPJA."""

    def __init__(
        self,
        nama: str,
        id_petugas: str,
        no_hp: str,
        wilayah: str,
        status: str = "Aktif",
    ) -> None:
        self._nama = nama
        self._id_petugas = id_petugas
        self._no_hp = no_hp
        self._wilayah = wilayah
        self._status = status

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def id_petugas(self) -> str:
        return self._id_petugas

    @property
    def no_hp(self) -> str:
        return self._no_hp

    @property
    def wilayah(self) -> str:
        return self._wilayah

    @property
    def status(self) -> str:
        return self._status

    def informasi(self) -> str:
        """Mengembalikan informasi singkat petugas."""
        return f"{self._nama} ({self._id_petugas}) - {self._wilayah}"

    def aktif(self) -> bool:
        """Mengembalikan status aktif petugas."""
        return self._status == "Aktif"
