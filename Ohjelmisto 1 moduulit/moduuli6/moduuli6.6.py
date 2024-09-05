"""Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
 senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
 pizzan yksikköhinnan euroina per neliömetri.
 Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle
(eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota."""

import math

pizza1halk = float(input("Anna 1. pizzan halkaisija senttimetreinä: "))
pizza1hint = float(input("Anna 1. pizzan hinta euroina: "))
pizza2halk = float(input("Anna 2. pizzan halkaisija senttimetreinä: "))
pizza2hint = float(input("Anna 2. pizzan hinta euroina: "))

def pizza (pizzahalk,pizzahint):
    pizzametreina = pizzahalk/100
    pintaala = math.pi*(pizzametreina/2)**2
    return pizzahint/pintaala

if pizza(pizza1halk,pizza1hint) < pizza(pizza2halk,pizza2hint):
    print("Pizza 1 on parempi vastine rahalle")
else:
     print(f"Pizza 2 on parempi vastine rahalle")




