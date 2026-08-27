sukupuoli = input("Mikä on sukupuolesi? ")
hemo = int(input("Kuinka suuri on hemoglobiiniarvosi? "))

if sukupuoli == "Nainen":
    if hemo <= 116:
        print("Sinun hemoglobiiniarvo on alhainen.")
    elif hemo >= 117 and hemo <= 175:
        print("Sinun hemoglobiiniarvo on normaali.")
    else:
        print("Sinun hemoglobiiniarvo on korkea.")
elif sukupuoli == "Mies":
    if hemo <= 133:
        print("Sinun hemoglobiiniarvo on alhainen.")
    elif hemo >= 134 and hemo <= 195:
        print("Sinun hemoglobiiniarvo on normaali.")
    else:
        print("Sinun hemoglobiiniarvo on korkea.")
else:
    print("Sukupuola ei tunnistettu.")