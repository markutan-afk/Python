import random

kolme_numeroa = [str(random.randint(0, 9)) for _ in range(3)]

nelja_numeroa = [str(random.randint(1, 6)) for _ in range(4)]

print(f"Kolmenumeroinen koodi: {kolme_numeroa}")
print(f"Nelinumeroinen koodi: {nelja_numeroa}")