"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
 Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman."""

annaluku = input("Anna lukuja: ")
lukuja = int(annaluku)
minluku = lukuja
maxluku =lukuja

while annaluku != "":
    lukuja = int(annaluku)
    if lukuja > maxluku:
        maxluku = lukuja
    if lukuja < minluku:
        minluku = lukuja
    annaluku = input("Anna lukuja: ")


print(f"Pienin luku oli {minluku}")
print(f"Isoin luku oli {maxluku}")

