print("selamat datang di perpustakaan teknik")
print("list buku :")
daftar_buku = ("Mekanika Mesin",
    "buku tulis",
    "buku nikah",
    "buku yasin",
    "matematika diskrit",
    "cara kaya ala yahudi")
pinjaman = []

for buku in daftar_buku:
    print(buku)
while True:
    print("\nDAFTAR BUKU:")
    print("Menu:")
    print("1. Pinjam buku")
    print("2. Hapus pinjaman")
    print("3. Ubah pinjaman")
    print("4. Selesai")
    pilihan = input("Pilih: ")
    if pilihan == "1":
        buku = input("Masukkan judul buku: ")
        if buku in daftar_buku:
            pinjaman.append(buku)
            print("Buku berhasil dipinjam")
        else:
            print("Buku tidak tersedia")
    elif pilihan == "2":
        print("Pinjaman:", pinjaman)
        buku = input("Masukkan buku yang ingin dihapus: ")
        if buku in pinjaman:
            pinjaman.remove(buku)
            print("Buku berhasil dihapus")
        else:
            print("Buku tidak ada dalam pinjaman")
    elif pilihan == "3":
        print("Pinjaman:", pinjaman)
        buku_lama = input("Buku yang ingin diubah: ")
        buku_baru = input("Buku pengganti: ")
        if buku_lama in pinjaman and buku_baru in daftar_buku:
            posisi = pinjaman.index(buku_lama)
            pinjaman[posisi] = buku_baru
            print("Pinjaman berhasil diubah")
        else:
            print("Buku tidak tersedia")
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid")
print("BUKU YANG DIPINJAM PETER:")
for buku in pinjaman:
    print("-", buku)
