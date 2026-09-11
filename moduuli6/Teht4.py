def laske_summa(lukulista):
    """
    Funktio saa parametrinaan listan kokonaislukuja
    ja palauttaa niiden summan.
    """
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa


def paaohjelma():
    """
    Pääohjelma testausta varten. Luodaan lista,
    kutsutaan funktiota ja tulostetaan tulos.
    """

    esimerkkilista = [5, 10, 15, 20, 25]

    tulos = laske_summa(esimerkkilista)

    print(f"Listan {esimerkkilista} lukujen summa on: {tulos}")

if __name__ == "__main__":
    paaohjelma()