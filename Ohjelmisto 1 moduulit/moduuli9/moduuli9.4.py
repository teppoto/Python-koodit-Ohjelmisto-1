import random

class Auto:
    def __init__(self, rek, huippunopeus, nyknopeus = 0, matka = 0,):
        self.rek = rek
        self.huippunopeus = huippunopeus
        self.nyknopeus = nyknopeus
        self.matka = matka

    def kiihdytä(self, muutos):
        self.nyknopeus += muutos
        if self.nyknopeus > self.huippunopeus:
            self.nyknopeus = self.huippunopeus
        elif self.nyknopeus < 0:
            self.nyknopeus = 0
        print(f"Auton nopeus on nyt: {self.nyknopeus} km/h")

    def kulje(self,tunnit):
        self.matka += tunnit * self.nyknopeus
        print(f"Auton kuljettu matka on nyt: {self.matka} km")

autolista = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", 0)
    autolista.append(auto)

while matka <= 10000:
    tunnit = 0
    huippunopeus = random.randint(100, 200)
    kiihdytä(random.randint(15, -10))
    kulje(1)



