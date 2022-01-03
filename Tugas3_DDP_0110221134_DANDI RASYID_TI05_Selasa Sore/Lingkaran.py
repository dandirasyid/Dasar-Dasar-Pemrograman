class Lingkaran:
    jari2 = 0

    def __init__(self):
        print("="*10, "Lingkaran", 10*"=")
        self.jari2 = int(input("Masukkan Jari-jari Lingkaran: "))

    def hasil(self):
        if(self.jari2 > 0):
            k = 2 * 3.14 * self.jari2
            l = 3.14 * self.jari2 * self.jari2

        print("==== Lingkaran ===="
              "\nJari2: ", self.jari2,
              "\nKeliling: ", k,
              "\nLuas: ", l,
              "\n===================="
              "\n")
