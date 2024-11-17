"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää."""

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


auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)





