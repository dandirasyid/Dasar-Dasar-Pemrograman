class PersegiPanjang:
    panjang = 0
    lebar = 0

    def __init__(self):
        print("="*10, "Persegi Panjang", 10*"=")
        self.panjang = int(input("Masukkan Panjang Persegi Panjang: "))
        self.lebar = int(input("Masukkan Lebar Persegi Panjang: "))

    def hasil(self):
        l = self.panjang * self.lebar
        k = 2 * (self.panjang + self.lebar)

        print("===== Persegi Panjang ======"
              "\nPanjang: ", self.panjang,
              "\nLebar: ", self.lebar,
              "\nLuas: ", l,
              "\nKeliling: ", k,
              "\n==========================="
              "\n")
