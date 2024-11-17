import random

class Auto:
    def __init__(self, rek, huippunopeus):
        self.rek = rek
        self.huippunopeus = huippunopeus
        self.nyknopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nyknopeus += muutos
        if self.nyknopeus > self.huippunopeus:
            self.nyknopeus = self.huippunopeus
        elif self.nyknopeus < 0:
            self.nyknopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nyknopeus

autolista = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i}", huippunopeus)
    autolista.append(auto)

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autolista:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteri':<10} {'Huippunopeus (km/h)':<20} {'Nykyinen nopeus (km/h)':<25} {'Matka (km)':<15}")
print("=" * 70)
for auto in autolista:
    print(f"{auto.rek:<10} {auto.huippunopeus:<20} {auto.nyknopeus:<25} {auto.matka:<15.2f}")
