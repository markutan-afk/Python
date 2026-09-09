import random

noppien_maara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(noppien_maara):
    heitto = random.randint(1, 6)
    summa += heitto

print(f"Silmälukujen summa on {summa}")