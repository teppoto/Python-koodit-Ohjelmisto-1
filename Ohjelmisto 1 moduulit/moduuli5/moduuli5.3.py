"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

kokonaisluku = int(input("Anna kokonaisluku: "))

alkuluku = True

if kokonaisluku <= 1:
    alkuluku = False
else:
    for luku in range(2, kokonaisluku):
        if kokonaisluku % luku == 0:
            alkuluku = False
            break

if alkuluku:
    print(f"On alkuluku")
else:
    print(f"Ei ole alkuluku")














