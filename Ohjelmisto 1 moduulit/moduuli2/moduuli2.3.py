import math

kanta = float(input("Paljonko on suorakulmion kanta: "))
korkeus = float(input("Paljonko on suorakulmion korkeus: "))

pintaala = kanta*korkeus
piiri = korkeus*2+kanta*2

print(f"Suorakulmion pintaala on: {pintaala:.5f} ")
print(f"Suorakulmion piiri on: {piiri:.5f} ")
