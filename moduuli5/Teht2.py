luvut = []

while True:
    syote = input("Syötä luku (tyhjä lopettaa): ")

    if syote == "":
        break

    luku = float(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

print("\nViisi suurinta lukua suurimmasta alkaen:")
for luku in viisi_suurinta:
    print(luku)