"""Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
 käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen."""

kaupungit = []
for kmaara in range(5):
    kaupunki = input("Anna seuraava kaupungin nimi: ")
    kaupungit.append(kaupunki)
for kmaara in kaupungit:
    print(kmaara)
