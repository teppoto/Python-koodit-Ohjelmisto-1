"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen palauttaman summan."""

lista = []

luvut = input("Anna kokonaislukuluku: ")

def kokonaislukuja (luvut):
    summa = sum(lista)
    print(summa)
    return summa

while luvut != "":
    luvut = int(luvut)
    lista.append(luvut)
    luvut = input("Anna luku tai paina Enter tulostaaksesi summan: ")

kokonaislukuja(luvut)







