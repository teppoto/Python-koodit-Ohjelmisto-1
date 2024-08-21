import math

kok1 = float(input("Kirjoita 1. kokonaisluku: "))
kok2 = float(input("Kirjoita 2. kokonaisluku: "))
kok3 = float(input("Kirjoita 3. kokonaisluku: "))

summa = kok1+kok2+kok3
tulo  = kok1*kok2*kok3
keskiarvo = (kok1+kok2+kok3)/3

print(f"summa on: {summa: 0.5f} \ntulo on: {tulo: 0.5f} \nkeskiarvo on: {keskiarvo: 0.5f}")
