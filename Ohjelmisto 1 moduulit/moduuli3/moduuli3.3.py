sukupuoli = input("Sukupuoli: ")
hemoglob = float(input("Mikä on hemoglobiiniarvosi g/l?: "))

if sukupuoli == "Mies" or "mies"  and hemoglob >=135 and hemoglob <=195:
    print("Hemoglobiiniarvosi on normaali")
elif sukupuoli == "Nainen" or sukupuoli == "nainen" and hemoglob >=117 and hemoglob <=175:
    print("Hemoglobiiniarvosi on normaali")

if sukupuoli == "Mies" or "mies" and hemoglob <=135:
    print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli == "Nainen" or sukupuoli == "nainen" and hemoglob <=117:
    print("Hemoglobiiniarvosi on alhainen")

if sukupuoli == "Mies" or "mies" and hemoglob >=195:
    print("Hemoglobiiniarvosi on korkea")
elif sukupuoli == "Nainen" or sukupuoli == "nainen" and hemoglob >=175:
    print("Hemoglobiiniarvosi on korkea")






