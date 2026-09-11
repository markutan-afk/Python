lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")
    
    valinta = input("Valintasi (1/2/3): ")
    
    if valinta == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper().strip()
        nimi = input("Syötä lentoaseman nimi: ").strip()

        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")
        
    elif valinta == "2":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper().strip()

        if icao in lentoasemat:
            print(f"ICAO-koodia {icao} vastaava lentoasema on: {lentoasemat[icao]}")
        else:
            print(f"Lentoasemaa koodilla {icao} osattu löytää.")
            
    elif valinta == "3":
        print("Ohjelman suoritus päättyy. Hei hei!")
        break
        
    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")