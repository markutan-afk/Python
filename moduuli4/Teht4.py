import random

salainen_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1..10: "))
        
        if arvaus > salainen_luku:
            print("Liian suuri arvaus")
        elif arvaus < salainen_luku:
            print("Liian pieni arvaus")
        else:
            print("Oikein")
            break
            
    except ValueError:
        print("Syötäthän kelvollisen kokonaisluvun!")