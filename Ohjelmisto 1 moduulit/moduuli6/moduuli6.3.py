"""Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.

Yksi gallona on 3,785 litraa.
"""
gallonamaara = float(input("Anna gallonamaara: "))

def muunnos():
    litra = 3.875 * gallonamaara
    print(f"{gallonamaara} on {litra} litraa")
    return litra

while gallonamaara >= 0:
    litraa = muunnos()
    gallonamaara = float(input("Anna gallonamaara: "))


