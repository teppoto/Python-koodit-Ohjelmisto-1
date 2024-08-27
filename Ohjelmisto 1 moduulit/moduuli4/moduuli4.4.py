"""Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti,
 kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
  Liian pieni arvaus tai Oikein.
  Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä."""

import random
lukulista = random.randint (1, 10)
arvaus = int(input("Anna arvaus: "))

while arvaus != lukulista:
    if arvaus < lukulista:
        print("Liian pieni arvaus")
    elif arvaus > lukulista:
        print("Liian suuri arvaus")
    arvaus = int(input("Anna arvaus: "))
else:
    print("Oikein")