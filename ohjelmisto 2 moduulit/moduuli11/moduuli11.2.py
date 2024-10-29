
class Auto:
    def __init__(self, nimi, huippunopeus):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 100

    def kulje(self):
        self.matka += self.nopeus

class Sähköauto(Auto):

    def __init__(self, nimi, huippunopeus, akkukapasiteetti):
        super().__init__(nimi, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):

    def __init__(self, nimi, huippunopeus, bensatankki):
        super().__init__(nimi, huippunopeus)
        self.bensatankki = bensatankki

autot = []
autot.append(Sähköauto("ABC-15", "180 km/h", "52.5 kWh"))
autot.append(Polttomoottoriauto("ACD-123", "165 km/h", "32.3 l"))

tunnit = 0
while tunnit <= 4:
    for auto in autot:
        auto.kulje()
        print(f"Rekisterinumero: {auto.nimi:<15} Mittarilukema: {auto.matka:<15}")
        tunnit = tunnit + 1










