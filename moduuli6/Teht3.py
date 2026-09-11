def gallonat_litroiksi(gallonat):
    """
    Funktio ottaa parametrina gallonamäärän ja palauttaa sen litroina.
    Yksi gallona on 3.785 litraa.
    """
    return gallonat * 3.785


def paaohjelma():
    """
    Pääohjelma, joka kysyy käyttäjältä gallonamäärää ja tulostaa vastauksen litroina.
    Silmukka päättyy, kun syötetään negatiivinen luku.
    """
    print("Gallona-litra-muunnin (syötä negatiivinen luku lopettaaksesi)")
    
    while True:
        try:
            kayttajan_syote = float(input("Syötä bensiinin määrä gallonoina: "))

            if kayttajan_syote < 0:
                print("Ohjelma lopetettu.")
                break

            litrat = gallonat_litroiksi(kayttajan_syote)
            print(f"{kayttajan_syote} gallonaa on {litrat:.3f} litraa.\n")
            
        except ValueError:
            print("Virheellinen syöte! Anna luku.\n")

if __name__ == "__main__":
    paaohjelma()