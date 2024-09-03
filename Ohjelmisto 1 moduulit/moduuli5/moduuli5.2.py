
luvut = []

maara = input("Anna ensimmäinen luku: ")
while maara != "":
    maara = float(maara)
    luvut.append(maara)
    maara = input("Anna seuraava luku tai lopeta painamalla Enter: ")

luvut.sort(reverse=True)

print(f"Viisi isointa lukua ovat: {luvut[0:5]}")
