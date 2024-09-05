"""Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
 Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen
  nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
   joka kysytään käyttäjältä ohjelman suorituksen alussa"""

import random

maxsilmaluku = int(input("Anna maksimisilmaluku: "))

def noppa():
    noppaheitto = random.randint(1,21)
    return noppaheitto

while True:
    heitto = noppa()
    print(heitto)
    if heitto == maxsilmaluku:
        break