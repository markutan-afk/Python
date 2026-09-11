def karsi_parittomat(lukulista):
    """
    Funktio saa parametrinaan listan kokonaislukuja.
    Se palauttaa uuden listan, josta on karsittu pois parittomat luvut.
    """
    parilliset = []
    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def paaohjelma():
    """
    Pääohjelma testausta varten. Luodaan alkuperäinen lista,
    kutsutaan funktiota ja tulostetaan molemmat listat.
    """

    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    karsittu_lista = karsi_parittomat(alkuperainen_lista)

    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista (vain parilliset): {karsittu_lista}")

if __name__ == "__main__":
    paaohjelma()