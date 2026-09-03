luvut = []

while True:
    syote = input("Anna luku: ")

    if syote == "":
        break

    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Syötäthän numeron.")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt mitään")