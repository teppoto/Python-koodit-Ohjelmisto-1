class Julkaisu:

    julkaisujen_lukumaara = 0

    def __init__(self, nimi):
        Julkaisu.julkaisujen_lukumaara += 1
        self.julkaisumaara = Julkaisu.julkaisujen_lukumaara
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.julkaisumaara} {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.kirjoittaja} {self.sivumaara}")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.paatoimittaja}")

julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6", "Rosa", "200"))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for j in julkaisut:
    j.tulosta_tiedot()
