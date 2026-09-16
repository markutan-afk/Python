import mysql.connector
from geopy.distance import geodesic

def hae_koordinaatit(kursori, icao_koodi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao_koodi,))
    return kursori.fetchone()

def laske_lentokenttien_etaisyys_tietokannasta():
    yhteys = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sukram260106",
        database="flight_game"
    )
    
    kursori = yhteys.cursor()
    
    print("--- Lentokenttien etäisyyslaskuri (Tietokanta + Geopy) ---")

    koodi1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").strip().upper()
    koodi2 = input("Anna toisen lentokentän ICAO-koodi: ").strip().upper()

    koordinaatit1 = hae_koordinaatit(kursori, koodi1)
    koordinaatit2 = hae_koordinaatit(kursori, koodi2)

    if not koordinaatit1:
        print(f"Virhe: Lentokenttää {koodi1} ei löytynyt tietokannasta.")
        kursori.close()
        yhteys.close()
        return
        
    if not koordinaatit2:
        print(f"Virhe: Lentokenttää {koodi2} ei löytynyt tietokannasta.")
        kursori.close()
        yhteys.close()
        return

    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers

    print(f"\nLentokenttien {koodi1} ja {koodi2} välinen etäisyys on {etaisyys:.1f} km.")

    kursori.close()
    yhteys.close()

if __name__ == "__main__":
    laske_lentokenttien_etaisyys_tietokannasta()