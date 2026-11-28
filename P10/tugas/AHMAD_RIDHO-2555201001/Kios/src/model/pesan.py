
from src.model.errors import (
    FormatBarisTidakValid,
    HargaBukanAngka,
    HargaJualDiAtasMaksimum,
    HargaJualDiBawahMinimum,
    HargaJualTidakWajar,
    KodeProdukTidakValid,
    ModalTidakValid,
    NamaProdukTidakValid,
)


def terjemahkan_eksepsi(kesalahan: Exception) -> str:
    """Mengubah eksepsi menjadi pesan yang mudah dipahami pemilik kios."""
    try:
        raise kesalahan
    except KodeProdukTidakValid:
        return "Pendaftaran gagal: kode produk belum diisi."
    except NamaProdukTidakValid:
        return "Pendaftaran gagal: nama produk belum diisi."
    except FormatBarisTidakValid:
        return "Pendaftaran gagal: data harus terdiri dari empat kolom."
    except HargaBukanAngka:
        return "Pendaftaran gagal: harga harus diisi menggunakan angka."
    except ModalTidakValid:
        return "Pendaftaran gagal: harga modal harus lebih dari nol."
    except HargaJualDiBawahMinimum:
        return "Pendaftaran gagal: harga jual di bawah batas minimum."
    except HargaJualDiAtasMaksimum:
        return "Pendaftaran gagal: harga jual melebihi batas maksimum."
    except HargaJualTidakWajar:
        return "Pendaftaran gagal: harga jual belum memenuhi margin minimum."
    except Exception:
        return "Terjadi kesalahan yang tidak dapat diproses."
