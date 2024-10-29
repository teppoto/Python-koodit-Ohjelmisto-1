import random

class Auto:
    def __init__(self, nimi, huippunopeus):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kulje(self):
        self.matka += self.nopeus

    def muuta_nopeutta(self):
        muutos = random.randint(-10, 15)
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.muuta_nopeutta()
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        print("-" * 45)
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.matka:<15}")
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

if __name__ == "__main__":
    autot = [
        Auto("Auto 1", 180),
        Auto("Auto 2", 200),
        Auto("Auto 3", 190),
        Auto("Auto 4", 175),
        Auto("Auto 5", 165),
        Auto("Auto 6", 195),
        Auto("Auto 7", 180),
        Auto("Auto 8", 170),
        Auto("Auto 9", 160),
        Auto("Auto 10", 200)
    ]

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1

        if tunti % 10 == 0:
            print(f"Tunnin {tunti} tilanne:")
            kilpailu.tulosta_tilanne()

    print("Kilpailu päättyi! Lopputilanne:")
    kilpailu.tulosta_tilanne()