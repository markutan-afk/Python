import mysql.connector

def hae_lentokentat_tyypeittain():
    maakoodi = input("Anna maakoodi (esim. FI): ").strip().upper()
    
    try:
        yhteys = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sukram260106",
            database="flight_game"
        )
        
        kursori = yhteys.cursor()

        sql = """
            SELECT type, COUNT(*) 
            FROM airport 
            WHERE iso_country = %s 
            GROUP BY type
        """
        
        kursori.execute(sql, (maakoodi,))
        tulokset = kursori.fetchall()

        if not tulokset:
            print(f"Maakoodilla '{maakoodi}' ei löytynyt lentokenttiä.")
            return
            
        print(f"\nLentokenttien lukumäärät maassa {maakoodi}:")

        for tyyppi, maara in tulokset:
            suomennos = tyyppi
            if tyyppi == "small_airport":
                suomennos = "pieniä lentokenttiä"
            elif tyyppi == "heliport":
                suomennos = "helikopterikenttiä"
            elif tyyppi == "medium_airport":
                suomennos = "keskisuuria lentokenttiä"
            elif tyyppi == "large_airport":
                suomennos = "suuria lentokenttiä"
            elif tyyppi == "closed":
                suomennos = "suljettuja lentokenttiä"
                
            print(f"- {suomennos.capitalize()}: {maara} kappaletta")
            
    except mysql.connector.Error as virhe:
        print(f"Tietokantavirhe: {virhe}")
        
    finally:
        if 'yhteys' in locals() and yhteys.is_connected():
            kursori.close()
            yhteys.close()

if __name__ == "__main__":
    hae_lentokentat_tyypeittain()