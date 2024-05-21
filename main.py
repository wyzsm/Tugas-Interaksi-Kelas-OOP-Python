class Matkul:
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.nama} ({self.sks} SKS)"


class KRS:
    def __init__(self):
        self.matkul_list = []

    def tambah_matkul(self, matkul):
        self.matkul_list.append(matkul)

    def hapus_matkul(self, nama_matkul):
        for matkul in self.matkul_list:
            if matkul.nama == nama_matkul:
                self.matkul_list.remove(matkul)
                return True
        return False

    def total_sks(self):
        return sum(matkul.sks for matkul in self.matkul_list)

    def tampilkan_krs(self):
        if not self.matkul_list:
            print("KRS masih kosong.")
        else:
            print("Daftar Mata Kuliah di KRS:")
            for matkul in self.matkul_list:
                print(f"- {matkul}")
            print(f"Total SKS: {self.total_sks()}")


def tambah_matkul_ke_krs(krs):
    nama = input("Masukkan nama mata kuliah: ")
    sks = int(input("Masukkan jumlah SKS: "))
    matkul = Matkul(nama, sks)
    krs.tambah_matkul(matkul)
    print(f"Mata kuliah {nama} berhasil ditambahkan.\n")


def hapus_matkul_dari_krs(krs):
    nama = input("Masukkan nama mata kuliah yang ingin dihapus: ")
    if krs.hapus_matkul(nama):
        print(f"Mata kuliah {nama} berhasil dihapus.\n")
    else:
        print(f"Mata kuliah {nama} tidak ditemukan dalam KRS.\n")


def main():
    krs_mahasiswa = KRS()

    while True:
        print("\nSelamat Datang di Sistem KRS. Apa yang ingin Anda lakukan?")
        print("1. Tambah Mata Kuliah")
        print("2. Hapus Mata Kuliah")
        print("3. Tampilkan KRS")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            tambah_matkul_ke_krs(krs_mahasiswa)
        elif pilihan == "2":
            hapus_matkul_dari_krs(krs_mahasiswa)
        elif pilihan == "3":
            krs_mahasiswa.tampilkan_krs()
        elif pilihan == "4":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
