print("\t\t\tDandi Cerdas Elektronik",
      "\n\t\t\t-----------------------")
namapelanggan = input("Masukan nama pelanggan: ")
produk = input("Masukan nama barang: ")
if (produk == "kipas angin"):
    harga = 1000000
    print("Harga Produk: %i" % (harga))
elif (produk == "TV" or produk == "tv"):
    harga = 2000000
    print("Harga Produk: %i" % (harga))
elif (produk == "mesin cuci"):
    harga = 3000000
    print("Harga Produk: %i" % (harga))
elif (produk == "AC" or produk == "ac"):
    harga = 4000000
    print("Harga Produk: %i" % (harga))
elif (produk == "kulkas"):
    harga = 5000000
else:
    print("Tidak ada barang")
    exit()

jumlahbeli = int(input("jumlah barang:"))
hargakotor = harga * jumlahbeli

if (produk == "kulkas" and jumlahbeli >= 5):
    diskon = 0.20 * hargakotor

elif (produk == "ac" and jumlahbeli >= 3):
    diskon = 0.10 * hargakotor

else:
    diskon = 0.05 * hargakotor

ppn = hargakotor - diskon * 0.10
print("PPN: %i" % (ppn))
hargabersih = hargakotor - diskon + ppn
print("----------------------------",
      "\nDaftar Belanja")

print("Nama Pelanggan:%s" % (namapelanggan))
print("Nama Barang:%s" % (produk))
print("Harga Satuan Produk:Rp%i" % (harga))
print("Jumlah barang yang di beli: %i" % (jumlahbeli))
print("Harga bersih produk: Rp %i" % (hargakotor))
print("PPN: Rp %i " % (ppn))
print("Total Harga: Rp %i" % (hargabersih))

print("-----------------------------")
