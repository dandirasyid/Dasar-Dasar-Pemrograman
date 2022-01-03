class SegitigaSiku2:
    alas = 0
    tinggi = 0
    sisi1 = 0
    sisi2 = 0

    def __init__(self):
        print("="*10, "Segitiga Siku-siku", 10*"=")
        self.alas = int(input("Masukkan Alas Segitiga Siku-siku: "))
        self.tinggi = int(input("Masukkan Tinggi Segitiga Siku-siku: "))

    def hasil(self):
        l = 0.5 * self.alas * self.tinggi
        k = self.alas + self.sisi1 + self.sisi2

        print("===== Segitiga ======"
              "\nPanjang: ", self.alas,
              "\nLebar: ", self.tinggi,
              "\nLuas: ", l,
              "\nKeliling: ", k,
              "\n==========================="
              "\n")
