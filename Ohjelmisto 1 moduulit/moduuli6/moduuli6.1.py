"""Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun."""
import random

def noppa():
    noppaheitto = random.randint(1,6)
    return noppaheitto

while True:
    heitto = noppa()
    print(heitto)
    if heitto == 6:
        break



