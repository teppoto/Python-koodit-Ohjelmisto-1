vuosiluku = float(input("Vuosiluku: "))

if vuosiluku %4 == 0:
    print(f"{vuosiluku:} on karkausvuosi")
elif vuosiluku %100 == 0:
    print(f"{vuosiluku:} ei ole karkausvuosi")
elif vuosiluku %400 == 0:
    print(f"{vuosiluku:} on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")
