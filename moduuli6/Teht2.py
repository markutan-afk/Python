import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def main():
    maksimi = int(input("Anna nopan tahkojen yhteismäärä: "))
    
    while True:
        heitto = heita_noppaa(maksimi)
        print(f"Heitit: {heitto}")

        if heitto == maksimi:
            break

if __name__ == "__main__":
    main()