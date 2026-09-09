kaupungit = []

for i in range(5):
    kaupunki = input(f"Syötä {i+1}. kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("\nSyötetyt kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)