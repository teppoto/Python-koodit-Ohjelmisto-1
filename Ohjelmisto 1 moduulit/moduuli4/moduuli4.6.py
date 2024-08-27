"""Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon laskennan
 edellä kuvatulla menetelmällä. Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle."""

import random

pisteet = float(input("Anna pisteiden maara: "))
x = random.uniform (-1, 1)
y = random.uniform (-1, 1)
i = 0
kerrat = 0

while i <= pisteet:
	x = random.uniform (-1, 1)
	y = random.uniform (-1, 1)
	if x ** 2 + y ** 2 < 1:
		kerrat += 1
	i += 1
print(kerrat)
print(f"Piin likiarvo on noin {kerrat*4/pisteet}")







