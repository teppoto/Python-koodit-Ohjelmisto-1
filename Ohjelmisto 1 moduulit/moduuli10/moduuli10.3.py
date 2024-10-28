class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print(f"Virhe: Kerros {kohde_kerros} ei ole sallittu.")
            return
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissi_numero + 1} kohteeseen {kohde_kerros}:")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Virhe: Hissiä {hissi_numero + 1} ei ole olemassa.")

    def palohälytys(self):
        print("\nPalohälytys! Kaikki hissit siirretään alimpaan kerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"\nSiirretään hissi {i + 1} alimpaan kerrokseen:")
            hissi.siirry_kerrokseen(self.alin_kerros)


# Pääohjelma
if __name__ == "__main__":
    talo = Talo(1, 10, 3)

    talo.aja_hissiä(0, 5)
    talo.aja_hissiä(1, 8)
    talo.aja_hissiä(2, 3)

    talo.palohälytys()