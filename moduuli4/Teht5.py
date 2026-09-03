OIKEA_TUNNUS = "python"
OIKEA_SALASANA = "rules"
YRITYKSET_MAX = 5

yritykset = 0
kirjautunut = False

while yritykset < YRITYKSET_MAX:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset += 1

    if tunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        kirjautunut = True
        break

if kirjautunut:
    print("Tervetuloa")
else:
    print("Pääsy evätty")