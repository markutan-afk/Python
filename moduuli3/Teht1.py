kuha = int(input("Kuinka pitkä kuha on senttimetreinä? "))
alamitta = 37 - kuha

if kuha <= 36:
    print("kuha on alamittainen")
    print(f"Kuha on {alamitta} cm liian pieni")
else:
    print(F"Kuha on {kuha} cm pitkä")