pegawai1 = "Ahmad"
agama = "Islam"
gajipokok1 = 4000000
anak1 = 2
tunjanganjabatan = 0.2 * gajipokok1

if (anak1 <= 2):
    tunjangankeluarga = 0.10 * gajipokok1
elif (anak1 >= 2):
    tunjangankeluarga = 0.2 * gajipokok1
else:
    tunjangankeluarga = 0

gajikotor = gajipokok1 + tunjanganjabatan + tunjangankeluarga
# pake tuple
zakatprofesi = (0, 0.025)[agama == "Islam" and gajikotor >= 6000000]

gajibersih = gajikotor + zakatprofesi

print("Slip Gaji PT. Dandi Cerdas Indonesia"
      "\n------------------------------------"
      "\nNama Pegawai\t\t:", pegawai1,
      "\nAgama\t\t\t:", agama,
      "\nJumlah Anak\t\t:", anak1,
      "\nGaji Pokok\t\t:", "Rp.", gajipokok1,
      "\nTunjangan Jabatan\t:", "Rp.", tunjanganjabatan,
      "\nTunjangan Keluarga\t:", "Rp.", tunjangankeluarga,
      "\nGaji Kotor\t\t:", "Rp.", gajikotor,
      "\nZakat Profesi\t\t:", "Rp.", zakatprofesi,
      "\nTake Home Pay\t\t:", "Rp.", gajibersih,
      "\n"
      )

pegawai2 = "Alex"
agama = "Kristen Protestan"
gajipokok2 = 6000000
anak2 = 5
tunjanganjabatan = 0.2 * gajipokok2

if (anak2 <= 2):
    tunjangankeluarga = 0.10 * gajipokok2
elif (anak2 >= 2):
    tunjangankeluarga = 0.2 * gajipokok2
else:
    tunjangankeluarga = 0

gajikotor = gajipokok2 + tunjanganjabatan + tunjangankeluarga
# pake tuple
zakatprofesi = (0, 0.025)[agama == "Islam" and gajikotor >= 6000000]
gajibersih = gajikotor - zakatprofesi

print("Slip Gaji PT. Dandi Cerdas Indonesia"
      "\n------------------------------------"
      "\nNama Pegawai\t\t:", pegawai2,
      "\nAgama\t\t\t:", agama,
      "\nJumlah Anak\t\t:", anak2,
      "\nGaji Pokok\t\t:", "Rp.", gajipokok2,
      "\nTunjangan Jabatan\t:", "Rp.", tunjanganjabatan,
      "\nTunjangan Keluarga\t:", "Rp.", tunjangankeluarga,
      "\nGaji Kotor\t\t:", "Rp.", gajikotor,
      "\nZakat Profesi\t\t:", "Rp.", zakatprofesi,
      "\nTake Home Pay\t\t:", "Rp.", gajibersih
      )
