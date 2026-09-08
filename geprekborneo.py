print("selamat datang di perpustakaan teknik")
buku = (
    "Tips mengerjakan 5 laprak dalam semalam",
    "trik cepat kaya ala yahudi",
    "cara profit modal seribu",
    "Resep bebek madu khas ngawi",
    "Trik UTBK SNBT 2045 auto jadi generasi emas",
    "modal jualan bubur bisa naik haji",
    "mekanika mesin dasar",
    "Amalkan bacaan ini saat utbk, Rektor gelisah ingin menerimamu",
    "memasak nasi goreng tanpa nasi",
    "dasar dasar python")
pinjaman = []
print("\nDAFTAR BUKU")
for i in range(10):
    print(i + 1, buku[i])

while True:
    print("\nMenu Layanan")
    print("1. Pinjam Buku")
    print("2. Hapus Buku")
    print("3. Ubah Pinjaman Buku")
    print("4. Selesai")
    pilih = input("Pilih: ")
    if pilih == "1":
        nomor = int(input("Nomor buku: "))
        if nomor >= 1 and nomor <= 10:
            pinjaman.append(buku[nomor - 1])
            print("Buku berhasil dipinjam")
        else:
            print("Buku tidak tersedia")
    elif pilih == "2":
        print("Pinjaman:", pinjaman)
        nomor = int(input("Nomor pinjaman yang dihapus: "))
        if nomor >= 1 and nomor <= len(pinjaman):
            pinjaman.pop(nomor - 1)
            print("Buku berhasil dihapus")
    elif pilih == "3":
        print("Pinjaman:", pinjaman)
        nomor = int(input("Nomor pinjaman yang diubah: "))
        buku_baru = int(input("Nomor buku baru: "))
        if nomor >= 1 and nomor <= len(pinjaman) and buku_baru >= 1 and buku_baru <= 10:
            pinjaman[nomor - 1] = buku[buku_baru - 1]
            print("Buku berhasil diubah")
    elif pilih == "4":
        break
print("\nBUKU YANG DIPINJAM PETER:")
for x in pinjaman:
    print("-", x)
