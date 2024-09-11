"""Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
 Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
 monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
 mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi."""

vuodenajat = ("talvi", "kevät", "kesä", "syksy")
"""Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka
jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi."""

kevat = ("3", "4", "5")
kesa = ("6", "7", "8")
syksy = ("9", "10", "11")
talvi = ("12", "1", "2")

kuukausinumero = input("Anna kuukauden numero 1-12: ")
while kuukausinumero != "":
    if kuukausinumero in kevat:
        print("Kevat")
        break
    elif kuukausinumero in kesa:
        print("Kesa")
        break
    elif kuukausinumero in syksy:
        print("Syksy")
        break
    else:
        print("Talvi")
        break












