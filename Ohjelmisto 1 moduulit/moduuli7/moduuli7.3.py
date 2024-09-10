"""Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo
syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä
vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)"""

lentoasemat = {}

lentoasemat["ICAO"] = "nimi"

def uusi_lentokentta():
    icao = input("Anna ICAO: ")
    nimi = input("Anna nimi: ")
    lentoasemat[icao] = nimi
    print(f"Lisätty {icao}: {nimi}")

def haku():
    hakuicao = input("Anna ICAO: ")
    if hakuicao in lentoasemat:
        print(f"{hakuicao} on {lentoasemat[hakuicao]}")

def lopetus():
    lopettaa = input("Paina mitä vain lopettaaksesi: ")
    print("Kiitos käytöstä, ohjelma lopetettu!")

kasky = input("Haluatko lisätä uuden lentokentän(yksi), hakea lentokenttää (kaksi) vai lopettaa(kolme)?: ")

while kasky != "":
    if kasky == "yksi":
        uusi_lentokentta()
        kasky = input("Haluatko lisätä uuden lentokentän(yksi), hakea lentokenttää (kaksi) vai lopettaa(kolme)?: ")
    elif kasky == "kaksi":
        haku()
        kasky = input("Haluatko lisätä uuden lentokentän(yksi), hakea lentokenttää (kaksi) vai lopettaa(kolme)?: ")
    else:
        lopetus()
        break











