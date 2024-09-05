"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi
että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan."""

lista = list(range(100))

def karsittu(luvut):
    for i in luvut:
        if i % 2 == 1:
            luvut.remove(i)
    print(luvut)

print(lista)
karsittu(lista)
