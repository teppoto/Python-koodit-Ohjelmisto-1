class Auto:
    def __init__(self, rek, huippunopeus, nyknopeus = 60, matka = 0,):
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

auto = Auto("ABC-123", 142)
auto.kulje(1.5)
