"""Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
 senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
 pizzan yksikköhinnan euroina per neliömetri.
 Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle
(eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota."""

import math

pizza1halk = float(input("Anna 1. pizzan halkaisija: "))
pizza1hint = float(input("Anna 1. pizzan hinta: "))
pizza2halk = float(input("Anna 2. pizza halkaisija: "))
pizza2hint = float(input("Anna 2. pizza hinta: "))

def pizza (pizza1halk,pizza1hint,pizza2halk,pizza2hint):
    pintaala = math.pi*(pizza1halk/2)**2
    pintaala2 = math.pi*(pizza2halk/2)**2
    suhde = pizza1hint/pintaala
    suhde2 = pizza2hint/pintaala2
    if suhde < suhde2:
        print("Pizza 1 on parempi vastine rahalle")
    elif suhde > suhde2:
        print(f"Pizza 2 on parempi vastine rahalle")
    return

pizza(pizza1halk,pizza1hint,pizza2halk,pizza2hint)




