gramma = 1
luoti = 13.3 * gramma
naula = 32 * luoti
leiviska = 20 * naula

leiv = input("Anna leiviskat: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")

leiv = float(leiv)
naulat = float(naulat)
luodit = float(luodit)

grammoina = luodit*luoti+naulat*naula+leiv*leiviska
kilos = int(luodit*luoti+naulat*naula+leiv*leiviska)/1000
print(f"Massa: {grammoina//1000:.0f} kiloa ja {grammoina%1000:.0f} grammaa")
