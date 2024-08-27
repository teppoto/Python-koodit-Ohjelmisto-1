"""Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules)"""

oikea_kayttaja = "python"
oikea_salasana = "rules"
yritykset = 0

while yritykset < 5:
    kayttaja = input("Kayttaja: ")
    salasana = input("Salasana: ")
    if kayttaja == oikea_kayttaja and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Kirjautuminen epaonnistui")
    yritykset += 1
    if yritykset == 5:
        print("Paasy evatty")


