""" Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
    Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
    Käytä for-toistorakennetta."""
import random

maara = int(input("Arpakuutioiden lukumaara: "))
summa = 0

for luku in range(maara):
    summa += random.randint(1,6)
    print(summa)

print(f"Summa on {summa}")

