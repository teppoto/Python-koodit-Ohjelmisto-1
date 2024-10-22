class Auto:
    def __init__(self, rek, huippunopeus, nyknopeus = 0, matka = 0):
        self.rek = rek
        self.huippunopeus = huippunopeus
        self.nyknopeus = nyknopeus
        self.matka = matka

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.rek:}, auton huippunopeus on {auto.huippunopeus}, auton nykyinen nopeus on {auto.nyknopeus}, auton kuljettu matka on {auto.matka}")